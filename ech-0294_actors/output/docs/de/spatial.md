---
search:
  boost: 5.0
---

# Slot: spatial 


_Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land). Formate: Gemeinde: ld.admin.ch/municipality/1234, Kanton: ld.admin.ch/canton/23, Bund: ld.admin.ch/country/CHE._

__



<div data-search-exclude markdown="1">



URI: [act:spatial](https://ld.ech.ch/schema/0294/actors/spatial)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Group](Group.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: spatial
annotations:
  description_de:
    tag: description_de
    value: 'Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land).
      Formate: Gemeinde: ld.admin.ch/municipality/1234, Kanton: ld.admin.ch/canton/23,
      Bund: ld.admin.ch/country/CHE.

      '
description: 'Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land).
  Formate: Gemeinde: ld.admin.ch/municipality/1234, Kanton: ld.admin.ch/canton/23,
  Bund: ld.admin.ch/country/CHE.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- Group
range: string

```
</details></div>