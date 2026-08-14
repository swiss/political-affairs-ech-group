---
search:
  boost: 5.0
---

# Slot: num 


_Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003)._




<div data-search-exclude markdown="1">



URI: [laws:num](https://ld.ech.ch/schema/0296/laws/num)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |  no  |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |  no  |
| [Part](Part.md) | Teil-Ebene eines Erlasses (akn:part) |  no  |
| [Chapter](Chapter.md) | Kapitel-Ebene eines Erlasses (akn:chapter) |  no  |
| [Subchapter](Subchapter.md) | Unterkapitel-Ebene (akn:subchapter) |  no  |
| [Section](Section.md) | Abschnitt-Ebene (akn:section) |  no  |
| [Subsection](Subsection.md) | Unterabschnitt-Ebene (akn:subsection) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |
| [Article](Article.md) | Ein Artikel, die primäre legislative Einheit (akn:article) |  yes  |
| [Subdivision](Subdivision.md) | Ein Unterabschnitt in einem Artikel, der zusammengehörige Absätze gruppiert (... |  no  |
| [Paragraph](Paragraph.md) | Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph) |  no  |
| [Transitional](Transitional.md) | Eine Übergangsbestimmung im Hauptteil eines Erlasses (akn:transitional) |  no  |
| [Proviso](Proviso.md) | Ein Vorbehalt im Hauptteil eines Erlasses (akn:proviso) |  no  |
| [BlockListItem](BlockListItem.md) | Ein einzelner Punkt in einer Auflistung (akn:item) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MixedText](MixedText.md) |
| Domäne von | [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Section](Section.md), [Subsection](Subsection.md), [Level](Level.md), [Article](Article.md), [Subdivision](Subdivision.md), [Paragraph](Paragraph.md), [Transitional](Transitional.md), [Proviso](Proviso.md), [BlockListItem](BlockListItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: num
annotations:
  description_de:
    tag: description_de
    value: 'Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num).
      Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading
      stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).

      '
  schematron_rules:
    tag: schematron_rules
    value: 'FLX-HD-001: max one num; FLX-HD-002: num before heading; FLX-HD-003: num
      before subheading'
description: 'Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num).
  Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen
  (FLX-HD-001, FLX-HD-002, FLX-HD-003).

  '
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:num
rank: 1000
domain_of:
- Book
- Title
- Part
- Chapter
- Subchapter
- Section
- Subsection
- Level
- Article
- Subdivision
- Paragraph
- Transitional
- Proviso
- BlockListItem
range: MixedText

```
</details></div>