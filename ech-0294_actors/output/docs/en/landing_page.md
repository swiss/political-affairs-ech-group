---
search:
  boost: 5.0
---

# Slot: landing_page 


_Website providing further information. Where the site is published under a separate address per language, one entry per language is recorded._




<div data-search-exclude markdown="1">



URI: [act:landingPage](https://ld.ech.ch/schema/0294/actors/landingPage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualUri](MultilingualUri.md) |
| Domain Of | [Group](Group.md) |
| Slot URI | [act:landingPage](https://ld.ech.ch/schema/0294/actors/landingPage) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: landing_page
annotations:
  description_de:
    tag: description_de
    value: 'Website mit weiteren Informationen. Wird die Website je Sprache unter
      einer eigenen Adresse publiziert, wird pro Sprache ein Eintrag erfasst.

      '
  description_fr:
    tag: description_fr
    value: 'Site web fournissant de plus amples informations. Lorsque le site est
      publié à une adresse propre par langue, une entrée est saisie par langue.

      '
description: 'Website providing further information. Where the site is published under
  a separate address per language, one entry per language is recorded.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:landingPage
domain_of:
- Group
range: MultilingualUri
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>