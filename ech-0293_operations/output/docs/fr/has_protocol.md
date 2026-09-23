---
search:
  boost: 5.0
---

# Slot: has_protocol 


_Référence au procès-verbal de cette séance, établi après celle-ci. Seul l'identifiant du procès-verbal est indiqué ; le procès-verbal lui-même est livré dans la liste `protocols` du conteneur. Il constitue une entité à part entière dotée de son propre identifiant et est en règle générale publié après la séance, raison pour laquelle il est référencé et non imbriqué._




<div data-search-exclude markdown="1">



URI: [ops:hasProtocol](https://ch.paf.link/schema/operations/hasProtocol)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Protocol](Protocol.md) |
| Domaine de | [Meeting](Meeting.md) |
| URI du slot | [ops:hasProtocol](https://ch.paf.link/schema/operations/hasProtocol) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Référence au procès-verbal de cette séance, établi après celle-ci. Seul
  l''identifiant du procès-verbal est indiqué ; le procès-verbal lui-même est livré
  dans la liste `protocols` du conteneur. Il constitue une entité à part entière dotée
  de son propre identifiant et est en règle générale publié après la séance, raison
  pour laquelle il est référencé et non imbriqué.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:hasProtocol
domain_of:
- Meeting
range: Protocol

```
</details></div>