---
search:
  boost: 5.0
---

# Slot: heading 


_Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005)._




<div data-search-exclude markdown="1">



URI: [laws:heading](https://ld.ech.ch/schema/0296/laws/heading)
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
| [Article](Article.md) | Ein Artikel, die primäre legislative Einheit (akn:article) |  no  |
| [Subdivision](Subdivision.md) | Ein Unterabschnitt in einem Artikel, der zusammengehörige Absätze gruppiert (... |  no  |
| [Paragraph](Paragraph.md) | Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph) |  no  |
| [Transitional](Transitional.md) | Eine Übergangsbestimmung im Hauptteil eines Erlasses (akn:transitional) |  no  |
| [Proviso](Proviso.md) | Ein Vorbehalt im Hauptteil eines Erlasses (akn:proviso) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MixedText](MixedText.md) |
| Domäne von | [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Section](Section.md), [Subsection](Subsection.md), [Level](Level.md), [Article](Article.md), [Subdivision](Subdivision.md), [Paragraph](Paragraph.md), [Transitional](Transitional.md), [Proviso](Proviso.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: heading
annotations:
  description_de:
    tag: description_de
    value: 'Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup
      einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt).
      Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).

      '
  xml_element:
    tag: xml_element
    value: akn:heading
  schematron_rules:
    tag: schematron_rules
    value: 'FLX-HD-004: max one heading; FLX-HD-005: heading before subheading; FLX-TXT-001:
      br permitted here

      '
description: 'Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup
  einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss
  vor subheading stehen (FLX-HD-004, FLX-HD-005).

  '
from_schema: https://ld.ech.ch/schema/0296/laws
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
range: MixedText

```
</details></div>