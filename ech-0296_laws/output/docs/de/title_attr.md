---
search:
  boost: 5.0
---

# Slot: title_attr 


_Menschenlesbare Bezeichnung der ausgezeichneten Stelle (@title)._



<div data-search-exclude markdown="1">



URI: [laws:title_attr](https://ld.ech.ch/schema/0296/laws/title_attr)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [DocNumber](DocNumber.md) | Die Dokumentnummer im Vorspann |  no  |
| [DocTitle](DocTitle.md) | Der Dokumenttitel im Vorspann |  no  |
| [DocketNumber](DocketNumber.md) | Die Ordnungsnummer des Erlasses, wie sie kantonale Sammlungen führen |  no  |
| [ShortTitle](ShortTitle.md) | Der Kurztitel des Erlasses |  no  |
| [Abbr](Abbr.md) | Die Abkürzung des Erlasses |  no  |
| [DocDate](DocDate.md) | Ein Datum im Vorspann, mit dem maschinenlesbaren Wert in @date |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [DocNumber](DocNumber.md), [DocTitle](DocTitle.md), [DocketNumber](DocketNumber.md), [ShortTitle](ShortTitle.md), [Abbr](Abbr.md), [DocDate](DocDate.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| Abkürzung |
| Erlasstitel |
| Kurztitel |





## LinkML-Quelle

<details>
```yaml
name: title_attr
annotations:
  description_de:
    tag: description_de
    value: Menschenlesbare Bezeichnung der ausgezeichneten Stelle (@title).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: title
description: Menschenlesbare Bezeichnung der ausgezeichneten Stelle (@title).
examples:
- value: Abkürzung
- value: Erlasstitel
- value: Kurztitel
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- DocNumber
- DocTitle
- DocketNumber
- ShortTitle
- Abbr
- DocDate
range: string

```
</details></div>