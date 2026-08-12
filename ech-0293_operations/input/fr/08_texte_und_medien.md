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

{{include:ech-0293_operations/output/docs/TextSegment.md}}

{{include:ech-0293_operations/output/docs/Media.md}}

{{include:ech-0293_operations/output/docs/MultilingualString.md}}

{{include:ech-0293_operations/output/docs/Container.md}}
