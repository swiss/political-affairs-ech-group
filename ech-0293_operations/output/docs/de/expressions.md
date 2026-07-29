---
search:
  boost: 5.0
---

# Slot: expressions 


_Die Sprachfassungen (Expressions) eines Works._




<div data-search-exclude markdown="1">



URI: [meta:expressions](https://ch.paf.link/schema/meta/expressions)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Expression](Expression.md) |
| Domäne von | [Work](Work.md) |
| Slot-URI | [meta:expressions](https://ch.paf.link/schema/meta/expressions) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: expressions
annotations:
  description_de:
    tag: description_de
    value: 'Die Sprachfassungen (Expressions) eines Works.

      '
  description_fr:
    tag: description_fr
    value: 'Les versions linguistiques (Expressions) d''un Work.

      '
description: 'Die Sprachfassungen (Expressions) eines Works.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:expressions
domain_of:
- Work
range: Expression
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>