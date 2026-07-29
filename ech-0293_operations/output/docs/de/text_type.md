---
search:
  boost: 5.0
---

# Slot: text_type 


_Typ des Textes (Rohfassung, bearbeitete Fassung)._




<div data-search-exclude markdown="1">



URI: [ops:text_type](https://ch.paf.link/schema/operations/text_type)
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
| final |





## LinkML-Quelle

<details>
```yaml
name: text_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ des Textes (Rohfassung, bearbeitete Fassung).

      '
  description_fr:
    tag: description_fr
    value: 'Type de texte (version brute, version éditée).

      '
description: 'Typ des Textes (Rohfassung, bearbeitete Fassung).

  '
examples:
- value: final
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>