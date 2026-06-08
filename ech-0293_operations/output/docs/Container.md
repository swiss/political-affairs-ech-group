

## Class: Container 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| legislatures | * <br/> [Legislature](Legislature.md) | None |
| sessions | * <br/> [Session](Session.md) | None |
| meetings | * <br/> [Meeting](Meeting.md) | None |
| agenda_items | * <br/> [AgendaItem](AgendaItem.md) | None |
| protocols | * <br/> [Protocol](Protocol.md) | Collection of protocol records |
| votings | * <br/> [Voting](Voting.md) | Collection of voting records |
| elections | * <br/> [Election](Election.md) | Collection of election records |
| individual_votes | * <br/> [IndividualVote](IndividualVote.md) | Collection of individual vote records |
| attendances | * <br/> [Attendance](Attendance.md) | Collection of attendance records |
| individual_attendances | * <br/> [IndividualAttendance](IndividualAttendance.md) | Collection of individual attendance records |
| speeches | * <br/> [Speech](Speech.md) | Collection of speech records |
| resolutions | * <br/> [Resolution](Resolution.md) | Collection of resolutionrecords |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |

















### Examples
#### Example: Container-meeting_complete

```yaml
global_uri: ops:meeting_examples_2025

meetings:

- global_uri: ops:meeting_sg_2025_03_15
  body_key: "SG"
  meeting_type: "session"
  name:
    - text: "Kantonsratssitzung vom 15. März 2025"
      language: "de"
  url:
    - text: "https://www.ratsinfo.sg.ch/sessions/2025-03-15"
      language: "de"
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/265"
    label: "Kantonsrat St. Gallen"
    abbreviation:
      - value: "KR"
        language: de
  actor_name: "Kantonsrat St. Gallen"
  datetime_begin_planned: "2025-03-15T08:00:00Z"
  datetime_end_planned: "2025-03-15T18:00:00Z"
  datetime_begin_actual: "2025-03-15T08:15:00Z"
  datetime_end_actual: "2025-03-15T17:30:00Z"
  state: "planned"
  location: "Kantonsratssaal, Regierungsgebäude St. Gallen"
  parent_legislature: ops:legislature_sg_2024_2028
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T17:30:00Z"

- global_uri: ops:meeting_be_committee_wak_2025_05_12
  body_key: "BE"
  meeting_type: "committee"
  name:
    - text: "Sitzung Kommission für Wirtschaft und Abgaben"
      language: "de"
    - text: "Séance Commission de l'économie et des redevances"
      language: "fr"
  url:
    - text: "https://www.gr.be.ch/kommissionen/wak/2025-05-12"
      language: "de"
  actor_id:
    global_uri: "actors:committee_wak_be"
    label: "Kommission für Wirtschaft und Abgaben (WAK)"
    abbreviation:
      - value: "WAK"
        language: de
  actor_name: "Kommission für Wirtschaft und Abgaben (WAK)"
  datetime_begin_planned: "2025-05-12T14:00:00Z"
  datetime_end_planned: "2025-05-12T17:00:00Z"
  datetime_begin_actual: "2025-05-12T14:10:00Z"
  datetime_end_actual: "2025-05-12T16:45:00Z"
  state: "planned"
  location: "Kommissionszimmer 301, Rathaus Bern"
  parent_legislature: ops:legislature_be_2022_2026
  datetime_created: "2025-04-15T09:00:00Z"
  datetime_modified: "2025-05-12T16:45:00Z"

- global_uri: ops:meeting_gl_landsgemeinde_2025
  body_key: "GL"
  meeting_type: "sitting"
  name:
    - text: "Landsgemeinde 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/2025"
      language: "de"
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/258"
    label: "Landsgemeinde Glarus"
    abbreviation:
      - value: "LG"
        language: de
  actor_name: "Landsgemeinde Glarus"
  datetime_begin_planned: "2025-05-04T09:30:00Z"
  datetime_end_planned: "2025-05-04T14:00:00Z"
  datetime_begin_actual: "2025-05-04T09:30:00Z"
  datetime_end_actual: "2025-05-04T13:45:00Z"
  state: "planned"
  location: "Zaunplatz, Glarus"
  parent_legislature: ops:legislature_gl_2024_2028
  datetime_created: "2025-01-10T12:00:00Z"
  datetime_modified: "2025-05-04T13:45:00Z"

agenda_items:

- global_uri: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  agenda_item_type: "item"
  agenda_item_number: "15"
  agenda_item_position: 15
  agenda_item_title:
    - text: "Energiegesetz - Schlussabstimmung"
      language: "de"
  agenda_item_description:
    - text: "Schlussabstimmung über das revidierte Energiegesetz des Kantons St. Gallen"
      language: "de"
  agenda_item_category: "Gesetzgebung"
  state_id: "completed"
  datetime_begin_planned: "2025-03-15T14:00:00Z"
  datetime_begin_actual: "2025-03-15T14:30:00Z"
  affair_id: "affairs:sg_2024_123_energiegesetz"
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T14:35:00Z"

- global_uri: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_committee_wak_2025_05_12
  agenda_item_type: "item"
  agenda_item_number: "4.2"
  agenda_item_position: 42
  agenda_item_title:
    - text: "Steuergesetz - Detailberatung Art. 5"
      language: "de"
    - text: "Loi fiscale - Délibération détaillée art. 5"
      language: "fr"
  agenda_item_description:
    - text: "Beratung von Änderungsanträgen zu Artikel 5 des Steuergesetzes"
      language: "de"
    - text: "Délibération sur les propositions de modification de l'article 5 de la loi fiscale"
      language: "fr"
  agenda_item_category: "Gesetzgebung"
  state_id: "completed"
  datetime_begin_planned: "2025-05-12T15:00:00Z"
  datetime_begin_actual: "2025-05-12T15:15:00Z"
  affair_id: "affairs:be_2024_089_steuergesetz"
  datetime_created: "2025-04-15T09:00:00Z"
  datetime_modified: "2025-05-12T15:20:00Z"

- global_uri: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  agenda_item_type: "item"
  agenda_item_number: "8"
  agenda_item_position: 8
  agenda_item_title:
    - text: "Budget 2026"
      language: "de"
  agenda_item_description:
    - text: "Beratung und Beschlussfassung über das Kantonsbudget für das Jahr 2026"
      language: "de"
  agenda_item_category: "Budget und Finanzen"
  state_id: "completed"
  datetime_begin_planned: "2025-11-20T16:00:00Z"
  datetime_begin_actual: "2025-11-20T16:45:00Z"
  affair_id: "affairs:zh_2025_budget_2026"
  datetime_created: "2025-10-01T08:00:00Z"
  datetime_modified: "2025-11-20T16:50:00Z"

```
#### Example: Container-session

```yaml
global_uri: ops:sessions_example_2025
sessions:

- global_uri: ops:session_5207
  body_key: "CHE"
  name:
    - text: "Frühjahrssession 2025"
      language: "de"
    - text: "Session de printemps 2025"
      language: "fr"
    - text: "Sessione primaverile 2025"
      language: "it"
  url:
    - text: "https://www.parlament.ch/de/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "de"
    - text: "https://www.parlament.ch/fr/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "fr"
    - text: "https://www.parlament.ch/it/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "it"
  date_begin_planned: "2025-03-03"
  date_end_planned: "2025-03-21"
  parent_legislature: ops:legislature_51
  datetime_modified: "2025-04-24T00:19:37Z"
  datetime_created: "2025-03-20T14:27:09Z"

- global_uri: ops:session_be_summer_2025
  body_key: "BE"
  name:
    - text: "Sommersession 2025"
      language: "de"
    - text: "Session d'été 2025"
      language: "fr"
  url:
    - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
      language: "de"
    - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
      language: "fr"
  date_begin_planned: "2025-06-02"
  date_end_planned: "2025-06-12"
  datetime_modified: "2025-05-19T01:06:44Z"
  datetime_created: "2025-04-25T11:10:24Z"

- global_uri: ops:session_gl_landrat_2025_02_26
  body_key: "GL"
  name:
    - text: "Sitzung des Landrates vom 26.02.2025"
      language: "de"
  url:
    - text: "https://www.gl.ch/parlament/landrat/landratsprotokolle-ab-30-juni-2010.html/239"
      language: "de"
  date_begin_planned: "2025-02-26"
  date_end_planned: "2025-02-26"
  datetime_modified: "2025-04-25T13:40:34Z"
  datetime_created: "2025-04-23T22:58:39Z"

- global_uri: ops:session_gl_landsgemeinde_2025_05_04
  body_key: "GL"
  name:
    - text: "Landsgemeinde vom 04. Mai 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/landsgemeinde/2025-05-04"
      language: "de"
  date_begin_planned: "2025-05-04"
  date_end_planned: "2025-05-04"
  datetime_modified: "2025-04-25T13:40:34Z"
  datetime_created: "2025-04-23T22:58:39Z"

```
#### Example: Container-voting

```yaml
global_uri: ops:voting_examples_2025

votings:

- global_uri: ops:voting_sg_2025_001
  voting_title:
    - text: "Schlussabstimmung Energiegesetz"
      language: "de"
  voting_type: "final_vote"
  datetime_begin: "2025-03-15T14:30:00Z"
  datetime_end: "2025-03-15T14:35:00Z"
  total_count_yes: 78
  total_count_no: 42
  total_count_abstention: 5
  total_absent: 3
  total: 128
  majority_type: "absolute"
  majority_count: 65
  result_text: "Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen"
  parent_agenda_item: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/265"
    label: "Kantonsrat St. Gallen"
    abbreviation:
      - value: "KR"
        language: de
  datetime_created: "2025-03-15T14:30:00Z"
  datetime_modified: "2025-03-15T14:35:00Z"

- global_uri: ops:voting_be_2025_042
  voting_title:
    - text: "Änderungsantrag Art. 5 Abs. 2"
      language: "de"
    - text: "Proposition de modification art. 5 al. 2"
      language: "fr"
  voting_type: "preliminary_vote"
  datetime_begin: "2025-06-05T10:15:00Z"
  datetime_end: "2025-06-05T10:17:00Z"
  total_count_yes: 45
  total_count_no: 87
  total_count_abstention: 8
  total_absent: 10
  total: 150
  majority_type: "absolute"
  majority_count: 76
  result_text: "Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt"
  parent_agenda_item: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/253"
    label: "Grosser Rat Bern"
    abbreviation:
      - value: "GR"
        language: de
  datetime_created: "2025-06-05T10:15:00Z"
  datetime_modified: "2025-06-05T10:15:00Z"

- global_uri: ops:voting_zh_budget_2026
  voting_title:
    - text: "Budgetbeschluss 2026"
      language: "de"
  voting_type: "final_vote"
  datetime_begin: "2025-11-20T16:45:00Z"
  datetime_end: "2025-11-20T16:50:00Z"
  total_count_yes: 105
  total_count_no: 70
  total_count_abstention: 5
  total_absent: 0
  total: 180
  majority_type: "absolute"
  majority_count: 91
  result_text: "Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen"
  parent_agenda_item: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/275"
    label: "Kantonsrat Zürich"
    abbreviation:
      - value: "KR"
        language: de
  datetime_created: "2025-11-20T16:45:00Z"
  datetime_modified: "2025-11-20T16:50:00Z"

individual_votes:

- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27235"
    label: "Paul Schlegel"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27234"
    label: "Andreas Eggenberger"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27233"
    label: "Thomas Ammann"
  seat_nr: "3"
  individual_vote_type: "abstention"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/25177"
    label: "Ruedi Thomann"
  seat_nr: "4"
  individual_vote_type: "not_voted"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27237"
    label: "Thomas Wolf"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-11-20T16:45:00Z"

- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/25208"
    label: "Jean-Daniel Strub"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-11-20T16:45:00Z"

```
#### Example: Container-meeting_sr_winter25_Sitzung6

```yaml
global_uri: ops:data_meeting_sr_winter25_Sitzung6

meetings:
  - global_uri: "parl:sr_winter25_sitzung_6"
    body_key: "CHE"
    meeting_type: "session"
    name:
      - text: "Sechste Sitzung"
        language: "de"
      - text: "Sixième séance"
        language: "fr"
    url:
      - text: "https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin"
        language: "de"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/bodies/42"
      label: "Ständerat"
      abbreviation:
        - value: "SR"
          language: de
    actor_name: "Ständerat"
    datetime_begin_planned: "2025-12-19T08:15:00+01:00"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

agenda_items:
  - global_uri: ops:69905
    parent_meeting: "parl:sr_winter25_sitzung_6"
    agenda_item_type: "item"
    datetime_begin_planned: "2025-12-19T09:15:00+01:00"
    datetime_begin_actual: "2025-12-19T09:20:00+01:00"
    agenda_item_number: "6"
    agenda_item_position: 4
    agenda_item_title:
      - text: "Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen, um die Verzögerungen zu verstehen"
        language: "de"
    affair_id: "affairs:24.4471"
    landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3"
    agenda_item_category: "agenda_item"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

speeches:
  - global_uri: ops:366631
    language: "fr"
    datetime_begin: "2025-12-19T09:20:00+01:00"
    datetime_end: "2025-12-19T09:25:00+01:00"
    actor_fullname: "Pascal Broulis"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/persons/18682"
      wikidata_uri: "https://www.wikidata.org/wiki/Q116407"
      label: "Pascal Broulis"
    role: "speaker"
    text: >-
      Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec attention
      les différents commentaires qui ont été effectués sur mon postulat. Cela reste un postulat,
      ce n'est pas une motion. D'abord, je ne partage pas l'avis selon lequel ce postulat
      n'apporterait pas une valeur ajoutée. En effet, un "benchmark", à savoir un modèle chiffré
      de performance, permettrait de mieux comprendre les raisons des retards que notre pays
      rencontre en comparaison avec les principaux pays européens.
    text_format: "html"
    text_type: "final"
    landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631"
    media_url: "https://par-pcache.simplex.tv/content?externalid=366631"
    media_type: "video"
    media_format: "video/mp4"

```
#### Example: Container-meeting_item

```yaml
global_uri: ops:agenda_items_1
agenda_items:
  - global_uri: ops:cea750a5bd7b420fa4da1c914f801384
    parent_meeting: ops:meeting_bern_2022_03_17
    agenda_item_type: item
    datetime_begin_planned: '2022-03-17T17:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '8'
    agenda_item_title:
      - text: >-
          Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche
          Konsequenzen haben die Klimaziele für das Gasnetz in Bern?
        language: de
    affair_id: affairs:2020.SR.000007
    url:
      - text: >-
          https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
        language: de
    datetime_created: '2025-01-17T21:25:52Z'
    datetime_modified: '2025-01-17T21:25:52Z'
  - global_uri: ops:2023_10_03-52
    parent_meeting: ops:meeting_lausanne_2023_10_03
    agenda_item_type: item
    datetime_begin_planned: '2023-10-03T00:00:00Z'
    agenda_item_position: 52
    agenda_item_number: '52'
    agenda_item_title:
      - text: >-
          Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité
          commerciale » (FIM)
        language: fr
    state_id: postponed
    agenda_item_category: RAPPORTS
    affair_id: affairs:POS22/029
    url:
      - text: >-
          https://www.lausanne.ch/apps/agir/affaire/81/b7157ea2a4994086b65cf176768c6381.htm
        language: fr
    datetime_created: '2025-02-08T12:33:10Z'
    datetime_modified: '2025-02-08T12:33:10Z'
  - global_uri: ops:2025_05_20-23
    parent_meeting: ops:meeting_lausanne_2025_05_20
    agenda_item_type: item
    datetime_begin_planned: '2025-05-20T00:00:00Z'
    agenda_item_position: 23
    agenda_item_number: '23'
    agenda_item_title:
      - text: >-
          Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : «
          Interpellation urgente de Kulmiye Yusuf et crts – Solidarité sans
          frontières, Lausanne en faveur du respect du droit international et de
          la protection des populations civiles à Gaza »
        language: fr
    state_id: not_treated
    agenda_item_category: ANNONCES ET INTERPELLATIONS
    affair_id: affairs:INT25/027
    url:
      - text: >-
          https://www.lausanne.ch/apps/agir/affaire/6c/049b6c612fe2428f9be66ea39522ac6c.htm
        language: fr
    datetime_created: '2025-06-07T23:50:18Z'
    datetime_modified: '2025-06-07T23:50:18Z'
  - global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
    parent_meeting: ops:meeting_vaud_2008_04_30
    agenda_item_type: item
    datetime_begin_planned: '2008-04-30T00:00:00Z'
    agenda_item_position: 7
    agenda_item_number: '7'
    agenda_item_title:
      - text: >-
          Révision partielle de sept ordonnances fédérales relatives aux
          produits chimiques
        language: fr
    agenda_item_description:
      - text: >
          Le Conseil d'Etat approuve le projet de révision partielle de sept
          ordonnances fédérales relatives aux produits chimiques. Il salue la
          volonté des autorités fédérales d'introduire dans la législation
          fédérale les modifications nécessaires découlant des nouveaux
          règlements européens, afin d'éliminer des entraves au commerce et
          d'augmenter la sécurité d'évaluation des produits chimiques.
        language: fr
    url:
      - text: >-
          https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
        language: fr
    datetime_created: '2024-12-06T10:50:04Z'
    datetime_modified: '2024-12-06T10:50:04Z'
  - global_uri: ops:06fb582b753c416d8fdb05fa13873545
    parent_meeting: ops:meeting_2011_11_23
    agenda_item_type: item
    datetime_begin_planned: '2011-11-23T00:00:00Z'
    agenda_item_position: 2
    agenda_item_title:
      - text: >-
          Interpellation Peter Mark betr. elektronische Datenerfassung durch
          Mitarbeiter im Werkhof – Versuchsphase
        language: de
    datetime_created: '2025-03-21T23:15:19Z'
    datetime_modified: '2025-03-21T23:15:19Z'
  - global_uri: ops:16155798_3
    parent_meeting: ops:meeting_schaffhausen_2025_03_31
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 2
    agenda_item_number: '2'
    agenda_item_title:
      - text: >-
          Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend
          zeitgemässe Abzüge in den Art. 35 und 37 des Gesetzes über die
          direkten Steuern
        language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2023_9
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'
  - global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
    parent_meeting: ops:meeting_bern_rr_2025_04_02
    agenda_item_type: item
    datetime_begin_planned: '2025-04-02T00:00:00Z'
    agenda_item_title:
      - text: >-
          Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe
          Betreuungsgutscheine für alle Anbieter im Kanton Bern».
          Regierungsrätliches Antwortschreiben
        language: de
    affair_id: affairs:2025.STA.622
    url:
      - text: >-
          https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
        language: de
    datetime_created: '2025-04-25T11:11:40Z'
    datetime_modified: '2025-04-25T11:11:40Z'
  - global_uri: ops:49_253
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
  - global_uri: ops:16155798_4
    parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 3
    agenda_item_number: '3'
    agenda_item_title:
      - text: >-
          Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff
          (Erstunterzeichnende) sowie weitere 150 Mitunterzeichnende vom 22.
          März 2024 mit dem Titel: «Für eine Stimme der Studierenden im
          Hochschulrat der Pädagogischen Hochschule Schaffhausen (PHSH)»
        language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2024_1
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'
  - global_uri: ops:87b69a72919445a493a061d9b0daeba3
    parent_meeting: ops:meeting_be_2025_06_02
    agenda_item_type: item
    datetime_begin_planned: '2025-06-02T00:00:00Z'
    agenda_item_title:
      - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
        language: de
    affair_id: affairs:2025.GRPARL.81
    datetime_created: '2025-04-25T11:10:35Z'
    datetime_modified: '2025-04-25T11:10:35Z'
  - global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
    parent_meeting: ops:meeting_luzern_2025_01_28
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '29'
    agenda_item_title:
      - text: >-
          Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung
          des Sonderschulkonkordats und zur gezielten Behebung des
          Fachkräftemangels im Bereich schulische Heilpädagogik / Bildungs- und
          Kulturdepartement
        language: de
    agenda_item_category: voting
    url:
      - text: >-
          https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
        language: de
    affair_id: affairs:2024P_125
    datetime_created: '2025-01-29T06:59:41Z'
    datetime_modified: '2025-01-29T06:59:41Z'
  - global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
    parent_meeting: ops:meeting_luzern_2025_01_28_b
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 14
    agenda_item_number: '14'
    agenda_item_title:
      - text: >-
          Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und
          Anpassung der Kriterien zum früheren Eintritt von Kindern in die
          Basisstufe (den freiwilligen Kindergarten) / Bildungs- und
          Kulturdepartement
        language: de
    agenda_item_category: voting
    url:
      - text: >-
          https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=fa732e0e-7e5f-4d45-994a-fc74720c0781
        language: de
    affair_id: affairs:2023P_102
    datetime_created: '2025-01-29T06:59:41Z'
    datetime_modified: '2025-01-29T06:59:41Z'

```
#### Example: Container-meeting

```yaml
global_uri: ops:meetings_1
meetings:
  - body_key: "BE"
    global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
    meeting_type: "session"
    name:
      - text: "Regierungssitzung vom 31. März 2021"
        language: "de"
      - text: "Séance du gouvernement du 31 mars 2021"
        language: "fr"
    url:
      - text: "https://www.rr.be.ch/de/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc"
        language: "de"
      - text: "https://www.rr.be.ch/fr/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc"
        language: "fr"
    actor_id:
      global_uri: "actors:rr_be"
      label: "Regierungsrat Bern"
      abbreviation:
        - value: "RR"
          language: de
    actor_name: "Regierungsrat Bern"
    date_begin_planned: "2021-03-31"
    date_end_planned: "2021-03-31"
    datetime_created: "2024-10-28T01:22:26Z"
    datetime_modified: "2024-11-27T20:40:57Z"

  - body_key: "BE"
    global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
    meeting_type: "session"
    name:
      - text: "Donnerstag (Nachmittag)"
        language: "de"
    url:
      - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "de"
      - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "fr"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/bodies/253"
      label: "Grosser Rat Bern"
      abbreviation:
        - value: "GR"
          language: de
    actor_name: "Grosser Rat Bern"
    date_begin_planned: "2025-06-05"
    date_end_planned: "2025-06-05"
    datetime_created: "2025-04-25T11:10:25Z"
    datetime_modified: "2025-05-19T01:06:45Z"

```






</div>