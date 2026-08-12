\newpage

# Texts and media

Parliamentary debates are recorded not only as structured data but also as texts and multimedia recordings. These entities enable the management of transcripts, audio and video recordings and further media formats, as well as the technical infrastructure for data exchange and multilingualism.

## TextSegment

### Purpose
Records text passages with versioning and language variants. Used primarily for transcriptions of speeches, but can also be applied to other text documents.

### Structure
- **text**: the actual text content
- **language**: language code (ISO 639-1)
- **format**: format of the text (plain, markdown, html)
- **version_type**: kind of version
  - **raw**: unedited raw transcript
  - **edited**: editorially revised version
  - **translated**: translation into another language
  - **summary**: summary

### Design decision
**Why a separate entity?**
- Allows several versions of the same text (raw, edited, translated)
- Version control and traceability of changes
- Flexibility regarding formats (plain, markdown, HTML for different output channels)

### Application
Mainly linked with Speech entities:
```
Speech
  ├─ TextSegment (raw transcript, de)
  ├─ TextSegment (edited protocol, de)
  ├─ TextSegment (translation, fr)
  └─ TextSegment (summary, de)
```

## Media

### Purpose
References media files (audio, video, documents) belonging to parliamentary activities.

### Structure
- **media_type**: kind of media file
  - **audio**: audio recording
  - **video**: video recording
  - **document**: documents (PDF, etc.)
  - **image**: images
- **url**: URL of the media file
- **mime_type**: MIME type (audio/mp3, video/mp4, application/pdf, etc.)
- **title**: title of the media file
- **description**: description
- **language**: language (for language-based media)
- **duration**: duration (for audio/video, in seconds)
- **file_size**: file size in bytes
- **quality**: quality indication (e.g. "720p", "high", "low")

### Design decision
**Why a generic Media entity?**
- Uniform structure for all media types
- Extensible for new formats
- Technical metadata recorded centrally
- Several quality levels of the same recording possible

### Application
Can be attached to various entities:
```
Speech
  ├─ Media (audio recording, MP3, 256 kbps)
  ├─ Media (audio recording, MP3, 128 kbps)
  ├─ Media (video recording, MP4, 1080p)
  └─ Media (video recording, MP4, 480p)

AgendaItem
  └─ Media (PDF of the bill)

Meeting
  └─ Media (livestream URL)
```

{{include:ech-0293_operations/output/docs/TextSegment.md}}

{{include:ech-0293_operations/output/docs/Media.md}}
