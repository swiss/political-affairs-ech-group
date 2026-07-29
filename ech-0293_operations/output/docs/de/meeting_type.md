---
search:
  boost: 5.0
---

# Slot: meeting_type 


_Art der Sitzung, z.B. Session, Kommission, Sessionssitzung, Verschiedenes._




<div data-search-exclude markdown="1">



URI: [ops:meetingType](https://ch.paf.link/schema/operations/meetingType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MeetingTypeEnum](MeetingTypeEnum.md) |
| Domäne von | [Meeting](Meeting.md) |
| Slot-URI | [ops:meetingType](https://ch.paf.link/schema/operations/meetingType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| committee |
| session |
| sitting |





## LinkML-Quelle

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
description: 'Art der Sitzung, z.B. Session, Kommission, Sessionssitzung, Verschiedenes.

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