---
search:
  boost: 5.0
---

# Slot: spatial 


_Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE._




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
### Wertebeschränkungen

| Eigenschaft | Wert |
| --- | --- |
| Regex Pattern | `^https://ld\.admin\.ch/(country/[A-Z]{3}|canton/[0-9]+|district/[0-9]+|municipality/[0-9]+)$` |











## Beispiele

| Wert |
| --- |
| https://ld.admin.ch/canton/10 |
| https://ld.admin.ch/canton/12 |
| https://ld.admin.ch/canton/15 |





## LinkML-Quelle

<details>
```yaml
name: spatial
annotations:
  description_de:
    tag: description_de
    value: 'Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer,
      Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234,
      Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23,
      Bund: https://ld.admin.ch/country/CHE.

      '
  description_fr:
    tag: description_fr
    value: 'Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro
      OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234,
      district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23,
      pays : https://ld.admin.ch/country/CHE.

      '
description: 'Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer,
  Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk:
  https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund:
  https://ld.admin.ch/country/CHE.

  '
examples:
- value: https://ld.admin.ch/canton/10
- value: https://ld.admin.ch/canton/12
- value: https://ld.admin.ch/canton/15
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- Group
range: string
pattern: ^https://ld\.admin\.ch/(country/[A-Z]{3}|canton/[0-9]+|district/[0-9]+|municipality/[0-9]+)$

```
</details></div>