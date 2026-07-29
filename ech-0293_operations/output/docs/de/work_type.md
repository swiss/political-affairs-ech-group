---
search:
  boost: 5.0
---

# Slot: work_type 


_Art des Dokuments (z.B. Protokoll, eingereichte Fassung, geltendes Recht)._




<div data-search-exclude markdown="1">



URI: [meta:workType](https://ch.paf.link/schema/meta/workType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [WorkTypesEnum](WorkTypesEnum.md) |
| Domäne von | [Work](Work.md) |
| Slot-URI | [meta:workType](https://ch.paf.link/schema/meta/workType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Art des Dokuments (z.B. Protokoll, eingereichte Fassung, geltendes Recht).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:workType
domain_of:
- Work
range: WorkTypesEnum

```
</details></div>