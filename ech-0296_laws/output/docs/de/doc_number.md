---
search:
  boost: 5.0
---

# Slot: doc_number 


_Dokumentnummer im Vorspann (akn:docNumber). Pflicht gemäss FLX-PF-001. Typischerweise die SR-Nummer, z.B. '101'._




<div data-search-exclude markdown="1">



URI: [laws:doc_number](https://ld.ech.ch/schema/0296/laws/doc_number)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [PrefaceP](PrefaceP.md) | Ein Vorspann-Absatz (akn:p), der Dokumentnummer und/oder -titel umschliesst |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [PrefaceP](PrefaceP.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| 101 |
| 152.3  |





## LinkML-Quelle

<details>
```yaml
name: doc_number
annotations:
  description_de:
    tag: description_de
    value: 'Dokumentnummer im Vorspann (akn:docNumber). Pflicht gemäss FLX-PF-001.
      Typischerweise die SR-Nummer, z.B. ''101''.

      '
  xml_element:
    tag: xml_element
    value: akn:docNumber
description: 'Dokumentnummer im Vorspann (akn:docNumber). Pflicht gemäss FLX-PF-001.
  Typischerweise die SR-Nummer, z.B. ''101''.

  '
examples:
- value: '101'
- value: '152.3 '
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:docNumber
rank: 1000
domain_of:
- PrefaceP
range: string

```
</details></div>