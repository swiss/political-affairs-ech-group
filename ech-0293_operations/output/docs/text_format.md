---
search:
  boost: 5.0
---

# Slot: text_format 


_[en] Format of text (text, html, html_with_timestamps)_

_[de] Format des Textes (text, html, html_with_timestamps)_

__



<div data-search-exclude markdown="1">



URI: [ops:text_format](https://ch.paf.link/schema/operations/text_format)
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
| html |





## LinkML Source

<details>
```yaml
name: text_format
description: '[en] Format of text (text, html, html_with_timestamps)

  [de] Format des Textes (text, html, html_with_timestamps)

  '
examples:
- value: html
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>