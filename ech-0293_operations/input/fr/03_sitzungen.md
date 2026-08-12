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
