---
search:
  boost: 5.0
---

# Slot: meeting_abbreviation 


_Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour la session de printemps 2024)._




<div data-search-exclude markdown="1">



URI: [ops:meeting_abbreviation](https://ch.paf.link/schema/operations/meeting_abbreviation)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






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
description: 'Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour
  la session de printemps 2024).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>