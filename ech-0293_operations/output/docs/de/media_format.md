---
search:
  boost: 5.0
---

# Slot: media_format 


_MIME-Typ der Mediendatei._




<div data-search-exclude markdown="1">



URI: [ops:media_format](https://ch.paf.link/schema/operations/media_format)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Speech](Speech.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| video/mp4 |





## LinkML-Quelle

<details>
```yaml
name: media_format
annotations:
  description_de:
    tag: description_de
    value: 'MIME-Typ der Mediendatei.

      '
  description_fr:
    tag: description_fr
    value: 'Type MIME du fichier média.

      '
description: 'MIME-Typ der Mediendatei.

  '
examples:
- value: video/mp4
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>