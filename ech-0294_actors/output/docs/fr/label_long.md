---
search:
  boost: 5.0
---

# Slot: label_long 


_Attribuer un label étendu à une information structurée (par ex. nom d'affichage avec titre, poste, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  yes  |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |  yes  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Person](Person.md), [PersonReference](PersonReference.md) |
| URI du slot | [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: label_long
annotations:
  description_de:
    tag: description_de
    value: 'Möglichkeit bei einer strukturierten Information, ein erweitertesLabel
      zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).

      '
  description_fr:
    tag: description_fr
    value: 'Attribuer un label étendu à une information structurée (par ex. nom d''affichage
      avec titre, poste, etc.).

      '
description: 'Attribuer un label étendu à une information structurée (par ex. nom
  d''affichage avec titre, poste, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:labelLong
domain_of:
- Person
- PersonReference
range: string

```
</details></div>