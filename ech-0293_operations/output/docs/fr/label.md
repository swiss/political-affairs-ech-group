---
search:
  boost: 5.0
---

# Slot: label 


_Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.)._




<div data-search-exclude markdown="1">



URI: [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [TotalOther](TotalOther.md) | Décomptes de voix supplémentaires lorsque plusieurs options sont soumises au ... |  no  |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |  yes  |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [TotalOther](TotalOther.md), [PersonReference](PersonReference.md), [GroupReference](GroupReference.md) |
| URI du slot | [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: label
annotations:
  description_de:
    tag: description_de
    value: 'Möglichkeit bei einer strukturierten Information, ein Label zu vergeben
      (bspw. Anzeigename, Anstellung, etc.).

      '
  description_fr:
    tag: description_fr
    value: 'Attribuer un label à une information structurée (par ex. nom d''affichage,
      poste, etc.).

      '
description: 'Attribuer un label à une information structurée (par ex. nom d''affichage,
  poste, etc.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:label
domain_of:
- TotalOther
- PersonReference
- GroupReference
range: string

```
</details></div>