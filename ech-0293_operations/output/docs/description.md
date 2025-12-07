

# Slot: description 



URI: [ops:description](https://ch.paf.link/schema/operations/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:description |
| native | ops:description |




## LinkML Source

<details>
```yaml
name: description
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: description
domain_of:
- Legislature
- Meeting
- Motion
range: string

```
</details>