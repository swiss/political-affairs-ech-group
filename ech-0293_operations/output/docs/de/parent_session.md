---
search:
  boost: 5.0
---

# Slot: parent_session 


_Identifikator der Session, zu der die Sitzung gehört._




<div data-search-exclude markdown="1">



URI: [ops:parent_session](https://ch.paf.link/schema/operations/parent_session)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: parent_session
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator der Session, zu der die Sitzung gehört.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la session à laquelle la séance appartient.

      '
description: 'Identifikator der Session, zu der die Sitzung gehört.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>