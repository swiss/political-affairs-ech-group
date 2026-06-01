

## Class: Gender 


_Gender of a person indicating a gender code and temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| gender_code | 0..1 <br/> [String](String.md) | Gender code (e.g., according to ISO 5218).  |
| pronouns | * <br/> [String](String.md) | Pronouns used by the person.  |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [genders](genders.md) | range | [Gender](Gender.md) |



















</div>