---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_Identifikator der Legislaturperiode, zu der die Session gehört._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Session](Session.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: parent_legislature
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator der Legislaturperiode, zu der die Session gehört.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la législature à laquelle la session appartient.

      '
description: 'Identifikator der Legislaturperiode, zu der die Session gehört.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
range: string

```
</details></div>