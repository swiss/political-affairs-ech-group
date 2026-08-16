---
search:
  boost: 5.0
---

# Slot: block_name 


_Zweck des Blocks (akn:block/@name)._



<div data-search-exclude markdown="1">



URI: [laws:block_name](https://ld.ech.ch/schema/0296/laws/block_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Block](Block.md) | Ein generischer Block (akn:block), dessen @name den Zweck nennt; trägt gemisc... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [BlockNameEnum](BlockNameEnum.md) |
| Domäne von | [Block](Block.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| heading |





## LinkML-Quelle

<details>
```yaml
name: block_name
annotations:
  description_de:
    tag: description_de
    value: Zweck des Blocks (akn:block/@name).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: name
description: Zweck des Blocks (akn:block/@name).
examples:
- value: heading
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Block
range: BlockNameEnum

```
</details></div>