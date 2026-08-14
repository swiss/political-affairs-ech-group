---
search:
  boost: 5.0
---

# Slot: eId 


_Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'._




<div data-search-exclude markdown="1">



URI: [laws:eId](https://ld.ech.ch/schema/0296/laws/eId)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TLCOrganization](TLCOrganization.md) | Eine benannte Organisation als Referenz im Dokument (akn:TLCOrganization) |  no  |
| [TLCRole](TLCRole.md) | Eine benannte Rolle als Referenz im Dokument (akn:TLCRole) |  no  |
| [TLCReference](TLCReference.md) | Eine generische benannte Referenz im Dokument (akn:TLCReference) |  no  |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |  yes  |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |  yes  |
| [Part](Part.md) | Teil-Ebene eines Erlasses (akn:part) |  yes  |
| [Chapter](Chapter.md) | Kapitel-Ebene eines Erlasses (akn:chapter) |  yes  |
| [Subchapter](Subchapter.md) | Unterkapitel-Ebene (akn:subchapter) |  yes  |
| [Section](Section.md) | Abschnitt-Ebene (akn:section) |  yes  |
| [Subsection](Subsection.md) | Unterabschnitt-Ebene (akn:subsection) |  yes  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  yes  |
| [Article](Article.md) | Ein Artikel, die primäre legislative Einheit (akn:article) |  yes  |
| [Subdivision](Subdivision.md) | Ein Unterabschnitt in einem Artikel, der zusammengehörige Absätze gruppiert (... |  yes  |
| [Paragraph](Paragraph.md) | Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph) |  yes  |
| [Transitional](Transitional.md) | Eine Übergangsbestimmung im Hauptteil eines Erlasses (akn:transitional) |  yes  |
| [Proviso](Proviso.md) | Ein Vorbehalt im Hauptteil eines Erlasses (akn:proviso) |  yes  |
| [BlockList](BlockList.md) | Eine Auflistung von nummerierten oder buchstabierten Punkten (akn:blockList),... |  no  |
| [BlockListItem](BlockListItem.md) | Ein einzelner Punkt in einer Auflistung (akn:item) |  no  |
| [MixedText](MixedText.md) | Wiederverwendbarer Halter für gemischten Inhalt: eine geordnete Folge aus Tex... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [EIdType](EIdType.md) |
| Domäne von | [TLCOrganization](TLCOrganization.md), [TLCRole](TLCRole.md), [TLCReference](TLCReference.md), [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Section](Section.md), [Subsection](Subsection.md), [Level](Level.md), [Article](Article.md), [Subdivision](Subdivision.md), [Paragraph](Paragraph.md), [Transitional](Transitional.md), [Proviso](Proviso.md), [BlockList](BlockList.md), [BlockListItem](BlockListItem.md), [MixedText](MixedText.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| art_1 |
| art_1/para |
| art_2 |





## LinkML-Quelle

<details>
```yaml
name: eId
annotations:
  description_de:
    tag: description_de
    value: 'Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron
      gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen.
      Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. ''ti_1'',
      ''ch_1'', ''art_1'', ''art_1-para_1''.

      '
  xml_attribute:
    tag: xml_attribute
    value: 'true'
description: 'Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron
  gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen.
  Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. ''ti_1'',
  ''ch_1'', ''art_1'', ''art_1-para_1''.

  '
examples:
- value: art_1
- value: art_1/para
- value: art_2
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- TLCOrganization
- TLCRole
- TLCReference
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
- BlockList
- BlockListItem
- MixedText
range: EIdType

```
</details></div>