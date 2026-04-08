---
search:
  boost: 5.0
---

# Slot: contact_type 


_[de] Typ der Kontaktinformation._

_[en] Type of contact information._

__



<div data-search-exclude markdown="1">



URI: [act:contactType](https://ld.ech.ch/schema/0294/actors/contactType)
Alias: contact_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contact](Contact.md) | [de] Kontaktinformation einer Person mit Angabe eines Typs (z |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContactTypeEnum](ContactTypeEnum.md) |
| Domain Of | [Contact](Contact.md) |
| Slot URI | [act:contactType](https://ld.ech.ch/schema/0294/actors/contactType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:contactType |
| native | act:contact_type |




## LinkML Source

<details>
```yaml
name: contact_type
description: '[de] Typ der Kontaktinformation.

  [en] Type of contact information.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:contactType
alias: contact_type
domain_of:
- Contact
range: ContactTypeEnum

```
</details></div>