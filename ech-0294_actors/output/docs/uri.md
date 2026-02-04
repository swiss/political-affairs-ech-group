

# Slot: uri 


_[en] Globally valid identifier (e.g., politics.ld.admin.ch/party/1)._

_[de] Global gültiger Identifikator (z.B. politics.ld.admin.ch/party/1)._

__





URI: [act:uri](https://ch.paf.link/schema/actors/uri)
Alias: uri

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [GroupReference](GroupReference.md) | Reference to a group acting in a specific role |  no  |
| [PersonReference](PersonReference.md) | Reference to a person acting in a specific role or function |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:uri |
| native | act:uri |




## LinkML Source

<details>
```yaml
name: uri
description: '[en] Globally valid identifier (e.g., politics.ld.admin.ch/party/1).

  [de] Global gültiger Identifikator (z.B. politics.ld.admin.ch/party/1).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: uri
domain_of:
- Group
- PersonReference
- GroupReference
range: uriorcurie

```
</details>