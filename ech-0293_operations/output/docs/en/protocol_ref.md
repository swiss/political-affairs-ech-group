---
search:
  boost: 5.0
---

# Slot: protocol_ref 


_Reference to the protocol (minutes) of this meeting, recorded after the meeting. Only the identifier of the protocol is given; the protocol itself is delivered in the container's `protocols` list. It is an entity in its own right with its own identifier and is usually published later than the meeting, so it is referenced rather than embedded._




<div data-search-exclude markdown="1">



URI: [ops:protocolRef](https://ch.paf.link/schema/operations/protocolRef)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Protocol](Protocol.md) |
| Domain Of | [Meeting](Meeting.md) |
| Slot URI | [ops:protocolRef](https://ch.paf.link/schema/operations/protocolRef) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: protocol_ref
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf das nach der Sitzung erstellte Protokoll dieser Sitzung.
      Angegeben wird nur der Identifikator des Protokolls; das Protokoll selbst wird
      in der Liste `protocols` des Containers geliefert. Es ist eine eigenständige
      Entität mit eigenem Identifikator und wird in der Regel später veröffentlicht
      als die Sitzung, weshalb es referenziert und nicht eingebettet wird.

      '
  description_fr:
    tag: description_fr
    value: 'Référence au procès-verbal de cette séance, établi après celle-ci. Seul
      l''identifiant du procès-verbal est indiqué ; le procès-verbal lui-même est
      livré dans la liste `protocols` du conteneur. Il constitue une entité à part
      entière dotée de son propre identifiant et est en règle générale publié après
      la séance, raison pour laquelle il est référencé et non imbriqué.

      '
description: 'Reference to the protocol (minutes) of this meeting, recorded after
  the meeting. Only the identifier of the protocol is given; the protocol itself is
  delivered in the container''s `protocols` list. It is an entity in its own right
  with its own identifier and is usually published later than the meeting, so it is
  referenced rather than embedded.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:protocolRef
domain_of:
- Meeting
range: Protocol

```
</details></div>