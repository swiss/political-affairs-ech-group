

## Class: LanguageProficiency 


_Language proficiency of a person indicating the language and whether it is the preferred language or native language._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| language | 0..1 <br/> [String](String.md) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| is_correspondence | 0..1 <br/> [Boolean](Boolean.md) | Indicates if this is the preferred language.  |
| is_native | 0..1 <br/> [Boolean](Boolean.md) | Indicates if this is the native language.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [language_proficiencies](language_proficiencies.md) | range | [LanguageProficiency](LanguageProficiency.md) |



















</div>