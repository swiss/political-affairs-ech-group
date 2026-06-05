---
search:
  boost: 5.0
---

# Slot: question 

<div data-search-exclude markdown="1">



URI: [tutorial:question](https://ch.paf.link/schema/tutorial/question)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vote](Vote.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Vote](Vote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| Soll die Farbe Auberginen-Oliv werden? |
| Soll die Farbe geändert werden? |
| Soll die Hymne geändert werden? |



## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:question |
| native | tutorial:question |




## LinkML Source

<details>
```yaml
name: question
examples:
- value: Soll die Farbe Auberginen-Oliv werden?
- value: Soll die Farbe geändert werden?
- value: Soll die Hymne geändert werden?
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
domain_of:
- Vote
range: string
required: true

```
</details></div>