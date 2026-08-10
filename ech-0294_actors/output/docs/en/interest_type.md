---
search:
  boost: 5.0
---

# Slot: interest_type 


_Type of interest link, following the categories the disclosure registers maintain (professional activity, seat on a governing body, mandate for an interest group, public mandate, membership)._




<div data-search-exclude markdown="1">



URI: [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InterestTypeEnum](InterestTypeEnum.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| governing_body |
| interest_group_mandate |
| professional_activity |





## LinkML Source

<details>
```yaml
name: interest_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der Interessenbindung, den Kategorien der Offenlegungsregister folgend
      (berufliche Tätigkeit, Sitz in einem Führungsgremium, Mandat für eine Interessengruppe,
      Amt in der öffentlichen Hand, Mitgliedschaft).

      '
  description_fr:
    tag: description_fr
    value: 'Type de lien d''intérêts, suivant les catégories tenues par les registres
      de publicité (activité professionnelle, siège dans un organe de direction, mandat
      pour un groupe d''intérêts, fonction dans la sphère publique, appartenance).

      '
description: 'Type of interest link, following the categories the disclosure registers
  maintain (professional activity, seat on a governing body, mandate for an interest
  group, public mandate, membership).

  '
examples:
- value: governing_body
- value: interest_group_mandate
- value: professional_activity
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestType
domain_of:
- InterestLink
range: InterestTypeEnum
required: true

```
</details></div>