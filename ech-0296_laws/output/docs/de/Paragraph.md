

## Klasse: Paragraph 


_Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph). Constraints (FLX-PR-*): - nur Überschriften-Elemente und akn:content als Kinder erlaubt (FLX-PR-001) - nur als direktes Kind von akn:article oder akn:subdivision erlaubt (FLX-PR-002) - benötigt eindeutiges @eId (FLX-PR-003)_




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](MixedText.md) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](MixedText.md) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| content_ref | 0..1 <br/> [Content](Content.md) | Inhaltselement innerhalb eines Absatzes (akn:content). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Article](Article.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |
| [Subdivision](Subdivision.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |
| [Transitional](Transitional.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |
| [Proviso](Proviso.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |



















</div>