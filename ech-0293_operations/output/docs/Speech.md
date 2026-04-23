

# Class: Speech 


_[en] A speech or statement made during a meeting (also called Votum or speaker segment)._

_[de] Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt)._

__





URI: [ops:Speech](https://ch.paf.link/schema/operations/Speech)





```mermaid
 classDiagram
    class Speech
    click Speech href "../Speech/"
      HasIdentification <|-- Speech
        click HasIdentification href "../HasIdentification/"
      HasCreationModificationDates <|-- Speech
        click HasCreationModificationDates href "../HasCreationModificationDates/"
      
      Speech : actor_fullname
        
      Speech : actor_id
        
      Speech : date_created
        
      Speech : date_modified
        
      Speech : datetime_begin
        
      Speech : datetime_created
        
      Speech : datetime_end
        
      Speech : datetime_modified
        
      Speech : global_uri
        
      Speech : landing_page
        
      Speech : language
        
      Speech : local_id
        
      Speech : media_format
        
      Speech : media_type
        
      Speech : media_url
        
      Speech : role
        
      Speech : start
        
      Speech : text
        
      Speech : text_format
        
      Speech : text_type
        
      Speech : wikidata_uri
        
      
```





## Inheritance
* **Speech** [ [HasIdentification](HasIdentification.md) [HasCreationModificationDates](HasCreationModificationDates.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [language](language.md) | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format | direct |
| [start](start.md) | 0..1 <br/> [String](String.md) | Start indicator or position | direct |
| [datetime_begin](datetime_begin.md) | 0..1 <br/> [Datetime](Datetime.md) | [en] The date and time when the meeting or voting begins | direct |
| [datetime_end](datetime_end.md) | 0..1 <br/> [Datetime](Datetime.md) | [en] The date and time when the meeting or voting ends | direct |
| [actor_fullname](actor_fullname.md) | 0..1 <br/> [String](String.md) | Full name of the actor/person | direct |
| [actor_id](actor_id.md) | 0..1 <br/> [String](String.md) | [en] The political body organized by the term of office (e | direct |
| [role](role.md) | 0..1 <br/> [String](String.md) | Role of the person (e | direct |
| [text](text.md) | 1 <br/> [String](String.md) |  | direct |
| [text_format](text_format.md) | 0..1 <br/> [String](String.md) | [en] Format of text (text, html, html_with_timestamps) | direct |
| [text_type](text_type.md) | 0..1 <br/> [String](String.md) | [en] Type of text (raw draft, edited version) | direct |
| [landing_page](landing_page.md) | 0..1 <br/> [String](String.md) | [en] URL providing further information | direct |
| [media_url](media_url.md) | 0..1 <br/> [String](String.md) | URL to media file (audio/video) | direct |
| [media_type](media_type.md) | 0..1 <br/> [String](String.md) | Type of media (audio, video, document) | direct |
| [media_format](media_format.md) | 0..1 <br/> [String](String.md) | MIME type of the media file | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:Speech |
| native | ops:Speech |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Speech
description: '[en] A speech or statement made during a meeting (also called Votum
  or speaker segment).

  [de] Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt).

  '
from_schema: https://ch.paf.link/schema/operations
mixins:
- HasIdentification
- HasCreationModificationDates
slots:
- language
- start
- datetime_begin
- datetime_end
- actor_fullname
- actor_id
- role
- text
- text_format
- text_type
- landing_page
- media_url
- media_type
- media_format

```
</details>

### Induced

<details>
```yaml
name: Speech
description: '[en] A speech or statement made during a meeting (also called Votum
  or speaker segment).

  [de] Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt).

  '
from_schema: https://ch.paf.link/schema/operations
mixins:
- HasIdentification
- HasCreationModificationDates
attributes:
  language:
    name: language
    description: '[de] Sprachcode im ISO 639-1 Format.

      [en] Language code in ISO 639-1 format.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:language
    alias: language
    owner: Speech
    domain_of:
    - Speech
    - MultilingualString
    - MultilingualValue
    range: string
    pattern: ^[a-z]{2}$
  start:
    name: start
    description: Start indicator or position
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: start
    owner: Speech
    domain_of:
    - Speech
    range: string
  datetime_begin:
    name: datetime_begin
    description: '[en] The date and time when the meeting or voting begins.

      [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: datetime_begin
    owner: Speech
    domain_of:
    - Voting
    - Election
    - Attendance
    - Speech
    range: datetime
  datetime_end:
    name: datetime_end
    description: '[en] The date and time when the meeting or voting ends.

      [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: datetime_end
    owner: Speech
    domain_of:
    - Voting
    - Election
    - Speech
    range: datetime
  actor_fullname:
    name: actor_fullname
    description: Full name of the actor/person
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: actor_fullname
    owner: Speech
    domain_of:
    - Speech
    range: string
  actor_id:
    name: actor_id
    description: '[en] The political body organized by the term of office (e.g., Regierungsrat,
      Nationalrat, Ständerat).

      [de] Das politische Organ, das durch die Amtsdauer organisiert wird (z.B. Regierungsrat,
      Nationalrat, Ständerat).

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: actor_id
    owner: Speech
    domain_of:
    - Legislature
    - Meeting
    - Voting
    - IndividualVote
    - Election
    - Attendance
    - IndividualAttendance
    - Speech
    range: string
  role:
    name: role
    description: Role of the person (e.g., commission speaker)
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: role
    owner: Speech
    domain_of:
    - Speech
    range: string
  text:
    name: text
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: text
    owner: Speech
    domain_of:
    - Speech
    - TextSegment
    - MultilingualString
    range: string
    required: true
  text_format:
    name: text_format
    description: '[en] Format of text (text, html, html_with_timestamps)

      [de] Format des Textes (text, html, html_with_timestamps)

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: text_format
    owner: Speech
    domain_of:
    - Speech
    range: string
  text_type:
    name: text_type
    description: '[en] Type of text (raw draft, edited version)

      [de] Typ des Textes (Rohfassung, bearbeitete Fassung)

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: text_type
    owner: Speech
    domain_of:
    - Speech
    range: string
  landing_page:
    name: landing_page
    description: '[en] URL providing further information.

      [de] URL mit weiteren Informationen.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:landingPage
    alias: landing_page
    owner: Speech
    domain_of:
    - Legislature
    - Meeting
    - AgendaItem
    - Voting
    - Election
    - Speech
    range: string
  media_url:
    name: media_url
    description: URL to media file (audio/video)
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: media_url
    owner: Speech
    domain_of:
    - Speech
    range: string
  media_type:
    name: media_type
    description: Type of media (audio, video, document)
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: media_type
    owner: Speech
    domain_of:
    - Speech
    - Media
    range: string
  media_format:
    name: media_format
    description: MIME type of the media file
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: media_format
    owner: Speech
    domain_of:
    - Speech
    range: string
  local_id:
    name: local_id
    description: '[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      [en] Local identifier. For example, a UUID from the council information system.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:localId
    alias: local_id
    owner: Speech
    domain_of:
    - HasIdentification
    range: string
  global_uri:
    name: global_uri
    description: '[de] Eine eindeutige, global gültige URI für die Entität.

      [en] A unique, globally valid URI for the entity.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:globalURI
    identifier: true
    alias: global_uri
    owner: Speech
    domain_of:
    - HasIdentification
    range: uriorcurie
    required: true
  wikidata_uri:
    name: wikidata_uri
    description: '[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39
      für die Schweiz.

      [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39
      for Switzerland.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:wikidataUri
    alias: wikidata_uri
    owner: Speech
    domain_of:
    - HasIdentification
    range: uriorcurie
  date_created:
    name: date_created
    description: '[de] Das Datum, an dem eine Entität erstellt wurde.

      [en] The date when an entity was created.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateCreated
    alias: date_created
    owner: Speech
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_created:
    name: datetime_created
    description: '[de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.

      [en] The date and time when an entity was created.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeCreated
    alias: datetime_created
    owner: Speech
    domain_of:
    - HasCreationModificationDates
    range: datetime
  date_modified:
    name: date_modified
    description: '[de] Das Datum, an dem eine Entität zuletzt geändert wurde.

      [en] The date when an entity was last modified.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateModified
    alias: date_modified
    owner: Speech
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_modified:
    name: datetime_modified
    description: '[de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert
      wurde.

      [en] The date and time when an entity was last modified.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeModified
    alias: datetime_modified
    owner: Speech
    domain_of:
    - HasCreationModificationDates
    range: datetime

```
</details>