

# Slot: weight 


_[en] The number of votes held by the individual, if applicable (e.g., in cases where a person has multiple votes)._

_[de] Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B. in Fällen, in denen eine Person mehrere Stimmen hat)._

__





URI: [ops:weight](https://ch.paf.link/schema/operations/weight)
Alias: weight

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:weight |
| native | ops:weight |




## LinkML Source

<details>
```yaml
name: weight
description: '[en] The number of votes held by the individual, if applicable (e.g.,
  in cases where a person has multiple votes).

  [de] Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B. in
  Fällen, in denen eine Person mehrere Stimmen hat).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: weight
domain_of:
- IndividualVote
range: integer

```
</details>