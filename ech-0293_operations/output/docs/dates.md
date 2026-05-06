

# Slot: dates 



URI: [meta:dates](https://ch.paf.link/schema/meta/dates)
Alias: dates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manifestation](Manifestation.md) |  |  no  |
| [Expression](Expression.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Expression](Expression.md), [Manifestation](Manifestation.md) |
| Slot URI | [meta:dates](https://ch.paf.link/schema/meta/dates) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | meta:dates |
| native | ops:dates |




## LinkML Source

<details>
```yaml
name: dates
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dates
alias: dates
domain_of:
- Expression
- Manifestation
range: Date
multivalued: true
inlined: true
inlined_as_list: true

```
</details>