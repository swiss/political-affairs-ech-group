---
search:
  boost: 5.0
---

# Slot: id 


_Eindeutiger Identifikator des Elements._




<div data-search-exclude markdown="1">



URI: [ops:id](https://ch.paf.link/schema/operations/id)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |  no  |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |  no  |
| [Manifestation](Manifestation.md) | FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL a... |  no  |
| [WorkContainer](WorkContainer.md) | Container für die Dokumente (FRBR Works) dieses Schemas |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Work](Work.md), [Expression](Expression.md), [Manifestation](Manifestation.md), [WorkContainer](WorkContainer.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |
### Slot-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Identifikator | Yes |














## LinkML-Quelle

<details>
```yaml
name: id
annotations:
  description_de:
    tag: description_de
    value: 'Eindeutiger Identifikator des Elements.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant univoque de l''élément.

      '
description: 'Eindeutiger Identifikator des Elements.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
identifier: true
domain_of:
- Work
- Expression
- Manifestation
- WorkContainer
range: string
required: true

```
</details></div>