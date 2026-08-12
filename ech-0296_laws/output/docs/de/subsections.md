---
search:
  boost: 5.0
---

# Slot: subsections 


_Unterabschnitt-Kindelemente (akn:subsection)._



<div data-search-exclude markdown="1">



URI: [laws:subsections](https://ld.ech.ch/schema/0296/laws/subsections)
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
| [Section](Section.md) | Abschnitt-Ebene (akn:section) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Subsection](Subsection.md) |
| Domäne von | [ActBody](ActBody.md), [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Section](Section.md), [Level](Level.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: subsections
annotations:
  description_de:
    tag: description_de
    value: Unterabschnitt-Kindelemente (akn:subsection).
description: Unterabschnitt-Kindelemente (akn:subsection).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
- Book
- Title
- Part
- Chapter
- Subchapter
- Section
- Level
range: Subsection
multivalued: true

```
</details></div>