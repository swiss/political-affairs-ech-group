---
search:
  boost: 5.0
---

# Slot: vote_procedures 


_Procedures by which the vote was taken. Open procedures: show of hands, standing, electronic voting, roll call, and in crisis situations remote voting (votes communicated to the presidency beforehand and recorded together with the vote in the chamber), circulation procedure or voting in virtual sittings. Secret procedures: secret ballot with ballot papers, electronic secret voting. The procedure determines whether individual votes can be recorded._




<div data-search-exclude markdown="1">



URI: [ops:vote_procedures](https://ch.paf.link/schema/operations/vote_procedures)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | The formal decision taken on an agenda item, including the voting procedures ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Resolution](Resolution.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

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
description: 'Procedures by which the vote was taken. Open procedures: show of hands,
  standing, electronic voting, roll call, and in crisis situations remote voting (votes
  communicated to the presidency beforehand and recorded together with the vote in
  the chamber), circulation procedure or voting in virtual sittings. Secret procedures:
  secret ballot with ballot papers, electronic secret voting. The procedure determines
  whether individual votes can be recorded.

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