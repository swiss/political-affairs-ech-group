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
| [DocNumber](DocNumber.md) | Die Dokumentnummer im Vorspann |  no  |
| [DocTitle](DocTitle.md) | Der Dokumenttitel im Vorspann |  no  |
| [DocketNumber](DocketNumber.md) | Die Ordnungsnummer des Erlasses, wie sie kantonale Sammlungen führen |  no  |
| [ShortTitle](ShortTitle.md) | Der Kurztitel des Erlasses |  no  |
| [Abbr](Abbr.md) | Die Abkürzung des Erlasses |  no  |
| [DocDate](DocDate.md) | Ein Datum im Vorspann, mit dem maschinenlesbaren Wert in @date |  no  |
| [DateInline](DateInline.md) | Ein Datum im Fliesstext, mit dem maschinenlesbaren Wert in @date |  no  |
| [Signature](Signature.md) | Eine Unterschriftszeile |  no  |
| [Conclusions](Conclusions.md) | Die Schlussformel eines Erlasses: Ort, Datum und Unterschriften |  no  |
| [Note](Note.md) | Eine einzelne Anmerkung |  no  |
| [TLCConcept](TLCConcept.md) | Ein Begriff, auf den das Dokument verweist (akn:TLCConcept), etwa ein zeitlic... |  no  |
| [OriginalRef](OriginalRef.md) | Verweis auf die ursprüngliche Fassung des Erlasses (akn:original) |  no  |
| [ComponentRef](ComponentRef.md) | Verweis auf einen anderswo gehaltenen Dokumentbestandteil (akn:componentRef) |  no  |
| [Def](Def.md) | Ein im Text definierter Begriff |  no  |
| [NoteRef](NoteRef.md) | Verweis auf eine in den Metadaten gehaltene Anmerkung |  no  |
| [Role](Role.md) | Eine Rolle, die eine Person innehat, mit Verweis auf ihre Deklaration |  no  |
| [Person](Person.md) | Eine Person, mit Verweis auf ihre Deklaration und die innegehabte Rolle |  no  |
| [ActiveRef](ActiveRef.md) | Verweis auf einen Erlass, den dieses Dokument ändert |  no  |
| [Formula](Formula.md) | Eine Eingangs- oder Schlussformel des Vorspruchs (akn:formula) |  no  |
| [Citations](Citations.md) | Die Erwägungen des Vorspruchs — worauf sich der Erlass beruft |  no  |
| [Citation](Citation.md) | Eine einzelne Erwägung |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [EIdType](EIdType.md) |
| Domäne von | [TLCOrganization](TLCOrganization.md), [TLCRole](TLCRole.md), [TLCReference](TLCReference.md), [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Section](Section.md), [Subsection](Subsection.md), [Level](Level.md), [Article](Article.md), [Subdivision](Subdivision.md), [Paragraph](Paragraph.md), [Transitional](Transitional.md), [Proviso](Proviso.md), [BlockList](BlockList.md), [BlockListItem](BlockListItem.md), [MixedText](MixedText.md), [DocNumber](DocNumber.md), [DocTitle](DocTitle.md), [DocketNumber](DocketNumber.md), [ShortTitle](ShortTitle.md), [Abbr](Abbr.md), [DocDate](DocDate.md), [DateInline](DateInline.md), [Signature](Signature.md), [Conclusions](Conclusions.md), [Note](Note.md), [TLCConcept](TLCConcept.md), [OriginalRef](OriginalRef.md), [ComponentRef](ComponentRef.md), [Def](Def.md), [NoteRef](NoteRef.md), [Role](Role.md), [Person](Person.md), [ActiveRef](ActiveRef.md), [Formula](Formula.md), [Citations](Citations.md), [Citation](Citation.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| JI |
| SK |
| SK-Publ |





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
- value: JI
- value: SK
- value: SK-Publ
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
- DocNumber
- DocTitle
- DocketNumber
- ShortTitle
- Abbr
- DocDate
- DateInline
- Signature
- Conclusions
- Note
- TLCConcept
- OriginalRef
- ComponentRef
- Def
- NoteRef
- Role
- Person
- ActiveRef
- Formula
- Citations
- Citation
range: EIdType

```
</details></div>