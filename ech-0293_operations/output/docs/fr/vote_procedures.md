---
search:
  boost: 5.0
---

# Slot: vote_procedures 


_Procédures selon lesquelles le vote a eu lieu. Procédures ouvertes : main levée, assis-debout, vote électronique, appel nominal et, en situation de crise, vote à distance (voix communiquées à l'avance à la présidence et saisies en même temps que le vote au conseil), procédure par voie de circulation ou vote lors de séances virtuelles. Procédures secrètes : bulletin de vote, vote électronique secret. La procédure détermine si les voix individuelles peuvent être saisies._




<div data-search-exclude markdown="1">



URI: [ops:vote_procedures](https://ch.paf.link/schema/operations/vote_procedures)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | La décision formelle prise sur un point de l'ordre du jour, y compris les pro... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Resolution](Resolution.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: vote_procedures
annotations:
  description_de:
    tag: description_de
    value: 'Verfahren, in denen abgestimmt wurde. Offene Verfahren: Handzeichen, Aufstehen,
      elektronische Abstimmung, Namensaufruf, in Krisenlagen zudem externe Stimmabgabe
      (vorgängig dem Präsidium mitgeteilte Stimmen, die zusammen mit der Abstimmung
      im Rat erfasst werden), Zirkulationsverfahren oder Stimmabgabe an virtuellen
      Sitzungen. Geheime Verfahren: Stimmzettel, elektronische geheime Abstimmung.
      Das Verfahren bestimmt, ob Einzelstimmen erfasst werden können.

      '
  description_fr:
    tag: description_fr
    value: 'Procédures selon lesquelles le vote a eu lieu. Procédures ouvertes : main
      levée, assis-debout, vote électronique, appel nominal et, en situation de crise,
      vote à distance (voix communiquées à l''avance à la présidence et saisies en
      même temps que le vote au conseil), procédure par voie de circulation ou vote
      lors de séances virtuelles. Procédures secrètes : bulletin de vote, vote électronique
      secret. La procédure détermine si les voix individuelles peuvent être saisies.

      '
description: 'Procédures selon lesquelles le vote a eu lieu. Procédures ouvertes :
  main levée, assis-debout, vote électronique, appel nominal et, en situation de crise,
  vote à distance (voix communiquées à l''avance à la présidence et saisies en même
  temps que le vote au conseil), procédure par voie de circulation ou vote lors de
  séances virtuelles. Procédures secrètes : bulletin de vote, vote électronique secret.
  La procédure détermine si les voix individuelles peuvent être saisies.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>