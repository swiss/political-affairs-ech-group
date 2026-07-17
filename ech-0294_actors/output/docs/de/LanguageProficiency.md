

## Klasse: LanguageProficiency 


_Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die bevorzugte Sprache oder die Muttersprache handelt._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| language | 0..1 <br/> [String](String.md) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| is_correspondence | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob es sich um die bevorzugte Sprache handelt.  |
| is_native | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob es sich um die Muttersprache handelt.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [language_proficiencies](language_proficiencies.md) | range | [LanguageProficiency](LanguageProficiency.md) |



















</div>