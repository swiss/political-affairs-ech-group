---
search:
  boost: 5.0
---

# Slot: expression_language 


_[en] Language code in ISO 639-1 format._

_[de] Sprachcode im ISO 639-1-Format._

__



<div data-search-exclude markdown="1">



URI: [dcterms:language](http://purl.org/dc/terms/language)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Expression](Expression.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Expression](Expression.md) |
| Slot URI | [dcterms:language](http://purl.org/dc/terms/language) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |














## LinkML Source

<details>
```yaml
name: expression_language
description: '[en] Language code in ISO 639-1 format.

  [de] Sprachcode im ISO 639-1-Format.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: dcterms:language
domain_of:
- Expression
range: string
required: true
pattern: ^[a-z]{2}$

```
</details></div>