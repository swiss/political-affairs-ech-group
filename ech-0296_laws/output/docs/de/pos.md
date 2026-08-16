---
search:
  boost: 5.0
---

# Slot: pos 


_Lage der Änderung zum Ziel (@pos), z.B. „before“._



<div data-search-exclude markdown="1">



URI: [laws:pos](https://ld.ech.ch/schema/0296/laws/pos)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ModSource](ModSource.md) | Die Stelle, welche die Änderung bewirkt |  no  |
| [ModDestination](ModDestination.md) | Die Stelle, die geändert wird |  no  |
| [ModOld](ModOld.md) | Der Text, wie er vor der Änderung lautete |  no  |
| [ModNew](ModNew.md) | Der Text, wie er nach der Änderung lautet |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [ModSource](ModSource.md), [ModDestination](ModDestination.md), [ModOld](ModOld.md), [ModNew](ModNew.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: pos
annotations:
  description_de:
    tag: description_de
    value: Lage der Änderung zum Ziel (@pos), z.B. „before“.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: pos
description: Lage der Änderung zum Ziel (@pos), z.B. „before“.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ModSource
- ModDestination
- ModOld
- ModNew
range: string

```
</details></div>