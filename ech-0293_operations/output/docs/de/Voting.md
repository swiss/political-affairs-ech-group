

## Klasse: Voting 


_Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](VotingTypeEnum.md) | Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.).  |
| type_label | 0..1 <br/> [String](String.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| voting_title | * <br/> [MultilingualString](MultilingualString.md) | Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden ist, sollte nicht der Geschäftstitel verwendet werden.  |
| optional | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Sitzung oder Abstimmung optional ist.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| label_yes | 0..1 <br/> [String](String.md) | Bedeutung einer „Ja“-Stimme.  |
| label_no | 0..1 <br/> [String](String.md) | Bedeutung einer „Nein“-Stimme.  |
| label_abstention | 0..1 <br/> [String](String.md) | Bedeutung einer Enthaltungsstimme.  |
| tie_breaker | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.  |
| total_count_yes | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der „Ja“-Stimmen.  |
| total_count_no | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der „Nein“-Stimmen.  |
| total_count_abstention | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der Enthaltungen.  |
| total_other | * <br/> [TotalOther](TotalOther.md) | Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B. 5 Knöpfe in Zürich).  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> [String](String.md) | Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. „Mit 78 Stimmen angenommen“.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.  |
| affair_id | 0..1 <br/> [String](String.md) | Die Verbindung zu den Geschäften des Traktandums.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [votings](votings.md) | range | [Voting](Voting.md) |
| [Protocol](Protocol.md) | [votings](votings.md) | range | [Voting](Voting.md) |
| [IndividualVote](IndividualVote.md) | [parent_voting](parent_voting.md) | range | [Voting](Voting.md) |














### Beispiele
#### Beispiel Voting: Intermediate voting on an amendment

```yaml
votings:
- global_uri: ops:voting_be_2025_042
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
#### Beispiel Voting: Final vote with individual votes

```yaml
votings:
- global_uri: ops:voting_sg_2025_001
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
#### Beispiel Voting: Final vote on the budget

```yaml
votings:
- global_uri: ops:voting_zh_budget_2026
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
#### Beispiel Voting: Motions in the same direction with multiple choice

```yaml
votings:
- global_uri: ops:voting_zh_gr_2024_2023_361
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