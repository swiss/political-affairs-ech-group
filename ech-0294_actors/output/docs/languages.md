

# Slot: languages 



URI: [act:language](https://ch.paf.link/schema/actors/language)
Alias: languages

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [LanguageProficiency](LanguageProficiency.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:language |
| native | act:languages |




## LinkML Source

<details>
```yaml
name: languages
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:language
alias: languages
domain_of:
- Person
range: LanguageProficiency
multivalued: true
inlined: true
inlined_as_list: true

```
</details>