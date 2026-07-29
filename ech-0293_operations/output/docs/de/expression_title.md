---
search:
  boost: 5.0
---

# Slot: expression_title 


_Titel der Sprachfassung._




<div data-search-exclude markdown="1">



URI: [meta:title](https://ch.paf.link/schema/meta/title)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Expression](Expression.md) |
| Slot-URI | [meta:title](https://ch.paf.link/schema/meta/title) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |












## LinkML-Quelle

<details>
```yaml
name: expression_title
annotations:
  description_de:
    tag: description_de
    value: 'Titel der Sprachfassung.

      '
  description_fr:
    tag: description_fr
    value: 'Titre de la version linguistique.

      '
description: 'Titel der Sprachfassung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:title
domain_of:
- Expression
range: string
required: true

```
</details></div>