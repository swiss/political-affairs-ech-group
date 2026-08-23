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

Le champ **reason** (multilingue) permet de saisir en texte libre le motif d'une absence ou d'un retard.

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

{{include:ech-0293_operations/output/docs/Attendance.md}}

{{include:ech-0293_operations/output/docs/IndividualAttendance.md}}

{{include:ech-0293_operations/output/docs/AttendanceTypeEnum.md}}
