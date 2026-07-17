---
search:
  boost: 5.0
---

# Slot: organization_name 


_Name of the organization or enterprise._

__



<div data-search-exclude markdown="1">



URI: [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot URI | [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: organization_name
annotations:
  description_de:
    tag: description_de
    value: 'Name der Organisation oder des Unternehmens.

      '
description: 'Name of the organization or enterprise.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationName
domain_of:
- InterestLink
- Occupation
range: string

```
</details></div>