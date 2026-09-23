---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_Identifiant de la législature à laquelle la session ou la séance appartient. Une séance qui fait partie d'une session est rattachée à la législature par la session (parent_session) ; une séance sans session — par exemple une séance de commission ou une séance dans une unité fédérale sans sessions formelles — renvoie directement à la législature._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session : une période de séances continue au sein d'une législature |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: parent_legislature
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator der Legislaturperiode, zu der die Session oder Sitzung gehört.
      Eine Sitzung, die zu einer Session gehört, ist über die Session (parent_session)
      der Legislaturperiode zugeordnet; eine Sitzung ohne Session — etwa eine Kommissionssitzung
      oder eine Sitzung in einer Föderaleinheit ohne formale Sessionen — verweist
      direkt auf die Legislaturperiode.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la législature à laquelle la session ou la séance appartient.
      Une séance qui fait partie d''une session est rattachée à la législature par
      la session (parent_session) ; une séance sans session — par exemple une séance
      de commission ou une séance dans une unité fédérale sans sessions formelles
      — renvoie directement à la législature.

      '
description: 'Identifiant de la législature à laquelle la session ou la séance appartient.
  Une séance qui fait partie d''une session est rattachée à la législature par la
  session (parent_session) ; une séance sans session — par exemple une séance de commission
  ou une séance dans une unité fédérale sans sessions formelles — renvoie directement
  à la législature.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>