---
search:
  boost: 5.0
---

# Slot: doc_title 


_Dokumenttitel im Vorspann (akn:docTitle). Pflicht gemäss FLX-PF-002. Kann Inline-Markup und akn:br für Zeilenumbrüche enthalten._




<div data-search-exclude markdown="1">



URI: [laws:doc_title](https://ld.ech.ch/schema/0296/laws/doc_title)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [PrefaceP](PrefaceP.md) | Ein Vorspann-Absatz (akn:p), der Dokumentnummer und/oder -titel umschliesst |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MixedText](MixedText.md) |
| Domäne von | [PrefaceP](PrefaceP.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: doc_title
annotations:
  description_de:
    tag: description_de
    value: 'Dokumenttitel im Vorspann (akn:docTitle). Pflicht gemäss FLX-PF-002. Kann
      Inline-Markup und akn:br für Zeilenumbrüche enthalten.

      '
  xml_element:
    tag: xml_element
    value: akn:docTitle
  schematron_note:
    tag: schematron_note
    value: 'FLX-TXT-001: br allowed in docTitle (heading context)'
description: 'Dokumenttitel im Vorspann (akn:docTitle). Pflicht gemäss FLX-PF-002.
  Kann Inline-Markup und akn:br für Zeilenumbrüche enthalten.

  '
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:docTitle
rank: 1000
domain_of:
- PrefaceP
range: MixedText

```
</details></div>