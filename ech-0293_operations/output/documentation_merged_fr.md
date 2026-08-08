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

# Remarque

Le présent document recourt à une formulation épicène pour les désignations de personnes. Il se fonde sur les [directives](https://www.bk.admin.ch/bk/de/home/dokumentation/sprachen/hilfsmittel-textredaktion/leitfaden-zum-geschlechtergerechten-formulieren.html) de la Chancellerie fédérale. Selon les situations, on utilise des doublets (les citoyennes et les citoyens), des formes abstraites du point de vue du genre (la personne assurée), des formes neutres ou des paraphrases sans référence à des personnes. Le masculin générique n'est pas admis. Les formes complètes sont utilisées dans les textes suivis ; dans les passages abrégés, notamment dans les tableaux, les formes courtes sont admises. Les astérisques de genre et les graphies analogues ne sont pas utilisés.

\newpage

# Introduction

## Contexte : fonctionnement public des conseils

Aux niveaux fédéral, cantonal et communal, des conseils et des assemblées siègent, délibèrent sur des affaires politiques, prennent des décisions et contrôlent l'exécutif.

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

## Délimitation par rapport au groupe spécialisé « Droits politiques »

Outre le groupe spécialisé « Affaires politiques », l'association eCH compte le groupe spécialisé « Droits politiques ». Tous deux concernent le domaine politique, mais couvrent des domaines différents :

- **Affaires politiques** (la présente famille de normes) décrit le processus de formation de la volonté et de décision parlementaire et administratif : les acteurs (eCH-0294), le fonctionnement des conseils (eCH-0293), les affaires parlementaires (eCH-0295), les actes législatifs qui en découlent (eCH-0296) ainsi que les consultations en amont (eCH-0297).
- **Droits politiques** traite de l'exercice des droits politiques par les personnes ayant le droit de vote : registres des électeurs et des candidats, déroulement des votations et élections populaires, vote électronique (eVoting), cartes de vote ainsi que résultats des votations et des élections (notamment eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

Cette délimitation est particulièrement importante pour eCH-0293, puisque la norme modélise des votes et des élections. Ce qui est déterminant n'est pas de savoir qui a le droit de vote, mais **où la décision est prise** – dans l'assemblée réunie ou aux urnes :

- **Dans l'assemblée** – la présente norme : les votes et élections auxquels procède un organe siégeant dans le cadre d'une séance dotée d'un ordre du jour. En font partie les votes nominatifs et les votes finaux au parlement, tout comme l'élection de membres des autorités, de juges ou de présidences de commission par le conseil. Cela est consigné au moyen de `Voting`, `IndividualVote` et `Election`.
- **Aux urnes** – groupe spécialisé « Droits politiques » : les votations et élections populaires ainsi que les registres électoraux, le déroulement, les cartes de vote et les résultats. Ces éléments ne sont pas modélisés ici.

Se situent délibérément du côté de la présente norme les **Landsgemeinden et les assemblées communales** (`meeting_type: sitting`). Il s'agit certes d'assemblées des personnes ayant le droit de vote elles-mêmes, mais elles décident en tant qu'organe siégeant, avec ordre du jour, prises de parole et décisions – et sont donc représentées comme une séance de conseil.

Un second point de contact concerne les personnes élues : dans les résultats électoraux du groupe spécialisé « Droits politiques » figurent les candidats et les personnes élues. Dès qu'une personne exerce un mandat, elle est répertoriée dans eCH-0294 en tant qu'actrice ou acteur politique, avec ses rôles et ses affiliations – eCH-0293 la référence depuis là au moyen d'`actor_id`.

\newpage

<!-- ToDo: Christian -->

# Organisation temporelle de l'activité des conseils

L'activité parlementaire est organisée dans le temps à trois niveaux : les législatures constituent le cadre à long terme, les sessions structurent le travail au sein d'une législature, et les séances sont les rencontres concrètes au cours desquelles les affaires sont délibérées. Cette hiérarchie permet à la fois une planification à long terme et une adaptation souple aux besoins du moment.

## Legislature (législature)

### Notion et signification

Une législature désigne la période pour laquelle un parlement est élu et durant laquelle il exerce ses fonctions dans sa composition actuelle. Elle constitue l'unité temporelle la plus élevée de l'activité parlementaire et délimite le cadre du travail législatif d'un parlement.

En Suisse, la durée des législatures varie selon le niveau fédéral :

- **Niveau fédéral** : 4 ans (Conseil national et Conseil des États)
- **Cantons** : le plus souvent 4 ans, dans certains cantons 5 ans
- **Communes** : variable, souvent 4 ans

### Structure et hiérarchie

La législature se situe hiérarchiquement au-dessus des sessions et des séances :

```
Legislature (législature)
  └─ Sessions (p. ex. session de printemps, session d'automne)
      └─ Meetings (séances individuelles)
          └─ Agenda Items (points de l'ordre du jour)
```

### Contexte parlementaire

Chaque législature est rattachée à un organe parlementaire déterminé, identifié par :

- **actor_id** : renvoi au parlement en tant qu'acteur politique (p. ex. Conseil national, Grand Conseil) selon eCH-0294 Actors
- **administrative_id** : identifiant administratif du corps législatif (p. ex. commune, canton, pays)

### Situation temporelle

Une législature est caractérisée au moyen du mixin `IsEventWithDuration`. Les principaux champs de date sont :

- **date_begin_planned** / **date_begin_actual** : début planifié, respectivement effectif, de la législature (généralement après les élections)
- **date_end_planned** / **date_end_actual** : fin planifiée, respectivement effective, de la législature (avant les élections suivantes)

Au besoin, il existe des variantes analogues `datetime_*` avec indication de l'heure.

Exemple au niveau fédéral : la 51e législature du Parlement suisse a duré du 5 décembre 2019 au 4 décembre 2023.

### Identification

Le mixin `HasIdentification` met à disposition `local_id`, `global_uri` et `wikidata_uri`. Le `global_uri` est obligatoire et sert d'identifiant univoque.

### Documents liés

Le slot **documents** permet de lier des documents pertinents (p. ex. listes des membres de la législature, répertoires des affaires) sous forme de FRBR Works.



## Classe: Legislature 


_Durée du mandat d'un parlement en tant qu'assemblée législative. Elle est en règle générale de quatre ans._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| administrative_id | 0..1 <br/> [String](#String) | Identifiant administratif du corps législatif, p. ex. commune, canton ou pays.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Désignation complète multilingue.  |
| description | 0..1 <br/> [String](#String) | Texte descriptif de l'élément.  |
| landing_page | 0..1 <br/> [String](#String) | URL fournissant des informations complémentaires.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [legislatures](#legislatures) | range | [Legislature](#Legislature) |



















</div>

## Session (période de session)

### Notion et signification

Une session désigne une période de séances continue d'un parlement, au cours de laquelle plusieurs séances ont lieu. Elle constitue l'unité temporelle intermédiaire entre la législature et les séances individuelles.

### Distinction : session et séance

Cette distinction est importante pour comprendre la norme :

- **Session** : une période de séances qui s'étend typiquement sur plusieurs jours ou semaines
- **Meeting** : une séance individuelle au sein d'une session

#### Exemple au niveau fédéral
```
Legislature (51e législature)
  └─ Session (session de printemps 2024)
      ├─ Meeting (séance du Conseil national du 4 mars 2024)
      ├─ Meeting (séance du Conseil des États du 4 mars 2024)
      ├─ Meeting (séance du Conseil national du 5 mars 2024)
      └─ ...
```

### Rattachement aux organes

Une session se rapporte à l'organe politique qui organise les sessions comme suite de séances. Exemples :

- **Parlement** : sessions d'un Grand Conseil ou de l'Assemblée fédérale
- **Commissions** : périodes de séances des commissions parlementaires
- **Organes communs** : p. ex. sessions de l'Assemblée fédérale (Chambres réunies)

Le champ **body_key** permet de consigner l'organe (p. ex. « NR » pour le Conseil national, « SR » pour le Conseil des États) sous forme de clé. Le champ **parent_legislature** rattache la session à la législature correspondante.

### Identification et numérotation

Les sessions sont habituellement numérotées. Les slots suivants sont disponibles — ils sont compatibles avec la modélisation correspondante de Meeting :

- **number** : numéro courant (p. ex. au sein de la législature ou de l'année)
- **sequential_number** : numéro courant sous forme de chaîne (chiffres romains également possibles)
- **position** : position sous forme de nombre entier
- **abbreviation** : désignation abrégée (p. ex. « FS24 » pour la session de printemps 2024)
- **name** : désignation complète multilingue

Le mixin `HasIdentification` met en outre à disposition `local_id`, `global_uri` et `wikidata_uri`.

### Attributs temporels

Les sessions utilisent le mixin `IsEventWithDuration` et offrent ainsi les mêmes champs de date que les législatures et les séances :

- **date_begin_planned** / **datetime_begin_planned** : début planifié de la session
- **date_begin_actual** / **datetime_begin_actual** : début effectif
- **date_end_planned** / **datetime_end_planned** : fin planifiée de la session
- **date_end_actual** / **datetime_end_actual** : fin effective

### Liens

- **meetings** : liste des séances au sein de la session
- **documents** : FRBR Works liés (p. ex. programme de session, aperçu de la session)
- **url** : page d'accueil de la session

### Souplesse de la norme

La norme est délibérément souple afin de refléter différentes formes d'organisation. Les entités fédérées sans sessions formelles peuvent utiliser cette entité de manière facultative ou renvoyer directement aux séances.



## Classe: Session 


_Une session parlementaire qui regroupe plusieurs séances et s'étend sur une période déterminée._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| body_key | 0..1 <br/> [String](#String) | Clé identifiant l'organe politique ou la collectivité (p. ex. BE pour Berne, CHE pour la Suisse).  |
| name | * <br/> [MultilingualString](#MultilingualString) | Désignation complète multilingue.  |
| number | 0..1 <br/> [String](#String) | Numéro courant, p. ex. au sein de la législature, de la session ou de l'année.  |
| sequential_number | 0..1 <br/> [Integer](#Integer) | Numéro séquentiel de la séance, utilisé pour le tri.  |
| position | 0..1 <br/> [String](#String) | Position (nombre entier) au sein de la séquence supérieure.  |
| meeting_abbreviation | 0..1 <br/> [String](#String) | Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour la session de printemps 2024).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| parent_legislature | 0..1 <br/> [String](#String) | La législature dans le cadre de laquelle la séance a lieu.  |
| meetings | * <br/> [Meeting](#Meeting) | Ensemble des séances.  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [sessions](#sessions) | range | [Session](#Session) |














### Exemples
#### Exemple : Session fédérale avec désignation trilingue

```yaml
global_uri: ops:session_5207
body_key: CHE
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
#### Exemple : Landsgemeinde comme période de séance

```yaml
global_uri: ops:session_gl_landsgemeinde_2025_05_04
body_key: GL
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
#### Exemple : Session cantonale avec désignation bilingue

```yaml
global_uri: ops:session_be_summer_2025
body_key: BE
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
#### Exemple : Période de séance d'un jour d'un Grand Conseil

```yaml
global_uri: ops:session_gl_landrat_2025_02_26
body_key: GL
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






</div>

## Meeting (séance individuelle)

### Notion et signification

Un Meeting désigne une séance individuelle d'un organe parlementaire. Il s'agit de la manifestation concrète au cours de laquelle les membres d'un parlement, d'une commission ou d'un autre organe se réunissent pour délibérer d'affaires et prendre des décisions.

### Types de séances

La norme distingue différents types de séances au moyen du champ **meeting_type** (énumération `MeetingTypeEnum`) :

#### session
Séances plénières de l'ensemble du parlement ou d'une chambre

**Exemples :**
- Séance du Conseil national durant la session d'automne
- Séance du Grand Conseil
- Séance de l'Assemblée fédérale (Chambres réunies)

#### committee
Séances des commissions parlementaires

**Exemples :**
- Séance de la Commission de l'économie et des redevances (CER)
- Commission de gestion (CdG)
- Commission de politique extérieure (CPE)

#### sitting
Formes de séance particulières

**Exemples :**
- Landsgemeinden (dans les cantons de Glaris et d'Appenzell Rhodes-Intérieures)
- Assemblées bourgeoisiales
- Assemblées communales

#### various
Autres formes de séance n'entrant pas dans les catégories ci-dessus

### Hiérarchie et structure

Un Meeting fait partie d'une session (lorsque celle-ci est utilisée) et contient plusieurs Agenda Items (points de l'ordre du jour) :

```
Session (session de printemps 2024)
  └─ Meeting (séance du Conseil national, 4 mars 2024, 08h00)
      ├─ AgendaItem (point 1 : salutations)
      ├─ AgendaItem (point 2 : délibération législative)
      └─ AgendaItem (point 3 : votes)
```

### Planification temporelle et réalité

Au moyen du mixin `IsEventWithDuration`, le Meeting distingue les moments planifiés des moments effectifs :

#### Dates planifiées
- **date_begin_planned** / **datetime_begin_planned** : début planifié
- **date_end_planned** / **datetime_end_planned** : fin planifiée

#### Dates effectives
- **date_begin_actual** / **datetime_begin_actual** : début effectif
- **date_end_actual** / **datetime_end_actual** : fin effective

Cette distinction est importante, car :
- les séances peuvent prendre du retard
- les points de l'ordre du jour peuvent être avancés ou reportés
- les séances peuvent se terminer plus tôt que prévu

**Cas d'application :** une séance planifiée pour 14h00 ne commence, en raison de retards, qu'à 14h25 et se termine à 17h30 au lieu de 18h00.

### État de la séance

Le champ **state** (énumération `StateEnum`) saisit l'état actuel d'un Meeting :

- **planned** : la séance est planifiée et se tiendra comme prévu
- **canceled** : la séance a été annulée
- **postponed** : la séance a été reportée

Le champ **state_name** permet d'ajouter une description d'état divergente, en texte libre.

Cet état est important pour :
- l'information actuelle des membres du parlement et du public
- la traçabilité historique des changements de planification
- les notifications automatiques en cas de modification

### Identification et numérotation

Les séances sont identifiées par :

- **local_id** / **global_uri** / **wikidata_uri** (via le mixin `HasIdentification`)
- **number** : numéro courant (p. ex. « 5 » pour la 5e séance d'une session)
- **sequential_number** : numéro courant sous forme de chaîne (chiffres romains également possibles)
- **position** : position sous forme de nombre entier au sein de la session
- **abbreviation** : désignation abrégée (p. ex. « NR-24-05 »)
- **name** : désignation complète multilingue

### Lieu de la séance

Le champ **location** saisit le lieu de la séance :

- Lieu physique : « Palais fédéral, salle du Conseil national »
- Séances virtuelles : « Visioconférence via [plateforme] »
- Formats hybrides : « Palais fédéral et visioconférence »

### Rattachement aux organes

L'organe compétent est référencé au moyen d'**actor_id** (selon eCH-0294 Actors). Le champ **actor_name** permet en outre de consigner le nom de l'organe pour un accès rapide, **body_key** une clé courte (p. ex. « NR », « SR »). Le champ **administrative_id** permet d'indiquer le niveau administratif ; **group_name** et **group_id** complètent les regroupements lorsque cela est nécessaire.

- Séances plénières : renvoi à l'ensemble du parlement
- Séances de commission : renvoi à la commission concernée
- Séances communes : renvoi à l'organe commun

### Liens hiérarchiques

- **parent_meeting** : lorsqu'une séance fait partie d'une séance de rang supérieur
- **parent_legislature** : la législature dans le cadre de laquelle la séance a lieu

### Relations avec d'autres entités

Un Meeting relie différents éléments de l'activité parlementaire :

- **Agenda Items** : les points traités
- **Votings** : les votes durant la séance
- **Elections** : les élections durant la séance
- **Speeches** : les interventions et prises de parole
- **Attendance** : les listes de présence (via `Attendance.parent_meeting`)
- **documents** : FRBR Works liés (procès-verbaux, documents de séance, bulletin officiel, etc.)



## Classe: Meeting 


_Une classe générale de séance utilisée pour les sessions, les séances de commission, les séances individuelles d'une session et d'autres réunions diverses._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| body_key | 0..1 <br/> [String](#String) | Clé identifiant l'organe politique ou la collectivité (p. ex. BE pour Berne, CHE pour la Suisse).  |
| meeting_type | 0..1 <br/> [MeetingTypeEnum](#MeetingTypeEnum) | Type de séance, p. ex. session, commission, séance de session, divers.  |
| administrative_id | 0..1 <br/> [String](#String) | Identifiant administratif du corps législatif, p. ex. commune, canton ou pays.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Désignation complète multilingue.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| group_name | 0..1 <br/> [String](#String) | Nom du groupe ou de l'organe.  |
| group_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence au groupe ou à l'organe (instantané au moment de la mise en relation).  |
| number | 0..1 <br/> [String](#String) | Numéro courant, p. ex. au sein de la législature, de la session ou de l'année.  |
| landing_page | 0..1 <br/> [String](#String) | URL fournissant des informations complémentaires.  |
| sequential_number | 0..1 <br/> [Integer](#Integer) | Numéro séquentiel de la séance, utilisé pour le tri.  |
| position | 0..1 <br/> [String](#String) | Position (nombre entier) au sein de la séquence supérieure.  |
| meeting_abbreviation | 0..1 <br/> [String](#String) | Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour la session de printemps 2024).  |
| actor_name | 0..1 <br/> [String](#String) | Nom de l'organe politique (p. ex. Conseil national).  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| state | 0..1 <br/> [StateEnum](#StateEnum) | État actuel de la séance (planifiée, annulée, reportée).  |
| state_name | 0..1 <br/> [String](#String) | Description personnalisée de l'état de la séance.  |
| description | 0..1 <br/> [String](#String) | Texte descriptif de l'élément.  |
| location | 0..1 <br/> [String](#String) | Lieu où se tient la séance (salle physique, visioconférence ou format hybride).  |
| parent_meeting | 0..1 <br/> [String](#String) | Identifiant de la séance liée qui regroupe la séance courante.  |
| parent_legislature | 0..1 <br/> [String](#String) | La législature dans le cadre de laquelle la séance a lieu.  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| protocol_ref | 0..1 <br/> [Protocol](#Protocol) | Le procès-verbal de cette séance, établi après celle-ci.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [meetings](#meetings) | range | [Meeting](#Meeting) |
| [Session](#Session) | [meetings](#meetings) | range | [Meeting](#Meeting) |














### Exemples
#### Exemple : Séance du Conseil des États avec procès-verbal et interventions

```yaml
global_uri: parl:sr_winter25_sitzung_6
body_key: CHE
meeting_type: session
name:
- text: Sechste Sitzung
  language: de
- text: Sixième séance
  language: fr
url:
- text: https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin
  language: de
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/42
  label: Ständerat
  abbreviation:
  - value: SR
    language: de
actor_name: Ständerat
datetime_begin_planned: '2025-12-19T08:15:00+01:00'
datetime_created: '2026-01-12T00:00:00+01:00'
datetime_modified: '2026-01-12T00:00:00+01:00'

```
#### Exemple : Séance de Grand Conseil avec points de l'ordre du jour et votes

```yaml
global_uri: ops:meeting_sg_2025_03_15
body_key: SG
meeting_type: session
name:
- text: Kantonsratssitzung vom 15. März 2025
  language: de
url:
- text: https://www.ratsinfo.sg.ch/sessions/2025-03-15
  language: de
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/265
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
parent_legislature: ops:legislature_sg_2024_2028
datetime_created: '2025-02-01T10:00:00Z'
datetime_modified: '2025-03-15T17:30:00Z'

```
#### Exemple : Séance d'une demi-journée au sein d'une session

```yaml
body_key: BE
global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
meeting_type: session
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
  global_uri: https://api.openparldata.ch/v1/bodies/253
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
#### Exemple : Séance de commission avec liste de présence

```yaml
global_uri: ops:meeting_be_committee_wak_2025_05_12
body_key: BE
meeting_type: committee
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

```
#### Exemple : Séance du gouvernement avec désignation bilingue

```yaml
body_key: BE
global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
meeting_type: session
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
#### Exemple : Landsgemeinde comme type de séance « sitting »

```yaml
global_uri: ops:meeting_gl_landsgemeinde_2025
body_key: GL
meeting_type: sitting
name:
- text: Landsgemeinde 2025
  language: de
url:
- text: https://www.landsgemeinde.gl.ch/2025
  language: de
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/258
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
parent_legislature: ops:legislature_gl_2024_2028
datetime_created: '2025-01-10T12:00:00Z'
datetime_modified: '2025-05-04T13:45:00Z'

```






</div>

## Enum: MeetingTypeEnum 




_Type de séance._




<div data-search-exclude markdown="1">

URI: [ops:MeetingTypeEnum](https://ch.paf.link/schema/operations/MeetingTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| session |  Séance plénière de l'ensemble du parlement ou d'une chambre.  |
| | [ops:enum/meeting_type/session](ops:enum/meeting_type/session) |
| committee |  Séance d'une commission parlementaire.  |
| | [ops:enum/meeting_type/committee](ops:enum/meeting_type/committee) |
| sitting |  Formes particulières d'assemblée (p. ex. Landsgemeinde, assemblée communale).  |
| | [ops:enum/meeting_type/sitting](ops:enum/meeting_type/sitting) |
| various |  Autres formes de séance non couvertes par les catégories ci-dessus.  |
| | [ops:enum/meeting_type/various](ops:enum/meeting_type/various) |







</div>

## Enum: StateEnum 




_État de la séance._




<div data-search-exclude markdown="1">

URI: [ops:StateEnum](https://ch.paf.link/schema/operations/StateEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| planned |  La séance est planifiée et se tiendra comme prévu.  |
| | [ops:enum/state/planned](ops:enum/state/planned) |
| canceled |  La séance a été annulée.  |
| | [ops:enum/state/canceled](ops:enum/state/canceled) |
| postponed |  La séance a été reportée.  |
| | [ops:enum/state/postponed](ops:enum/state/postponed) |







</div>

# Présence et interventions

Outre les décisions formelles, la norme documente également la participation aux séances et les débats menés. Les listes de présence consignent qui a participé à une séance, tandis que les interventions retiennent le débat parlementaire au moyen d'enregistrements textuels et médiatiques.

## Attendance (présence)

## Notion et signification

L'Attendance (présence) saisit quels membres d'un organe parlementaire étaient présents, absents ou excusés lors d'une séance. Elle sert à documenter la participation et constitue la condition du quorum.

## Structure à deux niveaux

La norme distingue deux niveaux de saisie de la présence :

### 1. Attendance (niveau agrégé)
Récapitulation de la présence pour une séance :
- Nombre total de personnes présentes
- Nombre total de personnes absentes (excusées / non excusées)
- Quorum

### 2. IndividualAttendance (niveau individuel)
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

### Rattachement à la séance et à l'organe

- **parent_meeting** : renvoi à la séance à laquelle se rapporte la liste de présence
- **actor_id** : renvoi à l'organe (parlement, commission) selon eCH-0294 Actors
- **datetime_begin** : moment de la constatation de la présence

### Chiffres agrégés

- **total_count** : nombre total de membres de l'organe (valeur de référence pour le calcul du quorum, p. ex. 200 pour le Conseil national, 46 pour le Conseil des États)
- **total_present** : nombre de membres présents
- **total_excused** : nombre de membres excusés
- **total_absent** : nombre de membres absents non excusés

**Exemple :**
- Total : 200
- Présents : 185
- Excusés : 12
- Absents : 3

### Quorum

Le quorum résulte du rapport entre `total_present` et `total_count` ainsi que des règles de quorum propres à l'organe. Il n'est donc pas enregistré comme champ distinct, mais calculé au besoin à partir des données.

## IndividualAttendance (niveau individuel)

### Lien

- **parent_attendance** : renvoi à l'agrégat `Attendance` de rang supérieur (lui-même rattaché à la séance). La saisie individuelle est ainsi proprement rattachée à la séance.
- **actor_id** : renvoi à la personne selon eCH-0294 Actors

### Type de présence

Le champ **attendance_type** (énumération `AttendanceTypeEnum`) saisit le type de présence :

- **present** : présent en personne
- **remote** : présent à distance (p. ex. visioconférence)
- **substitute** : suppléance — une autre personne a participé en remplacement

> La modélisation de la suppléance (p. ex. qui a remplacé qui, avec quel droit de vote) est approfondie dans l'[issue #24](https://github.com/swiss/political-affairs-ech-group/issues/24).
>
> Un deuxième axe d'état `present` / `excused` / `absent` (« si présent ») parallèle à l'axe existant « comment présent » est en discussion comme extension.

### Motif

Le champ **reason** (multilingue) permet de saisir en texte libre le motif d'une absence ou d'un retard.

## Différence : Attendance et IndividualVote

Distinction importante :

| Aspect | Attendance | IndividualVote |
|--------|------------|----------------|
| Saisit | Présence à la séance | Expression de la voix lors d'un vote |
| Moment | Début / durant la séance | Moment du vote |
| Granularité | Par séance | Par vote |

**Exemple :** une personne peut être présente à la séance (Attendance : present), mais être enregistrée comme absente lors d'un vote déterminé (IndividualVote : absent), parce qu'elle a brièvement quitté la salle à ce moment-là.

## Utilisations

Les entités Attendance permettent :

1. **Documentation** : saisie traçable de la participation
2. **Vérification du quorum** : garantie de la capacité de décision
3. **Transparence** : information publique sur la présence
4. **Reddition de comptes** : contrôle de l'exécution des obligations
5. **Statistiques** : évaluation des taux de présence
6. **Administration** : calcul des indemnités et des frais



## Classe: Attendance 


_Liste de présence agrégée pour une séance (nombre de membres présents, absents, excusés)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](#String) | Identifiant de la séance liée qui regroupe la séance courante.  |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles la séance ou le vote commence.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| total_count | 0..1 <br/> [Integer](#Integer) | Nombre total de membres de l'organe (valeur de référence pour le calcul du quorum).  |
| total_present | 0..1 <br/> [Integer](#Integer) | Nombre total de membres présents.  |
| total_absent | 0..1 <br/> [Integer](#Integer) | Nombre total de membres absents. La distinction entre absent et absent excusé se fait dans la liste de présence.  |
| total_excused | 0..1 <br/> [Integer](#Integer) | Nombre total d'absences excusées.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [attendances](#attendances) | range | [Attendance](#Attendance) |
| [IndividualAttendance](#IndividualAttendance) | [parent_attendance](#parent_attendance) | range | [Attendance](#Attendance) |



















</div>



## Classe: IndividualAttendance 


_Constatation individuelle de la présence d'une personne à une séance (rattachée à l'agrégat Attendance parent)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| parent_attendance | 0..1 <br/> [Attendance](#Attendance) | L'agrégat Attendance auquel appartient cette constatation individuelle de présence.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Référence à la personne agissante (instantané au moment de la mise en relation).  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](#AttendanceTypeEnum) | Type de présence individuelle.  |
| reason | * <br/> [MultilingualString](#MultilingualString) | Motif de l'absence ou du retard (texte libre, multilingue).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [individual_attendances](#individual_attendances) | range | [IndividualAttendance](#IndividualAttendance) |



















</div>

## Enum: AttendanceTypeEnum 




_Type de présence individuelle._




<div data-search-exclude markdown="1">

URI: [ops:AttendanceTypeEnum](https://ch.paf.link/schema/operations/AttendanceTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| remote |  Participation à distance  |
| | [ops:enum/attendance_type/remote](ops:enum/attendance_type/remote) |
| substitute |  Suppléance  |
| | [ops:enum/attendance_type/substitute](ops:enum/attendance_type/substitute) |
| present |  Présent en personne  |
| | [ops:enum/attendance_type/present](ops:enum/attendance_type/present) |







</div>

\newpage

<!-- ToDo: Michel -->

# Ordre du jour, procès-verbal et décisions

L'ordre du jour d'une séance est structuré par des points de l'ordre du jour. Ces points valent comme planification d'une séance et ne sont plus modifiés dans les données une fois la séance ouverte. Les mêmes éléments de données sont ensuite utilisés pour consigner le procès-verbal et les décisions qu'il contient.

Si des modifications de l'ordre du jour interviennent durant une séance, elles sont consignées au procès-verbal, et l'ordre du jour de la séance suivante est adapté en conséquence.

## AgendaItem (point de l'ordre du jour)

### But de l'entité

AgendaItem structure l'ordre du jour d'une séance et relie l'organisation temporelle (Meeting) aux affaires de fond (Affairs selon eCH-0295). C'est l'entité centrale pour représenter le déroulement d'une séance.

### Hiérarchie et structure

Les Agenda Items peuvent être organisés hiérarchiquement afin de représenter la structure d'ordres du jour complexes :

```
Meeting (séance du 4 mars 2024)
  ├─ AgendaItem 1 : communications et salutations
  ├─ AgendaItem 2 : délibérations législatives
  │   ├─ AgendaItem 2.1 : loi sur l'énergie (discussion par article)
  │   ├─ AgendaItem 2.2 : loi sur l'énergie (vote final)
  │   └─ AgendaItem 2.3 : loi sur la santé (débat d'entrée en matière)
  └─ AgendaItem 3 : divers
```

La hiérarchie est représentée au moyen du champ **parent_agenda_item**, qui renvoie au point de l'ordre du jour de rang supérieur.

### Identification et numérotation

- **id** : identifiant univoque
- **number** : numéro du point à l'ordre du jour (p. ex. « 2.1 », « 3 »)
- **position** : ordre de tri (pour l'affichage)
- **title** : titre du point de l'ordre du jour

### Types d'Agenda Items

Le champ **agenda_item_type** distingue différents types :

- **item** : un point ordinaire avec délibération et, le cas échéant, vote
- **item_group** : un groupe de points (p. ex. « délibérations législatives »)
- **note** : entrées informatives sans vote (p. ex. « communications »)

### Relation avec les affaires parlementaires

Le champ **affairs** renvoie aux affaires parlementaires correspondantes selon eCH-0295. Un point de l'ordre du jour peut se rapporter à plusieurs affaires :

- **Affaire unique** : un point traite d'un projet déterminé
- **Plusieurs affaires** : un point regroupe des affaires connexes
- **Aucune affaire** : points administratifs (p. ex. « approbation du procès-verbal »)

**Exemple :** le point « Loi sur l'énergie — vote final » renvoie à l'affaire « 23.XXX Loi sur l'énergie » dans eCH-0295.

### Planification temporelle

- **date_time** : moment planifié du traitement
- **date_time_actual** : moment effectif du traitement

Cette distinction est importante, car :
- l'ordre du jour est fixé à l'avance
- le déroulement effectif peut s'en écarter
- des points peuvent être avancés, reportés ou ajournés

### Statut et résultat

#### Statut
Le champ **status** indique l'état d'avancement :
- « pending » : pas encore traité
- « in_progress » : actuellement en délibération
- « completed » : traitement achevé
- « postponed » : ajourné à une séance ultérieure
- « withdrawn » : retiré

#### Résultat
Le champ **result** saisit le résultat du traitement :
- « accepted » : accepté
- « rejected » : rejeté
- « referred » : renvoyé (p. ex. à la commission)
- « noted » : pris acte
- « no_decision » : aucune décision prise

### Catégorisation

Le champ **category** permet un regroupement selon des critères de fond :
- « Législation »
- « Budget et finances »
- « Interpellations et questions »
- « Élections »
- « Divers »

Cette catégorisation n'est pas normalisée et peut varier d'une entité fédérée à l'autre.

### Décisions relatives aux points de l'ordre du jour

Le champ **resolution** renvoie à la ou aux décisions prises sur ce point. Une décision documente le prononcé formel :

```
AgendaItem : « Loi sur l'énergie — vote final »
  └─ Resolution : « Acceptation de la loi sur l'énergie par 120 voix contre 75 et 5 abstentions »
      └─ Voting : détails du vote
```

### Description et URL

- **description** : description détaillée du point de l'ordre du jour
- **url** : tableau d'URL multilingues vers les documents de séance :
  - messages et rapports
  - propositions
  - propositions de modification
  - résultats des votes

### Particularités des différentes procédures

#### Procédure législative
Une affaire passe par plusieurs points de l'ordre du jour :
1. Débat d'entrée en matière
2. Discussion par article
3. Vote final
4. Le cas échéant, élimination des divergences entre les conseils

#### Interpellations et questions
- Dépôt comme point de l'ordre du jour
- Réponse du gouvernement
- Le cas échéant, discussion

#### Élections
- Proposition de candidature comme point de l'ordre du jour
- Déroulement de l'élection
- Proclamation du résultat

### Lien avec d'autres entités

Un AgendaItem est le maillon central entre :

- **Meeting** : la séance au cours de laquelle il est traité
- **Affairs** (eCH-0295) : les affaires de fond
- **Resolution** : la décision formelle
- **Voting** : le ou les votes relatifs au point
- **Speech** : les prises de parole et interventions relatives au point

### Exemples d'application

...

### Utilisations

1. Structuration du déroulement de la séance et de l'ordre du jour
2. Lien entre les Meetings et les Affairs (eCH-0295)
3. Documentation du statut et du résultat par point de l'ordre du jour
4. Base pour les procès-verbaux de séance et les publications



## Classe: AgendaItem 


_Un point de l'ordre du jour d'une séance._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](#String) | Identifiant de la séance liée qui regroupe la séance courante.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points.  |
| agenda_item_number | 0..1 <br/> [String](#String) | Numéro d'ordre du point de l'ordre du jour (type chaîne, afin de permettre les chiffres romains).  |
| agenda_item_position | 0..1 <br/> [Integer](#Integer) | Position (nombre entier) du point de l'ordre du jour dans le déroulement de la séance.  |
| leading_actor_id | 0..1 <br/> [String](#String) | Le département responsable du point de l'ordre du jour.  |
| speaking_actor_id | 0..1 <br/> [String](#String) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour.  |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Titre du point de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](#String) | Le lien vers les affaires rattachées au point de l'ordre du jour.  |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Sous-titre ou description détaillée du point de l'ordre du jour.  |
| state_id | 0..1 <br/> [String](#String) | Identifiant d'état (renvoi à l'énumération des états ou à un état propre).  |
| state_name | 0..1 <br/> [String](#String) | Description personnalisée de l'état de la séance.  |
| landing_page | 0..1 <br/> [String](#String) | URL fournissant des informations complémentaires.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| agenda_item_category | 0..1 <br/> [String](#String) | Catégorie pour les points de l'ordre du jour regroupés (p. ex. introduction, par département, points techniques).  |
| parent_agenda_item | 0..1 <br/> [String](#String) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour.  |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | La décision prise sur ce point de l'ordre du jour.  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [agenda_items](#agenda_items) | range | [AgendaItem](#AgendaItem) |
| [JointDebate](#JointDebate) | [agenda_items](#agenda_items) | range | [AgendaItem](#AgendaItem) |














### Exemples
#### Exemple : Point de l'ordre du jour budgétaire

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
#### Exemple : Motion dans un groupe de points de l'ordre du jour

```yaml
global_uri: ops:16155798_3
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
#### Exemple : Point de l'ordre du jour d'une séance du Conseil des États

```yaml
global_uri: ops:69905
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
#### Exemple : Postulat, catégorie « voting »

```yaml
global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
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
#### Exemple : Interpellation d'un groupe parlementaire

```yaml
global_uri: ops:cea750a5bd7b420fa4da1c914f801384
parent_meeting: ops:meeting_bern_2022_03_17
agenda_item_type: item
datetime_begin_planned: '2022-03-17T17:00:00Z'
agenda_item_position: 29
agenda_item_number: '8'
agenda_item_title:
- text: >-
    Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche Konsequenzen haben
    die Klimaziele für das Gasnetz in Bern?
  language: de
affair_id: affairs:2020.SR.000007
url:
- text: >-
    https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
  language: de
datetime_created: '2025-01-17T21:25:52Z'
datetime_modified: '2025-01-17T21:25:52Z'

```
#### Exemple : Pétition comme point de l'ordre du jour

```yaml
global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
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
#### Exemple : Révision partielle de plusieurs ordonnances, en français

```yaml
global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
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
#### Exemple : Affaire matérielle sans catégorie de point

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
#### Exemple : Discussion par article d'une loi

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
#### Exemple : Interpellation comme point de l'ordre du jour

```yaml
global_uri: ops:06fb582b753c416d8fdb05fa13873545
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
#### Exemple : Affaire matérielle issue d'un système d'information parlementaire cantonal

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
#### Exemple : Point de l'ordre du jour avec vote final

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
#### Exemple : Motion populaire dans un groupe de points de l'ordre du jour

```yaml
global_uri: ops:16155798_4
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
#### Exemple : Point de l'ordre du jour en français (postulat)

```yaml
global_uri: ops:2023_10_03-52
parent_meeting: ops:meeting_lausanne_2023_10_03
agenda_item_type: item
datetime_begin_planned: '2023-10-03T00:00:00Z'
agenda_item_position: 52
agenda_item_number: '52'
agenda_item_title:
- text: >-
    Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale » (FIM)
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
#### Exemple : Postulat avec vote

```yaml
global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
parent_meeting: ops:meeting_luzern_2025_01_28_b
agenda_item_type: item
datetime_begin_planned: '2025-01-28T00:00:00Z'
agenda_item_position: 14
agenda_item_number: '14'
agenda_item_title:
- text: >-
    Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und Anpassung der
    Kriterien zum früheren Eintritt von Kindern in die Basisstufe (den freiwilligen
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
#### Exemple : Interpellation urgente, en français

```yaml
global_uri: ops:2025_05_20-23
parent_meeting: ops:meeting_lausanne_2025_05_20
agenda_item_type: item
datetime_begin_planned: '2025-05-20T00:00:00Z'
agenda_item_position: 23
agenda_item_number: '23'
agenda_item_title:
- text: >-
    Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation urgente
    de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en faveur du respect
    du droit international et de la protection des populations civiles à Gaza »
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

## Enum: AgendaItemTypeEnum 




_Type de point de l'ordre du jour, distinguant les points isolés des points regroupés._




<div data-search-exclude markdown="1">

URI: [ops:AgendaItemTypeEnum](https://ch.paf.link/schema/operations/AgendaItemTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| item |  Point isolé de l'ordre du jour  |
| | [ops:enum/agenda_item_type/item](ops:enum/agenda_item_type/item) |
| group |  Groupe de points de l'ordre du jour  |
| | [ops:enum/agenda_item_type/group](ops:enum/agenda_item_type/group) |







</div>

## Procès-verbal (Protocol)

### But de l'entité

Alors que les points de l'ordre du jour représentent la **planification** d'une séance, le procès-verbal consigne le **déroulement effectif** après la séance. `Protocol` est un conteneur tenu exactement une fois par séance (`Meeting`) et qui regroupe les points effectivement traités (`protocol_items`), les votes, les interventions ainsi que les segments de texte in extenso et les documents.

```
Meeting
  ├─ agenda_items   (avant : points planifiés)
  └─ protocol_ref   (après : consignation)
        ├─ protocol_items  → ProtocolItem (comme AgendaItem)
        ├─ votings
        ├─ speeches
        ├─ text_segments
        └─ documents
```



## Classe: Protocol 


_Le procès-verbal établi après la séance. Un conteneur qui regroupe les points effectivement traités (protocol_items), les votes, les interventions, les segments de texte in extenso et les documents liés._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](#String) | Identifiant de la séance liée qui regroupe la séance courante.  |
| protocol_items | * <br/> [ProtocolItem](#ProtocolItem) | Points de l'ordre du jour tels qu'ils ont effectivement été consignés au procès-verbal.  |
| votings | * <br/> [Voting](#Voting) | Ensemble des votes.  |
| speeches | * <br/> [Speech](#Speech) | Ensemble des interventions.  |
| text_segments | * <br/> [TextSegment](#TextSegment) | Ensemble de segments de texte (p. ex. procès-verbal in extenso).  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [protocols](#protocols) | range | [Protocol](#Protocol) |
| [Meeting](#Meeting) | [protocol_ref](#protocol_ref) | range | [Protocol](#Protocol) |



















</div>

### ProtocolItem (point consigné au procès-verbal)

`ProtocolItem` hérite de tous les champs d'`AgendaItem` (`is_a: AgendaItem`) et représente un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-verbal.



## Classe: ProtocolItem 


_Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-verbal._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](#String) | Identifiant de la séance liée qui regroupe la séance courante. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| agenda_item_number | 0..1 <br/> [String](#String) | Numéro d'ordre du point de l'ordre du jour (type chaîne, afin de permettre les chiffres romains). <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| agenda_item_position | 0..1 <br/> [Integer](#Integer) | Position (nombre entier) du point de l'ordre du jour dans le déroulement de la séance. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| leading_actor_id | 0..1 <br/> [String](#String) | Le département responsable du point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| speaking_actor_id | 0..1 <br/> [String](#String) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Titre du point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| affair_id | 0..1 <br/> [String](#String) | Le lien vers les affaires rattachées au point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Sous-titre ou description détaillée du point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| state_id | 0..1 <br/> [String](#String) | Identifiant d'état (renvoi à l'énumération des états ou à un état propre). <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| state_name | 0..1 <br/> [String](#String) | Description personnalisée de l'état de la séance. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| landing_page | 0..1 <br/> [String](#String) | URL fournissant des informations complémentaires. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| agenda_item_category | 0..1 <br/> [String](#String) | Catégorie pour les points de l'ordre du jour regroupés (p. ex. introduction, par département, points techniques). <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| parent_agenda_item | 0..1 <br/> [String](#String) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | La décision prise sur ce point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité. <br/><br/>Héritage : [AgendaItem](#AgendaItem) |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | [protocol_items](#protocol_items) | range | [ProtocolItem](#ProtocolItem) |



















</div>

## Délibération commune (JointDebate)

### But de l'entité

`JointDebate` regroupe plusieurs points de l'ordre du jour délibérés conjointement — par exemple des affaires connexes traitées dans un seul et même débat.



## Classe: JointDebate 


_Points de l'ordre du jour traités conjointement._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Ensemble des points de l'ordre du jour.  |






















</div>

## Resolution (décision)

### But de l'entité

L'entité Resolution saisit la décision formelle relative à un point de l'ordre du jour. Elle documente **ce qui** a été décidé, tandis que Voting documente **comment** (selon quelle procédure et avec quel rapport de voix) la décision a été prise.

### Relation avec AgendaItem et Voting

```
AgendaItem (Loi sur l'énergie — vote final)
  ├─ Resolution (acceptation de la loi sur l'énergie)
  └─ Voting (120 oui, 75 non, 5 abstentions)
```

Un AgendaItem peut comporter plusieurs Resolutions (p. ex. en cas de plusieurs votes sur le même point). Chaque Resolution référence typiquement un Voting qui contient les détails du vote.

### Types de décisions

Le champ **resolution_type** utilise un vocabulaire contrôlé :

#### accepted
Le point de l'ordre du jour a été accepté

**Application :**
- Projets de loi acceptés
- Propositions approuvées
- Décisions prises

#### rejected
Le point de l'ordre du jour a été rejeté

**Application :**
- Projets de loi rejetés
- Propositions écartées
- Décisions de rejet

#### referred_back
Renvoi à un autre organe

**Application :**
- Renvoi à la commission pour remaniement
- Renvoi au gouvernement
- Retour à l'autre chambre (dans les systèmes bicaméraux)

#### noted
Pris acte

**Application :**
- Rapports sans vote
- Communications
- Points informatifs

#### postponed
Ajourné

**Application :**
- Report du traitement
- Pas encore mûr pour la décision
- Clarifications supplémentaires nécessaires

#### withdrawn
Retiré

**Application :**
- L'auteure ou l'auteur retire le projet
- L'affaire n'est pas poursuivie

#### amended
Accepté avec modifications

**Application :**
- Loi acceptée avec des amendements
- Version modifiée adoptée
- Solution de compromis

#### no_decision
Aucune décision prise

**Application :**
- Aucune majorité pour l'une ou l'autre proposition
- Situation d'égalité sans voix prépondérante
- Quorum non atteint

### Décision de conception : pourquoi une entité Resolution distincte ?

**L'alternative aurait été :** enregistrer le type de décision directement dans AgendaItem.

**Motifs en faveur d'une entité distincte :**

1. **Plusieurs décisions par point** : un point de l'ordre du jour peut donner lieu à plusieurs décisions (p. ex. d'abord une proposition de modification, puis le vote sur l'ensemble)

2. **Lien structuré avec les votes** : relation 1:1 claire entre Resolution et Voting

3. **Textes de décision multilingues** : une Resolution peut contenir des textes de décision détaillés en plusieurs langues

4. **Souplesse temporelle** : une Resolution peut être saisie séparément de l'AgendaItem dans le temps

### Texte de la décision

- **title** : résumé succinct de la décision
- **description** : texte détaillé de la décision

**Exemple :**
- title : « Acceptation de la loi sur l'énergie »
- description : « Le Conseil national accepte la loi fédérale sur le tournant énergétique dans la version de la commission par 120 voix contre 75 et 5 abstentions. »

### Lien avec le vote

Le champ **voting_id** renvoie au Voting correspondant, qui contient les détails du vote :

- Rapport de voix
- Procédure de vote
- Voix individuelles (en cas de vote nominatif)

**Toutes les Resolutions n'ont pas de Voting :**
- La « prise d'acte » intervient souvent sans vote formel
- Acceptations tacites
- Décisions administratives

### Horodatage

- **datetime_created** : moment de la décision
- **datetime_modified** : dernière modification (p. ex. en cas de corrections)

### URL et documentation

Le champ **url** peut renvoyer à des documents complémentaires :
- Textes de décision détaillés
- Motivations
- Bases légales

### Cas d'application dans différents contextes

#### Procédure législative
Plusieurs Resolutions correspondant à différentes phases :
1. Resolution « entrée en matière » (accepted/rejected)
2. Resolution sur l'article 1 (accepted/amended)
3. Resolution sur l'article 2 (accepted)
4. Resolution vote sur l'ensemble (accepted/rejected)

#### Élimination des divergences (système bicaméral)
- Resolution « adhésion à la version du premier conseil »
- Resolution « maintien de sa propre version »
- Resolution « acceptation de la proposition de compromis »

#### Travail en commission
- Resolution « renvoi à la commission avec mandat complémentaire »
- Resolution « adoption du rapport de commission »

### Considérations techniques

#### Granularité
La granularité de la saisie des Resolutions varie :
- **Détaillée** : chaque vote individuel donne lieu à sa propre Resolution
- **Agrégée** : seule la décision finale est saisie

La norme admet les deux approches.

#### Multilinguisme
Dans les parlements multilingues (CH, BE, etc.), les textes de décision doivent être saisis dans toutes les langues officielles. Cela se fait au moyen de tableaux MultilingualString dans title et description.

### Utilisations

1. **Documentation officielle** : qu'a-t-on décidé ?
2. **Force juridique** : preuve formelle de la décision
3. **Information du public** : résumé compréhensible de votes complexes
4. **Gestion des affaires** : suivi des décisions et de leur mise en œuvre
5. **Évaluation statistique** : taux d'acceptation et de rejet



## Classe: Resolution 


_Une décision prise sur un point de l'ordre du jour, y compris les procédures de vote._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](#ResolutionTypeEnum) | Type de décision prise sur le point de l'ordre du jour.  |
| type_label | 0..1 <br/> [String](#String) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| vote_procedures | * <br/> [String](#String) | Modalités du vote, p. ex. vote secret ou vote ouvert.  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [resolutions](#resolutions) | range | [Resolution](#Resolution) |
| [AgendaItem](#AgendaItem) | [has_resolution](#has_resolution) | range | [Resolution](#Resolution) |
| [ProtocolItem](#ProtocolItem) | [has_resolution](#has_resolution) | range | [Resolution](#Resolution) |



















</div>

## Enum: ResolutionTypeEnum 




_Type de décision prise sur un point de l'ordre du jour._




<div data-search-exclude markdown="1">

URI: [ops:ResolutionTypeEnum](https://ch.paf.link/schema/operations/ResolutionTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| accepted |  Acceptation  |
| | [ops:enum/resolution_type/accepted](ops:enum/resolution_type/accepted) |
| rejected |  Rejet  |
| | [ops:enum/resolution_type/rejected](ops:enum/resolution_type/rejected) |
| noted |  Prise d'acte  |
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

### But

Saisit les propositions déposées durant la séance (propositions de modification, propositions d'ordre, etc.).

### Structure

- **motion_type** : type de la proposition
  - **amendment** : proposition de modification d'un texte de loi
  - **procedural** : proposition d'ordre (p. ex. clôture du débat)
  - **referral** : proposition de renvoi
  - **other** : autres propositions
- **title** : titre court de la proposition
- **description** : texte complet de la proposition
- **proposer_person_id** : auteure ou auteur de la proposition
- **seconder_person_id** : cosignataires (si requis)
- **result** : résultat (accepted, rejected, withdrawn)

### Décision de conception

**Pourquoi une entité propre plutôt qu'une intégration dans AgendaItem ?**
- Un point de l'ordre du jour peut contenir plusieurs propositions
- Les propositions ont leur propre cycle de vie (déposée, soutenue, mise aux voix)
- Saisie structurée de l'auteure ou de l'auteur et des soutiens
- Votes distincts possibles pour chaque proposition

### Application

Liée à AgendaItem et, en option, à Voting :

```
AgendaItem (Loi sur l'énergie — art. 15)
  ├─ Motion (proposition de modification personne A)
  │   └─ Voting (vote sur la proposition de modification)
  ├─ Motion (proposition de modification personne B)
  │   └─ Voting (vote sur la proposition de modification)
  └─ Voting (vote sur l'article dans son ensemble)
```



## Classe: Motion 


_Une proposition formelle déposée au cours des délibérations._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| title | 0..1 <br/> [String](#String) | Titre de l'élément.  |
| description | 0..1 <br/> [String](#String) | Texte descriptif de l'élément.  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |






















</div>

\newpage

<!-- ToDo: Nicole -->

# Votes et élections

Les décisions parlementaires sont prises soit par des votes sur des questions matérielles, soit par des élections de personnes. La norme distingue clairement ces deux mécanismes et saisit en outre, dans les procédures ouvertes, le comportement de vote individuel de chaque membre du parlement. Les présidentes et présidents de parlement ne participent en principe pas aux votes ; ils ne votent que lors des élections. En cas d'égalité des voix lors d'un vote, ils départagent.

## Voting (vote)

## But de l'entité

« Voting » saisit le processus de vote et le résultat d'une décision formelle au parlement. L'entité documente aussi bien l'objet du vote (la question) que la procédure (comment il a été voté) et le résultat (avec quel rapport de voix).

## Types de votes

La norme distingue différents types de votes au moyen du champ **voting_type** :

### intermediate
Votes intermédiaires en cours de délibération.

**Exemples :**
- Vote sur l'entrée en matière relative à une affaire
- Vote sur une proposition
- Opposition de deux propositions qui s'excluent mutuellement ou qui portent sur le même passage de texte
- Vote éventuel lorsque plus de deux propositions portent sur le même objet
- Vote sur un article isolé d'une loi
- Vote sur l'ensemble après la première lecture d'un acte délibéré en deux lectures

### final
Le vote final portant sur l'ensemble du projet

**Exemples :**
- Vote final après la dernière lecture d'un acte
- Vote sur l'ensemble d'un arrêté
- Acceptation ou rejet d'un projet dans son ensemble
- Vote point par point sur une intervention

### casting
Voix prépondérante de la présidence en cas d'égalité des voix. La présidence ne participe pas aux votes, mais départage en cas d'égalité. En cas de vote secret, la proposition de l'organe qui a procédé à l'examen préalable est réputée acceptée en cas d'égalité des voix.

### secret
Expression secrète de la voix lors de votes et d'élections

**Application :**
- Élection de personnes
- Vote sur une affaire particulièrement délicate, telle qu'un recours en grâce ou la levée de l'immunité
- Vote après délibération à huis clos
- Vote secret sur proposition

## Structure d'un vote

Un vote est toujours rattaché à une phase de séance et/ou à une séance, à un point de l'ordre du jour (Agenda Item) et à une affaire avec son titre et son numéro. Il comprend le type de vote, l'objet du vote (la question), le résultat et — en cas de vote non secret — les voix individuelles des membres.
Il peut soit :

```
AgendaItem (15) affaire (Loi sur l'énergie — art. 15)
  └─ Voting (vote intermédiaire sur l'art. 15)
      ├─ IndividualVote (personne A : oui)
      ├─ IndividualVote (personne B : non)
      └─ IndividualVote (personne C : oui)
```


Exemple de sélection :
3 options : https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
5 options : https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=23f01ba9b3f3410cb9cfb85f32f3dfe0

## Procédures de vote

Le champ **procedure** décrit le mode de déroulement :

### Open procedures (votes ouverts)
- **show_of_hands** : à main levée (traditionnel)
- **standing** : par assis et levé (plus rare)
- **electronic** : vote électronique (fréquent aux niveaux fédéral et cantonal)
- **roll_call** : vote nominatif avec appel des noms
- **remote_voting** : expression de la voix à distance en situation de crise (des membres du conseil communiquent leur voix à la présidence du parlement avant le jour de séance. Les voix exprimées à distance sont saisies simultanément avec le vote en cours au conseil.)
- **circulation_voting** : procédure par voie de circulation en situation de crise (la présidence du parlement organise le vote par voie de circulation et informe du résultat)
- **virtual_voting** : expression de la voix lors de séances virtuelles en situation de crise.

### Secret procedures (votes secrets)
- **secret_ballot** : vote secret avec bulletins
- **electronic_secret** : vote secret électronique

Le choix de la procédure détermine si les voix individuelles peuvent être saisies :
- Procédures ouvertes : voix individuelles documentables
- Procédures secrètes : seul le résultat global est disponible


## Résultat du vote

Le résultat est saisi de deux manières :

### Chiffres détaillés
- **total_count_yes** : nombre de voix « oui »
- **total_count_no** : nombre de voix « non »
- **total_count_abstention** : nombre d'abstentions
- **total_other** : nombre de voix pour des options supplémentaires, lorsque le choix ne se limite pas à oui/non/abstention (voir la section « Options multiples »)
- **total_absent** : nombre de personnes absentes (qui n'ont pas pu voter)
- **total** : nombre total de membres votants (sans les absents ni la voix de la présidence)
- **majority_count** : nombre de voix nécessaires pour atteindre la majorité requise

### Résultat global
Le résultat est décrit en texte libre dans le champ **result_text** (p. ex. « Accepté par 120 voix contre 75 et 5 abstentions »). La décision catégorielle (accepté / rejeté / pris acte, etc.) n'est pas consignée sur le vote lui-même, mais au moyen de la classe **Resolution** (slot **resolution_type**) rattachée au point de l'ordre du jour. En cas d'égalité des voix, une éventuelle voix prépondérante de la présidence est modélisée au moyen d'un vote distinct (`voting_type: tie_breaker_president`), respectivement d'un nouveau vote.

**Exemple** (vote final, vote simple oui/non) :
- total_count_yes : 120
- total_count_no : 75
- total_count_abstention : 5
- total_absent : 0
- total : 200
- result_text : « Accepté par 120 voix contre 75 et 5 abstentions »
- Resolution.resolution_type : accepted

<!-- TODO: weitere komplexere Beispiele ergänzen — Ordnungsantrag, Wiederholung einer Abstimmung. (Cup-/Mehrfachabstimmung und Stichentscheid sind abgedeckt.) -->

### Options multiples (votes de sélection / « propositions de même sens »)

Tout vote ne se limite pas à oui, non et abstention. Lorsque plusieurs propositions de même sens portent sur la même question matérielle, les membres votent simultanément sur plus de deux variantes (à Zurich, familièrement « vote en coupe », techniquement au moyen de plusieurs boutons de vote). La variante qui l'emporte est celle qui obtient le plus de voix.

De telles procédures sont représentées comme suit :

- **voting_type** = `other`, complété par un **type_label** parlant (p. ex. « Propositions de même sens (choix multiple) »).
- Les champs standard **total_count_yes / total_count_no / total_count_abstention** restent vides, car les options ne correspondent pas à oui/non/abstention.
- Chaque option de sélection reçoit à la place une entrée dans **total_other** (liste de `TotalOther` avec **count** et **label**). Il est ainsi possible de saisir un nombre quelconque d'options avec leur nombre de voix respectif.
- Au niveau de la voix individuelle, **individual_vote_type** est mis à `other` et l'option choisie est consignée au moyen de **type_label** (p. ex. « Sélection A ») ; les membres absents reçoivent `not_voted`.
- Comme **majority_type**, on utilise `other`, puisque ce n'est pas un seuil fixe mais la majorité relative entre les options qui est déterminante.

**Exemple** (Conseil communal de la ville de Zurich, 86e séance du 28.02.2024, affaire 2023/361 « Immeuble d'habitation Magnusstrasse 27, crédit supplémentaire net ») — propositions de même sens avec quatre options :

| Option | Voix |
|--------|------|
| Sélection A (l'emporte) | 75 |
| Sélection B | 25 |
| Sélection C | 12 |
| Sélection D | 0 |
| Absents | 13 |

- Total des voix exprimées : 112 (sur 125 membres)
- Résultat : sélection A acceptée (majorité relative)

La modélisation complète de ce cas figure dans `data_voting.yaml` (`ops:voting_zh_gr_2024_2023_361`).

## Types de majorité

Le champ **majority_type** définit la majorité requise :

### simple
Majorité simple (plus de oui que de non)

**Application :**
- Cas standard pour la plupart des décisions
- Les abstentions ne comptent pas

**Exemple :** 100 oui, 80 non, 20 abstentions → accepté

### absolute
Majorité absolue (plus de la moitié de tous les membres)

**Application :**
- Élections
- Modifications constitutionnelles dans certains cantons
- Décisions particulièrement importantes

**Exemple :** avec 200 membres, au moins 101 voix « oui » sont nécessaires

### two_thirds
Majorité des deux tiers

**Application :**
- Clauses d'urgence au niveau fédéral
- Modifications constitutionnelles dans certains cantons
- Levée de l'immunité

**Exemple :** avec 200 membres, au moins 134 voix « oui » sont nécessaires

### qualified
Majorité qualifiée (autres seuils)

**Application :**
- Exigences particulières dans certains cantons ou certaines communes
- Le quorum concret est indiqué dans **majority_threshold**

## Seuil

Le champ **majority_threshold** indique, pour les majorités qualifiées, le seuil exact (p. ex. 0,6 pour 60 %).

## Quorum

Le champ **quorum** définit le nombre minimal de membres présents pour que l'organe puisse valablement décider :

**Exemple :** un parlement de 200 membres peut valablement décider lorsque 100 membres au moins sont présents (quorum : 100).

## Votes nominatifs
Le champ **named_vote** indique s'il s'agit d'un vote nominatif :

- **true** : les voix individuelles sont saisies et publiées
- **false** : seul le résultat global est saisi

Les votes nominatifs sont importants pour :
- la transparence du comportement de vote
- l'analyse des schémas de vote
- la reddition de comptes envers l'électorat

## Relation avec les voix individuelles

Lors des votes nominatifs, l'entité Voting renvoie aux différentes entités IndividualVote :

```
Voting
  ├─ IndividualVote (personne A)
  ├─ IndividualVote (personne B)
  └─ ...
```

**Exemple :** liste nominative en accordéon https://www.tagblatt.gr.be.ch/shareparl?agendaItemUid=e65d81c90d1d43deb19ef078f7e363f3&segmentType=vote&unitName=default&scroll=true&autoplay=false


## Description et documentation

- **description** : description de l'objet du vote (objet, question soumise au vote)
- **url** : URL multilingues vers les détails du vote

## Horodatage

- **datetime_created** : moment du déroulement du vote
- **datetime_modified** : dernière actualisation (p. ex. en cas de corrections du procès-verbal de vote)




## Classe: Voting 


_Une procédure de vote avec les voix individuelles et les résultats._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles la séance ou le vote se termine.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](#VotingTypeEnum) | Type de procédure de vote (vote intermédiaire, vote final, vote secret, etc.).  |
| type_label | 0..1 <br/> [String](#String) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| voting_title | * <br/> [MultilingualString](#MultilingualString) | Titre du vote, objet ou question soumise au vote. En l'absence d'objet propre, il ne faut pas reprendre le titre de l'affaire.  |
| optional | 0..1 <br/> [Boolean](#Boolean) | Indique si la séance ou le vote est facultatif.  |
| landing_page | 0..1 <br/> [String](#String) | URL fournissant des informations complémentaires.  |
| label_yes | 0..1 <br/> [String](#String) | Signification d'une voix « oui ».  |
| label_no | 0..1 <br/> [String](#String) | Signification d'une voix « non ».  |
| label_abstention | 0..1 <br/> [String](#String) | Signification d'une abstention.  |
| tie_breaker | 0..1 <br/> [Boolean](#Boolean) | Indique si une voix prépondérante a été utilisée lors du vote.  |
| total_count_yes | 0..1 <br/> [Integer](#Integer) | Nombre total de voix « oui ».  |
| total_count_no | 0..1 <br/> [Integer](#Integer) | Nombre total de voix « non ».  |
| total_count_abstention | 0..1 <br/> [Integer](#Integer) | Nombre total d'abstentions.  |
| total_other | * <br/> [TotalOther](#TotalOther) | Utilisé lorsque plusieurs options sont soumises au vote (p. ex. 5 boutons à Zurich).  |
| total_absent | 0..1 <br/> [Integer](#Integer) | Nombre total de membres absents. La distinction entre absent et absent excusé se fait dans la liste de présence.  |
| total | 0..1 <br/> [Integer](#Integer) | Nombre total de voix, sans les absents ni la voix de la présidence.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type de majorité requise pour le vote (absolue, deux tiers, etc.).  |
| majority_count | 0..1 <br/> [Integer](#Integer) | Nombre de voix requis pour atteindre le seuil de majorité déterminant.  |
| result_text | 0..1 <br/> [String](#String) | Texte libre décrivant le résultat du vote, p. ex. « Accepté par 78 voix ».  |
| parent_meeting | 0..1 <br/> [String](#String) | Identifiant de la séance liée qui regroupe la séance courante.  |
| parent_agenda_item | 0..1 <br/> [String](#String) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](#String) | Le lien vers les affaires rattachées au point de l'ordre du jour.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [votings](#votings) | range | [Voting](#Voting) |
| [Protocol](#Protocol) | [votings](#votings) | range | [Voting](#Voting) |
| [IndividualVote](#IndividualVote) | [parent_voting](#parent_voting) | range | [Voting](#Voting) |














### Exemples
#### Exemple : Vote intermédiaire sur une proposition de modification

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
#### Exemple : Vote final avec voix individuelles

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
#### Exemple : Vote final sur le budget

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
#### Exemple : Propositions de même sens avec choix multiple

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

## Enum: VotingTypeEnum 




_Type de procédure de vote._




<div data-search-exclude markdown="1">

URI: [ops:VotingTypeEnum](https://ch.paf.link/schema/operations/VotingTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| preliminary_vote |  Vote intermédiaire  |
| | [ops:enum/voting_type/preliminary_vote](ops:enum/voting_type/preliminary_vote) |
| final_vote |  Vote final  |
| | [ops:enum/voting_type/final_vote](ops:enum/voting_type/final_vote) |
| tie_breaker_president |  Voix prépondérante de la présidence  |
| | [ops:enum/voting_type/tie_breaker_president](ops:enum/voting_type/tie_breaker_president) |
| secret_vote |  Vote ou élection à bulletin secret  |
| | [ops:enum/voting_type/secret_vote](ops:enum/voting_type/secret_vote) |
| other |  Autre type de vote  |
| | [ops:enum/voting_type/other](ops:enum/voting_type/other) |







</div>

## Enum: MajorityTypeEnum 




_Type de majorité requise pour le vote._




<div data-search-exclude markdown="1">

URI: [ops:MajorityTypeEnum](https://ch.paf.link/schema/operations/MajorityTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| absolute |  Majorité absolue.  |
| | [ops:enum/majority_type/absolute](ops:enum/majority_type/absolute) |
| two_thirds |  Majorité des deux tiers.  |
| | [ops:enum/majority_type/two_thirds](ops:enum/majority_type/two_thirds) |
| other |  Autre seuil de majorité, non couvert par les catégories standard.  |
| | [ops:enum/majority_type/other](ops:enum/majority_type/other) |







</div>

## Individual Vote (voix individuelle)

## But de l'entité

IndividualVote saisit le comportement de vote de chaque membre du parlement lors des votes nominatifs. L'entité n'est créée que lorsqu'un vote n'a pas lieu à bulletin secret (Voting.is_nominal = true).

## Relation avec le vote

Chaque Individual Vote fait partie d'un Voting de rang supérieur :

```
Voting (vote final loi sur l'énergie)
  ├─ IndividualVote (conseillère nationale Anna Müller : oui)
  ├─ IndividualVote (conseiller national Beat Schweizer : non)
  ├─ IndividualVote (conseillère nationale Carla Rossi : abstention)
  └─ ...
```

## Identification de la personne

La personne votante est référencée au moyen du champ **person_id**. Cet identifiant correspond à une personne selon la norme eCH-0294 Actors.

D'autres données d'identification peuvent en outre être saisies :
- **person_name** : nom de la personne (pour un accès rapide)
- **person_number** : numéro interne (p. ex. numéro de mandat)
- **person_political_group** : appartenance à un groupe parlementaire
- **person_party** : appartenance à un parti

## Types de voix

TODO : traiter la manière de gérer les « autres » voix, c'est-à-dire les voix pour des possibilités qui ne relèvent pas de oui, non, abstention.

Le champ **vote** saisit le type d'expression de la voix :

### yes
Voix « oui » (approbation)

**Signification :** la personne approuve le projet ou la proposition.

### no
Voix « non » (rejet)

**Signification :** la personne rejette le projet ou la proposition.

### abstention
Abstention

**Signification :** la personne participe au vote, mais s'abstient. En cas de vote électronique, elle appuie sur le bouton « abstention ».

## Poids de la voix

Le champ **weight** saisit le poids de la voix :

- **Cas standard** : 1.0 (une voix)
- **Cas particuliers** : d'autres valeurs sont possibles

### Cas d'application d'un poids de voix divergent

1. **Suppléance** : dans certains systèmes, une personne peut voter pour une personne absente (weight : 2.0)
3. **Assemblées communales** : dans des cas particuliers, des personnes morales peuvent disposer de plusieurs voix
4. **Systèmes historiques** : autrefois, dans certains cantons, différents groupes de personnes disposaient d'un poids de voix différent

## Appartenance à un groupe

Le champ **group_id** saisit l'appartenance au groupe parlementaire au moment du vote :

**Utilité :**
- Analyse du comportement de vote par groupe
- Détermination de la discipline de parti
- Identification de coalitions

**Exemple :** lors d'un vote sur la loi sur l'énergie, 90 % du groupe PS votent oui et 80 % du groupe UDC votent non.

## Position et ordre

Le champ **position** définit le regroupement et l'ordre de tri à l'affichage :

**Application :**
- Tri alphabétique par nom de famille
- Tri par groupe parlementaire
- Tri par expression de la voix (d'abord les oui, puis les non, puis les abstentions)
- Regroupement par groupe parlementaire, à l'intérieur du groupe par oui, non, abstentions et, à l'intérieur du sous-groupe, par ordre alphabétique

## Description et contexte

Le champ **description** peut saisir des informations supplémentaires :

**Exemples :**
- « Abstention en raison d'un conflit d'intérêts (membre du conseil d'administration d'une entreprise énergétique) »
- « Absent pour cause de maladie »

## Horodatage

- **datetime_created** : première publication
- **datetime_modified** : dernière actualisation (p. ex. en cas de corrections de la publication)

## Présence et expression de la voix

Différence importante :

- **Attendance** (autre entité) : saisit la présence générale à une séance
- **IndividualVote** : saisit l'expression concrète de la voix lors d'un vote

Une personne peut être présente à une séance (Attendance), mais être enregistrée comme « absent » ou « did_not_vote » lors de votes isolés (p. ex. lorsqu'elle quitte brièvement la salle).

## Votes nominatifs et votes secrets

Les entités IndividualVote ne sont saisies que lors des votes nominatifs (ouverts) :

- **Vote nominatif** : chaque voix est saisie et est publique
- **Vote secret** : seul le résultat global est saisi, pas d'IndividualVotes



## Classe: IndividualVote 


_Une voix individuelle exprimée par un membre lors d'une procédure de vote._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| parent_voting | 0..1 <br/> [Voting](#Voting) | L'identifiant du vote auquel se rattache la voix individuelle.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Référence à la personne agissante (instantané au moment de la mise en relation).  |
| seat_nr | 0..1 <br/> [String](#String) | Le numéro de siège correspondant à la voix individuelle, le cas échéant.  |
| weight | 0..1 <br/> [Integer](#Integer) | Le nombre de voix dont dispose la personne, le cas échéant (p. ex. lorsqu'une personne détient plusieurs voix).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](#IndividualVoteTypeEnum) | Type de voix exprimée (oui, non, abstention, n'a pas voté, etc.).  |
| type_label | 0..1 <br/> [String](#String) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [individual_votes](#individual_votes) | range | [IndividualVote](#IndividualVote) |














### Exemples
#### Exemple : Voix « oui »

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
#### Exemple : Voix « non »

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
#### Exemple : Abstention

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
#### Exemple : Absent lors d'un choix multiple

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
#### Exemple : Voix « oui » sur le budget

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
#### Exemple : Voix « non » sur le budget

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
#### Exemple : N'a pas voté

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
#### Exemple : Voix individuelle pour l'option C

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
#### Exemple : Voix individuelle pour l'option A

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
#### Exemple : Voix individuelle pour l'option B

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

## Enum: IndividualVoteTypeEnum 




_Type de voix individuelle exprimée par un membre._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| yes |  Voix favorable (oui)  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  Voix défavorable (non)  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Abstention  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  N'a pas voté  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Voix prépondérante, généralement exprimée par la présidence  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Autre forme de vote  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>

## Election (élection)

## Notion et signification

Une Election (élection) désigne la désignation d'une ou de plusieurs personnes à une fonction par un organe parlementaire. Contrairement aux votes (Votings), qui portent sur des questions matérielles, les élections portent sur des décisions relatives à des personnes.

## Différence : élection et vote

| Critère | Election (élection) | Voting (vote) |
|---------|---------------------|---------------|
| Objet | Personnes | Questions matérielles, projets |
| Résultat | Personne(s) élue(s) | Accepté / rejeté |
| Procédure | Souvent secrète | Souvent ouverte |
| Majorité | Le plus souvent absolue | Le plus souvent simple |

## Types d'élections

La norme distingue différents types d'élections au moyen du champ **election_type** :

### open
Élection ouverte

**Caractéristique :**
- L'expression de la voix est visible publiquement
- Chaque membre exprime sa voix ouvertement
- On peut savoir qui a élu qui

**Application :**
- Lorsque la transparence est souhaitée
- Lors d'élections non contestées
- Dans les organes de petite taille

### secret
Élection à bulletin secret

**Caractéristique :**
- L'expression de la voix est anonyme
- Bulletins de vote ou système électronique de vote secret
- On ne peut pas savoir qui a élu qui

**Application :**
- Élections de personnes (standard)
- Lorsqu'une décision libre et non influencée doit être garantie
- Souvent prescrite par la loi

**Exemples au niveau fédéral :**
- Élection du Conseil fédéral
- Élection des juges fédéraux
- Élection des présidences de commission

**Exemples au niveau cantonal :**
- Élection de la présidente ou du président du parlement
- Élection de la présidente ou du président du gouvernement
- Élection des présidentes et présidents des tribunaux cantonaux supérieurs
- Élection des juges
- Élection de la chancelière ou du chancelier d'État
- Élection des présidentes ou des présidents de commission

### tacit
Élection tacite

**Caractéristique :**
- Aucun vote formel nécessaire
- L'élection intervient par acclamation ou par consensus
- Uniquement si aucune opposition n'est soulevée

**Application :**
- En cas d'unanimité
- Élections non contestées
- Réélections sans candidature adverse

**Exemple :** réélection d'une présidence de commission sans candidature adverse

## Rattachement aux points de l'ordre du jour

Chaque élection est rattachée à un AgendaItem :

```
AgendaItem (élection du Conseil fédéral)
  └─ Election (élection pour le département XY)
      ├─ Candidat A : 120 voix
      ├─ Candidat B : 75 voix
      └─ Bulletins blancs : 5
```

## Description et titre

- **title** : titre de l'élection (p. ex. « Élection de la présidence de la CER »)
- **description** : description détaillée, contexte, circonstances particulières

## Résultat de l'élection

Le champ **result** saisit le résultat :

- **elected** : personne(s) élue(s)
- **not_elected** : aucune personne élue (p. ex. majorité absolue non atteinte)
- **deferred** : élection reportée
- **withdrawn** : élection retirée

## Personne(s) élue(s)

Le champ **elected_person_id** contient le ou les identifiants des personnes élues selon eCH-0294 Actors.

En cas d'élections multiples (p. ex. élection simultanée de plusieurs membres d'une commission), plusieurs identifiants peuvent être saisis.

## Répartition des voix

Lors d'élections ouvertes ou après la publication des résultats :

- **total_votes** : nombre total de voix exprimées
- **valid_votes** : voix valables
- **invalid_votes** : voix nulles
- **blank_votes** : bulletins blancs

En complément, des détails par candidature (au moyen d'entités distinctes ou de données structurées).

## Procédure d'élection

Le champ **procedure** décrit la procédure concrète :

- **written_ballot** : élection écrite avec bulletins
- **electronic** : élection électronique
- **show_of_hands** : à main levée (lors d'élections ouvertes)
- **acclamation** : par acclamation (lors d'élections tacites)

## Rapports de majorité

Le champ **majority_type** définit la majorité requise :

### absolute
Majorité absolue (plus de la moitié des votants)

**Application :**
- Élection du Conseil fédéral
- Élection des présidences de commission
- Cas standard pour les élections de personnes

**Exemple :** avec 200 voix exprimées, au moins 101 voix sont nécessaires

**Particularité :** si personne n'atteint la majorité absolue au premier tour, un second tour suit généralement, au cours duquel la majorité simple suffit.

### simple
Majorité simple (plus de voix que les autres candidatures)

**Application :**
- Second tour après un premier tour infructueux
- Certaines élections de commission

### qualified
Majorité qualifiée

**Application :**
- Plus rare lors d'élections
- Fonctions particulières soumises à des exigences accrues

## Tours de scrutin

Lors d'élections requérant la majorité absolue au premier tour :

```
1er tour (majorité absolue requise)
   └─ Aucune candidature n'atteint la majorité absolue

2e tour (la majorité simple suffit)
   └─ Candidat A élu
```

Chaque tour de scrutin est saisi comme une entité Election distincte, reliée par l'AgendaItem commun.

## Horodatage

- **datetime_created** : moment du déroulement
- **datetime_modified** : dernière actualisation

## URL et documentation

- **url** : URL multilingues vers les documents électoraux :
  - profils des candidatures
  - résultats de l'élection
  - procès-verbaux

## Particularités des différentes élections

### Élection du Conseil fédéral
- Élection à bulletin secret
- Majorité absolue requise (au 1er tour)
- Par l'Assemblée fédérale (Chambres réunies)

### Élection des juges fédéraux
- Élection à bulletin secret
- Principe proportionnel (prise en compte des partis, des régions linguistiques, des genres)

### Présidences de commission
- Élection par le parlement concerné
- Souvent moins publique

### Niveaux cantonal et communal
- Grande diversité de procédures électorales
- En partie élection populaire au lieu d'une élection parlementaire
- Exigences de majorité différentes

## Transparence et confidentialité

Champ de tension :
- **Secret du vote** : protection de la décision électorale individuelle
- **Transparence** : intérêt public au résultat de l'élection

En cas d'élections secrètes :
- Seul le résultat global est publié
- Pas d'entités IndividualVote
- Protection de la liberté de vote

En cas d'élections ouvertes :
- Les voix individuelles peuvent être saisies
- Transparence accrue
- Effets potentiels de pression sociale



## Classe: Election 


_Une procédure d'élection visant à pourvoir des fonctions par des personnes._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles la séance ou le vote se termine.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](#ElectionTypeEnum) | Type de procédure d'élection.  |
| type_label | 0..1 <br/> [String](#String) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| title | 0..1 <br/> [String](#String) | Titre de l'élément.  |
| landing_page | 0..1 <br/> [String](#String) | URL fournissant des informations complémentaires.  |
| total_absent | 0..1 <br/> [Integer](#Integer) | Nombre total de membres absents. La distinction entre absent et absent excusé se fait dans la liste de présence.  |
| total | 0..1 <br/> [Integer](#Integer) | Nombre total de voix, sans les absents ni la voix de la présidence.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type de majorité requise pour le vote (absolue, deux tiers, etc.).  |
| majority_count | 0..1 <br/> [Integer](#Integer) | Nombre de voix requis pour atteindre le seuil de majorité déterminant.  |
| result_text | 0..1 <br/> [String](#String) | Texte libre décrivant le résultat du vote, p. ex. « Accepté par 78 voix ».  |
| parent_meeting | 0..1 <br/> [String](#String) | Identifiant de la séance liée qui regroupe la séance courante.  |
| parent_agenda_item | 0..1 <br/> [String](#String) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](#String) | Le lien vers les affaires rattachées au point de l'ordre du jour.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [elections](#elections) | range | [Election](#Election) |



















</div>

## Enum: ElectionTypeEnum 




_Type de procédure d'élection._




<div data-search-exclude markdown="1">

URI: [ops:ElectionTypeEnum](https://ch.paf.link/schema/operations/ElectionTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| secret |  Élection à bulletin secret  |
| | [ops:enum/election_type/secret](ops:enum/election_type/secret) |
| open |  Élection à main levée  |
| | [ops:enum/election_type/open](ops:enum/election_type/open) |
| silent |  Élection tacite sans candidature adverse  |
| | [ops:enum/election_type/silent](ops:enum/election_type/silent) |







</div>

\newpage

<!-- ToDo: David -->


Débat

* -> Enregistrement vidéo -> transcription des propos
*   -> Procès-verbal in extenso -> Text to Timestamp -> le texte contient les horodatages -> document texte (avec ou sans définition du format (types de span))
*   -> Procès-verbal remanié -> AgendaItem to Timestamp

## Speech (intervention, prise de parole)

## Notion et signification

Une Speech (intervention, prise de parole) désigne une contribution orale d'une personne au cours d'une séance parlementaire. Elle est l'instrument central du débat politique et de l'expression des opinions au parlement.

## Types de Speeches

Les interventions parlementaires prennent différentes formes :

### Interventions principales
- Prises de position détaillées sur une affaire
- Motivation de propositions
- Exposé de la position du groupe

### Interventions brèves
- Prises de parole courtes
- Questions intercalaires
- Rectifications

### Déclarations de groupe
- Prise de position officielle d'un groupe
- Présentée par la ou le porte-parole du groupe

### Interventions gouvernementales
- Prises de position de membres du gouvernement
- Réponses aux questions
- Défense de projets

## Structure et rattachement

Une Speech est toujours rattachée à un contexte déterminé :

```
Meeting (séance)
  └─ AgendaItem (point de l'ordre du jour)
      └─ Speech (intervention personne A)
          ├─ TextSegment (transcription)
          ├─ Media (enregistrement audio)
          └─ Media (enregistrement vidéo)
```

### Champs de rattachement

- **meeting_id** : la séance au cours de laquelle l'intervention a eu lieu
- **agenda_item_id** : le point de l'ordre du jour auquel se rapporte l'intervention
- **person_id** : la personne qui s'exprime (selon eCH-0294 Actors)

## Identification des personnes qui s'expriment

- **person_id** : identification univoque de la personne
- **person_name** : nom, pour un accès rapide
- **role** : rôle de la personne (p. ex. « présidence de groupe », « rapporteuse ou rapporteur », « conseillère fédérale / conseiller fédéral »)

## Saisie temporelle

- **start_time** : début de l'intervention
- **end_time** : fin de l'intervention
- **duration** : durée en secondes (calculée ou saisie)

Ces indications temporelles permettent :
- une référence précise dans les enregistrements audio et vidéo
- l'analyse du temps de parole par personne ou par groupe
- le contrôle du respect des limites de temps

## Langue de l'intervention

Le champ **language** saisit la langue dans laquelle l'intervention a été prononcée :

- **de** : allemand
- **fr** : français
- **it** : italien
- **rm** : romanche
- **en** : anglais

## Documents textuels

Le champ **text_segments** renvoie aux entités TextSegment qui contiennent le texte prononcé.

### Différentes versions du texte

#### Transcription brute
- Retranscription littérale
- Non remaniée, avec les mots de remplissage
- Disponible directement après la séance

#### Transcription remaniée
- Revue sur le plan rédactionnel
- Corrigée grammaticalement
- Version officielle du procès-verbal

#### Traductions
- Dans d'autres langues nationales
- Pour les publications internationales

### Structure de TextSegment

Chaque TextSegment peut contenir :
- **text** : le texte proprement dit
- **language** : langue du texte
- **version** : type de version (raw, edited, translated)
- **format** : format (plain, markdown, HTML)

## Enregistrements multimédias

Le champ **media** renvoie aux entités Media comportant des enregistrements audio et vidéo.

### Enregistrements audio
- Son original de l'intervention
- Format : MP3, WAV, etc.
- Métadonnées techniques (qualité, débit binaire)

### Enregistrements vidéo
- Enregistrement visuel (lors des séances plénières)
- Format : MP4, WebM, etc.
- Différentes résolutions

### Diffusion en direct
- Transmission en temps réel
- URL du flux
- Archivage après la séance

## Titre et description

- **title** : titre court (p. ex. « Intervention sur la politique énergétique »)
- **description** : résumé ou contexte de l'intervention

## Type d'intervention

Le champ **speech_type** permet de distinguer différents types :

- **statement** : prise de position
- **question** : question
- **response** : réponse (p. ex. du gouvernement à une question)
- **procedural** : proposition d'ordre
- **declaration** : déclaration



## Classe: Speech 


_Une intervention prononcée au cours d'une séance (également appelée prise de parole)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| language | 0..1 <br/> [String](#String) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |
| start | 0..1 <br/> [String](#String) | Indication de début ou position.  |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles la séance ou le vote se termine.  |
| actor_fullname | 0..1 <br/> [String](#String) | Nom complet de l'actrice ou de l'acteur, respectivement de la personne.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Référence à la personne agissante (instantané au moment de la mise en relation).  |
| role | 0..1 <br/> [String](#String) | Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission).  |
| text | 1 <br/> [String](#String) | Contenu textuel de l'élément.  |
| text_format | 0..1 <br/> [String](#String) | Format du texte (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> [String](#String) | Type de texte (version brute, version éditée).  |
| landing_page | 0..1 <br/> [String](#String) | URL fournissant des informations complémentaires.  |
| media_url | 0..1 <br/> [String](#String) | URL du fichier média (audio/vidéo).  |
| media_type | 0..1 <br/> [String](#String) | Type de média (audio, vidéo, document).  |
| media_format | 0..1 <br/> [String](#String) | Type MIME du fichier média.  |
| documents | * <br/> [Work](#Work) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [speeches](#speeches) | range | [Speech](#Speech) |
| [Protocol](#Protocol) | [speeches](#speeches) | range | [Speech](#Speech) |














### Exemples
#### Exemple : Intervention avec texte in extenso et enregistrement vidéo

```yaml
global_uri: ops:366631
language: fr
datetime_begin: '2025-12-19T09:20:00+01:00'
datetime_end: '2025-12-19T09:25:00+01:00'
actor_fullname: Pascal Broulis
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/18682
  wikidata_uri: http://www.wikidata.org/entity/Q116407
  label: Pascal Broulis
role: speaker
text: >-
  Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec attention
  les différents commentaires qui ont été effectués sur mon postulat. Cela reste un
  postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis selon lequel
  ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark", à savoir
  un modèle chiffré de performance, permettrait de mieux comprendre les raisons des
  retards que notre pays rencontre en comparaison avec les principaux pays européens.
text_format: html
text_type: final
landing_page: >-
  https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
media_url: https://par-pcache.simplex.tv/content?externalid=366631
media_type: video
media_format: video/mp4

```






</div>


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



## Classe: TextSegment 


_Un segment de texte tel qu'un renvoi ou un intertitre dans un procès-verbal de séance._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| text | 1 <br/> [String](#String) | Contenu textuel de l'élément.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | [text_segments](#text_segments) | range | [TextSegment](#TextSegment) |



















</div>



## Classe: Media 


_Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD ou les liens vers des contenus audio/vidéo)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| title | 0..1 <br/> [String](#String) | Titre de l'élément.  |
| media_type | 0..1 <br/> [String](#String) | Type de média (audio, vidéo, document).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| version | 0..1 <br/> [String](#String) | Numéro ou identifiant de version.  |
| parent_type | 0..1 <br/> [String](#String) | Type de l'objet parent (séance, point de l'ordre du jour, intervention, affaire).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |






















</div>



## Classe: MultilingualString 


_Une chaîne de caractères pouvant contenir du texte en plusieurs langues._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| text | 1 <br/> [String](#String) | Contenu textuel de l'élément.  |
| language | 1 <br/> [String](#String) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | [name](#name) | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | [name](#name) | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | [name](#name) | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | [agenda_item_title](#agenda_item_title) | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | [agenda_item_description](#agenda_item_description) | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | [agenda_item_title](#agenda_item_title) | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | [agenda_item_description](#agenda_item_description) | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [Voting](#Voting) | [voting_title](#voting_title) | range | [MultilingualString](#MultilingualString) |
| [IndividualAttendance](#IndividualAttendance) | [reason](#reason) | range | [MultilingualString](#MultilingualString) |
| [Media](#Media) | [url](#url) | range | [MultilingualString](#MultilingualString) |



















</div>



## Classe: Container 


_Conteneur pour les données de l'activité publique des conseils : législatures, sessions, séances, points de l'ordre du jour, procès-verbaux, votes, élections, présences, interventions et décisions._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
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
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |

















### Exemples
#### Exemple : meeting

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
#### Exemple : meeting sr winter25 Sitzung6

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

```
#### Exemple : meeting complete

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
#### Exemple : meeting item

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
#### Exemple : voting

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
  parent_agenda_item: ops:agenda_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: "2023/361"
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/"
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
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/1"
    label: "Mitglied Auswahl A"
  seat_nr: "12"
  individual_vote_type: "other"
  type_label: "Auswahl A"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/2"
    label: "Mitglied Auswahl B"
  seat_nr: "47"
  individual_vote_type: "other"
  type_label: "Auswahl B"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/3"
    label: "Mitglied Auswahl C"
  seat_nr: "88"
  individual_vote_type: "other"
  type_label: "Auswahl C"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/4"
    label: "Abwesendes Mitglied"
  seat_nr: "103"
  individual_vote_type: "not_voted"
  datetime_created: "2024-02-28T00:00:00Z"

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
#### Exemple : session

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






</div>

