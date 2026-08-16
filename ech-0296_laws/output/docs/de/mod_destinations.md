---
search:
  boost: 5.0
---

# Slot: mod_destinations 


_Die Stellen, die geändert werden (akn:destination)._



<div data-search-exclude markdown="1">



URI: [laws:mod_destinations](https://ld.ech.ch/schema/0296/laws/mod_destinations)
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
| Wertebereich | [ModDestination](ModDestination.md) |
| Domäne von | [TextualMod](TextualMod.md), [ForceMod](ForceMod.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: mod_destinations
annotations:
  description_de:
    tag: description_de
    value: Die Stellen, die geändert werden (akn:destination).
  xml_element:
    tag: xml_element
    value: akn:destination
description: Die Stellen, die geändert werden (akn:destination).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:destination
rank: 1000
domain_of:
- TextualMod
- ForceMod
range: ModDestination
multivalued: true

```
</details></div>