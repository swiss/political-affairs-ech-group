import pandas as pd
import asyncio

from display_result import display_result
from query import query

async def main():
    with open("sparql_query.txt", "r") as file:
        query_string = file.read()
    
    # "F" corresponds to F=https://fedlex.data.admin.ch/sparqlendpoint in the file sparql_endpoints.txt
    df_result = await query(query_string, "F")

    display_result(df_result)

# Ensure that main() is called in an asynchronous context when run as Python module, when the module is run directly, not when it's imported as a module into another script.
if __name__ == "__main__":
    asyncio.run(main())
