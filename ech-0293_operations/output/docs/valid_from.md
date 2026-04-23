

# Slot: valid_from 


_[de] Das Datum, ab dem die Information gültig ist._

_[en] The date from which the information is valid._

__





URI: [schema:validFrom](http://schema.org/validFrom)
Alias: valid_from

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
| Slot URI | [schema:validFrom](http://schema.org/validFrom) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:validFrom |
| native | ops:valid_from |




## LinkML Source

<details>
```yaml
name: valid_from
description: '[de] Das Datum, ab dem die Information gültig ist.

  [en] The date from which the information is valid.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: schema:validFrom
alias: valid_from
domain_of:
- HasTemporalValidity
range: date

```
</details>