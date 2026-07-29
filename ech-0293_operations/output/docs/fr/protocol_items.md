---
search:
  boost: 5.0
---

# Slot: protocol_items 


_Points de l'ordre du jour tels qu'ils ont effectivement été consignés au procès-verbal._




<div data-search-exclude markdown="1">



URI: [ops:protocolItem](https://ch.paf.link/schema/operations/protocolItem)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [ProtocolItem](ProtocolItem.md) |
| Domaine de | [Protocol](Protocol.md) |
| URI du slot | [ops:protocolItem](https://ch.paf.link/schema/operations/protocolItem) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: protocol_items
annotations:
  description_de:
    tag: description_de
    value: 'Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden.

      '
  description_fr:
    tag: description_fr
    value: 'Points de l''ordre du jour tels qu''ils ont effectivement été consignés
      au procès-verbal.

      '
description: 'Points de l''ordre du jour tels qu''ils ont effectivement été consignés
  au procès-verbal.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:protocolItem
domain_of:
- Protocol
range: ProtocolItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>