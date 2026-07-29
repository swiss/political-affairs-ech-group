---
search:
  boost: 5.0
---

# Slot: media_type 


_Type of media (audio, video, document)._




<div data-search-exclude markdown="1">



URI: [ops:media_type](https://ch.paf.link/schema/operations/media_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |
| [Media](Media.md) | Media files or documents (including protocols in PDF/HTML/WORD or links to au... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Speech](Speech.md), [Media](Media.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| video |





## LinkML Source

<details>
```yaml
name: media_type
annotations:
  description_de:
    tag: description_de
    value: 'Art des Mediums (Audio, Video, Dokument).

      '
  description_fr:
    tag: description_fr
    value: 'Type de média (audio, vidéo, document).

      '
description: 'Type of media (audio, video, document).

  '
examples:
- value: video
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
- Media
range: string

```
</details></div>