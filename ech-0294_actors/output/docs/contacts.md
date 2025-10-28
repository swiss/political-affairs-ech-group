

# Slot: contacts 



URI: [act:contact](https://ch.paf.link/schema/actors/contact)
Alias: contacts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

* Range: [Contact](Contact.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:contact |
| native | act:contacts |




## LinkML Source

<details>
```yaml
name: contacts
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:contact
alias: contacts
owner: Person
domain_of:
- Person
range: Contact
multivalued: true
inlined: true
inlined_as_list: true

```
</details>