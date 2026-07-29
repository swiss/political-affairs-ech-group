---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_Der gesetzgebende Körper, auf dem die Sitzung basiert._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md) |

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
    value: 'Der gesetzgebende Körper, auf dem die Sitzung basiert.

      '
  description_fr:
    tag: description_fr
    value: 'La législature dans le cadre de laquelle la séance a lieu.

      '
description: 'Der gesetzgebende Körper, auf dem die Sitzung basiert.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>