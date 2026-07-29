---
search:
  boost: 5.0
---

# Slot: text 


_Textinhalt des Elements._




<div data-search-exclude markdown="1">



URI: [ops:text](https://ch.paf.link/schema/operations/text)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |
| [TextSegment](TextSegment.md) | Ein Textsegment wie Querverweise oder Zwischentitel in Sitzungsprotokollen |  no  |
| [MultilingualString](MultilingualString.md) | Ein String, der Text in mehreren Sprachen enthalten kann |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Speech](Speech.md), [TextSegment](TextSegment.md), [MultilingualString](MultilingualString.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |












## LinkML-Quelle

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
description: 'Textinhalt des Elements.

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