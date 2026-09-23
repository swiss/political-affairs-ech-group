

## Class: IndividualVote 


_The vote cast by an individual member in a voting. Individual votes are only recorded for open votings; for secret votings only the overall result is published. An individual vote concerns one specific voting and differs from attendance (Attendance), which records presence at the meeting as a whole: a member present at the meeting may be recorded as not_voted in a single voting, for instance because they briefly left the room._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| parent_voting | 0..1 <br/> [Voting](Voting.md) | The ID of the voting associated with the individual vote.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | The member who cast the vote, as a reference to a person according to eCH-0294.  |
| seat_nr | 0..1 <br/> [String](String.md) | The seat number of the individual vote, if applicable.  |
| weight | 0..1 <br/> [Integer](Integer.md) | Voting weight of the member; normally 1. Other values arise, for instance, where a member also votes for an absent member (proxy, weight 2), in communal assemblies where legal entities hold several votes, or in historical systems in which different groups of persons had different voting weights.  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | Type of vote cast (yes, no, abstention, no vote, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | Custom type label when standard type values don't apply.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [individual_votes](individual_votes.md) | range | [IndividualVote](IndividualVote.md) |














### Examples
#### Example IndividualVote: No vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_andreas_eggenberger
    label: Andreas Eggenberger
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: No vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: actors:person_jean_daniel_strub
    label: Jean-Daniel Strub
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-11-20T16:45:00Z'

```
#### Example IndividualVote: Abstention

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_thomas_ammann
    label: Thomas Ammann
  seat_nr: '3'
  individual_vote_type: abstention
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: Yes vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_paul_schlegel
    label: Paul Schlegel
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: Individual vote for selection option B

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_2
    label: Mitglied Auswahl B
  seat_nr: '47'
  individual_vote_type: other
  type_label: Auswahl B
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Example IndividualVote: Individual vote for selection option C

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_3
    label: Mitglied Auswahl C
  seat_nr: '88'
  individual_vote_type: other
  type_label: Auswahl C
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Example IndividualVote: Did not vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_ruedi_thomann
    label: Ruedi Thomann
  seat_nr: '4'
  individual_vote_type: not_voted
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: Yes vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: actors:person_thomas_wolf
    label: Thomas Wolf
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-11-20T16:45:00Z'

```
#### Example IndividualVote: Individual vote for selection option A

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_1
    label: Mitglied Auswahl A
  seat_nr: '12'
  individual_vote_type: other
  type_label: Auswahl A
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Example IndividualVote: Absent in a multiple-choice voting

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_4
    label: Abwesendes Mitglied
  seat_nr: '103'
  individual_vote_type: not_voted
  datetime_created: '2024-02-28T00:00:00Z'

```






</div>