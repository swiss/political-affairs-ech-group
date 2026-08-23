\newpage

<!-- ToDo: Nicole -->

# Votes et élections

Les décisions parlementaires sont prises soit par des votes sur des questions matérielles, soit par des élections de personnes. La norme distingue clairement ces deux mécanismes et saisit en outre, dans les procédures ouvertes, le comportement de vote individuel de chaque membre du parlement. Les présidentes et présidents de parlement ne participent en principe pas aux votes ; ils ne votent que lors des élections. En cas d'égalité des voix lors d'un vote, ils départagent.

## Voting (vote)

### But de l'entité

« Voting » saisit le processus de vote et le résultat d'une décision formelle au parlement. L'entité documente aussi bien l'objet du vote (la question) que la procédure (comment il a été voté) et le résultat (avec quel rapport de voix).

### Types de votes

La norme distingue différents types de votes au moyen du champ **voting_type** :

#### intermediate
Votes intermédiaires en cours de délibération.

**Exemples :**
- Vote sur l'entrée en matière relative à une affaire
- Vote sur une proposition
- Opposition de deux propositions qui s'excluent mutuellement ou qui portent sur le même passage de texte
- Vote éventuel lorsque plus de deux propositions portent sur le même objet
- Vote sur un article isolé d'une loi
- Vote sur l'ensemble après la première lecture d'un acte délibéré en deux lectures

#### final
Le vote final portant sur l'ensemble du projet

**Exemples :**
- Vote final après la dernière lecture d'un acte
- Vote sur l'ensemble d'un arrêté
- Acceptation ou rejet d'un projet dans son ensemble
- Vote point par point sur une intervention

#### casting
Voix prépondérante de la présidence en cas d'égalité des voix. La présidence ne participe pas aux votes, mais départage en cas d'égalité. En cas de vote secret, la proposition de l'organe qui a procédé à l'examen préalable est réputée acceptée en cas d'égalité des voix.

#### secret
Expression secrète de la voix lors de votes et d'élections

**Application :**
- Élection de personnes
- Vote sur une affaire particulièrement délicate, telle qu'un recours en grâce ou la levée de l'immunité
- Vote après délibération à huis clos
- Vote secret sur proposition

### Structure d'un vote

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

### Procédures de vote

Le champ **procedure** décrit le mode de déroulement :

#### Open procedures (votes ouverts)
- **show_of_hands** : à main levée (traditionnel)
- **standing** : par assis et levé (plus rare)
- **electronic** : vote électronique (fréquent aux niveaux fédéral et cantonal)
- **roll_call** : vote nominatif avec appel des noms
- **remote_voting** : expression de la voix à distance en situation de crise (des membres du conseil communiquent leur voix à la présidence du parlement avant le jour de séance. Les voix exprimées à distance sont saisies simultanément avec le vote en cours au conseil.)
- **circulation_voting** : procédure par voie de circulation en situation de crise (la présidence du parlement organise le vote par voie de circulation et informe du résultat)
- **virtual_voting** : expression de la voix lors de séances virtuelles en situation de crise.

#### Secret procedures (votes secrets)
- **secret_ballot** : vote secret avec bulletins
- **electronic_secret** : vote secret électronique

Le choix de la procédure détermine si les voix individuelles peuvent être saisies :
- Procédures ouvertes : voix individuelles documentables
- Procédures secrètes : seul le résultat global est disponible


### Résultat du vote

Le résultat est saisi de deux manières :

#### Chiffres détaillés
- **total_count_yes** : nombre de voix « oui »
- **total_count_no** : nombre de voix « non »
- **total_count_abstention** : nombre d'abstentions
- **total_other** : nombre de voix pour des options supplémentaires, lorsque le choix ne se limite pas à oui/non/abstention (voir la section « Options multiples »)
- **total_absent** : nombre de personnes absentes (qui n'ont pas pu voter)
- **total** : nombre total de membres votants (sans les absents ni la voix de la présidence)
- **majority_count** : nombre de voix nécessaires pour atteindre la majorité requise

#### Résultat global
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

#### Options multiples (votes de sélection / « propositions de même sens »)

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

### Types de majorité

Le champ **majority_type** définit la majorité requise :

#### simple
Majorité simple (plus de oui que de non)

**Application :**
- Cas standard pour la plupart des décisions
- Les abstentions ne comptent pas

**Exemple :** 100 oui, 80 non, 20 abstentions → accepté

#### absolute
Majorité absolue (plus de la moitié de tous les membres)

**Application :**
- Élections
- Modifications constitutionnelles dans certains cantons
- Décisions particulièrement importantes

**Exemple :** avec 200 membres, au moins 101 voix « oui » sont nécessaires

#### two_thirds
Majorité des deux tiers

**Application :**
- Clauses d'urgence au niveau fédéral
- Modifications constitutionnelles dans certains cantons
- Levée de l'immunité

**Exemple :** avec 200 membres, au moins 134 voix « oui » sont nécessaires

#### qualified
Majorité qualifiée (autres seuils)

**Application :**
- Exigences particulières dans certains cantons ou certaines communes
- Le quorum concret est indiqué dans **majority_threshold**

### Seuil

Le champ **majority_threshold** indique, pour les majorités qualifiées, le seuil exact (p. ex. 0,6 pour 60 %).

### Quorum

Le champ **quorum** définit le nombre minimal de membres présents pour que l'organe puisse valablement décider :

**Exemple :** un parlement de 200 membres peut valablement décider lorsque 100 membres au moins sont présents (quorum : 100).

### Votes nominatifs
Le champ **named_vote** indique s'il s'agit d'un vote nominatif :

- **true** : les voix individuelles sont saisies et publiées
- **false** : seul le résultat global est saisi

Les votes nominatifs sont importants pour :
- la transparence du comportement de vote
- l'analyse des schémas de vote
- la reddition de comptes envers l'électorat

### Relation avec les voix individuelles

Lors des votes nominatifs, l'entité Voting renvoie aux différentes entités IndividualVote :

```
Voting
  ├─ IndividualVote (personne A)
  ├─ IndividualVote (personne B)
  └─ ...
```

**Exemple :** liste nominative en accordéon https://www.tagblatt.gr.be.ch/shareparl?agendaItemUid=e65d81c90d1d43deb19ef078f7e363f3&segmentType=vote&unitName=default&scroll=true&autoplay=false


### Description et documentation

- **description** : description de l'objet du vote (objet, question soumise au vote)
- **url** : URL multilingues vers les détails du vote

### Horodatage

- **datetime_created** : moment du déroulement du vote
- **datetime_modified** : dernière actualisation (p. ex. en cas de corrections du procès-verbal de vote)


{{include:ech-0293_operations/output/docs/Voting.md}}

{{include:ech-0293_operations/output/docs/VotingTypeEnum.md}}

{{include:ech-0293_operations/output/docs/MajorityTypeEnum.md}}

{{include:ech-0293_operations/output/docs/TotalOther.md}}

## Individual Vote (voix individuelle)

### But de l'entité

IndividualVote saisit le comportement de vote de chaque membre du parlement lors des votes nominatifs. L'entité n'est créée que lorsqu'un vote n'a pas lieu à bulletin secret (Voting.is_nominal = true).

### Relation avec le vote

Chaque Individual Vote fait partie d'un Voting de rang supérieur :

```
Voting (vote final loi sur l'énergie)
  ├─ IndividualVote (conseillère nationale Anna Müller : oui)
  ├─ IndividualVote (conseiller national Beat Schweizer : non)
  ├─ IndividualVote (conseillère nationale Carla Rossi : abstention)
  └─ ...
```

### Identification de la personne

La personne votante est référencée au moyen du champ **person_id**. Cet identifiant correspond à une personne selon la norme eCH-0294 Actors.

D'autres données d'identification peuvent en outre être saisies :
- **person_name** : nom de la personne (pour un accès rapide)
- **person_number** : numéro interne (p. ex. numéro de mandat)
- **person_political_group** : appartenance à un groupe parlementaire
- **person_party** : appartenance à un parti

### Types de voix

Outre `yes`, `no` et `abstention`, le champ connaît trois autres valeurs : `not_voted` pour les membres présents qui n'ont pas voté, `tie_breaker` pour la voix prépondérante de la présidence et `other` pour tout ce qui ne se laisse pas ramener à cet axe. `other` est le pendant individuel de `total_other` : lors d'un vote sélectif, la personne a voté, mais ni oui ni non — l'option qu'elle a choisie est retenue par `type_label` (« Auswahl A »). La voix individuelle reste ainsi exploitable sans que la norme doive tenir chaque mécanique de sélection cantonale comme valeur d'énumération propre.

Le champ **vote** saisit le type d'expression de la voix :

#### yes
Voix « oui » (approbation)

**Signification :** la personne approuve le projet ou la proposition.

#### no
Voix « non » (rejet)

**Signification :** la personne rejette le projet ou la proposition.

#### abstention
Abstention

**Signification :** la personne participe au vote, mais s'abstient. En cas de vote électronique, elle appuie sur le bouton « abstention ».

### Poids de la voix

Le champ **weight** saisit le poids de la voix :

- **Cas standard** : 1.0 (une voix)
- **Cas particuliers** : d'autres valeurs sont possibles

#### Cas d'application d'un poids de voix divergent

1. **Suppléance** : dans certains systèmes, une personne peut voter pour une personne absente (weight : 2.0)
3. **Assemblées communales** : dans des cas particuliers, des personnes morales peuvent disposer de plusieurs voix
4. **Systèmes historiques** : autrefois, dans certains cantons, différents groupes de personnes disposaient d'un poids de voix différent

### Appartenance à un groupe

Le champ **group_id** saisit l'appartenance au groupe parlementaire au moment du vote :

**Utilité :**
- Analyse du comportement de vote par groupe
- Détermination de la discipline de parti
- Identification de coalitions

**Exemple :** lors d'un vote sur la loi sur l'énergie, 90 % du groupe PS votent oui et 80 % du groupe UDC votent non.

### Position et ordre

Le champ **position** définit le regroupement et l'ordre de tri à l'affichage :

**Application :**
- Tri alphabétique par nom de famille
- Tri par groupe parlementaire
- Tri par expression de la voix (d'abord les oui, puis les non, puis les abstentions)
- Regroupement par groupe parlementaire, à l'intérieur du groupe par oui, non, abstentions et, à l'intérieur du sous-groupe, par ordre alphabétique

### Description et contexte

Le champ **description** peut saisir des informations supplémentaires :

**Exemples :**
- « Abstention en raison d'un conflit d'intérêts (membre du conseil d'administration d'une entreprise énergétique) »
- « Absent pour cause de maladie »

### Horodatage

- **datetime_created** : première publication
- **datetime_modified** : dernière actualisation (p. ex. en cas de corrections de la publication)

### Présence et expression de la voix

Différence importante :

- **Attendance** (autre entité) : saisit la présence générale à une séance
- **IndividualVote** : saisit l'expression concrète de la voix lors d'un vote

Une personne peut être présente à une séance (Attendance), mais être enregistrée comme « absent » ou « did_not_vote » lors de votes isolés (p. ex. lorsqu'elle quitte brièvement la salle).

### Votes nominatifs et votes secrets

Les entités IndividualVote ne sont saisies que lors des votes nominatifs (ouverts) :

- **Vote nominatif** : chaque voix est saisie et est publique
- **Vote secret** : seul le résultat global est saisi, pas d'IndividualVotes

{{include:ech-0293_operations/output/docs/IndividualVote.md}}

{{include:ech-0293_operations/output/docs/IndividualVoteTypeEnum.md}}

## Election (élection)

### Notion et signification

Une Election (élection) désigne la désignation d'une ou de plusieurs personnes à une fonction par un organe parlementaire. Contrairement aux votes (Votings), qui portent sur des questions matérielles, les élections portent sur des décisions relatives à des personnes.

### Différence : élection et vote

| Critère | Election (élection) | Voting (vote) |
|---------|---------------------|---------------|
| Objet | Personnes | Questions matérielles, projets |
| Résultat | Personne(s) élue(s) | Accepté / rejeté |
| Procédure | Souvent secrète | Souvent ouverte |
| Majorité | Le plus souvent absolue | Le plus souvent simple |

### Types d'élections

La norme distingue différents types d'élections au moyen du champ **election_type** :

#### open
Élection ouverte

**Caractéristique :**
- L'expression de la voix est visible publiquement
- Chaque membre exprime sa voix ouvertement
- On peut savoir qui a élu qui

**Application :**
- Lorsque la transparence est souhaitée
- Lors d'élections non contestées
- Dans les organes de petite taille

#### secret
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

#### tacit
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

### Rattachement aux points de l'ordre du jour

Chaque élection est rattachée à un AgendaItem :

```
AgendaItem (élection du Conseil fédéral)
  └─ Election (élection pour le département XY)
      ├─ Candidat A : 120 voix
      ├─ Candidat B : 75 voix
      └─ Bulletins blancs : 5
```

### Description et titre

- **title** : titre de l'élection (p. ex. « Élection de la présidence de la CER »)
- **description** : description détaillée, contexte, circonstances particulières

### Résultat de l'élection

Le champ **result** saisit le résultat :

- **elected** : personne(s) élue(s)
- **not_elected** : aucune personne élue (p. ex. majorité absolue non atteinte)
- **deferred** : élection reportée
- **withdrawn** : élection retirée

### Personne(s) élue(s)

Le champ **elected_person_id** contient le ou les identifiants des personnes élues selon eCH-0294 Actors.

En cas d'élections multiples (p. ex. élection simultanée de plusieurs membres d'une commission), plusieurs identifiants peuvent être saisis.

### Répartition des voix

Lors d'élections ouvertes ou après la publication des résultats :

- **total_votes** : nombre total de voix exprimées
- **valid_votes** : voix valables
- **invalid_votes** : voix nulles
- **blank_votes** : bulletins blancs

En complément, des détails par candidature (au moyen d'entités distinctes ou de données structurées).

### Procédure d'élection

Le champ **procedure** décrit la procédure concrète :

- **written_ballot** : élection écrite avec bulletins
- **electronic** : élection électronique
- **show_of_hands** : à main levée (lors d'élections ouvertes)
- **acclamation** : par acclamation (lors d'élections tacites)

### Rapports de majorité

Le champ **majority_type** définit la majorité requise :

#### absolute
Majorité absolue (plus de la moitié des votants)

**Application :**
- Élection du Conseil fédéral
- Élection des présidences de commission
- Cas standard pour les élections de personnes

**Exemple :** avec 200 voix exprimées, au moins 101 voix sont nécessaires

**Particularité :** si personne n'atteint la majorité absolue au premier tour, un second tour suit généralement, au cours duquel la majorité simple suffit.

#### simple
Majorité simple (plus de voix que les autres candidatures)

**Application :**
- Second tour après un premier tour infructueux
- Certaines élections de commission

#### qualified
Majorité qualifiée

**Application :**
- Plus rare lors d'élections
- Fonctions particulières soumises à des exigences accrues

### Tours de scrutin

Lors d'élections requérant la majorité absolue au premier tour :

```
1er tour (majorité absolue requise)
   └─ Aucune candidature n'atteint la majorité absolue

2e tour (la majorité simple suffit)
   └─ Candidat A élu
```

Chaque tour de scrutin est saisi comme une entité Election distincte, reliée par l'AgendaItem commun.

### Horodatage

- **datetime_created** : moment du déroulement
- **datetime_modified** : dernière actualisation

### URL et documentation

- **url** : URL multilingues vers les documents électoraux :
  - profils des candidatures
  - résultats de l'élection
  - procès-verbaux

### Particularités des différentes élections

#### Élection du Conseil fédéral
- Élection à bulletin secret
- Majorité absolue requise (au 1er tour)
- Par l'Assemblée fédérale (Chambres réunies)

#### Élection des juges fédéraux
- Élection à bulletin secret
- Principe proportionnel (prise en compte des partis, des régions linguistiques, des genres)

#### Présidences de commission
- Élection par le parlement concerné
- Souvent moins publique

#### Niveaux cantonal et communal
- Grande diversité de procédures électorales
- En partie élection populaire au lieu d'une élection parlementaire
- Exigences de majorité différentes

### Transparence et confidentialité

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

{{include:ech-0293_operations/output/docs/Election.md}}

{{include:ech-0293_operations/output/docs/ElectionTypeEnum.md}}
