

## Klasse: Meeting 


_Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Beschlüsse gefasst und Wortmeldungen festgehalten werden. Die Sitzung ist der Knoten, an dem die übrigen Klassen dieses Standards hängen: Ihre Traktanden (AgendaItem) sind in sie eingebettet (agenda_items), während Abstimmungen und Wahlen (Voting, Election), Wortmeldungen (Speech) sowie die Anwesenheitsliste (Attendance) über `parent_meeting` auf sie verweisen. Auf dieser Ebene fallen geplante und tatsächliche Zeiten regelmässig auseinander — eine für 14:00 angesetzte Sitzung beginnt wegen Verzögerungen erst um 14:25 und endet statt um 18:00 bereits um 17:30 —, weshalb Beginn und Ende sowohl geplant als auch tatsächlich erfasst werden._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| spatial | 0..1 <br/> [String](String.md) | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> [String](String.md) | Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Mehrsprachige vollständige Bezeichnung.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| group_name | 0..1 <br/> [String](String.md) | Name der Gruppe oder des Gremiums im Klartext, zusätzlich zur Referenz `group_id`.  |
| group_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf die Gruppe oder das Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| number | 0..1 <br/> [String](String.md) | Nummer der Session oder Sitzung, wie sie das Organ vergibt, z.B. innerhalb der Legislatur, der Session oder des Jahres. Als Zeichenkette erlaubt sie auch römische Ziffern. Nummeriert wird sehr unterschiedlich, weshalb number, sequential_number, position und meeting_abbreviation nebeneinander zur Verfügung stehen.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> [String](String.md) | Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z.B. einer Session innerhalb der Legislaturperiode.  |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession 2024).  |
| actor_name | 0..1 <br/> [String](String.md) | Name des politischen Organs im Klartext (z.B. Nationalrat), zusätzlich zur Referenz `actor_id`.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| state | 0..1 <br/> [StateEnum](StateEnum.md) | Ob die Sitzung überhaupt wie vorgesehen stattfindet (geplant, abgesagt, verschoben). Eine abweichende, freitextliche Bezeichnung nimmt `state_name` auf.  |
| state_name | 0..1 <br/> [String](String.md) | Abweichende, freitextliche Statusbezeichnung der Sitzung, wo die Werte von `state` nicht genügen.  |
| description | 0..1 <br/> [String](String.md) | Beschreibender Text zum Element.  |
| location | 0..1 <br/> [String](String.md) | Ort, an dem die Sitzung stattfindet — der physische Raum („Bundeshaus, Nationalratssaal“), eine Videokonferenz oder ein hybrides Format.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung bezeichnet er die übergeordnete Sitzung, bei Abstimmung, Wahl, Wortmeldung, Anwesenheitsliste oder Protokoll die Sitzung, in der der Eintrag entstanden ist. Traktanden führen ihn nicht: Sie sind in ihre Sitzung eingebettet.  |
| parent_legislature | 0..1 <br/> [String](String.md) | Identifikator der Legislaturperiode, zu der die Session oder Sitzung gehört. Eine Sitzung, die zu einer Session gehört, ist über die Session (parent_session) der Legislaturperiode zugeordnet; eine Sitzung ohne Session — etwa eine Kommissionssitzung oder eine Sitzung in einer Föderaleinheit ohne formale Sessionen — verweist direkt auf die Legislaturperiode.  |
| parent_session | 0..1 <br/> [String](String.md) | Identifikator der Session, zu der die Sitzung gehört.  |
| documents | * <br/> [Work](Work.md) | Sitzungsunterlagen wie Tagblatt oder Beilagen, als FRBR-Works. Das Protokoll wird nicht hier, sondern über `has_protocol` verknüpft.  |
| agenda_items | * <br/> [AgendaItem](AgendaItem.md) | Für diese Sitzung oder Session geplante Traktanden, eingebettet als Liste. Bei einer Sitzung bilden sie deren Traktandenliste. Bei einer Session enthalten sie Traktanden, die direkt auf Ebene der Session geplant sind — wo eine Föderaleinheit die Session nicht in einzelne Sitzungen gliedert (z.B. eine Landsgemeinde oder eine eintägige Sitzung eines Kantonsparlaments) oder für Traktanden, die (noch) keiner bestimmten Sitzung zugeordnet sind, wie in einem Sessionsprogramm. Das Gegenstück nach der Sitzung sind die im Protokoll festgehaltenen Traktanden (Protocol.protocol_items).  |
| has_protocol | 0..1 <br/> [Protocol](Protocol.md) | Referenz auf das nach der Sitzung erstellte Protokoll dieser Sitzung. Angegeben wird nur der Identifikator des Protokolls; das Protokoll selbst wird in der Liste `protocols` des Containers geliefert. Es ist eine eigenständige Entität mit eigenem Identifikator und wird in der Regel später veröffentlicht als die Sitzung, weshalb es referenziert und nicht eingebettet wird.  |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird; bei einer Sitzung oder Session die darin geführten gemeinsamen Beratungen.  |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |
| [Session](Session.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |














### Beispiele
#### Beispiel Meeting: meeting item meeting be 2025 06 02

```yaml
meetings:
- global_uri: ops:meeting_be_2025_06_02
  date_begin_planned: '2025-06-02'
  agenda_items:
  - global_uri: ops:87b69a72919445a493a061d9b0daeba3
    agenda_item_type: item
    datetime_begin_planned: '2025-06-02T00:00:00Z'
    agenda_item_title:
    - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
      language: de
    affair_id: affairs:2025.GRPARL.81
    datetime_created: '2025-04-25T11:10:35Z'
    datetime_modified: '2025-04-25T11:10:35Z'

```
#### Beispiel Meeting: Committee sitting with an attendance list

```yaml
meetings:
- global_uri: ops:meeting_be_committee_wak_2025_05_12
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Sitzung Kommission für Wirtschaft und Abgaben
    language: de
  - text: Séance Commission de l'économie et des redevances
    language: fr
  url:
  - text: https://www.gr.be.ch/kommissionen/wak/2025-05-12
    language: de
  actor_id:
    global_uri: actors:committee_wak_be
    label: Kommission für Wirtschaft und Abgaben (WAK)
    abbreviation:
    - value: WAK
      language: de
  actor_name: Kommission für Wirtschaft und Abgaben (WAK)
  datetime_begin_planned: '2025-05-12T14:00:00Z'
  datetime_end_planned: '2025-05-12T17:00:00Z'
  datetime_begin_actual: '2025-05-12T14:10:00Z'
  datetime_end_actual: '2025-05-12T16:45:00Z'
  state: planned
  location: Kommissionszimmer 301, Rathaus Bern
  parent_legislature: ops:legislature_be_2022_2026
  datetime_created: '2025-04-15T09:00:00Z'
  datetime_modified: '2025-05-12T16:45:00Z'
  agenda_items:
  - global_uri: ops:agenda_item_be_2025_042
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
    - text: >-
        Délibération sur les propositions de modification de l'article 5 de la loi
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
#### Beispiel Meeting: meeting item meeting schaffhausen 2025 03 31 b

```yaml
meetings:
- global_uri: ops:meeting_schaffhausen_2025_03_31_b
  date_begin_planned: '2025-03-31'
  agenda_items:
  - global_uri: ops:16155798_4
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 3
    agenda_item_number: '3'
    agenda_item_title:
    - text: >-
        Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff (Erstunterzeichnende)
        sowie weitere 150 Mitunterzeichnende vom 22. März 2024 mit dem Titel: «Für
        eine Stimme der Studierenden im Hochschulrat der Pädagogischen Hochschule
        Schaffhausen (PHSH)»
      language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2024_1
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'

```
#### Beispiel Meeting: meeting item meeting vaud 2008 04 30

```yaml
meetings:
- global_uri: ops:meeting_vaud_2008_04_30
  date_begin_planned: '2008-04-30'
  agenda_items:
  - global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
    agenda_item_type: item
    datetime_begin_planned: '2008-04-30T00:00:00Z'
    agenda_item_position: 7
    agenda_item_number: '7'
    agenda_item_title:
    - text: >-
        Révision partielle de sept ordonnances fédérales relatives aux produits chimiques
      language: fr
    agenda_item_description:
    - text: 'Le Conseil d''Etat approuve le projet de révision partielle de sept ordonnances
        fédérales relatives aux produits chimiques. Il salue la volonté des autorités
        fédérales d''introduire dans la législation fédérale les modifications nécessaires
        découlant des nouveaux règlements européens, afin d''éliminer des entraves
        au commerce et d''augmenter la sécurité d''évaluation des produits chimiques.

        '
      language: fr
    url:
    - text: >-
        https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
      language: fr
    datetime_created: '2024-12-06T10:50:04Z'
    datetime_modified: '2024-12-06T10:50:04Z'

```
#### Beispiel Meeting: Landsgemeinde as meeting type sitting

```yaml
meetings:
- global_uri: ops:meeting_gl_landsgemeinde_2025
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Landsgemeinde 2025
    language: de
  url:
  - text: https://www.landsgemeinde.gl.ch/2025
    language: de
  actor_id:
    global_uri: actors:landsgemeinde_gl
    label: Landsgemeinde Glarus
    abbreviation:
    - value: LG
      language: de
  actor_name: Landsgemeinde Glarus
  datetime_begin_planned: '2025-05-04T09:30:00Z'
  datetime_end_planned: '2025-05-04T14:00:00Z'
  datetime_begin_actual: '2025-05-04T09:30:00Z'
  datetime_end_actual: '2025-05-04T13:45:00Z'
  state: planned
  location: Zaunplatz, Glarus
  parent_session: ops:session_gl_landsgemeinde_2025
  datetime_created: '2025-01-10T12:00:00Z'
  datetime_modified: '2025-05-04T13:45:00Z'

```
#### Beispiel Meeting: meeting item meeting bern 2022 03 17

```yaml
meetings:
- global_uri: ops:meeting_bern_2022_03_17
  date_begin_planned: '2022-03-17'
  agenda_items:
  - global_uri: ops:cea750a5bd7b420fa4da1c914f801384
    agenda_item_type: item
    datetime_begin_planned: '2022-03-17T17:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '8'
    agenda_item_title:
    - text: >-
        Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche Konsequenzen
        haben die Klimaziele für das Gasnetz in Bern?
      language: de
    affair_id: affairs:2020.SR.000007
    url:
    - text: >-
        https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
      language: de
    datetime_created: '2025-01-17T21:25:52Z'
    datetime_modified: '2025-01-17T21:25:52Z'

```
#### Beispiel Meeting: Council of States sitting with protocol and speeches

```yaml
meetings:
- global_uri: parl:sr_winter25_sitzung_6
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: Sechste Sitzung
    language: de
  - text: Sixième séance
    language: fr
  url:
  - text: https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin
    language: de
  actor_id:
    global_uri: actors:staenderat
    label: Ständerat
    abbreviation:
    - value: SR
      language: de
  actor_name: Ständerat
  datetime_begin_planned: '2025-12-19T08:15:00+01:00'
  has_protocol: ops:protokoll_sr_winter25_sitzung_6
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'
  agenda_items:
  - global_uri: ops:69905
    agenda_item_type: item
    datetime_begin_planned: '2025-12-19T09:15:00+01:00'
    datetime_begin_actual: '2025-12-19T09:20:00+01:00'
    agenda_item_number: '6'
    agenda_item_position: 4
    agenda_item_title:
    - text: >-
        Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
        durchführen, um die Verzögerungen zu verstehen
      language: de
    affair_id: affairs:24.4471
    landing_page: >-
      https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
    agenda_item_category: agenda_item
    datetime_created: '2026-01-12T00:00:00+01:00'
    datetime_modified: '2026-01-12T00:00:00+01:00'

```
#### Beispiel Meeting: Government sitting with a bilingual designation

```yaml
meetings:
- spatial: https://ld.admin.ch/canton/2
  global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
  name:
  - text: Regierungssitzung vom 31. März 2021
    language: de
  - text: Séance du gouvernement du 31 mars 2021
    language: fr
  url:
  - text: >-
      https://www.rr.be.ch/de/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
    language: de
  - text: >-
      https://www.rr.be.ch/fr/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
    language: fr
  actor_id:
    global_uri: actors:rr_be
    label: Regierungsrat Bern
    abbreviation:
    - value: RR
      language: de
  actor_name: Regierungsrat Bern
  date_begin_planned: '2021-03-31'
  date_end_planned: '2021-03-31'
  datetime_created: '2024-10-28T01:22:26Z'
  datetime_modified: '2024-11-27T20:40:57Z'

```
#### Beispiel Meeting: Cantonal parliament sitting with agenda items and votings

```yaml
meetings:
- global_uri: ops:meeting_sg_2025_03_15
  spatial: https://ld.admin.ch/canton/17
  name:
  - text: Kantonsratssitzung vom 15. März 2025
    language: de
  url:
  - text: https://www.ratsinfo.sg.ch/sessions/2025-03-15
    language: de
  actor_id:
    global_uri: actors:kr_sg
    label: Kantonsrat St. Gallen
    abbreviation:
    - value: KR
      language: de
  actor_name: Kantonsrat St. Gallen
  datetime_begin_planned: '2025-03-15T08:00:00Z'
  datetime_end_planned: '2025-03-15T18:00:00Z'
  datetime_begin_actual: '2025-03-15T08:15:00Z'
  datetime_end_actual: '2025-03-15T17:30:00Z'
  state: planned
  location: Kantonsratssaal, Regierungsgebäude St. Gallen
  parent_session: ops:session_sg_2025_03
  datetime_created: '2025-02-01T10:00:00Z'
  datetime_modified: '2025-03-15T17:30:00Z'
  agenda_items:
  - global_uri: ops:agenda_item_sg_2025_015
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
#### Beispiel Meeting: meeting item meeting 2011 11 23

```yaml
meetings:
- global_uri: ops:meeting_2011_11_23
  date_begin_planned: '2011-11-23'
  agenda_items:
  - global_uri: ops:06fb582b753c416d8fdb05fa13873545
    agenda_item_type: item
    datetime_begin_planned: '2011-11-23T00:00:00Z'
    agenda_item_position: 2
    agenda_item_title:
    - text: >-
        Interpellation Peter Mark betr. elektronische Datenerfassung durch Mitarbeiter
        im Werkhof – Versuchsphase
      language: de
    datetime_created: '2025-03-21T23:15:19Z'
    datetime_modified: '2025-03-21T23:15:19Z'

```
#### Beispiel Meeting: meeting item meeting lausanne 2025 05 20

```yaml
meetings:
- global_uri: ops:meeting_lausanne_2025_05_20
  date_begin_planned: '2025-05-20'
  agenda_items:
  - global_uri: ops:2025_05_20-23
    agenda_item_type: item
    datetime_begin_planned: '2025-05-20T00:00:00Z'
    agenda_item_position: 23
    agenda_item_number: '23'
    agenda_item_title:
    - text: >-
        Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation
        urgente de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en
        faveur du respect du droit international et de la protection des populations
        civiles à Gaza »
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

```
#### Beispiel Meeting: meeting item meeting 2025 03 31

```yaml
meetings:
- global_uri: ops:meeting_2025_03_31
  date_begin_planned: '2025-03-31'
  agenda_items:
  - global_uri: ops:49_253
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
#### Beispiel Meeting: meeting item meeting schaffhausen 2025 03 31

```yaml
meetings:
- global_uri: ops:meeting_schaffhausen_2025_03_31
  date_begin_planned: '2025-03-31'
  agenda_items:
  - global_uri: ops:16155798_3
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 2
    agenda_item_number: '2'
    agenda_item_title:
    - text: >-
        Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend zeitgemässe
        Abzüge in den Art. 35 und 37 des Gesetzes über die direkten Steuern
      language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2023_9
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'

```
#### Beispiel Meeting: meeting item meeting bern rr 2025 04 02

```yaml
meetings:
- global_uri: ops:meeting_bern_rr_2025_04_02
  date_begin_planned: '2025-04-02'
  agenda_items:
  - global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
    agenda_item_type: item
    datetime_begin_planned: '2025-04-02T00:00:00Z'
    agenda_item_title:
    - text: >-
        Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe Betreuungsgutscheine
        für alle Anbieter im Kanton Bern». Regierungsrätliches Antwortschreiben
      language: de
    affair_id: affairs:2025.STA.622
    url:
    - text: >-
        https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
      language: de
    datetime_created: '2025-04-25T11:11:40Z'
    datetime_modified: '2025-04-25T11:11:40Z'

```
#### Beispiel Meeting: Half-day sitting within a session

```yaml
meetings:
- spatial: https://ld.admin.ch/canton/2
  global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
  name:
  - text: Donnerstag (Nachmittag)
    language: de
  url:
  - text: >-
      https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: de
  - text: >-
      https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: fr
  actor_id:
    global_uri: actors:gr_be
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  actor_name: Grosser Rat Bern
  date_begin_planned: '2025-06-05'
  date_end_planned: '2025-06-05'
  datetime_created: '2025-04-25T11:10:25Z'
  datetime_modified: '2025-05-19T01:06:45Z'

```
#### Beispiel Meeting: meeting item meeting lausanne 2023 10 03

```yaml
meetings:
- global_uri: ops:meeting_lausanne_2023_10_03
  date_begin_planned: '2023-10-03'
  agenda_items:
  - global_uri: ops:2023_10_03-52
    agenda_item_type: item
    datetime_begin_planned: '2023-10-03T00:00:00Z'
    agenda_item_position: 52
    agenda_item_number: '52'
    agenda_item_title:
    - text: >-
        Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale
        » (FIM)
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

```
#### Beispiel Meeting: meeting complete meeting zh 2025 11 20

```yaml
meetings:
- global_uri: ops:meeting_zh_2025_11_20
  date_begin_planned: '2025-11-20'
  agenda_items:
  - global_uri: ops:agenda_item_zh_budget_2026
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
#### Beispiel Meeting: meeting item meeting luzern 2025 01 28

```yaml
meetings:
- global_uri: ops:meeting_luzern_2025_01_28
  date_begin_planned: '2025-01-28'
  agenda_items:
  - global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '29'
    agenda_item_title:
    - text: >-
        Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung des
        Sonderschulkonkordats und zur gezielten Behebung des Fachkräftemangels im
        Bereich schulische Heilpädagogik / Bildungs- und Kulturdepartement
      language: de
    agenda_item_category: voting
    url:
    - text: >-
        https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
      language: de
    affair_id: affairs:2024P_125
    datetime_created: '2025-01-29T06:59:41Z'
    datetime_modified: '2025-01-29T06:59:41Z'

```
#### Beispiel Meeting: meeting item meeting luzern 2025 01 28 b

```yaml
meetings:
- global_uri: ops:meeting_luzern_2025_01_28_b
  date_begin_planned: '2025-01-28'
  agenda_items:
  - global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 14
    agenda_item_number: '14'
    agenda_item_title:
    - text: >-
        Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und Anpassung
        der Kriterien zum früheren Eintritt von Kindern in die Basisstufe (den freiwilligen
        Kindergarten) / Bildungs- und Kulturdepartement
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






</div>