

# Slot: total_other 


_[en] Used when multiple options are presented for voting (e.g., 5 buttons in Zurich)._

_[de] Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B. 5 Knöpfe in Zürich)._

__





URI: [ops:total_other](https://ch.paf.link/schema/operations/total_other)
Alias: total_other

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

* Range: [TotalOther](TotalOther.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:total_other |
| native | ops:total_other |




## LinkML Source

<details>
```yaml
name: total_other
description: '[en] Used when multiple options are presented for voting (e.g., 5 buttons
  in Zurich).

  [de] Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B.
  5 Knöpfe in Zürich).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: total_other
domain_of:
- Voting
range: TotalOther
multivalued: true
inlined: true
inlined_as_list: true

```
</details>