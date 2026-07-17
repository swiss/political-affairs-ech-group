---
search:
  boost: 5.0
---

# Slot: contacts 


_Contact information (email, website, social media). Guideline: email is quasi-mandatory and should always be provided where available._

__



<div data-search-exclude markdown="1">



URI: [act:contact](https://ld.ech.ch/schema/0294/actors/contact)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |






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












## LinkML Source

<details>
```yaml
name: contacts
annotations:
  description_de:
    tag: description_de
    value: 'Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail
      ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.

      '
description: 'Contact information (email, website, social media). Guideline: email
  is quasi-mandatory and should always be provided where available.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:contact
domain_of:
- Person
- Group
range: Contact
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>