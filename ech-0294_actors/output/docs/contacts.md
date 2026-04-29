---
search:
  boost: 5.0
---

# Slot: contacts 


_[en] Contact information (email, website, social media)._

_[de] Kontaktinformationen (E-Mail, Website, Social Media)._

__



<div data-search-exclude markdown="1">



URI: [act:contact](https://ld.ech.ch/schema/0294/actors/contact)
Alias: contacts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Contact](Contact.md) |
| Domain Of | [Person](Person.md), [Group](Group.md) |
| Slot URI | [act:contact](https://ld.ech.ch/schema/0294/actors/contact) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:contact |
| native | act:contacts |




## LinkML Source

<details>
```yaml
name: contacts
description: '[en] Contact information (email, website, social media).

  [de] Kontaktinformationen (E-Mail, Website, Social Media).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:contact
alias: contacts
domain_of:
- Person
- Group
range: Contact
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>