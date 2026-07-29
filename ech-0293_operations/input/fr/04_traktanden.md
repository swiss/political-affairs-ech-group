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

{{include:ech-0293_operations/output/docs/AgendaItem.md}}

{{include:ech-0293_operations/output/docs/AgendaItemTypeEnum.md}}

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

{{include:ech-0293_operations/output/docs/Protocol.md}}

### ProtocolItem (point consigné au procès-verbal)

`ProtocolItem` hérite de tous les champs d'`AgendaItem` (`is_a: AgendaItem`) et représente un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-verbal.

{{include:ech-0293_operations/output/docs/ProtocolItem.md}}

## Délibération commune (JointDebate)

### But de l'entité

`JointDebate` regroupe plusieurs points de l'ordre du jour délibérés conjointement — par exemple des affaires connexes traitées dans un seul et même débat.

{{include:ech-0293_operations/output/docs/JointDebate.md}}

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

{{include:ech-0293_operations/output/docs/Resolution.md}}

{{include:ech-0293_operations/output/docs/ResolutionTypeEnum.md}}

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

{{include:ech-0293_operations/output/docs/Motion.md}}
