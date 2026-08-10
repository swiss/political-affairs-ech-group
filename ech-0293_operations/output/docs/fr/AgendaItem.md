

## Classe: AgendaItem 


_Un point de l'ordre du jour d'une séance._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance liée qui regroupe la séance courante.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | Numéro d'ordre du point de l'ordre du jour (type chaîne, afin de permettre les chiffres romains).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Position (nombre entier) du point de l'ordre du jour dans le déroulement de la séance.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | Le département responsable du point de l'ordre du jour.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titre du point de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](String.md) | Le lien vers les affaires rattachées au point de l'ordre du jour.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Sous-titre ou description détaillée du point de l'ordre du jour.  |
| state_id | 0..1 <br/> [String](String.md) | Identifiant d'état (renvoi à l'énumération des états ou à un état propre).  |
| state_name | 0..1 <br/> [String](String.md) | Description personnalisée de l'état de la séance.  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| agenda_item_category | 0..1 <br/> [String](String.md) | Catégorie pour les points de l'ordre du jour regroupés (p. ex. introduction, par département, points techniques).  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | La décision prise sur ce point de l'ordre du jour.  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |
| [JointDebate](JointDebate.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |














### Exemples
#### Exemple AgendaItem : Budget agenda item

```yaml
agenda_items:
- global_uri: ops:agenda_item_zh_budget_2026
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
#### Exemple AgendaItem : Motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_3
  parent_meeting: ops:meeting_schaffhausen_2025_03_31
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
#### Exemple AgendaItem : Agenda item of a Council of States sitting

```yaml
agenda_items:
- global_uri: ops:69905
  parent_meeting: parl:sr_winter25_sitzung_6
  agenda_item_type: item
  datetime_begin_planned: '2025-12-19T09:15:00+01:00'
  datetime_begin_actual: '2025-12-19T09:20:00+01:00'
  agenda_item_number: '6'
  agenda_item_position: 4
  agenda_item_title:
  - text: >-
      Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen,
      um die Verzögerungen zu verstehen
    language: de
  affair_id: affairs:24.4471
  landing_page: >-
    https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
  agenda_item_category: agenda_item
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```
#### Exemple AgendaItem : Postulate category voting

```yaml
agenda_items:
- global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
  parent_meeting: ops:meeting_luzern_2025_01_28
  agenda_item_type: item
  datetime_begin_planned: '2025-01-28T00:00:00Z'
  agenda_item_position: 29
  agenda_item_number: '29'
  agenda_item_title:
  - text: >-
      Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung des Sonderschulkonkordats
      und zur gezielten Behebung des Fachkräftemangels im Bereich schulische Heilpädagogik
      / Bildungs- und Kulturdepartement
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
#### Exemple AgendaItem : Interpellation of a parliamentary group

```yaml
agenda_items:
- global_uri: ops:cea750a5bd7b420fa4da1c914f801384
  parent_meeting: ops:meeting_bern_2022_03_17
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
#### Exemple AgendaItem : Petition as an agenda item

```yaml
agenda_items:
- global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
  parent_meeting: ops:meeting_bern_rr_2025_04_02
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
#### Exemple AgendaItem : Partial revision of several ordinances in French

```yaml
agenda_items:
- global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
  parent_meeting: ops:meeting_vaud_2008_04_30
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
      découlant des nouveaux règlements européens, afin d''éliminer des entraves au
      commerce et d''augmenter la sécurité d''évaluation des produits chimiques.

      '
    language: fr
  url:
  - text: >-
      https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
    language: fr
  datetime_created: '2024-12-06T10:50:04Z'
  datetime_modified: '2024-12-06T10:50:04Z'

```
#### Exemple AgendaItem : Substantive affair without an agenda category

```yaml
agenda_items:
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

```
#### Exemple AgendaItem : Detailed deliberation of an article of an act

```yaml
agenda_items:
- global_uri: ops:agenda_item_be_2025_042
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
  - text: >-
      Délibération sur les propositions de modification de l'article 5 de la loi fiscale
    language: fr
  agenda_item_category: Gesetzgebung
  state_id: completed
  datetime_begin_planned: '2025-05-12T15:00:00Z'
  datetime_begin_actual: '2025-05-12T15:15:00Z'
  affair_id: affairs:be_2024_089_steuergesetz
  datetime_created: '2025-04-15T09:00:00Z'
  datetime_modified: '2025-05-12T15:20:00Z'

```
#### Exemple AgendaItem : Interpellation as an agenda item

```yaml
agenda_items:
- global_uri: ops:06fb582b753c416d8fdb05fa13873545
  parent_meeting: ops:meeting_2011_11_23
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
#### Exemple AgendaItem : Substantive affair from a cantonal parliamentary information system

```yaml
agenda_items:
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

```
#### Exemple AgendaItem : Agenda item with a final vote

```yaml
agenda_items:
- global_uri: ops:agenda_item_sg_2025_015
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
#### Exemple AgendaItem : Popular motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_4
  parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
  agenda_item_type: item
  datetime_begin_planned: '2025-03-31T00:00:00Z'
  agenda_item_position: 3
  agenda_item_number: '3'
  agenda_item_title:
  - text: >-
      Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff (Erstunterzeichnende)
      sowie weitere 150 Mitunterzeichnende vom 22. März 2024 mit dem Titel: «Für eine
      Stimme der Studierenden im Hochschulrat der Pädagogischen Hochschule Schaffhausen
      (PHSH)»
    language: de
  agenda_item_category: Traktanden
  affair_id: affairs:MOT_2024_1
  datetime_created: '2025-05-02T11:23:49Z'
  datetime_modified: '2025-05-02T11:23:49Z'

```
#### Exemple AgendaItem : French-language agenda item postulate

```yaml
agenda_items:
- global_uri: ops:2023_10_03-52
  parent_meeting: ops:meeting_lausanne_2023_10_03
  agenda_item_type: item
  datetime_begin_planned: '2023-10-03T00:00:00Z'
  agenda_item_position: 52
  agenda_item_number: '52'
  agenda_item_title:
  - text: >-
      Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale »
      (FIM)
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
#### Exemple AgendaItem : Postulate with a voting

```yaml
agenda_items:
- global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
  parent_meeting: ops:meeting_luzern_2025_01_28_b
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
#### Exemple AgendaItem : Urgent interpellation in French

```yaml
agenda_items:
- global_uri: ops:2025_05_20-23
  parent_meeting: ops:meeting_lausanne_2025_05_20
  agenda_item_type: item
  datetime_begin_planned: '2025-05-20T00:00:00Z'
  agenda_item_position: 23
  agenda_item_number: '23'
  agenda_item_title:
  - text: >-
      Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation
      urgente de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en faveur
      du respect du droit international et de la protection des populations civiles
      à Gaza »
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






</div>