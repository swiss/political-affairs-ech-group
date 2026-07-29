---
search:
  boost: 5.0
---

# Slot: works 


_Die im Container enthaltenen Dokumente (FRBR Works)._




<div data-search-exclude markdown="1">



URI: [meta:works](https://ch.paf.link/schema/meta/works)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [WorkContainer](WorkContainer.md) | Container für die Dokumente (FRBR Works) dieses Schemas |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Work](Work.md) |
| Domäne von | [WorkContainer](WorkContainer.md) |
| Slot-URI | [meta:works](https://ch.paf.link/schema/meta/works) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: works
annotations:
  description_de:
    tag: description_de
    value: 'Die im Container enthaltenen Dokumente (FRBR Works).

      '
  description_fr:
    tag: description_fr
    value: 'Les documents (FRBR Works) contenus dans le conteneur.

      '
description: 'Die im Container enthaltenen Dokumente (FRBR Works).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:works
domain_of:
- WorkContainer
range: Work
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>