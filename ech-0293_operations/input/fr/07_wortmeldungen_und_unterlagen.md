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

{{include:ech-0293_operations/output/docs/Speech.md}}
