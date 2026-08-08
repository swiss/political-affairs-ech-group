---
search:
  boost: 5.0
---

# Slot: abbreviation 


_Abkürzung (kann mehrsprachig sein)._




<div data-search-exclude markdown="1">



URI: [mcm:abbreviation](https://ld.ech.ch/schema/0292/meta-common/abbreviation)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualValue](MultilingualValue.md) |
| Domäne von | [GroupReference](GroupReference.md) |
| Slot-URI | [mcm:abbreviation](https://ld.ech.ch/schema/0292/meta-common/abbreviation) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: abbreviation
annotations:
  description_de:
    tag: description_de
    value: 'Abkürzung (kann mehrsprachig sein).

      '
  description_fr:
    tag: description_fr
    value: 'Abréviation (peut être multilingue).

      '
description: 'Abkürzung (kann mehrsprachig sein).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:abbreviation
domain_of:
- GroupReference
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>