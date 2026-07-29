---
search:
  boost: 5.0
---

# Slot: media_url 


_URL to media file (audio/video)._




<div data-search-exclude markdown="1">



URI: [ops:media_url](https://ch.paf.link/schema/operations/media_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: media_url
annotations:
  description_de:
    tag: description_de
    value: 'URL zur Mediendatei (Audio/Video).

      '
  description_fr:
    tag: description_fr
    value: 'URL du fichier média (audio/vidéo).

      '
description: 'URL to media file (audio/video).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>