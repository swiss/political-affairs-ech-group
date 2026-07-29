---
search:
  boost: 5.0
---

# Slot: body_key 


_Clé identifiant l'organe politique ou la collectivité (p. ex. BE pour Berne, CHE pour la Suisse)._




<div data-search-exclude markdown="1">



URI: [ops:body_key](https://ch.paf.link/schema/operations/body_key)
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
description: 'Clé identifiant l''organe politique ou la collectivité (p. ex. BE pour
  Berne, CHE pour la Suisse).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>