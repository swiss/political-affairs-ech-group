---
search:
  boost: 5.0
---

# Slot: interest_type 


_Type of interest link (professional activity, political office, association)._

__



<div data-search-exclude markdown="1">



URI: [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [InterestTypeEnum](InterestTypeEnum.md) |
| Domaine de | [InterestLink](InterestLink.md) |
| URI du slot | [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Requis | Yes |









## Exemples

| Valeur |
| --- |
| association |
| professional_activity |





## Source LinkML

<details>
```yaml
name: interest_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).

      '
description: 'Type of interest link (professional activity, political office, association).

  '
examples:
- value: association
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