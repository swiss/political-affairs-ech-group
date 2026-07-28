---
search:
  boost: 5.0
---

# Slot: legal_form 


_Legal form of the organization. See controlled vocabulary: https://register.ld.admin.ch/i14y/concept/legalForm_

__



<div data-search-exclude markdown="1">



URI: [act:legalForm](https://ld.ech.ch/schema/0294/actors/legalForm)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LegalFormEnum](LegalFormEnum.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:legalForm](https://ld.ech.ch/schema/0294/actors/legalForm) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 0106 |
| 0107 |
| 0109 |





## LinkML Source

<details>
```yaml
name: legal_form
annotations:
  description_de:
    tag: description_de
    value: 'Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm

      '
  description_fr:
    tag: description_fr
    value: 'Forme juridique de l''organisation. Voir le vocabulaire contrôlé : https://register.ld.admin.ch/i14y/concept/legalForm

      '
description: 'Legal form of the organization. See controlled vocabulary: https://register.ld.admin.ch/i14y/concept/legalForm

  '
examples:
- value: '0106'
- value: '0107'
- value: 0109
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:legalForm
domain_of:
- InterestLink
range: LegalFormEnum

```
</details></div>