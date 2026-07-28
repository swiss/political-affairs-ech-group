---
search:
  boost: 5.0
---

# Slot: organization_name 


_Nom de l'organisation ou de l'entreprise._

__



<div data-search-exclude markdown="1">



URI: [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |  no  |






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
  description_fr:
    tag: description_fr
    value: 'Nom de l''organisation ou de l''entreprise.

      '
description: 'Nom de l''organisation ou de l''entreprise.

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