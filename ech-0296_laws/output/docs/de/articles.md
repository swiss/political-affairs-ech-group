---
search:
  boost: 5.0
---

# Slot: articles 


_Artikel-Kindelemente (akn:article)._



<div data-search-exclude markdown="1">



URI: [laws:articles](https://ld.ech.ch/schema/0296/laws/articles)
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
| [Subsection](Subsection.md) | Unterabschnitt-Ebene (akn:subsection) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |
| [Transitional](Transitional.md) | Eine Übergangsbestimmung im Hauptteil eines Erlasses (akn:transitional) |  no  |
| [Proviso](Proviso.md) | Ein Vorbehalt im Hauptteil eines Erlasses (akn:proviso) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Article](Article.md) |
| Domäne von | [ActBody](ActBody.md), [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Section](Section.md), [Subsection](Subsection.md), [Level](Level.md), [Transitional](Transitional.md), [Proviso](Proviso.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: articles
annotations:
  description_de:
    tag: description_de
    value: Artikel-Kindelemente (akn:article).
description: Artikel-Kindelemente (akn:article).
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
- Subsection
- Level
- Transitional
- Proviso
range: Article
multivalued: true

```
</details></div>