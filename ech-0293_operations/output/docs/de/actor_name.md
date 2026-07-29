---
search:
  boost: 5.0
---

# Slot: actor_name 


_Name des politischen Organs (z.B. Nationalrat)._




<div data-search-exclude markdown="1">



URI: [ops:actor_name](https://ch.paf.link/schema/operations/actor_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: actor_name
annotations:
  description_de:
    tag: description_de
    value: 'Name des politischen Organs (z.B. Nationalrat).

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organe politique (p. ex. Conseil national).

      '
description: 'Name des politischen Organs (z.B. Nationalrat).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>