

# Slot: organization_uid 


_[en] UID of the organization (for analysis with NOGA codes, etc.)._

_[de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.)._

__





URI: [act:organizationUid](https://ch.paf.link/schema/actors/organizationUid)
Alias: organization_uid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:organizationUid |
| native | act:organization_uid |




## LinkML Source

<details>
```yaml
name: organization_uid
description: '[en] UID of the organization (for analysis with NOGA codes, etc.).

  [de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:organizationUid
alias: organization_uid
domain_of:
- InterestLink
range: string

```
</details>