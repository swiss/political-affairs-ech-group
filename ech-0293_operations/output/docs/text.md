---
search:
  boost: 5.0
---

# Slot: text 

<div data-search-exclude markdown="1">



URI: [ops:text](https://ch.paf.link/schema/operations/text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |  no  |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Speech](Speech.md), [TextSegment](TextSegment.md), [MultilingualString](MultilingualString.md) |

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
| self | ops:text |
| native | ops:text |




## LinkML Source

<details>
```yaml
name: text
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
- TextSegment
- MultilingualString
range: string
required: true

```
</details></div>