---
search:
  boost: 5.0
---

# Slot: text_segments 


_Sammlung von Textsegmenten (z.B. Wortprotokoll)._




<div data-search-exclude markdown="1">



URI: [ops:textSegment](https://ch.paf.link/schema/operations/textSegment)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [TextSegment](TextSegment.md) |
| Domäne von | [Protocol](Protocol.md) |
| Slot-URI | [ops:textSegment](https://ch.paf.link/schema/operations/textSegment) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: text_segments
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Textsegmenten (z.B. Wortprotokoll).

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble de segments de texte (p. ex. procès-verbal in extenso).

      '
description: 'Sammlung von Textsegmenten (z.B. Wortprotokoll).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:textSegment
domain_of:
- Protocol
range: TextSegment
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>