---
search:
  boost: 5.0
---

# Slot: meeting_abbreviation 


_Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession 2024)._




<div data-search-exclude markdown="1">



URI: [ops:meeting_abbreviation](https://ch.paf.link/schema/operations/meeting_abbreviation)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






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
name: meeting_abbreviation
annotations:
  description_de:
    tag: description_de
    value: 'Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession
      2024).

      '
  description_fr:
    tag: description_fr
    value: 'Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour
      la session de printemps 2024).

      '
description: 'Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession
  2024).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>