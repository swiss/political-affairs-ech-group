#!/bin/bash

# convert schema.yaml to schema.ttl
gen-owl schema.yaml > ../output/schema.ttl

# convert schema.yaml to schema.json
gen-json-schema schema.yaml > ../output/schema.json

# all data_*.yaml files to data_*.ttl
for yaml_file in data_*.yaml; do
    base_name=$(basename "$yaml_file" .yaml)
    linkml-convert -s schema.yaml -t rdf "$yaml_file" > "../output/${base_name}.ttl"
done

# all data_*.yaml files to data_*.json
for yaml_file in data_*.yaml; do
    base_name=$(basename "$yaml_file" .yaml)
    linkml-convert -s schema.yaml -t json "$yaml_file" > "../output/${base_name}.json"
done