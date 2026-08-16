

## Klasse: ActBody 


_Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie. Erlaubte direkte Kinder: book, title, part, chapter, subchapter, section, subsection, level, article, transitional, proviso. Keine anderen Elemente erlaubt (FLX-BD-001)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| period | 0..1 <br/> [String](String.md) | Die Zeitgruppe, in der die Änderung gilt (@period). |
| status | 0..1 <br/> [String](String.md) | Bearbeitungsstand des Elements (@status), z.B. „edited“. |
| books | * <br/> [Book](Book.md) | Buch-Kindelemente (akn:book). |
| titles | * <br/> [Title](Title.md) | Titel-Kindelemente (akn:title). |
| parts | * <br/> [Part](Part.md) | Teil-Kindelemente (akn:part). |
| chapters | * <br/> [Chapter](Chapter.md) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](Subchapter.md) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](Section.md) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](Subsection.md) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](Level.md) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](Article.md) | Artikel-Kindelemente (akn:article). |
| transitionals | * <br/> [Transitional](Transitional.md) | Übergangsbestimmungs-Elemente (akn:transitional). |
| provisos | * <br/> [Proviso](Proviso.md) | Vorbehalt-Elemente (akn:proviso). |
| component_refs | * <br/> [ComponentRef](ComponentRef.md) | Verweise auf anderswo gehaltene Bestandteile (akn:componentRef). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](Act.md) | [body](body.md) | range | [ActBody](ActBody.md) |



















</div>