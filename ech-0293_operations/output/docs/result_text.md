

# Slot: result_text 


_[en] Free text describing the outcome of the vote, e.g., "Accepted with 78 votes"._

_[de] Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. "Mit 78 Stimmen angenommen"._

__





URI: [ops:result_text](https://ch.paf.link/schema/operations/result_text)
Alias: result_text

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:result_text |
| native | ops:result_text |




## LinkML Source

<details>
```yaml
name: result_text
description: '[en] Free text describing the outcome of the vote, e.g., "Accepted with
  78 votes".

  [de] Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. "Mit 78 Stimmen
  angenommen".

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: result_text
domain_of:
- Voting
- Election
range: string

```
</details>