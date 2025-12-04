

# Slot: administrative_id 


_[en] Administrative ID of the legislative body, such as a municipality, canton, or country._

_[de] Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land._

__





URI: [ops:administrative_id](https://ch.paf.link/schema/operations/administrative_id)
Alias: administrative_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:administrative_id |
| native | ops:administrative_id |




## LinkML Source

<details>
```yaml
name: administrative_id
description: '[en] Administrative ID of the legislative body, such as a municipality,
  canton, or country.

  [de] Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: administrative_id
domain_of:
- Legislature
- Meeting
range: string

```
</details>