---
search:
  boost: 5.0
---

# Slot: group_label 


_Name of the body/group at time of linking._

__



<div data-search-exclude markdown="1">



URI: [mcm:groupLabel](https://ld.ech.ch/schema/0292/meta-common/groupLabel)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [PersonReference](PersonReference.md) |
| Slot-URI | [mcm:groupLabel](https://ld.ech.ch/schema/0292/meta-common/groupLabel) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: group_label
annotations:
  description_de:
    tag: description_de
    value: 'Name des Gremiums zum Zeitpunkt der Verknüpfung.

      '
description: 'Name of the body/group at time of linking.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:groupLabel
domain_of:
- PersonReference
range: string

```
</details></div>