---
search:
  boost: 5.0
---

# Slot: mod_sources 


_Die Stellen, welche die Änderung bewirken (akn:source)._



<div data-search-exclude markdown="1">



URI: [laws:mod_sources](https://ld.ech.ch/schema/0296/laws/mod_sources)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TextualMod](TextualMod.md) | Eine Textänderung: der Wortlaut eines anderen Erlasses wird eingefügt, ersetz... |  no  |
| [ForceMod](ForceMod.md) | Eine Änderung der Rechtskraft: ein Erlass oder ein Teil davon tritt in Kraft,... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ModSource](ModSource.md) |
| Domäne von | [TextualMod](TextualMod.md), [ForceMod](ForceMod.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: mod_sources
annotations:
  description_de:
    tag: description_de
    value: Die Stellen, welche die Änderung bewirken (akn:source).
  xml_element:
    tag: xml_element
    value: akn:source
description: Die Stellen, welche die Änderung bewirken (akn:source).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:source
rank: 1000
domain_of:
- TextualMod
- ForceMod
range: ModSource
multivalued: true

```
</details></div>