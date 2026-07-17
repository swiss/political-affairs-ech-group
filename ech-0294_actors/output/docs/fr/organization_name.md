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





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| URI du slot | [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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