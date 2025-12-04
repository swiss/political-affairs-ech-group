

# Slot: seat_nr 


_[en] The seat number of the individual vote, if applicable._

_[de] Die Sitznummer der Einzelstimme, falls zutreffend._

__





URI: [ops:seat_nr](https://ch.paf.link/schema/operations/seat_nr)
Alias: seat_nr

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:seat_nr |
| native | ops:seat_nr |




## LinkML Source

<details>
```yaml
name: seat_nr
description: '[en] The seat number of the individual vote, if applicable.

  [de] Die Sitznummer der Einzelstimme, falls zutreffend.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: seat_nr
domain_of:
- IndividualVote
range: string

```
</details>