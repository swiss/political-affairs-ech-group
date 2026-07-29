---
search:
  boost: 5.0
---

# Slot: meeting_type 


_Type de séance, p. ex. session, commission, séance de session, divers._




<div data-search-exclude markdown="1">



URI: [ops:meetingType](https://ch.paf.link/schema/operations/meetingType)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MeetingTypeEnum](MeetingTypeEnum.md) |
| Domaine de | [Meeting](Meeting.md) |
| URI du slot | [ops:meetingType](https://ch.paf.link/schema/operations/meetingType) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| committee |
| session |
| sitting |





## Source LinkML

<details>
```yaml
name: meeting_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der Sitzung, z.B. Session, Kommission, Sessionssitzung, Verschiedenes.

      '
  description_fr:
    tag: description_fr
    value: 'Type de séance, p. ex. session, commission, séance de session, divers.

      '
description: 'Type de séance, p. ex. session, commission, séance de session, divers.

  '
examples:
- value: committee
- value: session
- value: sitting
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:meetingType
domain_of:
- Meeting
range: MeetingTypeEnum

```
</details></div>