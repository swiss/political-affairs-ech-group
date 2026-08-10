

## Klasse: Expression 


_FRBR Expression: eine konkrete Sprachfassung eines Works._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| id | 1 <br/> [String](String.md) | Eindeutiger Identifikator des Elements.  |
| dates | * <br/> [Date](Date.md) | Datumsangaben zum Element, jeweils mit Typangabe.  |
| expression_language | 1 <br/> [String](String.md) | Sprachcode im ISO 639-1-Format.  |
| expression_title | 1 <br/> [String](String.md) | Titel der Sprachfassung.  |
| expression_description | 0..1 <br/> [String](String.md) | Beschreibender Text zur Sprachfassung.  |
| manifestations | * <br/> [Manifestation](Manifestation.md) | Die Dateiformen (Manifestations) einer Expression.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Work](Work.md) | [expressions](expressions.md) | range | [Expression](Expression.md) |



















</div>