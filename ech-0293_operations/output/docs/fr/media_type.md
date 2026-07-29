---
search:
  boost: 5.0
---

# Slot: media_type 


_Type de média (audio, vidéo, document)._




<div data-search-exclude markdown="1">



URI: [ops:media_type](https://ch.paf.link/schema/operations/media_type)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [Media](Media.md) | Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD o... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Speech](Speech.md), [Media](Media.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| video |





## Source LinkML

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
description: 'Type de média (audio, vidéo, document).

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