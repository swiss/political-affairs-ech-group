---
search:
  boost: 5.0
---

# Slot: chapters 


_Kapitel-Kindelemente (akn:chapter)._



<div data-search-exclude markdown="1">



URI: [laws:chapters](https://ld.ech.ch/schema/0296/laws/chapters)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |  no  |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |  no  |
| [Part](Part.md) | Teil-Ebene eines Erlasses (akn:part) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Chapter](Chapter.md) |
| Domäne von | [ActBody](ActBody.md), [Book](Book.md), [Title](Title.md), [Part](Part.md), [Level](Level.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: chapters
annotations:
  description_de:
    tag: description_de
    value: Kapitel-Kindelemente (akn:chapter).
description: Kapitel-Kindelemente (akn:chapter).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
- Book
- Title
- Part
- Level
range: Chapter
multivalued: true

```
</details></div>