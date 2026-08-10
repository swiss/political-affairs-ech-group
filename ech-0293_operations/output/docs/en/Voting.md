

## Class: Voting 


_A voting procedure with individual votes and results._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the meeting or voting ends.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](VotingTypeEnum.md) | Type of voting procedure (preliminary, final, secret, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | Custom type label when standard type values don't apply.  |
| voting_title | * <br/> [MultilingualString](MultilingualString.md) | Title or question being voted on. If no specific subject exists, do not use the business item title.  |
| optional | 0..1 <br/> [Boolean](Boolean.md) | Indicates if the meeting or voting is optional.  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| label_yes | 0..1 <br/> [String](String.md) | Meaning of a 'yes' vote.  |
| label_no | 0..1 <br/> [String](String.md) | Meaning of a 'no' vote.  |
| label_abstention | 0..1 <br/> [String](String.md) | Meaning of an 'abstention' vote.  |
| tie_breaker | 0..1 <br/> [Boolean](Boolean.md) | Indicates if a tie-breaker was used in the voting.  |
| total_count_yes | 0..1 <br/> [Integer](Integer.md) | Total number of 'yes' votes.  |
| total_count_no | 0..1 <br/> [Integer](Integer.md) | Total number of 'no' votes.  |
| total_count_abstention | 0..1 <br/> [Integer](Integer.md) | Total number of abstentions.  |
| total_other | * <br/> [TotalOther](TotalOther.md) | Used when multiple options are presented for voting (e.g., 5 buttons in Zurich).  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list.  |
| total | 0..1 <br/> [Integer](Integer.md) | Total number of votes, excluding absent and president's vote.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Type of majority required for the vote (absolute, two-thirds, etc.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Number of votes required for the relevant majority threshold.  |
| result_text | 0..1 <br/> [String](String.md) | Free text describing the outcome of the vote, e.g., "Accepted with 78 votes".  |
| parent_meeting | 0..1 <br/> [String](String.md) | The linked meeting ID that groups the current meeting.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | If needed, this slot builds a hierarchy of agenda items.  |
| affair_id | 0..1 <br/> [String](String.md) | The connection to the affairs (business items) of the agenda item.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [votings](votings.md) | range | [Voting](Voting.md) |
| [Protocol](Protocol.md) | [votings](votings.md) | range | [Voting](Voting.md) |
| [IndividualVote](IndividualVote.md) | [parent_voting](parent_voting.md) | range | [Voting](Voting.md) |














### Examples
#### Example Voting: Intermediate voting on an amendment

```yaml
global_uri: ops:voting_be_2025_042
voting_title:
- text: Änderungsantrag Art. 5 Abs. 2
  language: de
- text: Proposition de modification art. 5 al. 2
  language: fr
voting_type: preliminary_vote
datetime_begin: '2025-06-05T10:15:00Z'
datetime_end: '2025-06-05T10:17:00Z'
total_count_yes: 45
total_count_no: 87
total_count_abstention: 8
total_absent: 10
total: 150
majority_type: absolute
majority_count: 76
result_text: Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt
parent_agenda_item: ops:agenda_item_be_2025_042
parent_meeting: ops:meeting_be_2025_06_05
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/253
  label: Grosser Rat Bern
  abbreviation:
  - value: GR
    language: de
datetime_created: '2025-06-05T10:15:00Z'
datetime_modified: '2025-06-05T10:15:00Z'

```
#### Example Voting: Final vote with individual votes

```yaml
global_uri: ops:voting_sg_2025_001
voting_title:
- text: Schlussabstimmung Energiegesetz
  language: de
voting_type: final_vote
datetime_begin: '2025-03-15T14:30:00Z'
datetime_end: '2025-03-15T14:35:00Z'
total_count_yes: 78
total_count_no: 42
total_count_abstention: 5
total_absent: 3
total: 128
majority_type: absolute
majority_count: 65
result_text: Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen
parent_agenda_item: ops:agenda_item_sg_2025_015
parent_meeting: ops:meeting_sg_2025_03_15
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/265
  label: Kantonsrat St. Gallen
  abbreviation:
  - value: KR
    language: de
datetime_created: '2025-03-15T14:30:00Z'
datetime_modified: '2025-03-15T14:35:00Z'

```
#### Example Voting: Final vote on the budget

```yaml
global_uri: ops:voting_zh_budget_2026
voting_title:
- text: Budgetbeschluss 2026
  language: de
voting_type: final_vote
datetime_begin: '2025-11-20T16:45:00Z'
datetime_end: '2025-11-20T16:50:00Z'
total_count_yes: 105
total_count_no: 70
total_count_abstention: 5
total_absent: 0
total: 180
majority_type: absolute
majority_count: 91
result_text: Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen
parent_agenda_item: ops:agenda_item_zh_budget_2026
parent_meeting: ops:meeting_zh_2025_11_20
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/275
  label: Kantonsrat Zürich
  abbreviation:
  - value: KR
    language: de
datetime_created: '2025-11-20T16:45:00Z'
datetime_modified: '2025-11-20T16:50:00Z'

```
#### Example Voting: Motions in the same direction with multiple choice

```yaml
global_uri: ops:voting_zh_gr_2024_2023_361
voting_title:
- text: >-
    Liegenschaften Stadt Zürich, Wohnhaus Magnusstrasse 27, Gesamtinstandsetzung,
    Grundrissanpassung, Netto-Zusatzkredit (Geschäft 2023/361)
  language: de
voting_type: other
type_label: Gleichgerichtete Anträge (Mehrfachauswahl)
datetime_begin: '2024-02-28T00:00:00Z'
datetime_end: '2024-02-28T00:00:00Z'
landing_page: >-
  https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
total_other:
- count: 75
  label: Auswahl A (siegreich)
- count: 25
  label: Auswahl B
- count: 12
  label: Auswahl C
- count: 0
  label: Auswahl D
total_absent: 13
total: 112
majority_type: other
result_text: >-
  Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl
  C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern).
parent_agenda_item: ops:agenda_item_zh_gr_2024_2023_361
parent_meeting: ops:meeting_zh_gr_2024_02_28
affair_id: 2023/361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/
  label: Gemeinderat der Stadt Zürich
  abbreviation:
  - value: GR
    language: de
datetime_created: '2024-02-28T00:00:00Z'
datetime_modified: '2024-02-28T00:00:00Z'

```






</div>