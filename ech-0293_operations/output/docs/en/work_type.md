---
search:
  boost: 5.0
---

# Slot: work_type 


_Type of the document (e.g. minutes, submitted version, current law)._




<div data-search-exclude markdown="1">



URI: [meta:workType](https://ch.paf.link/schema/meta/workType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: the abstract document as such, independent of a concrete language ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [WorkTypesEnum](WorkTypesEnum.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [meta:workType](https://ch.paf.link/schema/meta/workType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: work_type
annotations:
  description_de:
    tag: description_de
    value: 'Art des Dokuments (z.B. Protokoll, eingereichte Fassung, geltendes Recht).

      '
  description_fr:
    tag: description_fr
    value: 'Type de document (p. ex. procès-verbal, version déposée, droit en vigueur).

      '
description: 'Type of the document (e.g. minutes, submitted version, current law).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:workType
domain_of:
- Work
range: WorkTypesEnum

```
</details></div>