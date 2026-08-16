---
search:
  boost: 5.0
---

# Slot: date_attr 


_Das Datum, das dieses Element auszeichnet, nach ISO 8601 (@date)._



<div data-search-exclude markdown="1">



URI: [laws:date_attr](https://ld.ech.ch/schema/0296/laws/date_attr)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [DocDate](DocDate.md) | Ein Datum im Vorspann, mit dem maschinenlesbaren Wert in @date |  no  |
| [DateInline](DateInline.md) | Ein Datum im Fliesstext, mit dem maschinenlesbaren Wert in @date |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [DocDate](DocDate.md), [DateInline](DateInline.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_attr
annotations:
  description_de:
    tag: description_de
    value: Das Datum, das dieses Element auszeichnet, nach ISO 8601 (@date).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: date
description: Das Datum, das dieses Element auszeichnet, nach ISO 8601 (@date).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- DocDate
- DateInline
range: string

```
</details></div>