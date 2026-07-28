---
search:
  boost: 5.0
---

# Slot: picture 


_Link to an image (preferred: PNG, then JPG, then GIF)._

__



<div data-search-exclude markdown="1">



URI: [act:picture](https://ld.ech.ch/schema/0294/actors/picture)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Person](Person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: picture
annotations:
  description_de:
    tag: description_de
    value: 'Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF).

      '
  description_fr:
    tag: description_fr
    value: 'Lien vers une image (de préférence : PNG, puis JPG, puis GIF).

      '
description: 'Link to an image (preferred: PNG, then JPG, then GIF).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- Person
range: uri

```
</details></div>