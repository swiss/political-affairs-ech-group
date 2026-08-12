---
search:
  boost: 5.0
---

# Slot: sections 


_Abschnitt-Kindelemente (akn:section)._



<div data-search-exclude markdown="1">



URI: [laws:sections](https://ld.ech.ch/schema/0296/laws/sections)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |  no  |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |  no  |
| [Part](Part.md) | Teil-Ebene eines Erlasses (akn:part) |  no  |
| [Chapter](Chapter.md) | Kapitel-Ebene eines Erlasses (akn:chapter) |  no  |
| [Subchapter](Subchapter.md) | Unterkapitel-Ebene (akn:subchapter) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Section](Section.md) |
| Domäne von | [ActBody](ActBody.md), [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Level](Level.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: sections
annotations:
  description_de:
    tag: description_de
    value: Abschnitt-Kindelemente (akn:section).
description: Abschnitt-Kindelemente (akn:section).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
- Book
- Title
- Part
- Chapter
- Subchapter
- Level
range: Section
multivalued: true

```
</details></div>