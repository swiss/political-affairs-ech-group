---
search:
  boost: 5.0
---

# Slot: marker 


_Das gedruckte Zeichen eines Anmerkungsverweises (@marker)._



<div data-search-exclude markdown="1">



URI: [laws:marker](https://ld.ech.ch/schema/0296/laws/marker)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [NoteRef](NoteRef.md) | Verweis auf eine in den Metadaten gehaltene Anmerkung |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [NoteRef](NoteRef.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| 1 |
| 2 |
| 3 |





## LinkML-Quelle

<details>
```yaml
name: marker
annotations:
  description_de:
    tag: description_de
    value: Das gedruckte Zeichen eines Anmerkungsverweises (@marker).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: marker
description: Das gedruckte Zeichen eines Anmerkungsverweises (@marker).
examples:
- value: '1'
- value: '2'
- value: '3'
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- NoteRef
range: string

```
</details></div>