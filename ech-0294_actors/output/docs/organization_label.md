---
search:
  boost: 5.0
---

# Slot: organization_label 


_Label of the organization._

__



<div data-search-exclude markdown="1">



URI: [act:organizationLabel](https://ld.ech.ch/schema/0294/actors/organizationLabel)
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
| Slot URI | [act:organizationLabel](https://ld.ech.ch/schema/0294/actors/organizationLabel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| ASTAG Schweizerischer Nutzfahrzeugverband, Bern |
| Allianz Sicherheit Schweiz, Baden |
| Birchmeier Holding AG, Döttingen |





## LinkML Source

<details>
```yaml
name: organization_label
annotations:
  description_de:
    tag: description_de
    value: 'Bezeichnung der Organisation.

      '
description: 'Label of the organization.

  '
examples:
- value: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
- value: Allianz Sicherheit Schweiz, Baden
- value: Birchmeier Holding AG, Döttingen
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationLabel
domain_of:
- InterestLink
range: string

```
</details></div>