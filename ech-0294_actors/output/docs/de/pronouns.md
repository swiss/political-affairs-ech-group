---
search:
  boost: 5.0
---

# Slot: pronouns 


_Von der Person verwendete Pronomen._

__



<div data-search-exclude markdown="1">



URI: [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Gender](Gender.md) |
| Slot-URI | [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: pronouns
annotations:
  description_de:
    tag: description_de
    value: 'Von der Person verwendete Pronomen.

      '
description: 'Von der Person verwendete Pronomen.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:pronouns
domain_of:
- Gender
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>