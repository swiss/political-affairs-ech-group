---
search:
  boost: 5.0
---

# Slot: text 


_Text content of the element._




<div data-search-exclude markdown="1">



URI: [ops:text](https://ch.paf.link/schema/operations/text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |
| [TextSegment](TextSegment.md) | A text segment such as cross-references or subtitles in meeting protocols |  no  |
| [MultilingualString](MultilingualString.md) | A string that can contain text in multiple languages |  no  |






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












## LinkML Source

<details>
```yaml
name: text
annotations:
  description_de:
    tag: description_de
    value: 'Textinhalt des Elements.

      '
  description_fr:
    tag: description_fr
    value: 'Contenu textuel de l''élément.

      '
description: 'Text content of the element.

  '
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