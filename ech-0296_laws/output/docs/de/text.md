---
search:
  boost: 5.0
---

# Slot: text 


_Die Zeichendaten eines TextRun; wird als Textknoten in gemischtem Inhalt ausgegeben._



<div data-search-exclude markdown="1">



URI: [laws:text](https://ld.ech.ch/schema/0296/laws/text)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TextRun](TextRun.md) | Ein einfacher Textabschnitt in gemischtem Inhalt |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [TextRun](TextRun.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| (Alters-, Hinterlassenen- und Invalidenversicherung) |
| (Art. 22) |
| (BB vom 18. Dez. 1998, BRB vom 11. Aug. 1999 – |





## LinkML-Quelle

<details>
```yaml
name: text
annotations:
  description_de:
    tag: description_de
    value: Die Zeichendaten eines TextRun; wird als Textknoten in gemischtem Inhalt
      ausgegeben.
  xsd_text:
    tag: xsd_text
    value: 'true'
description: Die Zeichendaten eines TextRun; wird als Textknoten in gemischtem Inhalt
  ausgegeben.
examples:
- value: (Alters-, Hinterlassenen- und Invalidenversicherung)
- value: (Art. 22)
- value: (BB vom 18. Dez. 1998, BRB vom 11. Aug. 1999 –
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- TextRun
range: string

```
</details></div>