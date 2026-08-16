---
search:
  boost: 5.0
---

# Slot: act_name 


_Typ des Erlasses (akn:act/@name). Die zulässigen Werte von ActTypeEnum sind die von Fedlex verwendeten; kantonale Sammlungen benennen eigene Typen, weshalb eine freie Zeichenkette zulässig bleibt._




<div data-search-exclude markdown="1">



URI: [laws:act_name](https://ld.ech.ch/schema/0296/laws/act_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Act](Act.md) | Das Erlasselement (akn:act) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md)&nbsp;or&nbsp;<br />[ActTypeEnum](ActTypeEnum.md) |
| Domäne von | [Act](Act.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'ActTypeEnum'})
- AnonymousSlotExpression({'range': 'string'})

</details>










## Beispiele

| Wert |
| --- |
|  |
| Grunderlass |
| publicLaw |





## LinkML-Quelle

<details>
```yaml
name: act_name
annotations:
  description_de:
    tag: description_de
    value: 'Typ des Erlasses (akn:act/@name). Die zulässigen Werte von ActTypeEnum
      sind die von Fedlex verwendeten; kantonale Sammlungen benennen eigene Typen,
      weshalb eine freie Zeichenkette zulässig bleibt.

      '
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: name
description: 'Typ des Erlasses (akn:act/@name). Die zulässigen Werte von ActTypeEnum
  sind die von Fedlex verwendeten; kantonale Sammlungen benennen eigene Typen, weshalb
  eine freie Zeichenkette zulässig bleibt.

  '
examples:
- value: ''
- value: Grunderlass
- value: publicLaw
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Act
range: string
any_of:
- range: ActTypeEnum
- range: string

```
</details></div>