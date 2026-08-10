

## Class: Expression 


_FRBR Expression: a concrete language version of a Work._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| id | 1 <br/> [String](String.md) | Unique identifier of the element.  |
| dates | * <br/> [Date](Date.md) | Dates relating to the element, each with a type indication.  |
| expression_language | 1 <br/> [String](String.md) | Language code in ISO 639-1 format.  |
| expression_title | 1 <br/> [String](String.md) | Title of the language version.  |
| expression_description | 0..1 <br/> [String](String.md) | Descriptive text of the language version.  |
| manifestations | * <br/> [Manifestation](Manifestation.md) | The file forms (Manifestations) of an Expression.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Work](Work.md) | [expressions](expressions.md) | range | [Expression](Expression.md) |



















</div>