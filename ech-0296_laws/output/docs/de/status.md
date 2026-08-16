---
search:
  boost: 5.0
---

# Slot: status 


_Bearbeitungsstand des Elements (@status), z.B. „edited“._



<div data-search-exclude markdown="1">



URI: [laws:status](https://ld.ech.ch/schema/0296/laws/status)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [ActBody](ActBody.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: status
annotations:
  description_de:
    tag: description_de
    value: Bearbeitungsstand des Elements (@status), z.B. „edited“.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: status
description: Bearbeitungsstand des Elements (@status), z.B. „edited“.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
range: string

```
</details></div>