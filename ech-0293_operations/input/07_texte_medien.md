# Texte und Medien

Parlamentarische Debatten werden nicht nur als strukturierte Daten erfasst, sondern auch als Texte und Multimedia-Aufzeichnungen. Diese Entitäten ermöglichen die Verwaltung von Transkripten, Audio-/Video-Aufzeichnungen und weiteren Medienformaten sowie die technische Infrastruktur für Datenaustausch und Mehrsprachigkeit.

## TextSegment

### Zweck
Erfasst Textabschnitte mit Versionierung und Sprachvarianten. Wird primär für Transkriptionen von Wortmeldungen verwendet, kann aber auch für andere Textdokumente eingesetzt werden.

### Struktur
- **text**: Der eigentliche Textinhalt
- **language**: Sprachcode (ISO 639-1)
- **format**: Format des Texts (plain, markdown, html)
- **version_type**: Art der Version
  - **raw**: Unbearbeitetes Rohtranskript
  - **edited**: Redaktionell bearbeitete Version
  - **translated**: Übersetzung in andere Sprache
  - **summary**: Zusammenfassung

### Designentscheid
**Warum separate Entität?**
- Ermöglicht mehrere Versionen desselben Texts (Rohfassung, bearbeitet, übersetzt)
- Versionskontrolle und Nachvollziehbarkeit von Änderungen
- Flexibilität bei Formaten (Plain, Markdown, HTML für unterschiedliche Ausgabekanäle)

### Anwendung
Hauptsächlich verknüpft mit Speech-Entitäten:
```
Speech
  ├─ TextSegment (Rohtranskript, de)
  ├─ TextSegment (Bearbeitetes Protokoll, de)
  ├─ TextSegment (Übersetzung, fr)
  └─ TextSegment (Zusammenfassung, de)
```

## Media

### Zweck
Referenziert Mediendateien (Audio, Video, Dokumente), die zu parlamentarischen Aktivitäten gehören.

### Struktur
- **media_type**: Art der Mediendatei
  - **audio**: Audio-Aufzeichnung
  - **video**: Video-Aufzeichnung
  - **document**: Dokumente (PDF, etc.)
  - **image**: Bilder
- **url**: URL zur Mediendatei
- **mime_type**: MIME-Type (audio/mp3, video/mp4, application/pdf, etc.)
- **title**: Titel der Mediendatei
- **description**: Beschreibung
- **language**: Sprache (bei sprachbasierten Medien)
- **duration**: Dauer (bei Audio/Video, in Sekunden)
- **file_size**: Dateigrösse in Bytes
- **quality**: Qualitätsangabe (z.B. "720p", "high", "low")

### Designentscheid
**Warum generische Media-Entität?**
- Einheitliche Struktur für alle Medientypen
- Erweiterbar für neue Formate
- Technische Metadaten zentral erfasst
- Mehrere Qualitätsstufen derselben Aufzeichnung möglich

### Anwendung
Kann an verschiedene Entitäten gehängt werden:
```
Speech
  ├─ Media (Audio-Aufzeichnung, MP3, 256kbps)
  ├─ Media (Audio-Aufzeichnung, MP3, 128kbps)
  ├─ Media (Video-Aufzeichnung, MP4, 1080p)
  └─ Media (Video-Aufzeichnung, MP4, 480p)

AgendaItem
  └─ Media (PDF der Vorlage)

Meeting
  └─ Media (Livestream-URL)

{{include:ech-0293_operations/output/docs/TextSegment.md}}



{{include:ech-0293_operations/output/docs/Media.md}}

{{include:ech-0293_operations/output/docs/MultilingualString.md}}

{{include:ech-0293_operations/output/docs/Container.md}}
