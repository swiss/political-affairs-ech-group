---
search:
  boost: 5.0
---

# Slot: value 


_Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc._




<div data-search-exclude markdown="1">



URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [MultilingualValue](MultilingualValue.md) | Ein mehrsprachiger String mit Angabe der Sprache |  yes  |
| [MultilingualUri](MultilingualUri.md) | Eine URI zusammen mit der Sprache der Ressource, auf die sie verweist |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [MultilingualValue](MultilingualValue.md), [MultilingualUri](MultilingualUri.md) |
| Slot-URI | [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: value
annotations:
  description_de:
    tag: description_de
    value: 'Der eigentliche Wert einer Information neben weiteren attributen wie Typ,
      Sprache, etc.

      '
  description_fr:
    tag: description_fr
    value: 'La valeur proprement dite d''une information, en plus d''autres attributs
      tels que le type, la langue, etc.

      '
description: 'Der eigentliche Wert einer Information neben weiteren attributen wie
  Typ, Sprache, etc.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:value
domain_of:
- MultilingualValue
- MultilingualUri
range: string

```
</details></div>