---
search:
  boost: 5.0
---

# Slot: administrative_id 


_Identifiant administratif du corps législatif, p. ex. commune, canton ou pays._




<div data-search-exclude markdown="1">



URI: [ops:administrative_id](https://ch.paf.link/schema/operations/administrative_id)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Legislature](Legislature.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: administrative_id
annotations:
  description_de:
    tag: description_de
    value: 'Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder
      Land.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant administratif du corps législatif, p. ex. commune, canton
      ou pays.

      '
description: 'Identifiant administratif du corps législatif, p. ex. commune, canton
  ou pays.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
range: string

```
</details></div>