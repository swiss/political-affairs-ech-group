---
search:
  boost: 5.0
---

# Slot: is_paid 


_Gibt an, ob die Position bezahlt ist._

__



<div data-search-exclude markdown="1">



URI: [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Boolean](Boolean.md) |
| Domäne von | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot-URI | [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| False |
| True |





## LinkML-Quelle

<details>
```yaml
name: is_paid
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Position bezahlt ist.

      '
description: 'Gibt an, ob die Position bezahlt ist.

  '
examples:
- value: 'False'
- value: 'True'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isPaid
domain_of:
- InterestLink
- Occupation
range: boolean

```
</details></div>