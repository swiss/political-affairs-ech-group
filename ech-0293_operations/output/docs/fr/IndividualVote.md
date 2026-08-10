

## Classe: IndividualVote 


_Une voix individuelle exprimée par un membre lors d'une procédure de vote._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| parent_voting | 0..1 <br/> [Voting](Voting.md) | L'identifiant du vote auquel se rattache la voix individuelle.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | Référence à la personne agissante (instantané au moment de la mise en relation).  |
| seat_nr | 0..1 <br/> [String](String.md) | Le numéro de siège correspondant à la voix individuelle, le cas échéant.  |
| weight | 0..1 <br/> [Integer](Integer.md) | Le nombre de voix dont dispose la personne, le cas échéant (p. ex. lorsqu'une personne détient plusieurs voix).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | Type de voix exprimée (oui, non, abstention, n'a pas voté, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [individual_votes](individual_votes.md) | range | [IndividualVote](IndividualVote.md) |














### Exemples
#### Exemple IndividualVote : Yes vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27235
    label: Paul Schlegel
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Exemple IndividualVote : No vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27234
    label: Andreas Eggenberger
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Exemple IndividualVote : Abstention

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27233
    label: Thomas Ammann
  seat_nr: '3'
  individual_vote_type: abstention
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Exemple IndividualVote : Absent in a multiple-choice voting

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/4
    label: Abwesendes Mitglied
  seat_nr: '103'
  individual_vote_type: not_voted
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Exemple IndividualVote : Yes vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27237
    label: Thomas Wolf
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-11-20T16:45:00Z'

```
#### Exemple IndividualVote : No vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/25208
    label: Jean-Daniel Strub
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-11-20T16:45:00Z'

```
#### Exemple IndividualVote : Did not vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/25177
    label: Ruedi Thomann
  seat_nr: '4'
  individual_vote_type: not_voted
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Exemple IndividualVote : Individual vote for selection option C

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/3
    label: Mitglied Auswahl C
  seat_nr: '88'
  individual_vote_type: other
  type_label: Auswahl C
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Exemple IndividualVote : Individual vote for selection option A

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/1
    label: Mitglied Auswahl A
  seat_nr: '12'
  individual_vote_type: other
  type_label: Auswahl A
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Exemple IndividualVote : Individual vote for selection option B

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/2
    label: Mitglied Auswahl B
  seat_nr: '47'
  individual_vote_type: other
  type_label: Auswahl B
  datetime_created: '2024-02-28T00:00:00Z'

```






</div>