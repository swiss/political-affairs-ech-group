---
search:
  boost: 5.0
---

# Slot: fedlex_generator 


_Fedlex-Erweiterungsattribut fedlex:generator bei akn:FRBRformat[@value='xml']. Identifiziert das Werkzeug, das die XML-Datei erzeugt hat. Nur bei FRBRformat erlaubt (FLX-XF-002)._




<div data-search-exclude markdown="1">



URI: [laws:fedlex_generator](https://ld.ech.ch/schema/0296/laws/fedlex_generator)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FormatType](FormatType.md) | Halter für akn:FRBRformat: ein @value (typischerweise 'xml') plus das optiona... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [FormatType](FormatType.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: fedlex_generator
annotations:
  description_de:
    tag: description_de
    value: 'Fedlex-Erweiterungsattribut fedlex:generator bei akn:FRBRformat[@value=''xml''].
      Identifiziert das Werkzeug, das die XML-Datei erzeugt hat. Nur bei FRBRformat
      erlaubt (FLX-XF-002).

      '
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: fedlex:generator
  xml_namespace:
    tag: xml_namespace
    value: http://fedlex.admin.ch/
  schematron_rule:
    tag: schematron_rule
    value: 'FLX-XF-002: generator only allowed on FRBRformat[@value=''xml'']'
description: 'Fedlex-Erweiterungsattribut fedlex:generator bei akn:FRBRformat[@value=''xml''].
  Identifiziert das Werkzeug, das die XML-Datei erzeugt hat. Nur bei FRBRformat erlaubt
  (FLX-XF-002).

  '
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FormatType
range: string

```
</details></div>