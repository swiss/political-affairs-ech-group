

## Class: IndividualVote 


_[en] An individual vote cast by a member during a voting procedure._

_[de] Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_voting | 0..1 <br/> [Voting](Voting.md) | [en] The ID of the voting associated with the individual vote. [de] Die ID der Abstimmung, die mit der Einzelstimme verbunden ist.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | [en] Reference to the acting person (lightweight snapshot at time of linking). [de] Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| seat_nr | 0..1 <br/> [String](String.md) | [en] The seat number of the individual vote, if applicable. [de] Die Sitznummer der Einzelstimme, falls zutreffend.  |
| weight | 0..1 <br/> [Integer](Integer.md) | [en] The number of votes held by the individual, if applicable (e.g., in cases where a person has multiple votes). [de] Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B. in Fällen, in denen eine Person mehrere Stimmen hat).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | [en] Type of vote cast (yes, no, abstention, no vote, etc.). [de] Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | [en] Custom type label when standard type values don't apply. [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [individual_votes](individual_votes.md) | range | [IndividualVote](IndividualVote.md) |














### Examples
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_abs1

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
#### Example: IndividualVote-voting_vote_zh_budget_2026_person_102

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
#### Example: IndividualVote-voting_vote_sg_2025_001_person_789

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
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_b1

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
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_a1

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
#### Example: IndividualVote-voting_vote_zh_budget_2026_person_101

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
#### Example: IndividualVote-voting_vote_sg_2025_001_person_321

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
#### Example: IndividualVote-voting_vote_sg_2025_001_person_123

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
#### Example: IndividualVote-voting_vote_sg_2025_001_person_456

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
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_c1

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






</div>