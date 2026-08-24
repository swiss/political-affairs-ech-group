# Common Data Elements

One of the outputs of the eCH-0292 subgroup is a set of **common data elements** that can be used across all the standards developed by the eCH Specialist Group Political Affairs without duplication.

## Defining Common Data Elements

The common data elements are defined in the `schema_common.yaml` file. The classes and their slots defined in this file will mainly be used as **mixins** in the specific standards. With this approach, a class that declares a mixin can use all the slots defined in the mixin class without having to redefine them. This allows for a consistent definition of common data elements across all standards.

## Using Common Data Elements

The common data elements can be used by importing the `schema_common.yaml` file into the LinkML schema of a specific standard. This happens in the `import` section of the LinkML schema:

```yaml
imports:
  - linkml:types
  - ../../ech-0292_meta/input/schema_common
```

Afterwards, all the elements defined in the `schema_common.yaml` file can be used in the specific standard:

```yaml
classes:
    Person:
        description: A person with identifiers, names, addresses, citizenships, and occupations.
        mixins:
            - HasIdentification #import from schema_common.yaml
            - HasCreationModificationDates #import from schema_common.yaml
```
