

## Class: ElectoralDistrict 


_Electoral district or region where a person is politically active; with temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| district | 0..1 <br/> [String](String.md) | Electoral district or region.  |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |














### Examples
#### Example: ElectoralDistrict-swiss_politicians_Beat_Jans_1

```yaml
district: Basel-Stadt
valid_from: 2010-01-01

```






</div>