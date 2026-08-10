

## Klasse: IndividualVote 


_Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| parent_voting | 0..1 <br/> [Voting](Voting.md) | Die ID der Abstimmung, die mit der Einzelstimme verbunden ist.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| seat_nr | 0..1 <br/> [String](String.md) | Die Sitznummer der Einzelstimme, falls zutreffend.  |
| weight | 0..1 <br/> [Integer](Integer.md) | Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B. in Fällen, in denen eine Person mehrere Stimmen hat).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [individual_votes](individual_votes.md) | range | [IndividualVote](IndividualVote.md) |














### Beispiele
#### Beispiel IndividualVote: Yes vote

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
#### Beispiel IndividualVote: No vote

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
#### Beispiel IndividualVote: Abstention

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
#### Beispiel IndividualVote: Absent in a multiple-choice voting

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
#### Beispiel IndividualVote: Yes vote on the budget

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
#### Beispiel IndividualVote: No vote on the budget

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
#### Beispiel IndividualVote: Did not vote

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
#### Beispiel IndividualVote: Individual vote for selection option C

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
#### Beispiel IndividualVote: Individual vote for selection option A

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
#### Beispiel IndividualVote: Individual vote for selection option B

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