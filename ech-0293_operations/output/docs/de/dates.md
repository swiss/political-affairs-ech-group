---
search:
  boost: 5.0
---

# Slot: dates 


_Datumsangaben zum Element, jeweils mit Typangabe._




<div data-search-exclude markdown="1">



URI: [meta:dates](https://ch.paf.link/schema/meta/dates)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |  no  |
| [Manifestation](Manifestation.md) | FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL a... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [Expression](Expression.md), [Manifestation](Manifestation.md) |
| Slot-URI | [meta:dates](https://ch.paf.link/schema/meta/dates) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: dates
annotations:
  description_de:
    tag: description_de
    value: 'Datumsangaben zum Element, jeweils mit Typangabe.

      '
  description_fr:
    tag: description_fr
    value: 'Dates relatives à l''élément, chacune assortie d''une indication de type.

      '
description: 'Datumsangaben zum Element, jeweils mit Typangabe.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dates
domain_of:
- Expression
- Manifestation
range: Date
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>