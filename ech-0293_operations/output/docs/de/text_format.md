---
search:
  boost: 5.0
---

# Slot: text_format 


_Format des Textes (text, html, html_with_timestamps)._




<div data-search-exclude markdown="1">



URI: [ops:text_format](https://ch.paf.link/schema/operations/text_format)
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
| html |





## LinkML-Quelle

<details>
```yaml
name: text_format
annotations:
  description_de:
    tag: description_de
    value: 'Format des Textes (text, html, html_with_timestamps).

      '
  description_fr:
    tag: description_fr
    value: 'Format du texte (text, html, html_with_timestamps).

      '
description: 'Format des Textes (text, html, html_with_timestamps).

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