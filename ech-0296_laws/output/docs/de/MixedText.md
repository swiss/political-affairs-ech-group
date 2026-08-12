

## Klasse: MixedText 


_Wiederverwendbarer Halter für gemischten Inhalt: eine geordnete Folge aus Text und Inline-Markup. Range für num, heading, subheading, listIntroduction, docTitle; der umschliessende Elementname kommt vom referenzierenden Slot._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [PrefaceP](PrefaceP.md) | [doc_title](doc_title.md) | range | [MixedText](MixedText.md) |
| [Book](Book.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Book](Book.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Book](Book.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Title](Title.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Title](Title.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Title](Title.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Part](Part.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Part](Part.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Part](Part.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Chapter](Chapter.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Chapter](Chapter.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Chapter](Chapter.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Subchapter](Subchapter.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Subchapter](Subchapter.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Subchapter](Subchapter.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Section](Section.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Section](Section.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Section](Section.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Subsection](Subsection.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Subsection](Subsection.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Subsection](Subsection.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Level](Level.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Level](Level.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Level](Level.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Article](Article.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Article](Article.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Article](Article.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Subdivision](Subdivision.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Subdivision](Subdivision.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Subdivision](Subdivision.md) | [subheading](subheading.md) | range | [MixedText](MixedText.md) |
| [Paragraph](Paragraph.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Paragraph](Paragraph.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Transitional](Transitional.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Transitional](Transitional.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [Proviso](Proviso.md) | [num](num.md) | range | [MixedText](MixedText.md) |
| [Proviso](Proviso.md) | [heading](heading.md) | range | [MixedText](MixedText.md) |
| [BlockList](BlockList.md) | [list_introduction](list_introduction.md) | range | [MixedText](MixedText.md) |
| [BlockListItem](BlockListItem.md) | [num](num.md) | range | [MixedText](MixedText.md) |



















</div>