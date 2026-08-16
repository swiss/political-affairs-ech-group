---
search:
  boost: 5.0
---

# Slot: end_ref 


_Anker des Datums, an dem das Intervall endet (@end); leer, solange es offen ist._



<div data-search-exclude markdown="1">



URI: [laws:end_ref](https://ld.ech.ch/schema/0296/laws/end_ref)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TimeInterval](TimeInterval.md) | Ein Intervall zwischen zwei Daten |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [TimeInterval](TimeInterval.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: end_ref
annotations:
  description_de:
    tag: description_de
    value: Anker des Datums, an dem das Intervall endet (@end); leer, solange es offen
      ist.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: end
description: Anker des Datums, an dem das Intervall endet (@end); leer, solange es
  offen ist.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- TimeInterval
range: string

```
</details></div>