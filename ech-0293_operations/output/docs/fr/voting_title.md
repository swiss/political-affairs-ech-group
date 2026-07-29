---
search:
  boost: 5.0
---

# Slot: voting_title 


_Titre du vote, objet ou question soumise au vote. En l'absence d'objet propre, il ne faut pas reprendre le titre de l'affaire._




<div data-search-exclude markdown="1">



URI: [ops:voting_title](https://ch.paf.link/schema/operations/voting_title)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualString](MultilingualString.md) |
| Domaine de | [Voting](Voting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: voting_title
annotations:
  description_de:
    tag: description_de
    value: 'Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden
      ist, sollte nicht der Geschäftstitel verwendet werden.

      '
  description_fr:
    tag: description_fr
    value: 'Titre du vote, objet ou question soumise au vote. En l''absence d''objet
      propre, il ne faut pas reprendre le titre de l''affaire.

      '
description: 'Titre du vote, objet ou question soumise au vote. En l''absence d''objet
  propre, il ne faut pas reprendre le titre de l''affaire.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>