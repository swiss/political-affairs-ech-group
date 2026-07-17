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





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [LegalFormEnum](LegalFormEnum.md) |
| Domaine de | [InterestLink](InterestLink.md) |
| URI du slot | [act:legalForm](https://ld.ech.ch/schema/0294/actors/legalForm) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| 0106 |
| 0107 |
| 0109 |





## Source LinkML

<details>
```yaml
name: legal_form
annotations:
  description_de:
    tag: description_de
    value: 'Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm

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