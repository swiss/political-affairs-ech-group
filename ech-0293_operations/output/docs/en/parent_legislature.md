---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_Identifier of the legislature to which the session or meeting belongs. A meeting that belongs to a session is assigned to the legislature through the session (parent_session); a meeting without a session — for instance a committee sitting or a sitting in a federal unit without formal sessions — refers to the legislature directly._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A session: a contiguous period of sittings within a legislature |  no  |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

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
description: 'Identifier of the legislature to which the session or meeting belongs.
  A meeting that belongs to a session is assigned to the legislature through the session
  (parent_session); a meeting without a session — for instance a committee sitting
  or a sitting in a federal unit without formal sessions — refers to the legislature
  directly.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>