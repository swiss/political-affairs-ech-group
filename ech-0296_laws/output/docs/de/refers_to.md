---
search:
  boost: 5.0
---

# Slot: refers_to 


_Anker, der nennt, worauf sich das Element bezieht (@refersTo)._



<div data-search-exclude markdown="1">



URI: [laws:refers_to](https://ld.ech.ch/schema/0296/laws/refers_to)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [DateInline](DateInline.md) | Ein Datum im Fliesstext, mit dem maschinenlesbaren Wert in @date |  no  |
| [Role](Role.md) | Eine Rolle, die eine Person innehat, mit Verweis auf ihre Deklaration |  no  |
| [Person](Person.md) | Eine Person, mit Verweis auf ihre Deklaration und die innegehabte Rolle |  no  |
| [Citation](Citation.md) | Eine einzelne Erwägung |  no  |
| [TimeInterval](TimeInterval.md) | Ein Intervall zwischen zwei Daten |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [DateInline](DateInline.md), [Role](Role.md), [Person](Person.md), [Citation](Citation.md), [TimeInterval](TimeInterval.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: refers_to
annotations:
  description_de:
    tag: description_de
    value: Anker, der nennt, worauf sich das Element bezieht (@refersTo).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: refersTo
description: Anker, der nennt, worauf sich das Element bezieht (@refersTo).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- DateInline
- Role
- Person
- Citation
- TimeInterval
range: string

```
</details></div>