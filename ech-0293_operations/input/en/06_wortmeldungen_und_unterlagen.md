\newpage

<!-- ToDo: David -->


Debate

* -> video recording -> speech transcript
*   -> verbatim protocol -> text to timestamp -> text contains the timestamps -> text document (with or without a definition of the format (span types))
*   -> edited protocol -> agenda item to timestamp

## Speech

## Term and meaning

A speech denotes an oral contribution by a person during a parliamentary sitting. It is the central instrument of political debate and of expressing opinions in parliament.

## Types of speeches

Parliamentary speeches take various forms:

### Main statements
- Detailed positions on an affair
- Justification of motions
- Presentation of the group's opinion

### Short interventions
- Brief statements
- Interposed questions
- Corrections

### Group declarations
- Official position of a parliamentary group
- Delivered by the group's spokesperson

### Government statements
- Positions of government members
- Answering of questions
- Defence of bills

## Structure and assignment

A speech is always assigned to a specific context:

```
Meeting (sitting)
  └─ AgendaItem
      └─ Speech (statement of person A)
          ├─ TextSegment (transcription)
          ├─ Media (audio recording)
          └─ Media (video recording)
```

### Assignment fields

- **meeting_id**: the sitting in which the speech was made
- **agenda_item_id**: the agenda item that was spoken to
- **person_id**: the speaking person (according to eCH-0294 Actors)

## Identification of the speakers

- **person_id**: unique identification of the person
- **person_name**: name for quick access
- **role**: role of the person (e.g. "group president", "rapporteur", "Federal Councillor")

## Temporal recording

- **start_time**: start of the speech
- **end_time**: end of the speech
- **duration**: duration in seconds (calculated or recorded)

These time indications enable:
- precise referencing in audio and video recordings
- analysis of speaking time per person / group
- monitoring of compliance with time limits

## Language of the speech

The field **language** records the language in which the speech was made:

- **de**: German
- **fr**: French
- **it**: Italian
- **rm**: Romansh
- **en**: English

## Text documents

The field **text_segments** references TextSegment entities containing the spoken text.

### Different text versions

#### Raw transcript
- Verbatim transcription
- Unedited, with filler words
- Available directly after the sitting

#### Edited transcript
- Editorially revised
- Grammatically corrected
- Official protocol version

#### Translations
- Into other national languages
- For international publications

### TextSegment structure

Every TextSegment can contain:
- **text**: the actual text
- **language**: language of the text
- **version**: kind of version (raw, edited, translated)
- **format**: format (plain, markdown, HTML)

## Multimedia recordings

The field **media** references Media entities with audio and video recordings.

### Audio recordings
- Original sound of the speech
- Format: MP3, WAV, etc.
- Technical metadata (quality, bitrate)

### Video recordings
- Visual recording (in plenary sittings)
- Format: MP4, WebM, etc.
- Various resolutions

### Livestreaming
- Real-time transmission
- URL of the stream
- Archiving after the sitting

## Title and description

- **title**: short title (e.g. "Statement on energy policy")
- **description**: summary or context of the speech

## Type of speech

The field **speech_type** can distinguish various kinds:

- **statement**: position statement
- **question**: question
- **response**: answer (e.g. government to a question)
- **procedural**: procedural motion
- **declaration**: declaration

{{include:ech-0293_operations/output/docs/Speech.md}}


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

{{include:ech-0293_operations/output/docs/MultilingualString.md}}

{{include:ech-0293_operations/output/docs/Container.md}}
