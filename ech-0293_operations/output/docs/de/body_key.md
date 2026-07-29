---
search:
  boost: 5.0
---

# Slot: body_key 


_Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit (z.B. BE für Bern, CHE für Schweiz)._




<div data-search-exclude markdown="1">



URI: [ops:body_key](https://ch.paf.link/schema/operations/body_key)
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
name: body_key
annotations:
  description_de:
    tag: description_de
    value: 'Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit
      (z.B. BE für Bern, CHE für Schweiz).

      '
  description_fr:
    tag: description_fr
    value: 'Clé identifiant l''organe politique ou la collectivité (p. ex. BE pour
      Berne, CHE pour la Suisse).

      '
description: 'Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit
  (z.B. BE für Bern, CHE für Schweiz).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>