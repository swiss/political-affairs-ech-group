

# Slot: type_label 


_[en] Custom type label when standard type values don't apply._

_[de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen._

__





URI: [ops:type_label](https://ch.paf.link/schema/operations/type_label)
Alias: type_label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Resolution](Resolution.md) | [en] A resolutionor decision taken on an agenda item, including voting proced... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:type_label |
| native | ops:type_label |




## LinkML Source

<details>
```yaml
name: type_label
description: '[en] Custom type label when standard type values don''t apply.

  [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: type_label
domain_of:
- Resolution
- Voting
- IndividualVote
- Election
range: string

```
</details>