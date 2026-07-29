---
search:
  boost: 5.0
---

# Slot: work_type 


_Type de document (p. ex. procès-verbal, version déposée, droit en vigueur)._




<div data-search-exclude markdown="1">



URI: [meta:workType](https://ch.paf.link/schema/meta/workType)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work : le document abstrait en tant que tel, indépendamment d'une versio... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [WorkTypesEnum](WorkTypesEnum.md) |
| Domaine de | [Work](Work.md) |
| URI du slot | [meta:workType](https://ch.paf.link/schema/meta/workType) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Type de document (p. ex. procès-verbal, version déposée, droit en vigueur).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:workType
domain_of:
- Work
range: WorkTypesEnum

```
</details></div>