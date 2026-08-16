---
search:
  boost: 5.0
---

# Slot: period 


_Die Zeitgruppe, in der die Änderung gilt (@period)._



<div data-search-exclude markdown="1">



URI: [laws:period](https://ld.ech.ch/schema/0296/laws/period)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |
| [TextualMod](TextualMod.md) | Eine Textänderung: der Wortlaut eines anderen Erlasses wird eingefügt, ersetz... |  no  |
| [ForceMod](ForceMod.md) | Eine Änderung der Rechtskraft: ein Erlass oder ein Teil davon tritt in Kraft,... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [ActBody](ActBody.md), [TextualMod](TextualMod.md), [ForceMod](ForceMod.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| #tmgr_1 |
| #tmgr_2 |
| tmgr_1 |





## LinkML-Quelle

<details>
```yaml
name: period
annotations:
  description_de:
    tag: description_de
    value: Die Zeitgruppe, in der die Änderung gilt (@period).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: period
description: Die Zeitgruppe, in der die Änderung gilt (@period).
examples:
- value: '#tmgr_1'
- value: '#tmgr_2'
- value: tmgr_1
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
- TextualMod
- ForceMod
range: string

```
</details></div>