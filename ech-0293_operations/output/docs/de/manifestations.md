---
search:
  boost: 5.0
---

# Slot: manifestations 


_Die Dateiformen (Manifestations) einer Expression._




<div data-search-exclude markdown="1">



URI: [meta:manifestations](https://ch.paf.link/schema/meta/manifestations)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Manifestation](Manifestation.md) |
| Domäne von | [Expression](Expression.md) |
| Slot-URI | [meta:manifestations](https://ch.paf.link/schema/meta/manifestations) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: manifestations
annotations:
  description_de:
    tag: description_de
    value: 'Die Dateiformen (Manifestations) einer Expression.

      '
  description_fr:
    tag: description_fr
    value: 'Les formes de fichier (Manifestations) d''une Expression.

      '
description: 'Die Dateiformen (Manifestations) einer Expression.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:manifestations
domain_of:
- Expression
range: Manifestation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>