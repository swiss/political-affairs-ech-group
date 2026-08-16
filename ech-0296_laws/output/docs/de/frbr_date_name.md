---
search:
  boost: 5.0
---

# Slot: frbr_date_name 


_Art dieses Datums (akn:FRBRdate/@name). Fedlex verwendet das JoLux-Vokabular; die zulässigen Werte von FrbrDateNameEnum tragen die entsprechende ELI-Eigenschaft. Kantonale Publikationsstellen führen eigene Bezeichnungen, weshalb eine freie Zeichenkette zulässig bleibt._




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
| Wertebereich | [String](String.md)&nbsp;or&nbsp;<br />[FrbrDateNameEnum](FrbrDateNameEnum.md) |
| Domäne von | [FRBRDate](FRBRDate.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'FrbrDateNameEnum'})
- AnonymousSlotExpression({'range': 'string'})

</details>










## Beispiele

| Wert |
| --- |
|  |
| jolux:dateApplicability |
| jolux:dateDocument |





## LinkML-Quelle

<details>
```yaml
name: frbr_date_name
annotations:
  description_de:
    tag: description_de
    value: 'Art dieses Datums (akn:FRBRdate/@name). Fedlex verwendet das JoLux-Vokabular;
      die zulässigen Werte von FrbrDateNameEnum tragen die entsprechende ELI-Eigenschaft.
      Kantonale Publikationsstellen führen eigene Bezeichnungen, weshalb eine freie
      Zeichenkette zulässig bleibt.

      '
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: name
description: 'Art dieses Datums (akn:FRBRdate/@name). Fedlex verwendet das JoLux-Vokabular;
  die zulässigen Werte von FrbrDateNameEnum tragen die entsprechende ELI-Eigenschaft.
  Kantonale Publikationsstellen führen eigene Bezeichnungen, weshalb eine freie Zeichenkette
  zulässig bleibt.

  '
examples:
- value: ''
- value: jolux:dateApplicability
- value: jolux:dateDocument
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRDate
range: string
any_of:
- range: FrbrDateNameEnum
- range: string

```
</details></div>