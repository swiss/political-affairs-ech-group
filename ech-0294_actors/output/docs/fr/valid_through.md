---
search:
  boost: 5.0
---

# Slot: valid_through 


_The date until which the information is valid, inclusive._

__



<div data-search-exclude markdown="1">



URI: [schema:validThrough](http://schema.org/validThrough)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | A mixin class that provides slots for modeling a temporal validity of informa... |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Name](Name.md) | A name with a type (e |  no  |
| [Citizenship](Citizenship.md) | Citizenship (also used for Nationality) of a person indicating the country an... |  no  |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |
| [Training](Training.md) | Training or education of a person indicating a type (e |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Electoral district or region where a person is politically active; with tempo... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [HasTemporalValidity](HasTemporalValidity.md) |
| URI du slot | [schema:validThrough](http://schema.org/validThrough) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: valid_through
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, bis und mit dem die Information gültig ist.

      '
description: 'The date until which the information is valid, inclusive.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:validThrough
domain_of:
- HasTemporalValidity
range: date

```
</details></div>