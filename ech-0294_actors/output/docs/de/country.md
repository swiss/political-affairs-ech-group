---
search:
  boost: 5.0
---

# Slot: country 


_ISO 3166-1 alpha-2 Ländercode._

__



<div data-search-exclude markdown="1">



URI: [act:country](https://ld.ech.ch/schema/0294/actors/country)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Citizenship](Citizenship.md) | Staatsangehörigkeit (wird auch für Nationalität verwendet) einer Person unter... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Citizenship](Citizenship.md) |
| Slot-URI | [act:country](https://ld.ech.ch/schema/0294/actors/country) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
### Wertebeschränkungen

| Eigenschaft | Wert |
| --- | --- |
| Regex Pattern | `^[A-Z]{2}$` |











## Beispiele

| Wert |
| --- |
| CH |





## LinkML-Quelle

<details>
```yaml
name: country
annotations:
  description_de:
    tag: description_de
    value: 'ISO 3166-1 alpha-2 Ländercode.

      '
  description_fr:
    tag: description_fr
    value: 'Code de pays ISO 3166-1 alpha-2.

      '
description: 'ISO 3166-1 alpha-2 Ländercode.

  '
examples:
- value: CH
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:country
domain_of:
- Citizenship
range: string
pattern: ^[A-Z]{2}$

```
</details></div>