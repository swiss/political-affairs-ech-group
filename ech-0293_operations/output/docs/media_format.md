---
search:
  boost: 5.0
---

# Slot: media_format 


_MIME type of the media file_



<div data-search-exclude markdown="1">



URI: [ops:media_format](https://ch.paf.link/schema/operations/media_format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| video/mp4 |





## LinkML Source

<details>
```yaml
name: media_format
description: MIME type of the media file
examples:
- value: video/mp4
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>