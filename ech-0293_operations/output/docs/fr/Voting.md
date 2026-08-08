

## Classe: Voting 


_Une procédure de vote avec les voix individuelles et les résultats._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote se termine.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](VotingTypeEnum.md) | Type de procédure de vote (vote intermédiaire, vote final, vote secret, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| voting_title | * <br/> [MultilingualString](MultilingualString.md) | Titre du vote, objet ou question soumise au vote. En l'absence d'objet propre, il ne faut pas reprendre le titre de l'affaire.  |
| optional | 0..1 <br/> [Boolean](Boolean.md) | Indique si la séance ou le vote est facultatif.  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| label_yes | 0..1 <br/> [String](String.md) | Signification d'une voix « oui ».  |
| label_no | 0..1 <br/> [String](String.md) | Signification d'une voix « non ».  |
| label_abstention | 0..1 <br/> [String](String.md) | Signification d'une abstention.  |
| tie_breaker | 0..1 <br/> [Boolean](Boolean.md) | Indique si une voix prépondérante a été utilisée lors du vote.  |
| total_count_yes | 0..1 <br/> [Integer](Integer.md) | Nombre total de voix « oui ».  |
| total_count_no | 0..1 <br/> [Integer](Integer.md) | Nombre total de voix « non ».  |
| total_count_abstention | 0..1 <br/> [Integer](Integer.md) | Nombre total d'abstentions.  |
| total_other | * <br/> [TotalOther](TotalOther.md) | Utilisé lorsque plusieurs options sont soumises au vote (p. ex. 5 boutons à Zurich).  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Nombre total de membres absents. La distinction entre absent et absent excusé se fait dans la liste de présence.  |
| total | 0..1 <br/> [Integer](Integer.md) | Nombre total de voix, sans les absents ni la voix de la présidence.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Type de majorité requise pour le vote (absolue, deux tiers, etc.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Nombre de voix requis pour atteindre le seuil de majorité déterminant.  |
| result_text | 0..1 <br/> [String](String.md) | Texte libre décrivant le résultat du vote, p. ex. « Accepté par 78 voix ».  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance liée qui regroupe la séance courante.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](String.md) | Le lien vers les affaires rattachées au point de l'ordre du jour.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [votings](votings.md) | range | [Voting](Voting.md) |
| [Protocol](Protocol.md) | [votings](votings.md) | range | [Voting](Voting.md) |
| [IndividualVote](IndividualVote.md) | [parent_voting](parent_voting.md) | range | [Voting](Voting.md) |














### Exemples
#### Exemple : Intermediate voting on an amendment

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
#### Exemple : Final vote with individual votes

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
#### Exemple : Final vote on the budget

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
#### Exemple : Motions in the same direction with multiple choice

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