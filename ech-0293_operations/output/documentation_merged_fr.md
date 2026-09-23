---
title: "eCH-0293 Fonctionnement public des conseils"
lang: fr
toc: false
---

|**Nom**|**Fonctionnement public des conseils**|
|---|---|
|**Numéro eCH**|eCH-0293|
|**Catégorie**|Norme|
|**Degré de maturité**|Défini|
|**Version**|0.1.0|
|**Statut**|En cours d'élaboration|
|**Décidé le**||
|**Date de publication**||
|**Remplace la version**||
|**Conditions préalables**||
|**Annexes**|-|
|**Langues**|Allemand (original) - Anglais (modèle de données)|
|**Auteurs**|Groupe spécialisé Affaires politiques : Nicole Aeby, David Imseng, Jonas Schärer, Lena Mina Friedrich, Manuel Weingartner, Orhan Saeedi, Michel Moret, Laurens Abu-Talib|
|**Éditeur / Distribution**|Association eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Résumé

La norme eCH-0293 définit un modèle de données commun pour la saisie et la publication d'informations relatives au fonctionnement public des conseils en Suisse. Elle couvre l'organisation temporelle des travaux parlementaires (législatures, sessions), la structuration des séances et des points de l'ordre du jour, les votes et les élections, les voix individuelles, les listes de présence ainsi que les interventions et les décisions.

Cette norme s'adresse aux services parlementaires, aux fournisseuses et fournisseurs de logiciels de gestion parlementaire, aux utilisatrices et utilisateurs de données à des fins d'analyse et de visualisation ainsi qu'aux plateformes de données ouvertes.

eCH-0293 fait partie d'une famille de normes pour les données politiques et travaille en étroite articulation avec eCH-0294 (acteurs politiques), eCH-0295 (affaires parlementaires), eCH-0296 (actes législatifs et textes de loi) et eCH-0297 (consultations publiques).

\newpage

# Table des matières

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Clic droit &gt; « Mettre à jour les champs » pour générer la table des matières.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

\newpage

# Introduction

## La famille de normes « Affaires politiques »

La vie politique de la Suisse se déroule aux niveaux fédéral, cantonal et communal – dans les parlements et les assemblées communales, dans les exécutifs et les administrations, dans les procédures de consultation et les consultations publiques, ainsi qu'à travers la participation démocratique directe des personnes ayant le droit de vote. Le groupe spécialisé « Affaires politiques » de l'association eCH développe à cet effet une famille de normes coordonnées entre elles, qui structurent ces données par-delà les niveaux fédéraux. Les normes utilisent des éléments de données communs (eCH-0292) et se référencent mutuellement au moyen d'identifiants univoques.

La famille comprend :

- **eCH-0292 – Éléments de données communs (Meta) :** définit les éléments de données transversaux et les métaprocessus sur lesquels reposent les autres normes. eCH-0293 en reprend notamment les éléments d'identification et de date ainsi que la structure FRBR pour les documents liés.
- **eCH-0293 – Fonctionnement public des conseils (Operations) – la présente norme :** décrit le fonctionnement public des conseils – législatures et sessions, séances et points de l'ordre du jour, procès-verbaux et décisions, votes et élections, présences ainsi que prises de parole.
- **eCH-0294 – Acteurs politiques (Actors) :** définit les personnes, groupes et organes dans le contexte politique ainsi que leurs affiliations et liens d'intérêts. eCH-0293 référence ces acteurs au moyen d'`actor_id` – p. ex. quel parlement a siégé et quelle personne a voté.
- **eCH-0295 – Affaires parlementaires (Affairs) :** décrit le cycle de vie des affaires politiques. Les points de l'ordre du jour dans eCH-0293 renvoient à l'affaire correspondante au moyen d'`affair_id`.
- **eCH-0296 – Actes législatifs et textes de loi (Laws) :** consigne les résultats du processus parlementaire – les lois et actes législatifs adoptés.
- **eCH-0297 – Consultations publiques (Consultations) :** structure les procédures de consultation, qui constituent souvent le point de départ des affaires parlementaires.

L'objectif de cette famille de normes est de créer une structure utilisable en commun pour les données politiques et de mettre à la disposition des organisations qui publient des informations sur les affaires politiques un modèle de données robuste.

## Structure d'une livraison

Une livraison est un `Container` : une enveloppe dotée de sa propre `global_uri` et d'une collection par classe — `legislatures`, `sessions`, `meetings`, `agenda_items`, `protocols`, `votings`, `elections`, `individual_votes`, `attendances`, `individual_attendances`, `speeches` et `resolutions`. Toutes les collections sont facultatives : qui ne publie que des séances ne livre que `meetings`.

Les entités y sont placées côte à côte, à plat, et reliées par des références — `parent_meeting`, `parent_voting`, `parent_attendance`, et ainsi de suite — plutôt qu'imbriquées les unes dans les autres. Il est ainsi possible de livrer après coup une séance isolée sans réémettre toute la législature, et de référencer la même entité depuis plusieurs endroits. Là où l'imbrication rend mieux le lien, elle reste possible : la session reprend ses séances sous forme de liste, le procès-verbal ses points de l'ordre du jour, ses votes et ses interventions.



### Classe: Container []{#Container}


_Conteneur pour les données de l'activité publique des conseils : législatures, sessions, séances, points de l'ordre du jour, procès-verbaux, votes, élections, présences, interventions et décisions._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| legislatures | * <br/> [Legislature](#Legislature) | Ensemble des législatures.  |
| sessions | * <br/> [Session](#Session) | Ensemble des sessions.  |
| meetings | * <br/> [Meeting](#Meeting) | Ensemble des séances.  |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Ensemble des points de l'ordre du jour.  |
| protocols | * <br/> [Protocol](#Protocol) | Ensemble des procès-verbaux.  |
| votings | * <br/> [Voting](#Voting) | Ensemble des votes.  |
| elections | * <br/> [Election](#Election) | Ensemble des élections.  |
| individual_votes | * <br/> [IndividualVote](#IndividualVote) | Ensemble des voix individuelles.  |
| attendances | * <br/> [Attendance](#Attendance) | Ensemble des listes de présence.  |
| individual_attendances | * <br/> [IndividualAttendance](#IndividualAttendance) | Ensemble des constatations individuelles de présence.  |
| speeches | * <br/> [Speech](#Speech) | Ensemble des interventions.  |
| resolutions | * <br/> [Resolution](#Resolution) | Ensemble des décisions.  |

















#### Exemples
##### Exemple Container : meeting complete

```yaml
global_uri: ops:meeting_examples_2025

meetings:

- global_uri: ops:meeting_sg_2025_03_15
  spatial: "https://ld.admin.ch/canton/17"
  name:
    - text: "Kantonsratssitzung vom 15. März 2025"
      language: "de"
  url:
    - text: "https://www.ratsinfo.sg.ch/sessions/2025-03-15"
      language: "de"
  actor_id:
    global_uri: "actors:kr_sg"
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
  parent_session: ops:session_sg_2025_03
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T17:30:00Z"

- global_uri: ops:meeting_be_committee_wak_2025_05_12
  spatial: "https://ld.admin.ch/canton/2"
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
  datetime_created: "2025-04-15T09:00:00Z"
  datetime_modified: "2025-05-12T16:45:00Z"

- global_uri: ops:meeting_gl_landsgemeinde_2025
  spatial: "https://ld.admin.ch/canton/8"
  name:
    - text: "Landsgemeinde 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/2025"
      language: "de"
  actor_id:
    global_uri: "actors:landsgemeinde_gl"
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
  parent_session: ops:session_gl_landsgemeinde_2025
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
##### Exemple Container : meeting sr winter25 Sitzung6

```yaml
global_uri: ops:data_meeting_sr_winter25_Sitzung6

meetings:
  - global_uri: "parl:sr_winter25_sitzung_6"
    spatial: "https://ld.admin.ch/country/CHE"
    name:
      - text: "Sechste Sitzung"
        language: "de"
      - text: "Sixième séance"
        language: "fr"
    url:
      - text: "https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin"
        language: "de"
    actor_id:
      global_uri: "actors:staenderat"
      label: "Ständerat"
      abbreviation:
        - value: "SR"
          language: de
    actor_name: "Ständerat"
    datetime_begin_planned: "2025-12-19T08:15:00+01:00"
    # Referenz auf das Protokoll: nur der Identifikator. Das Protokoll selbst
    # steht unten unter `protocols` und wird in der Regel spaeter geliefert als
    # die Sitzung.
    has_protocol: "ops:protokoll_sr_winter25_sitzung_6"
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
    parent_meeting: "parl:sr_winter25_sitzung_6"
    parent_agenda_item: "ops:69905"
    language: "fr"
    datetime_begin: "2025-12-19T09:20:00+01:00"
    datetime_end: "2025-12-19T09:25:00+01:00"
    actor_fullname: "Pascal Broulis"
    actor_id:
      global_uri: "actors:person_pascal_broulis"
      wikidata_uri: "http://www.wikidata.org/entity/Q116407"
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

protocols:
  - global_uri: ops:protokoll_sr_winter25_sitzung_6
    parent_meeting: "parl:sr_winter25_sitzung_6"
    protocol_items:
      - global_uri: ops:protokollpunkt_69905
        parent_meeting: "parl:sr_winter25_sitzung_6"
        agenda_item_type: "item"
        agenda_item_number: "6"
        agenda_item_position: 4
        agenda_item_title:
          - text: "Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen, um die Verzögerungen zu verstehen"
            language: "de"
        affair_id: "affairs:24.4471"
        datetime_begin_actual: "2025-12-19T09:20:00+01:00"
        landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3"
        agenda_item_category: "agenda_item"
        datetime_created: "2026-01-12T00:00:00+01:00"
        datetime_modified: "2026-01-12T00:00:00+01:00"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

```
##### Exemple Container : voting

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
  parent_protocol: ops:protocol_sg_2025_03_15
  parent_protocol_item: ops:protocol_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: "actors:kr_sg"
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
  parent_protocol: ops:protocol_be_2025_06_05
  parent_protocol_item: ops:protocol_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: "actors:gr_be"
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
  parent_protocol: ops:protocol_zh_2025_11_20
  parent_protocol_item: ops:protocol_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: "actors:kr_zh"
    label: "Kantonsrat Zürich"
    abbreviation:
      - value: "KR"
        language: de
  datetime_created: "2025-11-20T16:45:00Z"
  datetime_modified: "2025-11-20T16:50:00Z"

# Realbeispiel Gemeinderat der Stadt Zürich (28.02.2024, 86. Sitzung):
# "Gleichgerichtete Anträge" mit mehreren Auswahloptionen (Zürich: mehrere Knöpfe).
# Die Optionen sind nicht Ja/Nein/Enthaltung, sondern Auswahl A–D und werden
# deshalb über total_other (Liste von TotalOther {count, label}) abgebildet.
# Quelle: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
- global_uri: ops:voting_zh_gr_2024_2023_361
  voting_title:
    - text: "Liegenschaften Stadt Zürich, Wohnhaus Magnusstrasse 27, Gesamtinstandsetzung, Grundrissanpassung, Netto-Zusatzkredit (Geschäft 2023/361)"
      language: "de"
  voting_type: "other"
  type_label: "Gleichgerichtete Anträge (Mehrfachauswahl)"
  datetime_begin: "2024-02-28T00:00:00Z"
  datetime_end: "2024-02-28T00:00:00Z"
  landing_page: "https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89"
  # Bei reinen Auswahlabstimmungen bleiben Ja/Nein/Enthaltung leer; jede Option
  # erhält einen eigenen TotalOther-Eintrag mit Stimmenzahl und Bezeichnung.
  total_other:
    - count: 75
      label: "Auswahl A (siegreich)"
    - count: 25
      label: "Auswahl B"
    - count: 12
      label: "Auswahl C"
    - count: 0
      label: "Auswahl D"
  total_absent: 13
  total: 112
  majority_type: "other"
  result_text: "Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern)."
  parent_protocol: ops:protocol_zh_gr_2024_02_28
  parent_protocol_item: ops:protocol_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: "2023/361"
  actor_id:
    global_uri: "actors:gr_stadt_zuerich"
    label: "Gemeinderat der Stadt Zürich"
    abbreviation:
      - value: "GR"
        language: de
  datetime_created: "2024-02-28T00:00:00Z"
  datetime_modified: "2024-02-28T00:00:00Z"

individual_votes:

# Einzelstimmen zum Zürcher Mehrfachoptionen-Beispiel: Da die Auswahloptionen
# nicht Ja/Nein/Enthaltung sind, wird individual_vote_type "other" mit type_label
# je gewählter Option verwendet; abwesende Mitglieder erhalten "not_voted".
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "actors:person_zh_stadt_1"
    label: "Mitglied Auswahl A"
  seat_nr: "12"
  individual_vote_type: "other"
  type_label: "Auswahl A"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "actors:person_zh_stadt_2"
    label: "Mitglied Auswahl B"
  seat_nr: "47"
  individual_vote_type: "other"
  type_label: "Auswahl B"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "actors:person_zh_stadt_3"
    label: "Mitglied Auswahl C"
  seat_nr: "88"
  individual_vote_type: "other"
  type_label: "Auswahl C"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "actors:person_zh_stadt_4"
    label: "Abwesendes Mitglied"
  seat_nr: "103"
  individual_vote_type: "not_voted"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_paul_schlegel"
    label: "Paul Schlegel"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_andreas_eggenberger"
    label: "Andreas Eggenberger"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_thomas_ammann"
    label: "Thomas Ammann"
  seat_nr: "3"
  individual_vote_type: "abstention"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_ruedi_thomann"
    label: "Ruedi Thomann"
  seat_nr: "4"
  individual_vote_type: "not_voted"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "actors:person_thomas_wolf"
    label: "Thomas Wolf"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-11-20T16:45:00Z"

- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "actors:person_jean_daniel_strub"
    label: "Jean-Daniel Strub"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-11-20T16:45:00Z"

```
##### Exemple Container : meeting item

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
##### Exemple Container : meeting

```yaml
global_uri: ops:meetings_1
meetings:
  - spatial: "https://ld.admin.ch/canton/2"
    global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
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

  - spatial: "https://ld.admin.ch/canton/2"
    global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
    name:
      - text: "Donnerstag (Nachmittag)"
        language: "de"
    url:
      - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "de"
      - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "fr"
    actor_id:
      global_uri: "actors:gr_be"
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
##### Exemple Container : session

```yaml
global_uri: ops:sessions_example_2025
sessions:

- global_uri: ops:session_5207
  spatial: "https://ld.admin.ch/country/CHE"
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
  spatial: "https://ld.admin.ch/canton/2"
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
  spatial: "https://ld.admin.ch/canton/8"
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
  spatial: "https://ld.admin.ch/canton/8"
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
##### Exemple Container : legislature

```yaml
global_uri: ops:legislature_examples
legislatures:

# Bund: abgeschlossene Legislaturperiode, vier Jahre, dreisprachige Bezeichnung.
- global_uri: ops:legislature_51
  wikidata_uri: http://www.wikidata.org/entity/Q71712404
  spatial: "https://ld.admin.ch/country/CHE"
  name:
    - text: "51. Legislaturperiode"
      language: "de"
    - text: "51e législature"
      language: "fr"
    - text: "51ª legislatura"
      language: "it"
  description: "Amtsdauer der am 20. Oktober 2019 gewählten Bundesversammlung; sie endete am Vortag der konstituierenden Sitzung der 52. Legislaturperiode vom 4. Dezember 2023."
  landing_page: "https://www.parlament.ch/de/ratsbetrieb/sessionen"
  actor_id:
    global_uri: "actors:bundesversammlung"
    label: "Bundesversammlung"
    abbreviation:
      - value: "BV"
        language: de
  date_begin_actual: "2019-12-02"
  date_end_actual: "2023-12-03"
  datetime_created: "2019-12-02T09:00:00+01:00"
  datetime_modified: "2023-12-04T08:30:00+01:00"

# Kanton mit vierjähriger Amtsdauer; Beginn und Ende sind hier von Gesetzes
# wegen auf den Tag festgelegt und deshalb schon bei der Planung bekannt.
- global_uri: ops:legislature_be_2022_2026
  local_id: "GR-BE-2022-2026"
  spatial: "https://ld.admin.ch/canton/2"
  name:
    - text: "Legislatur 2022–2026"
      language: "de"
    - text: "Législature 2022-2026"
      language: "fr"
  landing_page: "https://www.gr.be.ch/de/start/grosser-rat.html"
  actor_id:
    global_uri: "actors:gr_be"
    label: "Grosser Rat Bern"
    abbreviation:
      - value: "GR"
        language: de
  date_begin_planned: "2022-06-01"
  date_end_planned: "2026-05-31"
  date_begin_actual: "2022-06-01"
  date_end_actual: "2026-05-31"
  datetime_created: "2022-04-01T10:15:00+02:00"
  datetime_modified: "2026-06-01T07:00:00+02:00"

# Kanton mit fünfjähriger Amtsdauer: laufende Legislatur, deren Ende erst
# geplant ist -- date_end_actual bleibt deshalb leer.
- global_uri: ops:legislature_vd_2022_2027
  wikidata_uri: http://www.wikidata.org/entity/Q131627357
  spatial: "https://ld.admin.ch/canton/22"
  name:
    - text: "Législature 2022-2027"
      language: "fr"
  description: "Le Grand Conseil vaudois est élu pour cinq ans."
  landing_page: "https://www.vd.ch/gc"
  actor_id:
    global_uri: "actors:gc_vd"
    label: "Grand Conseil du canton de Vaud"
    abbreviation:
      - value: "GC"
        language: fr
  date_begin_actual: "2022-07-01"
  date_end_planned: "2027-06-30"
  datetime_created: "2022-05-10T14:00:00+02:00"
  datetime_modified: "2025-01-08T11:20:00+01:00"

```






</div>

\newpage

<!-- ToDo: Christian -->

# Organisation temporelle du fonctionnement des conseils

Le fonctionnement des conseils est structuré dans le temps en quatre classes :

```
Legislature (législature)
  └─ Session (p. ex. session de printemps)
      └─ Meeting (séance individuelle)
          └─ AgendaItem (point de l'ordre du jour)
```

La législature constitue le cadre à long terme, la session structure le travail au sein d'une législature, le Meeting est la séance concrète au cours de laquelle les affaires sont délibérées, et le point de l'ordre du jour articule la séance individuelle. Les niveaux s'emboîtent de deux manières : la session reprend ses séances sous forme de liste (`meetings`), tandis que la séance et le point de l'ordre du jour renvoient vers le haut par des références (`parent_legislature`, `parent_session`, `parent_meeting`, `parent_agenda_item`) : la session renvoie à sa législature, la séance à sa session.

Les trois premières classes sont décrites ci-après, le point de l'ordre du jour dans le chapitre suivant.

## Éléments communs

Les trois classes sont délibérément construites de la même manière. Les champs suivants ont la même signification à tous les niveaux.

**Identification.** `global_uri` est l'identifiant et est obligatoire. `local_id` reprend l'identifiant du système livreur, `wikidata_uri` renvoie à l'entrée Wikidata, lorsqu'elle existe.

**Début et fin.** Les indications temporelles sont consignées deux fois : `date_begin_planned` et `date_end_planned` retiennent ce qui était prévu, `date_begin_actual` et `date_end_actual` ce qui s'est effectivement passé. Lorsque l'heure importe, les variantes `datetime_*` sont à disposition.

**Espace et organe.** `spatial` renvoie à l'unité spatiale selon LINDAS — pays, canton, district ou commune, donc `https://ld.admin.ch/canton/2` et non « BE ». C'est le champ avec lequel eCH-0294 localise ses groupes, de sorte qu'un fonctionnement de conseil et les acteurs qui le portent renvoient à la même ressource. Qui siège au sein de cette unité spatiale est indiqué par `actor_id`, référence abrégée à l'organe selon eCH-0294.

**Documents liés.** `documents` relie des documents en tant que FRBR-Works selon eCH-0292 — pour la législature p. ex. les listes des membres et les répertoires des affaires, pour la session le programme de session, pour la séance le bulletin et les annexes (le procès-verbal, en revanche, via `has_protocol`).

## Legislature (législature)

Une législature désigne la période pour laquelle un parlement est élu et durant laquelle il exerce ses fonctions dans sa composition actuelle.



### Classe: Legislature []{#Legislature}


_Durée du mandat d'un parlement en tant qu'assemblée législative. Elle est en règle générale de quatre ans._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234, district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23, pays : https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> String | Identifiant administratif du corps législatif, p. ex. commune, canton ou pays.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Désignation complète multilingue.  |
| description | 0..1 <br/> String | Texte descriptif de l'élément.  |
| landing_page | 0..1 <br/> String | URL fournissant des informations complémentaires.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |
| date_begin_actual | 0..1 <br/> Date | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | legislatures | range | [Legislature](#Legislature) |














#### Exemples
##### Exemple Legislature : Législature cantonale en cours d'une durée de cinq ans

```yaml
legislatures:
- global_uri: ops:legislature_vd_2022_2027
  wikidata_uri: http://www.wikidata.org/entity/Q131627357
  spatial: https://ld.admin.ch/canton/22
  name:
  - text: Législature 2022-2027
    language: fr
  description: Le Grand Conseil vaudois est élu pour cinq ans.
  landing_page: https://www.vd.ch/gc
  actor_id:
    global_uri: actors:gc_vd
    label: Grand Conseil du canton de Vaud
    abbreviation:
    - value: GC
      language: fr
  date_begin_actual: '2022-07-01'
  date_end_planned: '2027-06-30'
  datetime_created: '2022-05-10T14:00:00+02:00'
  datetime_modified: '2025-01-08T11:20:00+01:00'

```
##### Exemple Legislature : Completed federal legislature

```yaml
legislatures:
- global_uri: ops:legislature_51
  wikidata_uri: http://www.wikidata.org/entity/Q71712404
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: 51. Legislaturperiode
    language: de
  - text: 51e législature
    language: fr
  - text: 51ª legislatura
    language: it
  description: >-
    Amtsdauer der am 20. Oktober 2019 gewählten Bundesversammlung; sie endete am Vortag
    der konstituierenden Sitzung der 52. Legislaturperiode vom 4. Dezember 2023.
  landing_page: https://www.parlament.ch/de/ratsbetrieb/sessionen
  actor_id:
    global_uri: actors:bundesversammlung
    label: Bundesversammlung
    abbreviation:
    - value: BV
      language: de
  date_begin_actual: '2019-12-02'
  date_end_actual: '2023-12-03'
  datetime_created: '2019-12-02T09:00:00+01:00'
  datetime_modified: '2023-12-04T08:30:00+01:00'

```
##### Exemple Legislature : Cantonal legislature with a four-year term

```yaml
legislatures:
- global_uri: ops:legislature_be_2022_2026
  local_id: GR-BE-2022-2026
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Legislatur 2022–2026
    language: de
  - text: Législature 2022-2026
    language: fr
  landing_page: https://www.gr.be.ch/de/start/grosser-rat.html
  actor_id:
    global_uri: actors:gr_be
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  date_begin_planned: '2022-06-01'
  date_end_planned: '2026-05-31'
  date_begin_actual: '2022-06-01'
  date_end_actual: '2026-05-31'
  datetime_created: '2022-04-01T10:15:00+02:00'
  datetime_modified: '2026-06-01T07:00:00+02:00'

```






</div>

## Session (période de séance)

Une session est une période de séance continue au cours de laquelle plusieurs séances ont lieu.

### Niveau facultatif

La session est le seul des trois niveaux auquel il est possible de renoncer : les entités fédérées sans sessions formelles s'en passent et gèrent directement leurs séances. Session et séance peuvent aussi coïncider — une séance d'un jour du Grand Conseil ou une Landsgemeinde est gérée comme une période de séance comportant une seule séance.

### Numérotation

La numérotation varie fortement d'une pratique à l'autre, raison pour laquelle quatre champs sont disponibles : `number` retient le numéro courant sous forme de nombre, `sequential_number` la même indication sous forme de chaîne de caractères (et donc aussi en chiffres romains), `position` la position au sein de la législature et `meeting_abbreviation` une désignation abrégée telle que « FS24 ». Le Meeting connaît les mêmes quatre champs.



### Classe: Session []{#Session}


_Une session parlementaire qui regroupe plusieurs séances et s'étend sur une période déterminée._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234, district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23, pays : https://ld.admin.ch/country/CHE.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Désignation complète multilingue.  |
| number | 0..1 <br/> String | Numéro courant, p. ex. au sein de la législature, de la session ou de l'année.  |
| sequential_number | 0..1 <br/> Integer | Numéro séquentiel de la séance, utilisé pour le tri.  |
| position | 0..1 <br/> String | Position (nombre entier) au sein de la séquence supérieure.  |
| meeting_abbreviation | 0..1 <br/> String | Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour la session de printemps 2024).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| parent_legislature | 0..1 <br/> String | Identifiant de la législature à laquelle la session appartient.  |
| meetings | * <br/> [Meeting](#Meeting) | Ensemble des séances.  |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Délibérations communes rattachées à cet enregistrement : pour un point de l'ordre du jour, les délibérations dans lesquelles il est traité conjointement avec d'autres points ; pour une séance ou une session, les délibérations communes qui s'y tiennent.  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |
| date_begin_actual | 0..1 <br/> Date | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | sessions | range | [Session](#Session) |














#### Exemples
##### Exemple Session : Session fédérale avec désignation trilingue

```yaml
sessions:
- global_uri: ops:session_5207
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: Frühjahrssession 2025
    language: de
  - text: Session de printemps 2025
    language: fr
  - text: Sessione primaverile 2025
    language: it
  url:
  - text: https://www.parlament.ch/de/ratsbetrieb/sessionen/fruehjahr-2025
    language: de
  - text: https://www.parlament.ch/fr/ratsbetrieb/sessionen/fruehjahr-2025
    language: fr
  - text: https://www.parlament.ch/it/ratsbetrieb/sessionen/fruehjahr-2025
    language: it
  date_begin_planned: '2025-03-03'
  date_end_planned: '2025-03-21'
  parent_legislature: ops:legislature_51
  datetime_modified: '2025-04-24T00:19:37Z'
  datetime_created: '2025-03-20T14:27:09Z'

```
##### Exemple Session : One-day sitting period of a cantonal parliament

```yaml
sessions:
- global_uri: ops:session_gl_landrat_2025_02_26
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Sitzung des Landrates vom 26.02.2025
    language: de
  url:
  - text: https://www.gl.ch/parlament/landrat/landratsprotokolle-ab-30-juni-2010.html/239
    language: de
  date_begin_planned: '2025-02-26'
  date_end_planned: '2025-02-26'
  datetime_modified: '2025-04-25T13:40:34Z'
  datetime_created: '2025-04-23T22:58:39Z'

```
##### Exemple Session : Cantonal session with a bilingual designation

```yaml
sessions:
- global_uri: ops:session_be_summer_2025
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Sommersession 2025
    language: de
  - text: Session d'été 2025
    language: fr
  url:
  - text: >-
      https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: de
  - text: >-
      https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: fr
  date_begin_planned: '2025-06-02'
  date_end_planned: '2025-06-12'
  datetime_modified: '2025-05-19T01:06:44Z'
  datetime_created: '2025-04-25T11:10:24Z'

```
##### Exemple Session : Landsgemeinde as a sitting period

```yaml
sessions:
- global_uri: ops:session_gl_landsgemeinde_2025_05_04
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Landsgemeinde vom 04. Mai 2025
    language: de
  url:
  - text: https://www.landsgemeinde.gl.ch/landsgemeinde/2025-05-04
    language: de
  date_begin_planned: '2025-05-04'
  date_end_planned: '2025-05-04'
  datetime_modified: '2025-04-25T13:40:34Z'
  datetime_created: '2025-04-23T22:58:39Z'

```






</div>

## Meeting (séance individuelle)

Un Meeting est la séance individuelle d'un organe — le niveau auquel les points de l'ordre du jour sont délibérés, les décisions prises et les interventions consignées.



### Classe: Meeting []{#Meeting}


_La séance individuelle d'un organe — le niveau auquel les points de l'ordre du jour sont délibérés, les décisions prises et les interventions consignées. La séance est le nœud auquel les autres classes de la présente norme se rattachent via `parent_meeting` : les points de l'ordre du jour (AgendaItem), les votes et élections (Voting, Election), les interventions (Speech) ainsi que la liste de présence (Attendance). À ce niveau, les heures prévues et les heures effectives divergent régulièrement — une séance fixée à 14h00 ne commence, en raison de retards, qu'à 14h25 et se termine à 17h30 au lieu de 18h00 —, raison pour laquelle le début et la fin sont consignés tant prévus qu'effectifs._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234, district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23, pays : https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> String | Identifiant administratif du corps législatif, p. ex. commune, canton ou pays.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Désignation complète multilingue.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| group_name | 0..1 <br/> String | Nom du groupe ou de l'organe en clair, en complément de la référence `group_id`.  |
| group_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence au groupe ou à l'organe (instantané au moment de la mise en relation).  |
| number | 0..1 <br/> String | Numéro courant, p. ex. au sein de la législature, de la session ou de l'année.  |
| landing_page | 0..1 <br/> String | URL fournissant des informations complémentaires.  |
| sequential_number | 0..1 <br/> Integer | Numéro séquentiel de la séance, utilisé pour le tri.  |
| position | 0..1 <br/> String | Position (nombre entier) au sein de la séquence supérieure.  |
| meeting_abbreviation | 0..1 <br/> String | Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour la session de printemps 2024).  |
| actor_name | 0..1 <br/> String | Nom de l'organe politique en clair (p. ex. Conseil national), en complément de la référence `actor_id`.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| state | 0..1 <br/> [StateEnum](#StateEnum) | Indique si la séance a lieu comme prévu (planifiée, annulée, reportée). Une désignation divergente, en texte libre, est reprise dans `state_name`.  |
| state_name | 0..1 <br/> String | Désignation de statut divergente, en texte libre, de la séance, là où les valeurs de `state` ne suffisent pas.  |
| description | 0..1 <br/> String | Texte descriptif de l'élément.  |
| location | 0..1 <br/> String | Lieu où se tient la séance — la salle physique (« Palais fédéral, salle du Conseil national »), une visioconférence ou un format hybride.  |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| parent_session | 0..1 <br/> String | Identifiant de la session à laquelle la séance appartient.  |
| documents | * <br/> Work | Documents de séance tels que le bulletin (Tagblatt) ou les annexes, sous forme de FRBR Works. Le procès-verbal n'est pas lié ici, mais via `has_protocol`.  |
| has_protocol | 0..1 <br/> [Protocol](#Protocol) | Référence au procès-verbal de cette séance, établi après celle-ci. Seul l'identifiant du procès-verbal est indiqué ; le procès-verbal lui-même est livré dans la liste `protocols` du conteneur. Il constitue une entité à part entière dotée de son propre identifiant et est en règle générale publié après la séance, raison pour laquelle il est référencé et non imbriqué.  |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Délibérations communes rattachées à cet enregistrement : pour un point de l'ordre du jour, les délibérations dans lesquelles il est traité conjointement avec d'autres points ; pour une séance ou une session, les délibérations communes qui s'y tiennent.  |
| date_begin_actual | 0..1 <br/> Date | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | meetings | range | [Meeting](#Meeting) |
| [Session](#Session) | meetings | range | [Meeting](#Meeting) |














#### Exemples
##### Exemple Meeting : Séance du Conseil des États avec procès-verbal et interventions

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

```
##### Exemple Meeting : Half-day sitting within a session

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
##### Exemple Meeting : Committee sitting with an attendance list

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
  datetime_created: '2025-04-15T09:00:00Z'
  datetime_modified: '2025-05-12T16:45:00Z'

```
##### Exemple Meeting : Landsgemeinde as meeting type sitting

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
##### Exemple Meeting : Government sitting with a bilingual designation

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
##### Exemple Meeting : Cantonal parliament sitting with agenda items and votings

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

```






</div>

### Enum: StateEnum []{#StateEnum}




_État de la séance._




<div data-search-exclude markdown="1">

URI: [ops:StateEnum](https://ch.paf.link/schema/operations/StateEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| planned |  La séance est planifiée et se tiendra comme prévu.  |
| | [ops:enum/state/planned](ops:enum/state/planned) |
| canceled |  La séance a été annulée.  |
| | [ops:enum/state/canceled](ops:enum/state/canceled) |
| postponed |  La séance a été reportée.  |
| | [ops:enum/state/postponed](ops:enum/state/postponed) |







</div>

\newpage

<!-- ToDo: Michel -->

# Ordre du jour, procès-verbal et décisions

L'ordre du jour d'une séance est structuré par des points de l'ordre du jour ; ce qui a effectivement été traité et décidé est consigné au procès-verbal.

## AgendaItem (point de l'ordre du jour)



### Classe: AgendaItem []{#AgendaItem}


_Un point de l'ordre du jour d'une séance, tel que planifié à l'avance. Il structure l'ordre du jour et relie l'organisation temporelle (Meeting) aux affaires matérielles (eCH-0295). Les points de l'ordre du jour représentent la planification d'une séance et ne sont plus modifiés dans les données une fois la séance ouverte : les écarts survenus durant la séance — points avancés, reportés ou ajoutés — sont consignés au procès-verbal (ProtocolItem) et se répercutent sur l'ordre du jour de la séance suivante. Pour la même raison, les heures prévues et effectives sont tenues séparément._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> Date | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_number | 0..1 <br/> String | Numéro du point sur l'ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne de caractères, afin de permettre aussi les chiffres romains). <br/><br/>Héritage : IsAgendaItem |
| agenda_item_position | 0..1 <br/> Integer | Position entière du point dans le déroulement de la séance, déterminante pour le tri et l'affichage. <br/><br/>Héritage : IsAgendaItem |
| leading_actor_id | 0..1 <br/> String | Le département responsable du point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| speaking_actor_id | 0..1 <br/> String | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Titre du point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| affair_id | 0..1 <br/> String | Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Sous-titre ou description détaillée du point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| state_id | 0..1 <br/> String | Identifiant d'état du point (renvoi à une énumération des états ou à un état propre), p. ex. pending (pas encore traité), in_progress (en délibération), completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn (retiré). <br/><br/>Héritage : IsAgendaItem |
| state_name | 0..1 <br/> String | Désignation de statut divergente, en texte libre, là où l'énumération des statuts ne suffit pas. <br/><br/>Héritage : IsAgendaItem |
| landing_page | 0..1 <br/> String | URL fournissant des informations complémentaires. <br/><br/>Héritage : IsAgendaItem |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_category | 0..1 <br/> String | Catégorisation libre du point selon son contenu ou son regroupement, p. ex. « Législation », « Budget et finances », « Interpellations et questions », « Élections », par département, ou points introductifs et techniques. La catégorisation n'est pas standardisée et peut varier selon l'unité fédérale. <br/><br/>Héritage : IsAgendaItem |
| parent_agenda_item | 0..1 <br/> String | Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il forme une hiérarchie de points — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l'énergie (discussion par article) » et « Loi sur l'énergie (vote final) » ; pour une intervention, il désigne le point sous lequel elle a été faite. <br/><br/>Héritage : IsAgendaItem |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | La décision formelle prise sur ce point de l'ordre du jour, p. ex. l'adoption de la loi sur l'énergie. Le vote sous-jacent avec son rapport de voix est saisi séparément comme Voting. <br/><br/>Héritage : IsAgendaItem |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Délibérations communes rattachées à cet enregistrement : pour un point de l'ordre du jour, les délibérations dans lesquelles il est traité conjointement avec d'autres points ; pour une séance ou une session, les délibérations communes qui s'y tiennent. <br/><br/>Héritage : IsAgendaItem |
| text_segments | * <br/> [TextSegment](#TextSegment) | Ensemble de segments de texte (p. ex. procès-verbal in extenso). <br/><br/>Héritage : IsAgendaItem |
| documents | * <br/> Work | Documents relatifs au point de l'ordre du jour, sous forme de FRBR Works, p. ex. messages et rapports, propositions et propositions d'amendement. <br/><br/>Héritage : IsAgendaItem |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | agenda_items | range | [AgendaItem](#AgendaItem) |














#### Exemples
##### Exemple AgendaItem : Point de l'ordre du jour avec vote final

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
##### Exemple AgendaItem : Interpellation as an agenda item

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
##### Exemple AgendaItem : Urgent interpellation in French

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
##### Exemple AgendaItem : Interpellation of a parliamentary group

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
##### Exemple AgendaItem : Detailed deliberation of an article of an act

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
##### Exemple AgendaItem : Postulate with a voting

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
##### Exemple AgendaItem : Petition as an agenda item

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
##### Exemple AgendaItem : Popular motion within a group of agenda items

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
##### Exemple AgendaItem : Budget agenda item

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
##### Exemple AgendaItem : Substantive affair without an agenda category

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
##### Exemple AgendaItem : Partial revision of several ordinances in French

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
##### Exemple AgendaItem : Substantive affair from a cantonal parliamentary information system

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
##### Exemple AgendaItem : Agenda item of a Council of States sitting

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
##### Exemple AgendaItem : French-language agenda item postulate

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
##### Exemple AgendaItem : Motion within a group of agenda items

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
##### Exemple AgendaItem : Postulate category voting

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






</div>

### Enum: AgendaItemTypeEnum []{#AgendaItemTypeEnum}




_Type de point de l'ordre du jour, distinguant les points isolés des points regroupés._




<div data-search-exclude markdown="1">

URI: [ops:AgendaItemTypeEnum](https://ch.paf.link/schema/operations/AgendaItemTypeEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| item |  Point individuel de l'ordre du jour, avec délibération et, le cas échéant, vote.  |
| | [ops:enum/agenda_item_type/item](ops:enum/agenda_item_type/item) |
| group |  Groupe de points (groupe de points de l'ordre du jour) sous lequel des sous-points sont rangés au moyen de parent_agenda_item, p. ex. « Délibérations législatives ».  |
| | [ops:enum/agenda_item_type/group](ops:enum/agenda_item_type/group) |







</div>

## Procès-verbal (Protocol)

Le procès-verbal est **référencé et non imbriqué**. La règle appliquée de bout en bout par la présente norme vaut donc ici aussi : est imbriqué ce qui ne possède pas d'identité propre (par exemple `PersonReference` ou `GroupReference`), est référencé ce qui en possède une.

```
Container
  ├─ meetings       → Meeting
  │                     └─ has_protocol → identifiant du procès-verbal
  ├─ agenda_items   → AgendaItem  (avant : points planifiés, parent_meeting)
  └─ protocols      → Protocol    (après : consignation, parent_meeting)
                        ├─ protocol_items  → ProtocolItem (mêmes éléments qu'AgendaItem)
                        ├─ votings
                        ├─ elections
                        ├─ speeches
                        ├─ text_segments
                        └─ documents
```



### Classe: Protocol []{#Protocol}


_Le procès-verbal d'une séance, établi après celle-ci et tenu exactement une fois par séance. Un conteneur qui regroupe les points effectivement traités (protocol_items), les votes, les élections, les interventions, les segments de texte in extenso et les documents liés. Le procès-verbal possède son propre identifiant, peut être cité de manière autonome et est en règle générale publié après la séance ; la séance ne fait donc que le référencer (Meeting.has_protocol), et le procès-verbal lui-même est livré dans Container.protocols, de sorte qu'il puisse être livré ultérieurement sans relivrer la séance. À l'intérieur du procès-verbal, les collections sont imbriquées, car elles naissent et sont livrées avec lui. Qui publie des votes ou des interventions indépendamment du procès-verbal les livre à plat dans Container.votings ou Container.speeches et les relie par parent_meeting et la référence au point de l'ordre du jour correspondante._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| protocol_items | * <br/> [ProtocolItem](#ProtocolItem) | Points de l'ordre du jour tels qu'ils ont effectivement été consignés au procès-verbal.  |
| votings | * <br/> [Voting](#Voting) | Ensemble des votes.  |
| elections | * <br/> [Election](#Election) | Ensemble des élections.  |
| speeches | * <br/> [Speech](#Speech) | Ensemble des interventions.  |
| text_segments | * <br/> [TextSegment](#TextSegment) | Ensemble de segments de texte (p. ex. procès-verbal in extenso).  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | protocols | range | [Protocol](#Protocol) |
| [Meeting](#Meeting) | has_protocol | range | [Protocol](#Protocol) |
| [Voting](#Voting) | parent_protocol | range | [Protocol](#Protocol) |
| [Election](#Election) | parent_protocol | range | [Protocol](#Protocol) |














#### Exemples
##### Exemple Protocol : Procès-verbal comme entité à part entière, référencé par la séance

```yaml
protocols:
- global_uri: ops:protokoll_sr_winter25_sitzung_6
  parent_meeting: parl:sr_winter25_sitzung_6
  protocol_items:
  - global_uri: ops:protokollpunkt_69905
    parent_meeting: parl:sr_winter25_sitzung_6
    agenda_item_type: item
    agenda_item_number: '6'
    agenda_item_position: 4
    agenda_item_title:
    - text: >-
        Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
        durchführen, um die Verzögerungen zu verstehen
      language: de
    affair_id: affairs:24.4471
    datetime_begin_actual: '2025-12-19T09:20:00+01:00'
    landing_page: >-
      https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
    agenda_item_category: agenda_item
    datetime_created: '2026-01-12T00:00:00+01:00'
    datetime_modified: '2026-01-12T00:00:00+01:00'
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```






</div>

### ProtocolItem (point consigné au procès-verbal)



### Classe: ProtocolItem []{#ProtocolItem}


_Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-verbal. Il porte les mêmes éléments qu'AgendaItem par le mixin IsAgendaItem, mais constitue une classe à part entière : le point consigné n'est pas un cas particulier du point planifié. Il naît indépendamment et peut comprendre des points jamais mis à l'ordre du jour, de même que l'ordre du jour peut comprendre des points jamais traités._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> Date | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_number | 0..1 <br/> String | Numéro du point sur l'ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne de caractères, afin de permettre aussi les chiffres romains). <br/><br/>Héritage : IsAgendaItem |
| agenda_item_position | 0..1 <br/> Integer | Position entière du point dans le déroulement de la séance, déterminante pour le tri et l'affichage. <br/><br/>Héritage : IsAgendaItem |
| leading_actor_id | 0..1 <br/> String | Le département responsable du point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| speaking_actor_id | 0..1 <br/> String | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Titre du point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| affair_id | 0..1 <br/> String | Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Sous-titre ou description détaillée du point de l'ordre du jour. <br/><br/>Héritage : IsAgendaItem |
| state_id | 0..1 <br/> String | Identifiant d'état du point (renvoi à une énumération des états ou à un état propre), p. ex. pending (pas encore traité), in_progress (en délibération), completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn (retiré). <br/><br/>Héritage : IsAgendaItem |
| state_name | 0..1 <br/> String | Désignation de statut divergente, en texte libre, là où l'énumération des statuts ne suffit pas. <br/><br/>Héritage : IsAgendaItem |
| landing_page | 0..1 <br/> String | URL fournissant des informations complémentaires. <br/><br/>Héritage : IsAgendaItem |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue. <br/><br/>Héritage : IsAgendaItem |
| agenda_item_category | 0..1 <br/> String | Catégorisation libre du point selon son contenu ou son regroupement, p. ex. « Législation », « Budget et finances », « Interpellations et questions », « Élections », par département, ou points introductifs et techniques. La catégorisation n'est pas standardisée et peut varier selon l'unité fédérale. <br/><br/>Héritage : IsAgendaItem |
| parent_agenda_item | 0..1 <br/> String | Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il forme une hiérarchie de points — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l'énergie (discussion par article) » et « Loi sur l'énergie (vote final) » ; pour une intervention, il désigne le point sous lequel elle a été faite. <br/><br/>Héritage : IsAgendaItem |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | La décision formelle prise sur ce point de l'ordre du jour, p. ex. l'adoption de la loi sur l'énergie. Le vote sous-jacent avec son rapport de voix est saisi séparément comme Voting. <br/><br/>Héritage : IsAgendaItem |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Délibérations communes rattachées à cet enregistrement : pour un point de l'ordre du jour, les délibérations dans lesquelles il est traité conjointement avec d'autres points ; pour une séance ou une session, les délibérations communes qui s'y tiennent. <br/><br/>Héritage : IsAgendaItem |
| text_segments | * <br/> [TextSegment](#TextSegment) | Ensemble de segments de texte (p. ex. procès-verbal in extenso). <br/><br/>Héritage : IsAgendaItem |
| documents | * <br/> Work | Documents relatifs au point de l'ordre du jour, sous forme de FRBR Works, p. ex. messages et rapports, propositions et propositions d'amendement. <br/><br/>Héritage : IsAgendaItem |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | protocol_items | range | [ProtocolItem](#ProtocolItem) |
| [Voting](#Voting) | parent_protocol_item | range | [ProtocolItem](#ProtocolItem) |
| [Election](#Election) | parent_protocol_item | range | [ProtocolItem](#ProtocolItem) |



















</div>

## Délibération commune (JointDebate)



### Classe: JointDebate []{#JointDebate}


_Une délibération commune : plusieurs points de l'ordre du jour sont traités ensemble, par exemple des affaires connexes délibérées dans un seul et même débat. La délibération commune est rattachée à un point de l'ordre du jour (AgendaItem), à un point du procès-verbal (ProtocolItem), à une séance (Meeting) ou à une session (Session) et renvoie, par leurs identifiants, aux points traités conjointement. Rattachée à une séance ou à une session, elle peut aussi réunir des points répartis sur plusieurs positions de l'ordre du jour ou sur plusieurs séances._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> String | Identifiants des points de l'ordre du jour traités conjointement (AgendaItem ou ProtocolItem).  |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Session](#Session) | joint_debates | range | [JointDebate](#JointDebate) |
| [Meeting](#Meeting) | joint_debates | range | [JointDebate](#JointDebate) |
| IsAgendaItem | joint_debates | range | [JointDebate](#JointDebate) |
| [AgendaItem](#AgendaItem) | joint_debates | range | [JointDebate](#JointDebate) |
| [ProtocolItem](#ProtocolItem) | joint_debates | range | [JointDebate](#JointDebate) |



















</div>

## Resolution (décision)



### Classe: Resolution []{#Resolution}


_La décision formelle prise sur un point de l'ordre du jour, y compris les procédures de vote appliquées. Elle retient ce qui a été décidé, tandis que Voting retient comment il a été décidé (procédure et rapport de voix). Toute décision ne repose pas sur un vote formel : les prises de connaissance, les adoptions tacites ou les décisions administratives interviennent sans vote._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](#ResolutionTypeEnum) | Type de décision prise sur le point de l'ordre du jour.  |
| type_label | 0..1 <br/> String | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| vote_procedures | * <br/> String | Procédures selon lesquelles le vote a eu lieu. Procédures ouvertes : main levée, assis-debout, vote électronique, appel nominal et, en situation de crise, vote à distance (voix communiquées à l'avance à la présidence et saisies en même temps que le vote au conseil), procédure par voie de circulation ou vote lors de séances virtuelles. Procédures secrètes : bulletin de vote, vote électronique secret. La procédure détermine si les voix individuelles peuvent être saisies.  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | resolutions | range | [Resolution](#Resolution) |
| IsAgendaItem | has_resolution | range | [Resolution](#Resolution) |
| [AgendaItem](#AgendaItem) | has_resolution | range | [Resolution](#Resolution) |
| [ProtocolItem](#ProtocolItem) | has_resolution | range | [Resolution](#Resolution) |



















</div>

### Enum: ResolutionTypeEnum []{#ResolutionTypeEnum}




_Type de décision prise sur un point de l'ordre du jour._




<div data-search-exclude markdown="1">

URI: [ops:ResolutionTypeEnum](https://ch.paf.link/schema/operations/ResolutionTypeEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| accepted |  Adoption : p. ex. un projet de loi adopté, une proposition approuvée, une décision prise.  |
| | [ops:enum/resolution_type/accepted](ops:enum/resolution_type/accepted) |
| rejected |  Rejet : p. ex. un projet de loi rejeté, une proposition repoussée.  |
| | [ops:enum/resolution_type/rejected](ops:enum/resolution_type/rejected) |
| noted |  Prise d'acte : p. ex. rapports sans vote, communications, points informatifs.  |
| | [ops:enum/resolution_type/noted](ops:enum/resolution_type/noted) |
| accepted_point_by_point |  Acceptation point par point  |
| | [ops:enum/resolution_type/accepted_point_by_point](ops:enum/resolution_type/accepted_point_by_point) |
| accepted_with_postulate |  Acceptation avec postulat  |
| | [ops:enum/resolution_type/accepted_with_postulate](ops:enum/resolution_type/accepted_with_postulate) |
| orally_settled |  Liquidé oralement  |
| | [ops:enum/resolution_type/orally_settled](ops:enum/resolution_type/orally_settled) |
| nearly_unanimous |  Quasi unanime  |
| | [ops:enum/resolution_type/nearly_unanimous](ops:enum/resolution_type/nearly_unanimous) |
| other |  Autre type de décision, non couvert par les catégories standard  |
| | [ops:enum/resolution_type/other](ops:enum/resolution_type/other) |







</div>

## Motion (propositions)



### Classe: Motion []{#Motion}


_Une proposition formelle déposée au cours des délibérations, par exemple une proposition d'amendement à un texte légal, une motion d'ordre (p. ex. clôture du débat) ou une proposition de renvoi. Elle constitue une entité propre, car un point de l'ordre du jour peut comprendre plusieurs propositions, chacune ayant son propre déroulement (déposée, soutenue, mise aux voix) et, le cas échéant, son propre vote._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Titre abrégé de la proposition.  |
| description | 0..1 <br/> String | Texte intégral de la proposition.  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |






















</div>

\newpage

<!-- ToDo: Nicole -->

# Votes et élections

Les décisions parlementaires sont prises soit par des votes sur des questions matérielles, soit par des élections de personnes. La norme distingue clairement ces deux mécanismes et saisit en outre, dans les procédures ouvertes, le comportement de vote individuel de chaque membre du parlement.

## Voting (vote)



### Classe: Voting []{#Voting}


_Un vote sur une question matérielle : l'objet du vote (la question), la procédure, le résultat avec le rapport de voix et — pour les votes ouverts — les voix individuelles des membres. Le vote a lieu au cours de la séance et est donc rattaché au procès-verbal (parent_protocol, parent_protocol_item) ; il est en outre lié à la séance (parent_meeting) et à l'affaire (affair_id). La présidente ou le président ne participe pas aux votes, mais départage en cas d'égalité des voix (tie_breaker). La décision catégorielle (adopté, rejeté, pris acte …) n'est pas retenue sur le vote, mais dans la Resolution du point de l'ordre du jour._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> Datetime | La date et l'heure auxquelles la séance ou le vote se termine.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](#VotingTypeEnum) | Type de procédure de vote (vote intermédiaire, vote final, vote secret, etc.).  |
| type_label | 0..1 <br/> String | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| voting_title | * <br/> [MultilingualString](#MultilingualString) | Titre du vote, objet ou question soumise au vote. En l'absence d'objet propre, il ne faut pas reprendre le titre de l'affaire.  |
| optional | 0..1 <br/> Boolean | Indique si la séance ou le vote est facultatif.  |
| landing_page | 0..1 <br/> String | URL fournissant des informations complémentaires.  |
| label_yes | 0..1 <br/> String | Signification d'une voix « oui ».  |
| label_no | 0..1 <br/> String | Signification d'une voix « non ».  |
| label_abstention | 0..1 <br/> String | Signification d'une abstention.  |
| tie_breaker | 0..1 <br/> Boolean | Indique si le résultat a été obtenu, en cas d'égalité des voix, par la voix prépondérante de la présidente ou du président.  |
| total_count_yes | 0..1 <br/> Integer | Nombre total de voix « oui ».  |
| total_count_no | 0..1 <br/> Integer | Nombre total de voix « non ».  |
| total_count_abstention | 0..1 <br/> Integer | Nombre total d'abstentions.  |
| total_other | * <br/> [TotalOther](#TotalOther) | Nombres de voix pour les options d'un vote à choix multiple, une entrée par option ; remplace total_count_yes, total_count_no et total_count_abstention (voir TotalOther).  |
| total_absent | 0..1 <br/> Integer | Nombre de membres absents qui n'ont pas pu participer. La liste de présence (Attendance) indique si une absence était excusée.  |
| total | 0..1 <br/> Integer | Nombre total de voix, sans les absents ni la voix de la présidence.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type de majorité requise pour le vote (absolue, deux tiers, etc.).  |
| majority_count | 0..1 <br/> Integer | Nombre de voix requis pour atteindre le seuil de majorité déterminant.  |
| result_text | 0..1 <br/> String | Texte libre décrivant le résultat, p. ex. « Adopté par 120 voix contre 75 et 5 abstentions ». Pour les votes, la décision catégorielle (adopté, rejeté, pris acte …) n'est pas retenue ici, mais dans la Resolution (resolution_type) du point de l'ordre du jour.  |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| parent_protocol | 0..1 <br/> [Protocol](#Protocol) | Le procès-verbal dans lequel le vote ou l'élection est consigné. Le vote a lieu au cours de la séance et se rattache donc au procès-verbal, et non à l'ordre du jour planifié à l'avance : ce qui a été mis à l'ordre du jour ne dit pas encore sur quoi il a effectivement été voté. Inversement, le procès-verbal reprend ses votes et élections sous forme de listes (votings, elections).  |
| parent_protocol_item | 0..1 <br/> [ProtocolItem](#ProtocolItem) | Le point consigné au procès-verbal (ProtocolItem) sous lequel le vote ou l'élection a eu lieu. Absent lorsque le vote a eu lieu sans point de l'ordre du jour ; le rattachement à la séance découle alors uniquement de parent_protocol et parent_meeting.  |
| affair_id | 0..1 <br/> String | Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | votings | range | [Voting](#Voting) |
| [Protocol](#Protocol) | votings | range | [Voting](#Voting) |
| [IndividualVote](#IndividualVote) | parent_voting | range | [Voting](#Voting) |














#### Exemples
##### Exemple Voting : Vote final sur le budget

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
  parent_protocol: ops:protocol_zh_2025_11_20
  parent_protocol_item: ops:protocol_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: actors:kr_zh
    label: Kantonsrat Zürich
    abbreviation:
    - value: KR
      language: de
  datetime_created: '2025-11-20T16:45:00Z'
  datetime_modified: '2025-11-20T16:50:00Z'

```
##### Exemple Voting : Motions in the same direction with multiple choice

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
  parent_protocol: ops:protocol_zh_gr_2024_02_28
  parent_protocol_item: ops:protocol_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: 2023/361
  actor_id:
    global_uri: actors:gr_stadt_zuerich
    label: Gemeinderat der Stadt Zürich
    abbreviation:
    - value: GR
      language: de
  datetime_created: '2024-02-28T00:00:00Z'
  datetime_modified: '2024-02-28T00:00:00Z'

```
##### Exemple Voting : Final vote with individual votes

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
  parent_protocol: ops:protocol_sg_2025_03_15
  parent_protocol_item: ops:protocol_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: actors:kr_sg
    label: Kantonsrat St. Gallen
    abbreviation:
    - value: KR
      language: de
  datetime_created: '2025-03-15T14:30:00Z'
  datetime_modified: '2025-03-15T14:35:00Z'

```
##### Exemple Voting : Intermediate voting on an amendment

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
  parent_protocol: ops:protocol_be_2025_06_05
  parent_protocol_item: ops:protocol_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: actors:gr_be
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  datetime_created: '2025-06-05T10:15:00Z'
  datetime_modified: '2025-06-05T10:15:00Z'

```






</div>

### Enum: VotingTypeEnum []{#VotingTypeEnum}




_Type de procédure de vote._




<div data-search-exclude markdown="1">

URI: [ops:VotingTypeEnum](https://ch.paf.link/schema/operations/VotingTypeEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| preliminary_vote |  Vote intermédiaire au cours de la délibération, p. ex. sur l'entrée en matière, sur une proposition, opposition de deux propositions qui s'excluent mutuellement ou portent sur le même passage, vote éventuel lorsque plus de deux propositions portent sur un même objet, sur un article isolé d'une loi, ou vote sur l'ensemble après la première lecture d'un acte délibéré en deux lectures.  |
| | [ops:enum/voting_type/preliminary_vote](ops:enum/voting_type/preliminary_vote) |
| final_vote |  Vote final sur l'objet dans son ensemble, p. ex. après la dernière lecture d'un acte, vote sur l'ensemble d'un arrêté, adoption ou rejet d'un objet dans sa totalité, ou vote point par point sur une intervention parlementaire.  |
| | [ops:enum/voting_type/final_vote](ops:enum/voting_type/final_vote) |
| tie_breaker_president |  Voix prépondérante de la présidente ou du président en cas d'égalité des voix. La présidente ou le président ne participe pas aux votes, mais tranche en cas d'égalité. Si un vote secret aboutit à une égalité, c'est la proposition de l'organe préparatoire qui est réputée adoptée.  |
| | [ops:enum/voting_type/tie_breaker_president](ops:enum/voting_type/tie_breaker_president) |
| secret_vote |  Vote secret, p. ex. sur des objets particulièrement sensibles tels qu'un recours en grâce ou la levée de l'immunité, après une délibération secrète ou sur demande. Seul le résultat global est publié.  |
| | [ops:enum/voting_type/secret_vote](ops:enum/voting_type/secret_vote) |
| other |  Autre type de vote, précisé dans type_label — p. ex. un vote à choix multiple sur plusieurs propositions de même sens (voir TotalOther).  |
| | [ops:enum/voting_type/other](ops:enum/voting_type/other) |







</div>

### Enum: MajorityTypeEnum []{#MajorityTypeEnum}




_Type de majorité requise pour le vote._




<div data-search-exclude markdown="1">

URI: [ops:MajorityTypeEnum](https://ch.paf.link/schema/operations/MajorityTypeEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| absolute |  Majorité absolue : plus de la moitié de la base de référence (membres ou voix exprimées, selon la réglementation applicable), p. ex. au moins 101 sur 200. Cas standard pour les élections de personnes telles que l'élection du Conseil fédéral ou des présidences de commission, et requise dans certains cantons pour les modifications constitutionnelles. Si personne ne l'atteint au premier tour d'une élection, un second tour suit généralement, où la majorité relative suffit.  |
| | [ops:enum/majority_type/absolute](ops:enum/majority_type/absolute) |
| two_thirds |  Majorité des deux tiers, p. ex. au moins 134 sur 200 ; requise dans certains cantons pour les modifications constitutionnelles.  |
| | [ops:enum/majority_type/two_thirds](ops:enum/majority_type/two_thirds) |
| other |  Autre seuil de majorité non couvert par les catégories standard, p. ex. la majorité relative entre plusieurs options d'un vote à choix multiple.  |
| | [ops:enum/majority_type/other](ops:enum/majority_type/other) |







</div>



### Classe: TotalOther []{#TotalOther}


_Nombre de voix pour une option d'un vote à choix multiple. Lorsque plusieurs propositions de même sens portent sur la même question, les membres votent simultanément sur plus de deux variantes, et la variante qui obtient le plus de voix l'emporte (à Zurich, familièrement « Cup-Abstimmung », au moyen de plusieurs boutons de vote). Un tel vote est représenté avec voting_type other et un type_label explicite ; total_count_yes, total_count_no et total_count_abstention restent vides, et chaque option reçoit une entrée avec count et label. Exemple : Gemeinderat de la Ville de Zurich, séance du 28 février 2024, affaire 2023/361, quatre options avec 75, 25, 12 et 0 voix._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| count | 0..1 <br/> Integer | Le nombre de voix pour la catégorie « autres ».  |
| label | 0..1 <br/> String | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Voting](#Voting) | total_other | range | [TotalOther](#TotalOther) |



















</div>

## Individual Vote (voix individuelle)



### Classe: IndividualVote []{#IndividualVote}


_La voix exprimée par un membre lors d'un vote. Les voix individuelles ne sont saisies que pour les votes ouverts ; pour les votes secrets, seul le résultat global est publié. Une voix individuelle concerne un vote déterminé et se distingue de la présence (Attendance), qui retient la présence à la séance dans son ensemble : un membre présent à la séance peut être saisi avec not_voted lors d'un vote particulier, par exemple parce qu'il a brièvement quitté la salle._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| parent_voting | 0..1 <br/> [Voting](#Voting) | L'identifiant du vote auquel se rattache la voix individuelle.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Le membre qui a exprimé la voix, sous forme de référence à une personne selon eCH-0294.  |
| seat_nr | 0..1 <br/> String | Le numéro de siège correspondant à la voix individuelle, le cas échéant.  |
| weight | 0..1 <br/> Integer | Poids de la voix du membre ; normalement 1. D'autres valeurs se présentent par exemple lorsqu'un membre vote aussi pour un membre absent (représentation, poids 2), dans les assemblées communales où des personnes morales disposent de plusieurs voix, ou dans des systèmes historiques où différents groupes de personnes avaient un poids de voix différent.  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](#IndividualVoteTypeEnum) | Type de voix exprimée (oui, non, abstention, n'a pas voté, etc.).  |
| type_label | 0..1 <br/> String | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_votes | range | [IndividualVote](#IndividualVote) |














#### Exemples
##### Exemple IndividualVote : Absent lors d'un choix multiple

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
##### Exemple IndividualVote : Abstention

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
##### Exemple IndividualVote : Yes vote

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
##### Exemple IndividualVote : Did not vote

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
##### Exemple IndividualVote : No vote

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
##### Exemple IndividualVote : Yes vote on the budget

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
##### Exemple IndividualVote : No vote on the budget

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
##### Exemple IndividualVote : Individual vote for selection option C

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
##### Exemple IndividualVote : Individual vote for selection option B

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
##### Exemple IndividualVote : Individual vote for selection option A

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






</div>

### Enum: IndividualVoteTypeEnum []{#IndividualVoteTypeEnum}




_Type de voix individuelle exprimée par un membre._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| yes |  Oui : le membre approuve l'objet ou la proposition.  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  Non : le membre rejette l'objet ou la proposition.  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Abstention : le membre participe au vote mais s'abstient ; en cas de vote électronique, il presse le bouton « abstention ».  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  N'a pas voté : le membre n'a pas exprimé de voix, par exemple parce qu'il était présent sans voter ou absent.  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Voix prépondérante, exprimée par la présidente ou le président en cas d'égalité des voix (voir voting_type tie_breaker_president).  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Voix qui ne peut être placée sur l'axe oui/non — par exemple lors d'un vote à choix multiple, où le membre a voté, mais ni oui ni non ; l'option choisie est retenue dans type_label (p. ex. « Choix A »). Pendant de total_other sur le vote ; la voix individuelle reste ainsi exploitable sans qu'il faille une valeur d'énumération propre pour chaque mécanisme de choix cantonal.  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>

## Election (élection)



### Classe: Election []{#Election}


_Une élection par laquelle un organe parlementaire désigne une ou plusieurs personnes à une charge ou à une fonction. Contrairement au vote (Voting), qui tranche des questions matérielles, l'élection est une décision portant sur des personnes : elle a souvent lieu au scrutin secret et requiert en général la majorité absolue, alors que les votes sont le plus souvent ouverts. La présidente ou le président, qui ne participe pas aux votes, prend part aux élections. Chaque tour de scrutin est saisi comme une élection distincte ; les tours d'une même élection sont reliés par le point de l'ordre du jour commun — par exemple un premier tour à la majorité absolue resté sans résultat, suivi d'un second tour où la majorité relative suffit._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> Datetime | La date et l'heure auxquelles la séance ou le vote se termine.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](#ElectionTypeEnum) | Type de procédure d'élection.  |
| type_label | 0..1 <br/> String | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| title | 0..1 <br/> String | Titre de l'élection, p. ex. « Élection à la présidence de la CER ».  |
| landing_page | 0..1 <br/> String | URL fournissant des informations complémentaires.  |
| total_absent | 0..1 <br/> Integer | Nombre de membres absents qui n'ont pas pu participer. La liste de présence (Attendance) indique si une absence était excusée.  |
| total | 0..1 <br/> Integer | Nombre total de voix, sans les absents ni la voix de la présidence.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type de majorité requise pour le vote (absolue, deux tiers, etc.).  |
| majority_count | 0..1 <br/> Integer | Nombre de voix requis pour atteindre le seuil de majorité déterminant.  |
| result_text | 0..1 <br/> String | Texte libre décrivant le résultat, p. ex. « Adopté par 120 voix contre 75 et 5 abstentions ». Pour les votes, la décision catégorielle (adopté, rejeté, pris acte …) n'est pas retenue ici, mais dans la Resolution (resolution_type) du point de l'ordre du jour.  |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| parent_protocol | 0..1 <br/> [Protocol](#Protocol) | Le procès-verbal dans lequel le vote ou l'élection est consigné. Le vote a lieu au cours de la séance et se rattache donc au procès-verbal, et non à l'ordre du jour planifié à l'avance : ce qui a été mis à l'ordre du jour ne dit pas encore sur quoi il a effectivement été voté. Inversement, le procès-verbal reprend ses votes et élections sous forme de listes (votings, elections).  |
| parent_protocol_item | 0..1 <br/> [ProtocolItem](#ProtocolItem) | Le point consigné au procès-verbal (ProtocolItem) sous lequel le vote ou l'élection a eu lieu. Absent lorsque le vote a eu lieu sans point de l'ordre du jour ; le rattachement à la séance découle alors uniquement de parent_protocol et parent_meeting.  |
| affair_id | 0..1 <br/> String | Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | elections | range | [Election](#Election) |
| [Protocol](#Protocol) | elections | range | [Election](#Election) |



















</div>

### Enum: ElectionTypeEnum []{#ElectionTypeEnum}




_Type de procédure d'élection._




<div data-search-exclude markdown="1">

URI: [ops:ElectionTypeEnum](https://ch.paf.link/schema/operations/ElectionTypeEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| secret |  Élection secrète : les voix sont exprimées anonymement, au moyen d'un bulletin ou d'un système électronique de vote secret, de sorte qu'on ne peut savoir qui a élu qui. Standard pour les élections de personnes et souvent prescrite par la loi — au niveau fédéral p. ex. le Conseil fédéral (par l'Assemblée fédérale Chambres réunies, à la majorité absolue lors des premiers tours), les juges fédérales et juges fédéraux et les présidences de commission ; au niveau cantonal p. ex. la présidence du parlement, la présidence du gouvernement, les présidences des tribunaux suprêmes, les juges, la chancelière ou le chancelier d'État et les présidences de commission. Seul le résultat global est publié, sans voix individuelles.  |
| | [ops:enum/election_type/secret](ops:enum/election_type/secret) |
| open |  Élection ouverte : les voix sont exprimées ouvertement et l'on peut savoir qui a élu qui ; les voix individuelles peuvent donc être saisies. Usuelle lorsque la transparence est souhaitée, pour les élections non disputées ou dans les organes de petite taille.  |
| | [ops:enum/election_type/open](ops:enum/election_type/open) |
| silent |  Élection tacite sans vote formel, par acclamation ou consensus ; possible uniquement si aucune opposition n'est formulée, p. ex. la réélection d'une présidente ou d'un président de commission sans candidature concurrente.  |
| | [ops:enum/election_type/silent](ops:enum/election_type/silent) |







</div>

\newpage

# Présence

Les listes de présence consignent qui a participé à une séance. Elles documentent la participation et constituent la base permettant d'apprécier la capacité de décision d'un organe.

## Attendance (présence)

### Notion et signification

L'Attendance (présence) saisit quels membres d'un organe parlementaire étaient présents, absents ou excusés lors d'une séance. Elle sert à documenter la participation et constitue la condition du quorum.

### Structure à deux niveaux

La norme distingue deux niveaux de saisie de la présence :

#### 1. Attendance (niveau agrégé)
Récapitulation de la présence pour une séance :
- Nombre total de personnes présentes
- Nombre total de personnes absentes (excusées / non excusées)
- Quorum

#### 2. IndividualAttendance (niveau individuel)
Saisie détaillée pour chaque personne :
- Qui était présent ?
- Qui était absent ?
- L'absence était-elle excusée ?

```
Meeting (séance du Conseil national du 4 mars 2024)
  └─ Attendance (présence agrégée)
      ├─ IndividualAttendance (personne A : présente)
      ├─ IndividualAttendance (personne B : excusée)
      ├─ IndividualAttendance (personne C : absente)
      └─ ...
```

## Attendance (niveau agrégé)

#### Rattachement à la séance et à l'organe

- **parent_meeting** : renvoi à la séance à laquelle se rapporte la liste de présence
- **actor_id** : renvoi à l'organe (parlement, commission) selon eCH-0294 Actors
- **datetime_begin** : moment de la constatation de la présence

#### Chiffres agrégés

- **total_count** : nombre total de membres de l'organe (valeur de référence pour le calcul du quorum, p. ex. 200 pour le Conseil national, 46 pour le Conseil des États)
- **total_present** : nombre de membres présents
- **total_excused** : nombre de membres excusés
- **total_absent** : nombre de membres absents non excusés

**Exemple :**
- Total : 200
- Présents : 185
- Excusés : 12
- Absents : 3

#### Quorum

Le quorum résulte du rapport entre `total_present` et `total_count` ainsi que des règles de quorum propres à l'organe. Il n'est donc pas enregistré comme champ distinct, mais calculé au besoin à partir des données.

## IndividualAttendance (niveau individuel)

#### Lien

- **parent_attendance** : renvoi à l'agrégat `Attendance` de rang supérieur (lui-même rattaché à la séance). La saisie individuelle est ainsi proprement rattachée à la séance.
- **actor_id** : renvoi à la personne selon eCH-0294 Actors

#### Type de présence

Le champ **attendance_type** (énumération `AttendanceTypeEnum`) saisit le type de présence :

- **present** : présent en personne
- **remote** : présent à distance (p. ex. visioconférence)
- **substitute** : suppléance — une autre personne a participé en remplacement

> La modélisation de la suppléance (p. ex. qui a remplacé qui, avec quel droit de vote) est approfondie dans l'[issue #24](https://github.com/swiss/political-affairs-ech-group/issues/24).
>
> Un deuxième axe d'état `present` / `excused` / `absent` (« si présent ») parallèle à l'axe existant « comment présent » est en discussion comme extension.

#### Motif

Le champ **reason** (multilingue) permet de saisir en texte libre le motif d'une absence, d'un retard ou d'une suppléance.

### Différence : Attendance et IndividualVote

Distinction importante :

| Aspect | Attendance | IndividualVote |
|--------|------------|----------------|
| Saisit | Présence à la séance | Expression de la voix lors d'un vote |
| Moment | Début / durant la séance | Moment du vote |
| Granularité | Par séance | Par vote |

**Exemple :** une personne peut être présente à la séance (Attendance : present), mais être enregistrée comme absente lors d'un vote déterminé (IndividualVote : absent), parce qu'elle a brièvement quitté la salle à ce moment-là.

### Utilisations

Les entités Attendance permettent :

1. **Documentation** : saisie traçable de la participation
2. **Vérification du quorum** : garantie de la capacité de décision
3. **Transparence** : information publique sur la présence
4. **Reddition de comptes** : contrôle de l'exécution des obligations
5. **Statistiques** : évaluation des taux de présence
6. **Administration** : calcul des indemnités et des frais



### Classe: Attendance []{#Attendance}


_Liste de présence agrégée pour une séance (nombre de membres présents, absents, excusés)._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| datetime_begin | 0..1 <br/> Datetime | La date et l'heure auxquelles la séance ou le vote commence.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| total_count | 0..1 <br/> Integer | Nombre total de membres de l'organe (valeur de référence pour le calcul du quorum).  |
| total_present | 0..1 <br/> Integer | Nombre total de membres présents.  |
| total_absent | 0..1 <br/> Integer | Nombre de membres absents qui n'ont pas pu participer. La liste de présence (Attendance) indique si une absence était excusée.  |
| total_excused | 0..1 <br/> Integer | Nombre total d'absences excusées.  |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | attendances | range | [Attendance](#Attendance) |
| [IndividualAttendance](#IndividualAttendance) | parent_attendance | range | [Attendance](#Attendance) |



















</div>



### Classe: IndividualAttendance []{#IndividualAttendance}


_Constatation individuelle de la présence d'une personne à une séance (rattachée à l'agrégat Attendance parent)._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| parent_attendance | 0..1 <br/> [Attendance](#Attendance) | L'agrégat Attendance auquel appartient cette constatation individuelle de présence.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Référence à la personne agissante (instantané au moment de la mise en relation).  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](#AttendanceTypeEnum) | Type de présence individuelle.  |
| reason | * <br/> [MultilingualString](#MultilingualString) | Motif de l'absence, du retard ou de la suppléance (texte libre, multilingue).  |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_attendances | range | [IndividualAttendance](#IndividualAttendance) |



















</div>

### Enum: AttendanceTypeEnum []{#AttendanceTypeEnum}




_Type de présence individuelle._




<div data-search-exclude markdown="1">

URI: [ops:AttendanceTypeEnum](https://ch.paf.link/schema/operations/AttendanceTypeEnum)

#### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| remote |  Participation à distance  |
| | [ops:enum/attendance_type/remote](ops:enum/attendance_type/remote) |
| substitute |  Suppléance  |
| | [ops:enum/attendance_type/substitute](ops:enum/attendance_type/substitute) |
| present |  Présent en personne  |
| | [ops:enum/attendance_type/present](ops:enum/attendance_type/present) |







</div>

\newpage

<!-- ToDo: David -->

<!--
Débat

* -> Enregistrement vidéo -> transcription des propos
*   -> Procès-verbal in extenso -> Text to Timestamp -> le texte contient les horodatages -> document texte (avec ou sans définition du format (types de span))
*   -> Procès-verbal remanié -> AgendaItem to Timestamp
-->

# Interventions

Les interventions consignent le débat parlementaire — qui a pris la parole, quand et sur quel point de l'ordre du jour, avec le texte in extenso et, lorsqu'il existe, l'enregistrement audio ou vidéo.

## Speech (intervention, prise de parole)

### Notion et signification

Une Speech (intervention, prise de parole) désigne une contribution orale d'une personne au cours d'une séance parlementaire. Elle est l'instrument central du débat politique et de l'expression des opinions au parlement.

### Types de Speeches

Les interventions parlementaires prennent différentes formes :

#### Interventions principales
- Prises de position détaillées sur une affaire
- Motivation de propositions
- Exposé de la position du groupe

#### Interventions brèves
- Prises de parole courtes
- Questions intercalaires
- Rectifications

#### Déclarations de groupe
- Prise de position officielle d'un groupe
- Présentée par la ou le porte-parole du groupe

#### Interventions gouvernementales
- Prises de position de membres du gouvernement
- Réponses aux questions
- Défense de projets

### Structure et rattachement

Une Speech est toujours rattachée à un contexte déterminé :

```
Meeting (séance)
  └─ AgendaItem (point de l'ordre du jour)
      └─ Speech (intervention personne A)
          ├─ TextSegment (transcription)
          ├─ Media (enregistrement audio)
          └─ Media (enregistrement vidéo)
```

#### Champs de rattachement

- **meeting_id** : la séance au cours de laquelle l'intervention a eu lieu
- **agenda_item_id** : le point de l'ordre du jour auquel se rapporte l'intervention
- **person_id** : la personne qui s'exprime (selon eCH-0294 Actors)

### Identification des personnes qui s'expriment

- **person_id** : identification univoque de la personne
- **person_name** : nom, pour un accès rapide
- **role** : rôle de la personne (p. ex. « présidence de groupe », « rapporteuse ou rapporteur », « conseillère fédérale / conseiller fédéral »)

### Saisie temporelle

- **start_time** : début de l'intervention
- **end_time** : fin de l'intervention
- **duration** : durée en secondes (calculée ou saisie)

Ces indications temporelles permettent :
- une référence précise dans les enregistrements audio et vidéo
- l'analyse du temps de parole par personne ou par groupe
- le contrôle du respect des limites de temps

### Langue de l'intervention

Le champ **language** saisit la langue dans laquelle l'intervention a été prononcée :

- **de** : allemand
- **fr** : français
- **it** : italien
- **rm** : romanche
- **en** : anglais

### Documents textuels

Le champ **text_segments** renvoie aux entités TextSegment qui contiennent le texte prononcé.

#### Différentes versions du texte

##### Transcription brute
- Retranscription littérale
- Non remaniée, avec les mots de remplissage
- Disponible directement après la séance

##### Transcription remaniée
- Revue sur le plan rédactionnel
- Corrigée grammaticalement
- Version officielle du procès-verbal

##### Traductions
- Dans d'autres langues nationales
- Pour les publications internationales

#### Structure de TextSegment

Chaque TextSegment peut contenir :
- **text** : le texte proprement dit
- **language** : langue du texte
- **version** : type de version (raw, edited, translated)
- **format** : format (plain, markdown, HTML)

### Enregistrements multimédias

Le champ **media** renvoie aux entités Media comportant des enregistrements audio et vidéo.

#### Enregistrements audio
- Son original de l'intervention
- Format : MP3, WAV, etc.
- Métadonnées techniques (qualité, débit binaire)

#### Enregistrements vidéo
- Enregistrement visuel (lors des séances plénières)
- Format : MP4, WebM, etc.
- Différentes résolutions

#### Diffusion en direct
- Transmission en temps réel
- URL du flux
- Archivage après la séance

### Titre et description

- **title** : titre court (p. ex. « Intervention sur la politique énergétique »)
- **description** : résumé ou contexte de l'intervention

### Type d'intervention

Le champ **speech_type** permet de distinguer différents types :

- **statement** : prise de position
- **question** : question
- **response** : réponse (p. ex. du gouvernement à une question)
- **procedural** : proposition d'ordre
- **declaration** : déclaration

### Rattachement à la séance

`parent_meeting` et `parent_agenda_item` indiquent au cours de quelle séance et sous quel point de l'ordre du jour une intervention a été prononcée. Les deux sont nécessaires, car une intervention peut être livrée de deux manières : imbriquée dans le procès-verbal, où la séance ressort du `Protocol` environnant mais non le point de l'ordre du jour — ou à plat dans `Container.speeches`, où tout rattachement ferait défaut sans ces références. Elles portent les mêmes valeurs que pour `Voting` et `Election` et rendent ainsi l'intervention exploitable indépendamment de sa forme de livraison.



### Classe: Speech []{#Speech}


_Une intervention prononcée au cours d'une séance (également appelée prise de parole)._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| parent_agenda_item | 0..1 <br/> String | Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il forme une hiérarchie de points — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l'énergie (discussion par article) » et « Loi sur l'énergie (vote final) » ; pour une intervention, il désigne le point sous lequel elle a été faite.  |
| language | 0..1 <br/> String | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |
| start | 0..1 <br/> String | Indication de début ou position.  |
| datetime_begin | 0..1 <br/> Datetime | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> Datetime | La date et l'heure auxquelles la séance ou le vote se termine.  |
| actor_fullname | 0..1 <br/> String | Nom complet de l'actrice ou de l'acteur, respectivement de la personne.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Référence à la personne agissante (instantané au moment de la mise en relation).  |
| role | 0..1 <br/> String | Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission).  |
| text | 1 <br/> String | Contenu textuel de l'élément.  |
| text_format | 0..1 <br/> String | Format du texte (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> String | Type de texte (version brute, version éditée).  |
| landing_page | 0..1 <br/> String | URL fournissant des informations complémentaires.  |
| media_url | 0..1 <br/> String | URL du fichier média (audio/vidéo).  |
| media_type | 0..1 <br/> String | Type de média (audio, vidéo, document).  |
| media_format | 0..1 <br/> String | Type MIME du fichier média.  |
| documents | * <br/> Work | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](#Container) | speeches | range | [Speech](#Speech) |
| [Protocol](#Protocol) | speeches | range | [Speech](#Speech) |














#### Exemples
##### Exemple Speech : Intervention avec texte in extenso et enregistrement vidéo

```yaml
speeches:
- global_uri: ops:366631
  parent_meeting: parl:sr_winter25_sitzung_6
  parent_agenda_item: ops:69905
  language: fr
  datetime_begin: '2025-12-19T09:20:00+01:00'
  datetime_end: '2025-12-19T09:25:00+01:00'
  actor_fullname: Pascal Broulis
  actor_id:
    global_uri: actors:person_pascal_broulis
    wikidata_uri: http://www.wikidata.org/entity/Q116407
    label: Pascal Broulis
  role: speaker
  text: >-
    Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec
    attention les différents commentaires qui ont été effectués sur mon postulat.
    Cela reste un postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis
    selon lequel ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark",
    à savoir un modèle chiffré de performance, permettrait de mieux comprendre les
    raisons des retards que notre pays rencontre en comparaison avec les principaux
    pays européens.
  text_format: html
  text_type: final
  landing_page: >-
    https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
  media_url: https://par-pcache.simplex.tv/content?externalid=366631
  media_type: video
  media_format: video/mp4

```






</div>

\newpage

# Textes et médias

Les débats parlementaires ne sont pas seulement saisis comme données structurées, mais également comme textes et enregistrements multimédias. Ces entités permettent la gestion des transcriptions, des enregistrements audio et vidéo et d'autres formats médiatiques, ainsi que l'infrastructure technique nécessaire à l'échange de données et au multilinguisme.

## TextSegment

### But
Saisit des passages de texte avec versionnage et variantes linguistiques. Utilisé principalement pour les transcriptions d'interventions, mais applicable également à d'autres documents textuels.

### Structure
- **text** : le contenu textuel proprement dit
- **language** : code de langue (ISO 639-1)
- **format** : format du texte (plain, markdown, html)
- **version_type** : type de version
  - **raw** : transcription brute non remaniée
  - **edited** : version remaniée sur le plan rédactionnel
  - **translated** : traduction dans une autre langue
  - **summary** : résumé

### Décision de conception
**Pourquoi une entité distincte ?**
- Permet plusieurs versions du même texte (version brute, remaniée, traduite)
- Contrôle des versions et traçabilité des modifications
- Souplesse quant aux formats (plain, markdown, HTML pour différents canaux de diffusion)

### Application
Principalement liée aux entités Speech :
```
Speech
  ├─ TextSegment (transcription brute, de)
  ├─ TextSegment (procès-verbal remanié, de)
  ├─ TextSegment (traduction, fr)
  └─ TextSegment (résumé, de)
```

### Porteurs d'un segment de texte

Les segments de texte ne se rattachent pas uniquement au procès-verbal in extenso : `Protocol` les porte pour le texte intégral de toute la séance, et `AgendaItem` — respectivement le `ProtocolItem` consigné — pour un texte se rapportant à un seul point de l'ordre du jour, par exemple un intertitre, un renvoi ou une motivation publiée déjà avec l'ordre du jour. Comme les deux classes portent le mixin `IsAgendaItem`, `text_segments` est disponible aussi bien du côté planifié que du côté consigné. L'intervention isolée, en revanche, porte son texte directement dans `text`, `text_format` et `text_type`.

## Media

### But
Référence des fichiers médias (audio, vidéo, documents) se rapportant aux activités parlementaires.

### Structure
- **media_type** : type du fichier média
  - **audio** : enregistrement audio
  - **video** : enregistrement vidéo
  - **document** : documents (PDF, etc.)
  - **image** : images
- **url** : URL du fichier média
- **mime_type** : type MIME (audio/mp3, video/mp4, application/pdf, etc.)
- **title** : titre du fichier média
- **description** : description
- **language** : langue (pour les médias fondés sur la langue)
- **duration** : durée (pour l'audio et la vidéo, en secondes)
- **file_size** : taille du fichier en octets
- **quality** : indication de qualité (p. ex. « 720p », « high », « low »)

### Décision de conception
**Pourquoi une entité Media générique ?**
- Structure uniforme pour tous les types de médias
- Extensible à de nouveaux formats
- Métadonnées techniques saisies de manière centralisée
- Plusieurs niveaux de qualité du même enregistrement possibles

### Application
Peut être rattachée à différentes entités :
```
Speech
  ├─ Media (enregistrement audio, MP3, 256 kbit/s)
  ├─ Media (enregistrement audio, MP3, 128 kbit/s)
  ├─ Media (enregistrement vidéo, MP4, 1080p)
  └─ Media (enregistrement vidéo, MP4, 480p)

AgendaItem
  └─ Media (PDF du projet)

Meeting
  └─ Media (URL du flux en direct)
```



### Classe: TextSegment []{#TextSegment}


_Un segment de texte tel qu'un renvoi ou un intertitre. Les segments de texte sont portés par le procès-verbal, par une intervention ou par un point de l'ordre du jour (AgendaItem planifié ou ProtocolItem consigné)._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| text | 1 <br/> String | Contenu textuel de l'élément.  |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| IsAgendaItem | text_segments | range | [TextSegment](#TextSegment) |
| [AgendaItem](#AgendaItem) | text_segments | range | [TextSegment](#TextSegment) |
| [Protocol](#Protocol) | text_segments | range | [TextSegment](#TextSegment) |
| [ProtocolItem](#ProtocolItem) | text_segments | range | [TextSegment](#TextSegment) |



















</div>



### Classe: Media []{#Media}


_Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD ou les liens vers des contenus audio/vidéo)._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Titre de l'élément.  |
| media_type | 0..1 <br/> String | Type de média (audio, vidéo, document).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| version | 0..1 <br/> String | Numéro ou identifiant de version.  |
| parent_type | 0..1 <br/> String | Type de l'objet parent (séance, point de l'ordre du jour, intervention, affaire).  |






















</div>

\newpage

# Éléments partagés

## Classes de référence

`PersonReference` et `GroupReference` désignent respectivement une personne et un groupe sans les décrire ici : ce qu'est une personne ou un organe est défini par eCH-0294 ; le fonctionnement des conseils ne fait qu'y renvoyer. Outre le renvoi, la référence retient les principales caractéristiques **au moment de la mise en relation** — pour une intervention, par exemple, le groupe parlementaire auquel la personne appartenait alors.

Cela sert trois objectifs :

- **Des données locales utiles** sans interrogation coûteuse de l'entité complète
- **Pas de redondance**, puisque toutes les indications ne doivent pas être répétées à chaque mention
- **Un versionnage implicite**, la référence restant inchangée même si la personne ou le groupe lié évolue par la suite

Contrairement à une entité, une référence n'est pas identifiée en propre — elle ne fait que désigner une entité identifiée. C'est pourquoi la `global_uri` n'y est pas obligatoire : il est seulement exigé qu'au moins l'une des deux indications `local_id` ou `global_uri` soit renseignée. Un système qui ne connaît de l'entité référencée que l'identifiant local indique celui-ci ; il est résolu au sein de la même livraison. Au-delà de la livraison, c'est la `global_uri` qui renvoie.



### Classe: PersonReference []{#PersonReference}


_Référence abrégée à une personne avec les principales données d'identification au moment de la liaison. Préserve l'exactitude historique même si la personne change ultérieurement. La personne référencée est désignée par `local_id` ou `global_uri` ; au moins l'un des deux est requis._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local de l'entité référencée. Il est résolu au sein de la même livraison. <br/><br/>Héritage : HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | L'URI unique et globalement valide de l'entité référencée. Contrairement à un local_id, elle est également résoluble au-delà de la livraison. <br/><br/>Héritage : HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, p. ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : HasReferenceIdentification |
| label | 1 <br/> String | Nom d'affichage court obligatoire permettant d'identifier la personne au sein de l'organisation (par ex. avec l'ajout de l'année de naissance afin de distinguer les personnes portant le même nom).  |
| label_long | 0..1 <br/> String | Nom d'affichage long facultatif comprenant les titres académiques et le nom officiel complet (par ex. « Dr. Maria Muster-Beispiel »).  |
| group_label | 0..1 <br/> String | Nom de l'organe/du groupe au moment de la liaison.  |

###### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- local_id
- global_uri










#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [IndividualVote](#IndividualVote) | actor_id | range | [PersonReference](#PersonReference) |
| [IndividualAttendance](#IndividualAttendance) | actor_id | range | [PersonReference](#PersonReference) |
| [Speech](#Speech) | actor_id | range | [PersonReference](#PersonReference) |



















</div>



### Classe: GroupReference []{#GroupReference}


_Référence abrégée à un groupe avec les principales données d'identification au moment de la liaison. Le groupe référencé est désigné par `local_id` ou `global_uri` ; au moins l'un des deux est requis. Un `local_id` est résolu au sein de la même livraison, un `global_uri` également au-delà._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local de l'entité référencée. Il est résolu au sein de la même livraison. <br/><br/>Héritage : HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | L'URI unique et globalement valide de l'entité référencée. Contrairement à un local_id, elle est également résoluble au-delà de la livraison. <br/><br/>Héritage : HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, p. ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : HasReferenceIdentification |
| label | 0..1 <br/> String | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| abbreviation | * <br/> MultilingualValue | Abréviation (peut être multilingue).  |

###### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- local_id
- global_uri










#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | actor_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | group_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | actor_id | range | [GroupReference](#GroupReference) |
| [Voting](#Voting) | actor_id | range | [GroupReference](#GroupReference) |
| [Election](#Election) | actor_id | range | [GroupReference](#GroupReference) |
| [Attendance](#Attendance) | actor_id | range | [GroupReference](#GroupReference) |



















</div>

## Textes multilingues

En Suisse, les désignations, titres et descriptions existent souvent en plusieurs langues. Plutôt que de tenir un champ distinct par langue, un slot de type `MultilingualString` reprend une liste d'entrées comportant `text` et `language`. Qui ne tient qu'une seule langue livre une entrée unique — la langue doit être indiquée là aussi. Les liens sont modélisés de la même manière : de nombreux systèmes d'information parlementaire tiennent une adresse propre par langue, raison pour laquelle `url` est également multilingue.



### Classe: MultilingualString []{#MultilingualString}


_Une chaîne de caractères pouvant contenir du texte en plusieurs langues._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| text | 1 <br/> String | Contenu textuel de l'élément.  |
| language | 1 <br/> String | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |





#### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | url | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | name | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | url | range | [MultilingualString](#MultilingualString) |
| IsAgendaItem | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| IsAgendaItem | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| IsAgendaItem | url | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | url | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | url | range | [MultilingualString](#MultilingualString) |
| [Voting](#Voting) | voting_title | range | [MultilingualString](#MultilingualString) |
| [IndividualAttendance](#IndividualAttendance) | reason | range | [MultilingualString](#MultilingualString) |
| [Media](#Media) | url | range | [MultilingualString](#MultilingualString) |



















</div>

## Classes mixin

Trois classes ne portent pas de données propres : elles regroupent des slots qui se présentent de la même manière dans de nombreuses classes — l'identification d'une entité, ses dates de création et de modification ainsi que le déroulement temporel d'un événement, avec un début et une fin planifiés et effectifs. Elles proviennent du schéma commun du groupe spécialisé (eCH-0292) et sont intégrées par les normes de celui-ci, afin que les mêmes indications portent partout le même nom et fonctionnent de la même façon.

Un mixin n'est pas une superclasse : aucune instance d'une classe mixin n'est créée et rien n'en apparaît dans les données. Les tableaux d'attributs des classes énumèrent donc individuellement les slots hérités et en signalent la provenance par la mention « Héritage » — les trois sections suivantes expliquent ce qui se cache derrière cette indication.



### Classe: HasIdentification []{#HasIdentification}


_Une classe mixin qui fournit des slots pour l'identification d'une entité. Elle est utilisée pour les entités identifiées en propre ; leur `global_uri` constitue l'identifiant et est donc obligatoire._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Identifiant local. Par exemple, un UUID issu du système d'information du conseil.  |
| global_uri | 1 <br/> Uriorcurie | Une URI unique et globalement valide pour l'entité.  |
| wikidata_uri | 0..1 <br/> Uriorcurie | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans.  |



#### Utilisation de mixin

[Container](#Container), [Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [ProtocolItem](#ProtocolItem), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech), [TextSegment](#TextSegment), [Motion](#Motion), [Media](#Media)





















</div>



### Classe: HasCreationModificationDates []{#HasCreationModificationDates}


_Une classe mixin qui fournit des slots pour modéliser les dates de création et de modification d'une entité._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_created | 0..1 <br/> Date | La date à laquelle une entité a été créée.  |
| datetime_created | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été créée.  |
| date_modified | 0..1 <br/> Date | La date à laquelle une entité a été modifiée pour la dernière fois.  |
| datetime_modified | 0..1 <br/> Datetime | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois.  |



#### Utilisation de mixin

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [ProtocolItem](#ProtocolItem), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech)





















</div>



### Classe: IsEventWithDuration []{#IsEventWithDuration}


_Une classe mixin qui fournit des slots pour modéliser des événements ou occurrences avec une durée._




<div data-search-exclude markdown="1">




#### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_begin_actual | 0..1 <br/> Date | La date de début effective d'un événement ou d'une occurrence avec durée.  |
| datetime_begin_actual | 0..1 <br/> Datetime | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée.  |
| date_begin_planned | 0..1 <br/> Date | La date de début planifiée d'un événement ou d'une occurrence avec durée.  |
| datetime_begin_planned | 0..1 <br/> Datetime | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée.  |
| date_end_actual | 0..1 <br/> Date | La date de fin effective d'un événement ou d'une occurrence avec durée.  |
| datetime_end_actual | 0..1 <br/> Datetime | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée.  |
| date_end_planned | 0..1 <br/> Date | La date de fin planifiée d'un événement ou d'une occurrence avec durée.  |
| datetime_end_planned | 0..1 <br/> Datetime | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée.  |



#### Utilisation de mixin

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [ProtocolItem](#ProtocolItem)





















</div>

\newpage

# Droits d'auteur

Quiconque élabore des normes eCH en conserve la propriété intellectuelle. Elle ou il s'engage toutefois à mettre gratuitement, et pour autant que ce soit possible, la propriété intellectuelle en question ou ses droits à une propriété intellectuelle de tiers à la disposition des groupes de spécialistes respectifs ainsi qu'à l'Association eCH pour une utilisation et un développement sans restriction dans le cadre des buts de l'association.

Les normes élaborées par les groupes de spécialistes peuvent, moyennant mention du détenteur/de la détentrice des droits d'auteur eCH respectifs, être utilisées, développées et déployées gratuitement et sans restriction.

Les normes eCH sont complètement documentées et libres de toute restriction relevant du droit des brevets ou de droits de licence. La documentation correspondante peut être obtenue gratuitement.

Les présentes dispositions s'appliquent exclusivement aux normes élaborées par eCH, non aux normes ou produits de tiers auxquels il est fait référence dans les normes eCH. Les normes incluront les références appropriées aux droits de tiers.

\newpage

# Annexe A – Références et bibliographie

Lorsqu'une version est indiquée, il s'agit de celle sur la base de laquelle la présente norme a été élaborée.

## Normes du groupe spécialisé « Affaires politiques »

Les normes du groupe spécialisé sont élaborées conjointement et se renvoient les unes aux autres. Elles portent actuellement toutes le statut « In Arbeit » (en cours d'élaboration ; état au 10 août 2026) ; aucune version n'est donc indiquée.

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0292|eCH-0292 : Métaprocessus relatifs aux affaires politiques – éléments de données communs, dont la présente norme tire les classes de référence et les mixins : [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0294|eCH-0294 : Acteurs politiques – définit les personnes et les groupes auxquels renvoient `PersonReference` et `GroupReference` : [https://www.ech.ch/de/ech/ech-0294](https://www.ech.ch/de/ech/ech-0294)|
|eCH-0295|eCH-0295 : Affaires parlementaires – les affaires traitées dans les points de l'ordre du jour, les votes et les interventions : [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0296|eCH-0296 : Actes législatifs et textes de loi : [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|eCH-0297|eCH-0297 : Consultations publiques : [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Listes de codes et autres sources

| | |
|------------------|----------------------------------------------------------------------------------|
|ISO 639-1|ISO (International Organization for Standardization). Codes de langue, utilisés dans le slot `language` de `MultilingualString`.|
|Dublin Core|DCMI Metadata Terms. Source de plusieurs attributions de `slot_uri` (préfixe `dcterms`) : [https://www.dublincore.org/specifications/dublin-core/dcmi-terms/](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)|
|LinkML|Langage de modélisation dans lequel la présente norme est définie : [https://linkml.io](https://linkml.io)|

