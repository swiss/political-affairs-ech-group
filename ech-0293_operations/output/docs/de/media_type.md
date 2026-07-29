---
search:
  boost: 5.0
---

# Slot: media_type 


_Art des Mediums (Audio, Video, Dokument)._




<div data-search-exclude markdown="1">



URI: [ops:media_type](https://ch.paf.link/schema/operations/media_type)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Speech](Speech.md), [Media](Media.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| video |





## LinkML-Quelle

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
description: 'Art des Mediums (Audio, Video, Dokument).

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