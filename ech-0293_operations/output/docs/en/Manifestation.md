

## Class: Manifestation 


_FRBR Manifestation: a concrete file format of an Expression, addressable via a URL._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | Unique identifier of the element.  |
| dates | * <br/> [Date](Date.md) | Dates relating to the element, each with a type indication.  |
| format | 0..1 <br/> [String](String.md) | The file format of the manifestation (e.g., pdf, html).  |
| manifestation_url | 0..1 <br/> [Uri](Uri.md) | URL under which the file form can be retrieved.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Expression](Expression.md) | [manifestations](manifestations.md) | range | [Manifestation](Manifestation.md) |



















</div>