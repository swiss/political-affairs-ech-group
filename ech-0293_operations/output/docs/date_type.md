

# Slot: date_type 



URI: [meta:dateType](https://ch.paf.link/schema/meta/dateType)
Alias: date_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Date](Date.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DateTypesEnum](DateTypesEnum.md) |
| Domain Of | [Date](Date.md) |
| Slot URI | [meta:dateType](https://ch.paf.link/schema/meta/dateType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | meta:dateType |
| native | ops:date_type |




## LinkML Source

<details>
```yaml
name: date_type
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dateType
alias: date_type
domain_of:
- Date
range: DateTypesEnum
required: true

```
</details>