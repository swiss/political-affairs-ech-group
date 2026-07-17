---
search:
  boost: 5.0
---

# Slot: label_long 


_Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  yes  |
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Person](Person.md), [PersonReference](PersonReference.md) |
| Slot-URI | [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Möglichkeit bei einer strukturierten Information, ein erweitertesLabel
  zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).

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