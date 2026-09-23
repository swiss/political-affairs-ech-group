---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_Identifikator der Legislaturperiode, zu der die Session oder Sitzung gehört. Eine Sitzung, die zu einer Session gehört, ist über die Session (parent_session) der Legislaturperiode zugeordnet; eine Sitzung ohne Session — etwa eine Kommissionssitzung oder eine Sitzung in einer Föderaleinheit ohne formale Sessionen — verweist direkt auf die Legislaturperiode._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislatu... |  no  |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Identifikator der Legislaturperiode, zu der die Session oder Sitzung
  gehört. Eine Sitzung, die zu einer Session gehört, ist über die Session (parent_session)
  der Legislaturperiode zugeordnet; eine Sitzung ohne Session — etwa eine Kommissionssitzung
  oder eine Sitzung in einer Föderaleinheit ohne formale Sessionen — verweist direkt
  auf die Legislaturperiode.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>