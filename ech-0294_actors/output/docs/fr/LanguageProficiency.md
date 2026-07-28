

## Classe: LanguageProficiency 


_Compétences linguistiques d'une personne indiquant la langue et le fait qu'il s'agisse ou non de la langue préférée ou de la langue maternelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| language | 1 <br/> [String](String.md) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |
| is_correspondence | 0..1 <br/> [Boolean](Boolean.md) | Indique s'il s'agit de la langue préférée.  |
| is_native | 0..1 <br/> [Boolean](Boolean.md) | Indique s'il s'agit de la langue maternelle.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [language_proficiencies](language_proficiencies.md) | range | [LanguageProficiency](LanguageProficiency.md) |



















</div>