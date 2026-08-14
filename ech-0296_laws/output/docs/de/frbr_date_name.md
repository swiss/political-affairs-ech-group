---
search:
  boost: 5.0
---

# Slot: frbr_date_name 


_Datumstyp (akn:FRBRdate/@name), mit Fedlex/JoLux-Vokabular, z.B. 'jolux:dateEntryInForce', 'jolux:dateDocument', 'jolux:dateApplicability'._




<div data-search-exclude markdown="1">



URI: [laws:frbr_date_name](https://ld.ech.ch/schema/0296/laws/frbr_date_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRDate](FRBRDate.md) | Ein Datumseintrag einer FRBR-Entität (akn:FRBRdate) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [FRBRDate](FRBRDate.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| jolux:dateApplicability |
| jolux:dateDocument |
| jolux:dateEntryInForce |





## LinkML-Quelle

<details>
```yaml
name: frbr_date_name
annotations:
  description_de:
    tag: description_de
    value: 'Datumstyp (akn:FRBRdate/@name), mit Fedlex/JoLux-Vokabular, z.B. ''jolux:dateEntryInForce'',
      ''jolux:dateDocument'', ''jolux:dateApplicability''.

      '
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: name
description: 'Datumstyp (akn:FRBRdate/@name), mit Fedlex/JoLux-Vokabular, z.B. ''jolux:dateEntryInForce'',
  ''jolux:dateDocument'', ''jolux:dateApplicability''.

  '
examples:
- value: jolux:dateApplicability
- value: jolux:dateDocument
- value: jolux:dateEntryInForce
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRDate
range: string

```
</details></div>