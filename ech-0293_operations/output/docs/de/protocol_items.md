---
search:
  boost: 5.0
---

# Slot: protocol_items 


_Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden._




<div data-search-exclude markdown="1">



URI: [ops:protocolItem](https://ch.paf.link/schema/operations/protocolItem)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ProtocolItem](ProtocolItem.md) |
| Domäne von | [Protocol](Protocol.md) |
| Slot-URI | [ops:protocolItem](https://ch.paf.link/schema/operations/protocolItem) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

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
description: 'Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden.

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