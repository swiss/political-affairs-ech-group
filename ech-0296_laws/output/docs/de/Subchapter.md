

## Klasse: Subchapter 


_Unterkapitel-Ebene (akn:subchapter). Erlaubte Kinder: section, subsection, level, sowie direkt article (FLX-HR-001-sh). Benötigt eindeutiges @eId (FLX-HR-002-sh)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](MixedText.md) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](MixedText.md) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](MixedText.md) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| sections | * <br/> [Section](Section.md) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](Subsection.md) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](Level.md) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](Article.md) | Artikel-Kindelemente (akn:article). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](ActBody.md) | [subchapters](subchapters.md) | range | [Subchapter](Subchapter.md) |
| [Book](Book.md) | [subchapters](subchapters.md) | range | [Subchapter](Subchapter.md) |
| [Title](Title.md) | [subchapters](subchapters.md) | range | [Subchapter](Subchapter.md) |
| [Part](Part.md) | [subchapters](subchapters.md) | range | [Subchapter](Subchapter.md) |
| [Chapter](Chapter.md) | [subchapters](subchapters.md) | range | [Subchapter](Subchapter.md) |
| [Level](Level.md) | [subchapters](subchapters.md) | range | [Subchapter](Subchapter.md) |



















</div>