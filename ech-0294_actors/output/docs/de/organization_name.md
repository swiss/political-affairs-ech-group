---
search:
  boost: 5.0
---

# Slot: organization_name 


_Name der Organisation oder des Unternehmens._

__



<div data-search-exclude markdown="1">



URI: [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName)
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
| Wertebereich | [String](String.md) |
| Domäne von | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot-URI | [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: organization_name
annotations:
  description_de:
    tag: description_de
    value: 'Name der Organisation oder des Unternehmens.

      '
description: 'Name der Organisation oder des Unternehmens.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationName
domain_of:
- InterestLink
- Occupation
range: string

```
</details></div>