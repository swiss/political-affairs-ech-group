

## Klasse: PrefaceP 


_Ein Vorspann-Absatz (akn:p), der Dokumentnummer und/oder -titel umschliesst. Fedlex verlangt akn:docNumber und akn:docTitle innerhalb eines akn:p des Vorspanns (FLX-PF-001/002)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| doc_number | 0..1 <br/> [String](String.md) | Dokumentnummer im Vorspann (akn:docNumber). Pflicht gemäss FLX-PF-001. Typischerweise die SR-Nummer, z.B. '101'.  |
| doc_title | 0..1 <br/> [MixedText](MixedText.md) | Dokumenttitel im Vorspann (akn:docTitle). Pflicht gemäss FLX-PF-002. Kann Inline-Markup und akn:br für Zeilenumbrüche enthalten.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preface](Preface.md) | [preface_paragraphs](preface_paragraphs.md) | range | [PrefaceP](PrefaceP.md) |



















</div>