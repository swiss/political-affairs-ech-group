---
search:
  boost: 5.0
---

# Slot: date_type 


_Bedeutung des Datums (z.B. Erstpublikation, letzte Revision)._




<div data-search-exclude markdown="1">



URI: [meta:dateType](https://ch.paf.link/schema/meta/dateType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Date](Date.md) | Ein Datum mit Typangabe (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [DateTypesEnum](DateTypesEnum.md) |
| Domäne von | [Date](Date.md) |
| Slot-URI | [meta:dateType](https://ch.paf.link/schema/meta/dateType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |












## LinkML-Quelle

<details>
```yaml
name: date_type
annotations:
  description_de:
    tag: description_de
    value: 'Bedeutung des Datums (z.B. Erstpublikation, letzte Revision).

      '
  description_fr:
    tag: description_fr
    value: 'Signification de la date (p. ex. première publication, dernière révision).

      '
description: 'Bedeutung des Datums (z.B. Erstpublikation, letzte Revision).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dateType
domain_of:
- Date
range: DateTypesEnum
required: true

```
</details></div>