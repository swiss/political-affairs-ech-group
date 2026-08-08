---
search:
  boost: 5.0
---

# Slot: label 


_Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.)._




<div data-search-exclude markdown="1">



URI: [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TotalOther](TotalOther.md) | Zusätzliche Stimmzahlen, wenn mehrere Optionen zur Abstimmung gestellt werden... |  no  |
| [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum... |  yes  |
| [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [TotalOther](TotalOther.md), [PersonReference](PersonReference.md), [GroupReference](GroupReference.md) |
| Slot-URI | [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Möglichkeit bei einer strukturierten Information, ein Label zu vergeben
  (bspw. Anzeigename, Anstellung, etc.).

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