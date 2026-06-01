---
search:
  boost: 5.0
---

# Slot: legal_form 


_Legal form of the organization._

__



<div data-search-exclude markdown="1">



URI: [act:legalForm](https://ld.ech.ch/schema/0294/actors/legalForm)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:legalForm](https://ld.ech.ch/schema/0294/actors/legalForm) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Aktiengesellschaft |
| Gesellschaft mit beschränkter Haftung |
| Stiftung |





## LinkML Source

<details>
```yaml
name: legal_form
annotations:
  description_de:
    tag: description_de
    value: 'Rechtsform der Organisation.

      '
description: 'Legal form of the organization.

  '
examples:
- value: Aktiengesellschaft
- value: Gesellschaft mit beschränkter Haftung
- value: Stiftung
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:legalForm
domain_of:
- InterestLink
range: string

```
</details></div>