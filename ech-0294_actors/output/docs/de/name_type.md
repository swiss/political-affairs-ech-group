---
search:
  boost: 5.0
---

# Slot: name_type 


_Typ des Namens gemäss eCH-0011 (personNameData)._

__



<div data-search-exclude markdown="1">



URI: [act:nameType](https://ld.ech.ch/schema/0294/actors/nameType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Name](Name.md) | Ein Name mit einem Typ (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [NameTypeEnum](NameTypeEnum.md) |
| Domäne von | [Name](Name.md) |
| Slot-URI | [act:nameType](https://ld.ech.ch/schema/0294/actors/nameType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| PersonFirstName |
| PersonOfficialName |





## LinkML-Quelle

<details>
```yaml
name: name_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ des Namens gemäss eCH-0011 (personNameData).

      '
description: 'Typ des Namens gemäss eCH-0011 (personNameData).

  '
examples:
- value: PersonFirstName
- value: PersonOfficialName
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:nameType
domain_of:
- Name
range: NameTypeEnum

```
</details></div>