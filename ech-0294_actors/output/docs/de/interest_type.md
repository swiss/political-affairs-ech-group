---
search:
  boost: 5.0
---

# Slot: interest_type 


_Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein)._

__



<div data-search-exclude markdown="1">



URI: [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [InterestTypeEnum](InterestTypeEnum.md) |
| Domäne von | [InterestLink](InterestLink.md) |
| Slot-URI | [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |









## Beispiele

| Wert |
| --- |
| association |
| professional_activity |





## LinkML-Quelle

<details>
```yaml
name: interest_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).

      '
description: 'Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).

  '
examples:
- value: association
- value: professional_activity
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestType
domain_of:
- InterestLink
range: InterestTypeEnum
required: true

```
</details></div>