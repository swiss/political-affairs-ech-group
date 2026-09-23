---
search:
  boost: 5.0
---

# Slot: has_protocol 


_Referenz auf das nach der Sitzung erstellte Protokoll dieser Sitzung. Angegeben wird nur der Identifikator des Protokolls; das Protokoll selbst wird in der Liste `protocols` des Containers geliefert. Es ist eine eigenständige Entität mit eigenem Identifikator und wird in der Regel später veröffentlicht als die Sitzung, weshalb es referenziert und nicht eingebettet wird._




<div data-search-exclude markdown="1">



URI: [ops:hasProtocol](https://ch.paf.link/schema/operations/hasProtocol)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Protocol](Protocol.md) |
| Domäne von | [Meeting](Meeting.md) |
| Slot-URI | [ops:hasProtocol](https://ch.paf.link/schema/operations/hasProtocol) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: has_protocol
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
description: 'Referenz auf das nach der Sitzung erstellte Protokoll dieser Sitzung.
  Angegeben wird nur der Identifikator des Protokolls; das Protokoll selbst wird in
  der Liste `protocols` des Containers geliefert. Es ist eine eigenständige Entität
  mit eigenem Identifikator und wird in der Regel später veröffentlicht als die Sitzung,
  weshalb es referenziert und nicht eingebettet wird.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:hasProtocol
domain_of:
- Meeting
range: Protocol

```
</details></div>