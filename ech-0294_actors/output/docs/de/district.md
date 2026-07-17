---
search:
  boost: 5.0
---

# Slot: district 


_Wahlkreis oder Wahlregion._

__



<div data-search-exclude markdown="1">



URI: [act:district](https://ld.ech.ch/schema/0294/actors/district)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitli... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [ElectoralDistrict](ElectoralDistrict.md) |
| Slot-URI | [act:district](https://ld.ech.ch/schema/0294/actors/district) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| Basel-Stadt |





## LinkML-Quelle

<details>
```yaml
name: district
annotations:
  description_de:
    tag: description_de
    value: 'Wahlkreis oder Wahlregion.

      '
description: 'Wahlkreis oder Wahlregion.

  '
examples:
- value: Basel-Stadt
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:district
domain_of:
- ElectoralDistrict
range: string

```
</details></div>