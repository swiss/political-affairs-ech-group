---
search:
  boost: 5.0
---

# Slot: committee 


_Committee or board within the organization (e.g., Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung), with the language it is published in; one entry is recorded per language._




<div data-search-exclude markdown="1">



URI: [act:committee](https://ld.ech.ch/schema/0294/actors/committee)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:committee](https://ld.ech.ch/schema/0294/actors/committee) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: committee
annotations:
  description_de:
    tag: description_de
    value: 'Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat,
      Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung) mit der Sprache, in der es
      publiziert wird; erfasst wird pro Sprache ein Eintrag.

      '
  description_fr:
    tag: description_fr
    value: 'Comité ou organe au sein de l''organisation (p. ex. conseil d''administration,
      conseil de fondation, comité directeur, conseil de surveillance, comité consultatif,
      direction), avec la langue dans laquelle il est publié ; une entrée est saisie
      par langue.

      '
description: 'Committee or board within the organization (e.g., Verwaltungsrat, Stiftungsrat,
  Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung), with the language it is published
  in; one entry is recorded per language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:committee
domain_of:
- InterestLink
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>