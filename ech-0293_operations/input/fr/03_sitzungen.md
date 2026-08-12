\newpage

<!-- ToDo: Christian -->

# Organisation temporelle du fonctionnement des conseils

Le fonctionnement des conseils s'organise dans le temps sur trois niveaux : les législatures constituent le cadre à long terme, les sessions structurent le travail au sein d'une législature, et les séances (Meetings) sont les réunions concrètes au cours desquelles les affaires sont délibérées.

```
Legislature (législature)
  └─ Session (p. ex. session de printemps)
      └─ Meeting (séance individuelle)
          └─ AgendaItem (point de l'ordre du jour)
```

Les trois classes sont délibérément construites de la même manière : l'identification, les indications temporelles, le rattachement à l'organe et les documents liés fonctionnent de façon identique aux trois niveaux. Ces conventions communes sont décrites une seule fois, à la législature ; pour la session et la séance ne suivent que les particularités du niveau concerné.

## Legislature (législature)

Une législature désigne la période pour laquelle un parlement est élu et durant laquelle il exerce ses fonctions dans sa composition actuelle. Sa durée n'est pas prescrite — les exemples à la fin de la présente section montrent un mandat de quatre ans et un mandat de cinq ans.

### Planifié et effectif

Le début et la fin sont consignés deux fois : `date_begin_planned` et `date_end_planned` retiennent la planification, `date_begin_actual` et `date_end_actual` le déroulement effectif. Lorsque l'heure importe, les variantes `datetime_*` sont à disposition. Pour une législature, planification et déroulement coïncident le plus souvent ; les mêmes champs valent tels quels pour la session et la séance, où ils divergent régulièrement.

### Identification

`global_uri` est l'identifiant et est obligatoire. `local_id` reprend l'identifiant du système livreur, `wikidata_uri` renvoie à l'entrée Wikidata, lorsqu'elle existe. Cela vaut de la même manière pour la session et la séance.

### Rattachement à l'organe

`actor_id` renvoie, sous forme de référence abrégée, à l'organe selon eCH-0294 (p. ex. Conseil national, Grand Conseil), `administrative_id` à l'unité administrative pour laquelle cet organe agit (pays, canton, commune). Ce couple se retrouve également dans le Meeting.

### Documents liés

`documents` relie des documents en tant que FRBR-Works selon eCH-0292 — pour la législature p. ex. les listes des membres et les répertoires des affaires, pour la session le programme de session, pour la séance le procès-verbal.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (période de séance)

Une session est une période de séance continue au cours de laquelle plusieurs séances ont lieu. Elle constitue le niveau intermédiaire — et elle est facultative : les entités fédérées sans sessions formelles s'en passent et gèrent directement leurs séances.

### Session ou séance ?

La session est la période, la séance la réunion individuelle qui s'y déroule :

```
Legislature (51e législature)
  └─ Session (session de printemps 2024)
      ├─ Meeting (séance du Conseil national du 4 mars 2024)
      ├─ Meeting (séance du Conseil des États du 4 mars 2024)
      └─ ...
```

Les deux niveaux peuvent coïncider : une séance d'un jour du Grand Conseil ou une Landsgemeinde est gérée comme une période de séance comportant une seule séance — les exemples montrent les deux cas.

### Numérotation

Les sessions sont numérotées, la pratique variant fortement : `number` retient le numéro courant sous forme de nombre, `sequential_number` la même indication sous forme de chaîne de caractères (et donc aussi en chiffres romains), `position` la position au sein de la législature et `meeting_abbreviation` une désignation abrégée telle que « FS24 ». Le Meeting connaît les mêmes quatre champs.

### Rattachement et liens

`body_key` retient l'organe sous forme de clé abrégée (p. ex. « NR », « SR »), `parent_legislature` rattache la session à sa législature, `meetings` énumère les séances correspondantes, `url` renvoie à la page d'accueil.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (séance individuelle)

Un Meeting est la séance individuelle d'un organe — le niveau auquel les points de l'ordre du jour sont délibérés, les décisions prises et les interventions consignées.

### Types de séance

`meeting_type` distingue quatre types : `session` pour les séances plénières d'un parlement ou d'une chambre, `committee` pour les séances de commission, `sitting` pour les assemblées telles que les Landsgemeinden, les assemblées communales et les assemblées de commune bourgeoise, et `various` comme valeur résiduelle. La valeur `sitting` procède d'un choix délibéré : les Landsgemeinden et les assemblées communales sont des assemblées des personnes ayant le droit de vote elles-mêmes, mais elles décident en tant qu'organe siégeant doté d'un ordre du jour et sont donc représentées comme une séance de conseil.

### Planification et réalité

Au niveau de la séance, planification et déroulement divergent régulièrement : une séance fixée à 14h00 ne commence, en raison de retards, qu'à 14h25 et se termine à 17h30 au lieu de 18h00. C'est précisément à cela que servent les champs `*_planned` et `*_actual` ; pour les heures, il convient d'utiliser les variantes `datetime_*`. `state` retient si une séance a lieu comme prévu (`planned`, `canceled`, `postponed`) ; `state_name` reprend une désignation de statut divergente, en texte libre.

### Lieu

`location` consigne le lieu de la séance — la salle physique (« Palais fédéral, salle du Conseil national »), une visioconférence ou un format hybride.

### Rattachement à l'organe et classement

Outre `actor_id` et `administrative_id`, `actor_name` retient le nom de l'organe pour un accès rapide et `body_key` une clé abrégée ; `group_name` et `group_id` complètent les regroupements là où c'est nécessaire. `parent_meeting` représente les séances qui font partie d'une séance de rang supérieur, `parent_legislature` rattache la séance à la législature. La numérotation se fait comme pour la session.

### Points d'ancrage

Le Meeting est le nœud auquel se rattachent les autres classes de la présente norme : les points de l'ordre du jour (`AgendaItem`), les votes et élections (`Voting`, `Election`), les interventions (`Speech`) ainsi que la liste de présence (`Attendance.parent_meeting`). `documents` relie les documents de séance tels que le bulletin ou les annexes, `protocol_ref` le procès-verbal.

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
