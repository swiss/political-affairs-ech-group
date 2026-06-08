

## Class: AgendaItem 


_[en] An agenda item of a meeting._

_[de] Ein Traktandum einer Sitzung._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](String.md) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | [en] Type of agenda item, distinguishing individual items from groups. [de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | [en] Sequential number of the agenda item (string type to support roman numerals). [de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | [en] Integer position of the agenda item in the meeting sequence. [de] Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | [en] The leading department for the agenda item. [de] Das federführende Departement für den Tagesordnungspunkt.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | [en] The speaker or head of the department for the agenda item. [de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | [en] Title of the agenda item. [de] Titel des Traktandums.  |
| affair_id | 0..1 <br/> [String](String.md) | [en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | [en] Subtitle or detailed description of the agenda item. [de] Untertitel oder ausführliche Beschreibung des Traktandums.  |
| state_id | 0..1 <br/> [String](String.md) | State identifier (reference to state enum or custom state) |
| state_name | 0..1 <br/> [String](String.md) | [en] Custom state description for the meeting. [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung.  |
| landing_page | 0..1 <br/> [String](String.md) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | None |
| agenda_item_category | 0..1 <br/> [String](String.md) | [en] Category for grouped agenda items (e.g., introduction, by department, technical agenda items). [de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden).  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | [en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | [en] The resolutionor decision taken on this agenda item. [de] Die Resolution oder Entscheidung zu diesem Traktandum.  |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |
| [JointDebate](JointDebate.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |














### Examples
#### Example: AgendaItem-meeting_item_fa732e0e-7e5f-4d45-994a-fc74720c0781

```yaml
global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
parent_meeting: ops:meeting_luzern_2025_01_28_b
agenda_item_type: item
datetime_begin_planned: '2025-01-28T00:00:00Z'
agenda_item_position: 14
agenda_item_number: '14'
agenda_item_title:
- text: Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und Anpassung
    der Kriterien zum früheren Eintritt von Kindern in die Basisstufe (den freiwilligen
    Kindergarten) / Bildungs- und Kulturdepartement
  language: de
agenda_item_category: voting
url:
- text: https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=fa732e0e-7e5f-4d45-994a-fc74720c0781
  language: de
affair_id: affairs:2023P_102
datetime_created: '2025-01-29T06:59:41Z'
datetime_modified: '2025-01-29T06:59:41Z'

```
#### Example: AgendaItem-meeting_item_21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de

```yaml
global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
parent_meeting: ops:meeting_bern_rr_2025_04_02
agenda_item_type: item
datetime_begin_planned: '2025-04-02T00:00:00Z'
agenda_item_title:
- text: 'Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe Betreuungsgutscheine
    für alle Anbieter im Kanton Bern». Regierungsrätliches Antwortschreiben'
  language: de
affair_id: affairs:2025.STA.622
url:
- text: https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
  language: de
datetime_created: '2025-04-25T11:11:40Z'
datetime_modified: '2025-04-25T11:11:40Z'

```
#### Example: AgendaItem-meeting_item_2023_10_03-52

```yaml
global_uri: ops:2023_10_03-52
parent_meeting: ops:meeting_lausanne_2023_10_03
agenda_item_type: item
datetime_begin_planned: '2023-10-03T00:00:00Z'
agenda_item_position: 52
agenda_item_number: '52'
agenda_item_title:
- text: 'Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale
    » (FIM)'
  language: fr
state_id: postponed
agenda_item_category: RAPPORTS
affair_id: affairs:POS22/029
url:
- text: https://www.lausanne.ch/apps/agir/affaire/81/b7157ea2a4994086b65cf176768c6381.htm
  language: fr
datetime_created: '2025-02-08T12:33:10Z'
datetime_modified: '2025-02-08T12:33:10Z'

```
#### Example: AgendaItem-meeting_item_49_253

```yaml
global_uri: ops:49_253
parent_meeting: ops:meeting_2025_03_31
agenda_item_type: item
datetime_begin_planned: '2025-03-31T00:00:00Z'
agenda_item_position: 2
agenda_item_number: '2'
agenda_item_title:
- text: Programmvereinbarungen 2024
  language: de
datetime_created: '2025-03-29T01:07:14Z'
datetime_modified: '2025-03-29T01:07:14Z'

```
#### Example: AgendaItem-meeting_item_87b69a72919445a493a061d9b0daeba3

```yaml
global_uri: ops:87b69a72919445a493a061d9b0daeba3
parent_meeting: ops:meeting_be_2025_06_02
agenda_item_type: item
datetime_begin_planned: '2025-06-02T00:00:00Z'
agenda_item_title:
- text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
  language: de
affair_id: affairs:2025.GRPARL.81
datetime_created: '2025-04-25T11:10:35Z'
datetime_modified: '2025-04-25T11:10:35Z'

```
#### Example: AgendaItem-meeting_complete_agenda_item_be_2025_042

```yaml
global_uri: ops:agenda_item_be_2025_042
parent_meeting: ops:meeting_be_committee_wak_2025_05_12
agenda_item_type: item
agenda_item_number: '4.2'
agenda_item_position: 42
agenda_item_title:
- text: Steuergesetz - Detailberatung Art. 5
  language: de
- text: Loi fiscale - Délibération détaillée art. 5
  language: fr
agenda_item_description:
- text: Beratung von Änderungsanträgen zu Artikel 5 des Steuergesetzes
  language: de
- text: Délibération sur les propositions de modification de l'article 5 de la loi
    fiscale
  language: fr
agenda_item_category: Gesetzgebung
state_id: completed
datetime_begin_planned: '2025-05-12T15:00:00Z'
datetime_begin_actual: '2025-05-12T15:15:00Z'
affair_id: affairs:be_2024_089_steuergesetz
datetime_created: '2025-04-15T09:00:00Z'
datetime_modified: '2025-05-12T15:20:00Z'

```
#### Example: AgendaItem-meeting_item_0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a

```yaml
global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
parent_meeting: ops:meeting_luzern_2025_01_28
agenda_item_type: item
datetime_begin_planned: '2025-01-28T00:00:00Z'
agenda_item_position: 29
agenda_item_number: '29'
agenda_item_title:
- text: Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung des
    Sonderschulkonkordats und zur gezielten Behebung des Fachkräftemangels im Bereich
    schulische Heilpädagogik / Bildungs- und Kulturdepartement
  language: de
agenda_item_category: voting
url:
- text: https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
  language: de
affair_id: affairs:2024P_125
datetime_created: '2025-01-29T06:59:41Z'
datetime_modified: '2025-01-29T06:59:41Z'

```
#### Example: AgendaItem-meeting_item_16155798_3

```yaml
global_uri: ops:16155798_3
parent_meeting: ops:meeting_schaffhausen_2025_03_31
agenda_item_type: item
datetime_begin_planned: '2025-03-31T00:00:00Z'
agenda_item_position: 2
agenda_item_number: '2'
agenda_item_title:
- text: Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend zeitgemässe
    Abzüge in den Art. 35 und 37 des Gesetzes über die direkten Steuern
  language: de
agenda_item_category: Traktanden
affair_id: affairs:MOT_2023_9
datetime_created: '2025-05-02T11:23:49Z'
datetime_modified: '2025-05-02T11:23:49Z'

```
#### Example: AgendaItem-meeting_complete_agenda_item_sg_2025_015

```yaml
global_uri: ops:agenda_item_sg_2025_015
parent_meeting: ops:meeting_sg_2025_03_15
agenda_item_type: item
agenda_item_number: '15'
agenda_item_position: 15
agenda_item_title:
- text: Energiegesetz - Schlussabstimmung
  language: de
agenda_item_description:
- text: Schlussabstimmung über das revidierte Energiegesetz des Kantons St. Gallen
  language: de
agenda_item_category: Gesetzgebung
state_id: completed
datetime_begin_planned: '2025-03-15T14:00:00Z'
datetime_begin_actual: '2025-03-15T14:30:00Z'
affair_id: affairs:sg_2024_123_energiegesetz
datetime_created: '2025-02-01T10:00:00Z'
datetime_modified: '2025-03-15T14:35:00Z'

```
#### Example: AgendaItem-meeting_item_7b3545e4-57dc-3901-aaa8-4020da6ab0c6

```yaml
global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
parent_meeting: ops:meeting_vaud_2008_04_30
agenda_item_type: item
datetime_begin_planned: '2008-04-30T00:00:00Z'
agenda_item_position: 7
agenda_item_number: '7'
agenda_item_title:
- text: Révision partielle de sept ordonnances fédérales relatives aux produits chimiques
  language: fr
agenda_item_description:
- text: 'Le Conseil d''Etat approuve le projet de révision partielle de sept ordonnances
    fédérales relatives aux produits chimiques. Il salue la volonté des autorités
    fédérales d''introduire dans la législation fédérale les modifications nécessaires
    découlant des nouveaux règlements européens, afin d''éliminer des entraves au
    commerce et d''augmenter la sécurité d''évaluation des produits chimiques.

    '
  language: fr
url:
- text: https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
  language: fr
datetime_created: '2024-12-06T10:50:04Z'
datetime_modified: '2024-12-06T10:50:04Z'

```
#### Example: AgendaItem-meeting_item_16155798_4

```yaml
global_uri: ops:16155798_4
parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
agenda_item_type: item
datetime_begin_planned: '2025-03-31T00:00:00Z'
agenda_item_position: 3
agenda_item_number: '3'
agenda_item_title:
- text: 'Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff (Erstunterzeichnende)
    sowie weitere 150 Mitunterzeichnende vom 22. März 2024 mit dem Titel: «Für eine
    Stimme der Studierenden im Hochschulrat der Pädagogischen Hochschule Schaffhausen
    (PHSH)»'
  language: de
agenda_item_category: Traktanden
affair_id: affairs:MOT_2024_1
datetime_created: '2025-05-02T11:23:49Z'
datetime_modified: '2025-05-02T11:23:49Z'

```
#### Example: AgendaItem-meeting_item_06fb582b753c416d8fdb05fa13873545

```yaml
global_uri: ops:06fb582b753c416d8fdb05fa13873545
parent_meeting: ops:meeting_2011_11_23
agenda_item_type: item
datetime_begin_planned: '2011-11-23T00:00:00Z'
agenda_item_position: 2
agenda_item_title:
- text: Interpellation Peter Mark betr. elektronische Datenerfassung durch Mitarbeiter
    im Werkhof – Versuchsphase
  language: de
datetime_created: '2025-03-21T23:15:19Z'
datetime_modified: '2025-03-21T23:15:19Z'

```
#### Example: AgendaItem-meeting_complete_agenda_item_zh_budget_2026

```yaml
global_uri: ops:agenda_item_zh_budget_2026
parent_meeting: ops:meeting_zh_2025_11_20
agenda_item_type: item
agenda_item_number: '8'
agenda_item_position: 8
agenda_item_title:
- text: Budget 2026
  language: de
agenda_item_description:
- text: Beratung und Beschlussfassung über das Kantonsbudget für das Jahr 2026
  language: de
agenda_item_category: Budget und Finanzen
state_id: completed
datetime_begin_planned: '2025-11-20T16:00:00Z'
datetime_begin_actual: '2025-11-20T16:45:00Z'
affair_id: affairs:zh_2025_budget_2026
datetime_created: '2025-10-01T08:00:00Z'
datetime_modified: '2025-11-20T16:50:00Z'

```
#### Example: AgendaItem-meeting_item_cea750a5bd7b420fa4da1c914f801384

```yaml
global_uri: ops:cea750a5bd7b420fa4da1c914f801384
parent_meeting: ops:meeting_bern_2022_03_17
agenda_item_type: item
datetime_begin_planned: '2022-03-17T17:00:00Z'
agenda_item_position: 29
agenda_item_number: '8'
agenda_item_title:
- text: 'Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche Konsequenzen
    haben die Klimaziele für das Gasnetz in Bern?'
  language: de
affair_id: affairs:2020.SR.000007
url:
- text: https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
  language: de
datetime_created: '2025-01-17T21:25:52Z'
datetime_modified: '2025-01-17T21:25:52Z'

```
#### Example: AgendaItem-meeting_item_2025_05_20-23

```yaml
global_uri: ops:2025_05_20-23
parent_meeting: ops:meeting_lausanne_2025_05_20
agenda_item_type: item
datetime_begin_planned: '2025-05-20T00:00:00Z'
agenda_item_position: 23
agenda_item_number: '23'
agenda_item_title:
- text: 'Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation
    urgente de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en faveur
    du respect du droit international et de la protection des populations civiles
    à Gaza »'
  language: fr
state_id: not_treated
agenda_item_category: ANNONCES ET INTERPELLATIONS
affair_id: affairs:INT25/027
url:
- text: https://www.lausanne.ch/apps/agir/affaire/6c/049b6c612fe2428f9be66ea39522ac6c.htm
  language: fr
datetime_created: '2025-06-07T23:50:18Z'
datetime_modified: '2025-06-07T23:50:18Z'

```
#### Example: AgendaItem-meeting_sr_winter25_Sitzung6_69905

```yaml
global_uri: ops:69905
parent_meeting: parl:sr_winter25_sitzung_6
agenda_item_type: item
datetime_begin_planned: '2025-12-19T09:15:00+01:00'
datetime_begin_actual: '2025-12-19T09:20:00+01:00'
agenda_item_number: '6'
agenda_item_position: 4
agenda_item_title:
- text: Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
    durchführen, um die Verzögerungen zu verstehen
  language: de
affair_id: affairs:24.4471
landing_page: https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
agenda_item_category: agenda_item
datetime_created: '2026-01-12T00:00:00+01:00'
datetime_modified: '2026-01-12T00:00:00+01:00'

```






</div>