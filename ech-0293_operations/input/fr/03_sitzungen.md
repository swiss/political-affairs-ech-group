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

La législature constitue le cadre à long terme, la session structure le travail au sein d'une législature, le Meeting est la séance concrète au cours de laquelle les affaires sont délibérées, et le point de l'ordre du jour articule la séance individuelle. Les niveaux s'emboîtent de deux manières : la session reprend ses séances sous forme de liste (`meetings`), tandis que la séance et le point de l'ordre du jour renvoient vers le haut par des références (`parent_legislature`, `parent_meeting`, `parent_agenda_item`). Qui ne tient pas de sessions livre ses séances isolément et les rattache à la législature au moyen de `parent_legislature`.

Les trois premières classes sont décrites ci-après, le point de l'ordre du jour dans le chapitre suivant.

## Éléments communs

Les trois classes sont délibérément construites de la même manière. Les champs suivants ont la même signification à tous les niveaux.

**Identification.** `global_uri` est l'identifiant et est obligatoire. `local_id` reprend l'identifiant du système livreur, `wikidata_uri` renvoie à l'entrée Wikidata, lorsqu'elle existe.

**Début et fin.** Les indications temporelles sont consignées deux fois : `date_begin_planned` et `date_end_planned` retiennent ce qui était prévu, `date_begin_actual` et `date_end_actual` ce qui s'est effectivement passé. Lorsque l'heure importe, les variantes `datetime_*` sont à disposition.

**Espace et organe.** `spatial` renvoie à l'unité spatiale selon LINDAS — pays, canton, district ou commune, donc `https://ld.admin.ch/canton/2` et non « BE ». C'est le champ avec lequel eCH-0294 localise ses groupes, de sorte qu'un fonctionnement de conseil et les acteurs qui le portent renvoient à la même ressource. Qui siège au sein de cette unité spatiale est indiqué par `actor_id`, référence abrégée à l'organe selon eCH-0294.

**Documents liés.** `documents` relie des documents en tant que FRBR-Works selon eCH-0292 — pour la législature p. ex. les listes des membres et les répertoires des affaires, pour la session le programme de session, pour la séance le procès-verbal.

## Legislature (législature)

Une législature désigne la période pour laquelle un parlement est élu et durant laquelle il exerce ses fonctions dans sa composition actuelle.

### Durée et déroulement

La durée n'est pas prescrite — les exemples montrent un mandat de quatre ans et un mandat de cinq ans. Contrairement à la séance, planification et déroulement ne divergent guère à ce niveau ; là où une législature est fixée au jour près par la loi, `*_planned` et `*_actual` portent les mêmes dates.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (période de séance)

Une session est une période de séance continue au cours de laquelle plusieurs séances ont lieu.

### Niveau facultatif

La session est le seul des trois niveaux auquel il est possible de renoncer : les entités fédérées sans sessions formelles s'en passent et gèrent directement leurs séances. Session et séance peuvent aussi coïncider — une séance d'un jour du Grand Conseil ou une Landsgemeinde est gérée comme une période de séance comportant une seule séance.

### Numérotation

La numérotation varie fortement d'une pratique à l'autre, raison pour laquelle quatre champs sont disponibles : `number` retient le numéro courant sous forme de nombre, `sequential_number` la même indication sous forme de chaîne de caractères (et donc aussi en chiffres romains), `position` la position au sein de la législature et `meeting_abbreviation` une désignation abrégée telle que « FS24 ». Le Meeting connaît les mêmes quatre champs.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (séance individuelle)

Un Meeting est la séance individuelle d'un organe — le niveau auquel les points de l'ordre du jour sont délibérés, les décisions prises et les interventions consignées.

### Types de séance

`meeting_type` distingue quatre types : `session` pour les séances plénières d'un parlement ou d'une chambre, `committee` pour les séances de commission, `sitting` pour les assemblées telles que les Landsgemeinden, les assemblées communales et les assemblées de commune bourgeoise, et `various` comme valeur résiduelle. La valeur `sitting` procède d'un choix délibéré : les Landsgemeinden et les assemblées communales sont des assemblées des personnes ayant le droit de vote elles-mêmes, mais elles décident en tant qu'organe siégeant doté d'un ordre du jour et sont donc représentées comme une séance de conseil.

### Planification et déroulement

À ce niveau, les heures prévues et les heures effectives divergent régulièrement : une séance fixée à 14h00 ne commence, en raison de retards, qu'à 14h25 et se termine à 17h30 au lieu de 18h00. `state` retient si une séance a lieu comme prévu (`planned`, `canceled`, `postponed`) ; `state_name` reprend une désignation de statut divergente, en texte libre. `location` consigne le lieu de la séance — la salle physique (« Palais fédéral, salle du Conseil national »), une visioconférence ou un format hybride.

### Points d'ancrage

Le Meeting est le nœud auquel se rattachent les autres classes de la présente norme : les points de l'ordre du jour (`AgendaItem`), les votes et élections (`Voting`, `Election`), les interventions (`Speech`) ainsi que la liste de présence (`Attendance.parent_meeting`). `documents` relie les documents de séance tels que le bulletin ou les annexes, `protocol_ref` le procès-verbal. `parent_meeting` représente les séances qui font partie d'une séance de rang supérieur ; `actor_name`, `group_name` et `group_id` retiennent en clair l'organe et le regroupement.

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
