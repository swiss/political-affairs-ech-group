---
search:
  boost: 5.0
---

# Slot: location 


_Ort, an dem die Sitzung stattfindet — der physische Raum („Bundeshaus, Nationalratssaal“), eine Videokonferenz oder ein hybrides Format._




<div data-search-exclude markdown="1">



URI: [ops:location](https://ch.paf.link/schema/operations/location)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| Kantonsratssaal, Regierungsgebäude St. Gallen |
| Kommissionszimmer 301, Rathaus Bern |
| Zaunplatz, Glarus |





## LinkML-Quelle

<details>
```yaml
name: location
annotations:
  description_de:
    tag: description_de
    value: 'Ort, an dem die Sitzung stattfindet — der physische Raum („Bundeshaus,
      Nationalratssaal“), eine Videokonferenz oder ein hybrides Format.

      '
  description_fr:
    tag: description_fr
    value: 'Lieu où se tient la séance — la salle physique (« Palais fédéral, salle
      du Conseil national »), une visioconférence ou un format hybride.

      '
description: 'Ort, an dem die Sitzung stattfindet — der physische Raum („Bundeshaus,
  Nationalratssaal“), eine Videokonferenz oder ein hybrides Format.

  '
examples:
- value: Kantonsratssaal, Regierungsgebäude St. Gallen
- value: Kommissionszimmer 301, Rathaus Bern
- value: Zaunplatz, Glarus
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>