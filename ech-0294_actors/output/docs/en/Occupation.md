

## Class: Occupation 


_Occupation or profession of a person indicating a label, an ISCO-19 code, whether the activity is paid, and temporal validity._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the activity is paid.  |
| occupation_code | 0..1 <br/> [String](String.md) | ISCO-19 code of the occupation.  |
| label | 0..1 <br/> [String](String.md) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| organization_uid | 0..1 <br/> [String](String.md) | UID of the organization from the federal UID register (uid.admin.ch), in the exchange format of eCH-0108: CHE followed by nine digits, without separators (e.g. CHE106063525). The last digit is a check digit calculated modulo 11. The dotted form CHE-106.063.525 is the presentation used by uid.admin.ch and is not recorded here.  |
| organization_name | 0..1 <br/> [String](String.md) | Name of the organization or enterprise.  |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |

##### Constraints


At least one of the following must be set:

- [occupation_code](occupation_code.md)
- [label](label.md)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [occupations](occupations.md) | range | [Occupation](Occupation.md) |














### Examples
#### Example Occupation: swiss politicians Sofia Fisch Juristin

```yaml
label: Jurist*in
is_active: true

```
#### Example Occupation: swiss politicians Beat Jans Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>