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

{{include:ech-0293_operations/output/docs/Legislature.md}}

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

{{include:ech-0293_operations/output/docs/Session.md}}

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

{{include:ech-0293_operations/output/docs/Meeting.md}}

{{include:ech-0293_operations/output/docs/MeetingTypeEnum.md}}

{{include:ech-0293_operations/output/docs/StateEnum.md}}

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

{{include:ech-0293_operations/output/docs/Attendance.md}}

{{include:ech-0293_operations/output/docs/IndividualAttendance.md}}

{{include:ech-0293_operations/output/docs/AttendanceTypeEnum.md}}
