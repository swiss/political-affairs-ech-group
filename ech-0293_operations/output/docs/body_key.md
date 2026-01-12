

# Slot: body_key 


_[en] Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland)._

_[de] Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit (z.B. BE für Bern, CHE für Schweiz)._

__





URI: [ops:body_key](https://ch.paf.link/schema/operations/body_key)
Alias: body_key

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:body_key |
| native | ops:body_key |




## LinkML Source

<details>
```yaml
name: body_key
description: '[en] Key identifying the political body or jurisdiction (e.g., BE for
  Bern, CHE for Switzerland).

  [de] Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit
  (z.B. BE für Bern, CHE für Schweiz).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: body_key
domain_of:
- Session
- Meeting
range: string

```
</details>