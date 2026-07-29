---
search:
  boost: 5.0
---

# Slot: protocol_items 


_Agenda items as actually recorded in the protocol._




<div data-search-exclude markdown="1">



URI: [ops:protocolItem](https://ch.paf.link/schema/operations/protocolItem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProtocolItem](ProtocolItem.md) |
| Domain Of | [Protocol](Protocol.md) |
| Slot URI | [ops:protocolItem](https://ch.paf.link/schema/operations/protocolItem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

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
description: 'Agenda items as actually recorded in the protocol.

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