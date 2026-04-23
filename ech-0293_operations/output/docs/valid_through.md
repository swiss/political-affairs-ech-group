

# Slot: valid_through 


_[de] Das Datum, bis und mit dem die Information gültig ist._

_[en] The date until which the information is valid, inclusive._

__





URI: [schema:validThrough](http://schema.org/validThrough)
Alias: valid_through

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gülti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot URI | [schema:validThrough](http://schema.org/validThrough) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:validThrough |
| native | ops:valid_through |




## LinkML Source

<details>
```yaml
name: valid_through
description: '[de] Das Datum, bis und mit dem die Information gültig ist.

  [en] The date until which the information is valid, inclusive.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: schema:validThrough
alias: valid_through
domain_of:
- HasTemporalValidity
range: date

```
</details>