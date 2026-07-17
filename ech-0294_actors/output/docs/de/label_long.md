---
search:
  boost: 5.0
---

# Slot: label_long 


_Assign an extended label to a structured piece of information (e.g., display name with title, position, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  yes  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Person](Person.md), [PersonReference](PersonReference.md) |
| Slot-URI | [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: label_long
annotations:
  description_de:
    tag: description_de
    value: 'Möglichkeit bei einer strukturierten Information, ein erweitertesLabel
      zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).

      '
description: 'Assign an extended label to a structured piece of information (e.g.,
  display name with title, position, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:labelLong
domain_of:
- Person
- PersonReference
range: string

```
</details></div>