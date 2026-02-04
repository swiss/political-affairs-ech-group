

# Slot: paid 


_[en] Indicates if the position is paid._

_[de] Gibt an, ob die Position bezahlt ist._

__





URI: [act:paid](https://ch.paf.link/schema/actors/paid)
Alias: paid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |
| [Occupation](Occupation.md) |  |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:paid |
| native | act:paid |




## LinkML Source

<details>
```yaml
name: paid
description: '[en] Indicates if the position is paid.

  [de] Gibt an, ob die Position bezahlt ist.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: paid
domain_of:
- InterestLink
- Occupation
range: boolean

```
</details>