import requests
import json
from io import StringIO
import pandas as pd


async def query(query_string, store="F", set_na=False):
    # Read endpoints from sparql_endpoints.txt
    endpoints = {}
    with open("sparql_endpoints.txt", "r") as file:
        for line in file:
            store_name, endpoint_url = line.strip().split("=")
            endpoints[store_name] = endpoint_url
    
    address = endpoints.get(store, store)

    # Try the POST request
    try:
        resp = requests.post(
            address,
            data={"query": query_string},
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "text/csv"})
        resp.raise_for_status()  # Raise exception for non-200 status codes
    except Exception as e:
        raise RuntimeError(f"Fetch failed: {str(e)}")

    if resp.ok:
        res = resp.text
        if '{"message":' in res:
            error = json.loads(res)
            raise RuntimeError("SPARQL query malformed: " + error["message"])
        elif 'Parse error:' in res:
            raise RuntimeError("SPARQL query malformed: " + res)
        else:
            df = pd.read_csv(StringIO(res), na_filter=set_na)
            return df
    else:
        if resp.status_code == 400:
            raise RuntimeError("Response status 400: Possible malformed SPARQL query. No syntactic advice available.")
        else:
            raise RuntimeError(f"Response status {resp.status_code}")