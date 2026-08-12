

## Klasse: Level 


_Transparente Strukturebene (akn:level). Ein level ist 'transparent': erlaubte Kinder entsprechen denen des nächsten nicht-level-Vorfahren (FLX-HR-001-lv). Ein level mit akn:content ist nur erlaubt, wenn der Inhalt ein Änderungselement (akn:mod) enthält (FLX-HR-003). fedlex:role='marginal' kennzeichnet es als Randnote (FLX-XF-004). Benötigt eindeutiges @eId (FLX-HR-002-lv, FLX-HR-004)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](MixedText.md) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](MixedText.md) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](MixedText.md) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| fedlex_role | 0..1 <br/> [FedlexRoleEnum](FedlexRoleEnum.md) | Wenn gesetzt, muss der Wert 'marginal' sein (FLX-XF-004). Der Wert 'reference' ist bei level nicht erlaubt; er ist für subheading reserviert (FLX-XF-005).  |
| content_ref | 0..1 <br/> [Content](Content.md) | Inhaltselement innerhalb eines Absatzes (akn:content). |
| books | * <br/> [Book](Book.md) | Buch-Kindelemente (akn:book). |
| titles | * <br/> [Title](Title.md) | Titel-Kindelemente (akn:title). |
| parts | * <br/> [Part](Part.md) | Teil-Kindelemente (akn:part). |
| chapters | * <br/> [Chapter](Chapter.md) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](Subchapter.md) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](Section.md) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](Subsection.md) | Unterabschnitt-Kindelemente (akn:subsection). |
| articles | * <br/> [Article](Article.md) | Artikel-Kindelemente (akn:article). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](ActBody.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Book](Book.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Title](Title.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Part](Part.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Chapter](Chapter.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Subchapter](Subchapter.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Section](Section.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Subsection](Subsection.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Transitional](Transitional.md) | [levels](levels.md) | range | [Level](Level.md) |
| [Proviso](Proviso.md) | [levels](levels.md) | range | [Level](Level.md) |



















</div>