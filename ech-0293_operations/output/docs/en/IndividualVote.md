

## Class: IndividualVote 


_An individual vote cast by a member during a voting procedure._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_voting | 0..1 <br/> [Voting](Voting.md) | The ID of the voting associated with the individual vote.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | Reference to the acting person (lightweight snapshot at time of linking).  |
| seat_nr | 0..1 <br/> [String](String.md) | The seat number of the individual vote, if applicable.  |
| weight | 0..1 <br/> [Integer](Integer.md) | The number of votes held by the individual, if applicable (e.g., in cases where a person has multiple votes).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | Type of vote cast (yes, no, abstention, no vote, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | Custom type label when standard type values don't apply.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [individual_votes](individual_votes.md) | range | [IndividualVote](IndividualVote.md) |














### Examples
#### Example: Yes vote

```yaml
global_uri: ops:vote_sg_2025_001_person_123
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27235
  label: Paul Schlegel
seat_nr: '1'
individual_vote_type: 'yes'
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: No vote

```yaml
global_uri: ops:vote_sg_2025_001_person_456
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27234
  label: Andreas Eggenberger
seat_nr: '2'
individual_vote_type: 'no'
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: Abstention

```yaml
global_uri: ops:vote_sg_2025_001_person_789
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27233
  label: Thomas Ammann
seat_nr: '3'
individual_vote_type: abstention
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: Absent in a multiple-choice voting

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_abs1
parent_voting: ops:voting_zh_gr_2024_2023_361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/personen/4
  label: Abwesendes Mitglied
seat_nr: '103'
individual_vote_type: not_voted
datetime_created: '2024-02-28T00:00:00Z'

```
#### Example: Yes vote on the budget

```yaml
global_uri: ops:vote_zh_budget_2026_person_101
parent_voting: ops:voting_zh_budget_2026
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27237
  label: Thomas Wolf
seat_nr: '1'
individual_vote_type: 'yes'
datetime_created: '2025-11-20T16:45:00Z'

```
#### Example: No vote on the budget

```yaml
global_uri: ops:vote_zh_budget_2026_person_102
parent_voting: ops:voting_zh_budget_2026
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/25208
  label: Jean-Daniel Strub
seat_nr: '2'
individual_vote_type: 'no'
datetime_created: '2025-11-20T16:45:00Z'

```
#### Example: Did not vote

```yaml
global_uri: ops:vote_sg_2025_001_person_321
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/25177
  label: Ruedi Thomann
seat_nr: '4'
individual_vote_type: not_voted
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: Individual vote for selection option C

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_c1
parent_voting: ops:voting_zh_gr_2024_2023_361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/personen/3
  label: Mitglied Auswahl C
seat_nr: '88'
individual_vote_type: other
type_label: Auswahl C
datetime_created: '2024-02-28T00:00:00Z'

```
#### Example: Individual vote for selection option A

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_a1
parent_voting: ops:voting_zh_gr_2024_2023_361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/personen/1
  label: Mitglied Auswahl A
seat_nr: '12'
individual_vote_type: other
type_label: Auswahl A
datetime_created: '2024-02-28T00:00:00Z'

```
#### Example: Individual vote for selection option B

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_b1
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