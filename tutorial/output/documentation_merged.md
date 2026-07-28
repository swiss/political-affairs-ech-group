# Head

Header Text from the input markdown file.

# Intro

Intro Text from the input markdown file.

# Introduction to Sessions Schema

# Classes

| Class | Description |
| --- | --- |
| [AgendaItem](#AgendaItem) | None |
| [Container](#Container) | None |
| [Session](#Session) | None |
| [Vote](#Vote) | None |



## Class: AgendaItem 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](#String) | None |
| name | * <br/> [MultilingualValue](#MultilingualValue) | None |
| votes | * <br/> [Vote](#Vote) | None |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Session](#Session) | [agenda_items](#agenda_items) | range | [AgendaItem](#AgendaItem) |
| [Vote](#Vote) | [is_part_of_agenda_item](#is_part_of_agenda_item) | range | [AgendaItem](#AgendaItem) |
| [Container](#Container) | [agenda_items](#agenda_items) | range | [AgendaItem](#AgendaItem) |














### Examples
#### Example: AgendaItem-hierarchical__en__en

```yaml
id: tutorial:s2025-2_t1
name:
- value: Landeshymne
  language: de
- value: National Anthem
  language: en
votes:
- id: tutorial:s2025-2_t1_a1
  question: Soll die Hymne geändert werden?
  datetime_actual: '2025-06-15T10:00:00+01:00'
  result: 'no'

```
#### Example: AgendaItem-flat__de

```yaml
id: tutorial:s2025-2_t1
name:
- value: Landeshymne
  language: de

```






</div>


## Class: Container 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](#String) | None |
| sessions | * <br/> [Session](#Session) | None |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | None |
| votes | * <br/> [Vote](#Vote) | None |

















### Examples
#### Example: Container-hierarchical

```yaml
id: tutorial:s2025
sessions:
  - id: tutorial:s2025-1
    date_begin_actual: "2025-03-01"
    date_end_actual: "2025-04-10"
    name: 
      - value: Frühlingssession 2025
        language: de
      - value: Spring Session 2025
        language: en
    agenda_items:
      - id: tutorial:s2025-1_t1
        name:
          - value: Fahnenfarbe
            language: de
          - value: Flag Color
            language: en
        votes:
          - id: tutorial:s2025-1_t1_a1
            question: Soll die Farbe geändert werden?
            datetime_actual: "2025-03-15T10:00:00Z"
            result: "yes"
          - id: tutorial:s2025-1_t1_a2
            question: Soll die Farbe Auberginen-Oliv werden?
            datetime_actual: "2025-03-16T10:00:00Z"
            result: "no"
  - id: tutorial:s2025-2
    date_begin_actual: "2025-06-01"
    date_end_actual: "2025-07-10"
    name: 
      - value: Sommersession 2025
        language: de
      - value: Summer Session 2025
        language: en
    agenda_items:
      - id: tutorial:s2025-2_t1
        name: 
          - value: Landeshymne
            language: de
          - value: National Anthem
            language: en
        votes:
          - id: tutorial:s2025-2_t1_a1
            question: Soll die Hymne geändert werden?
            datetime_actual: "2025-06-15T10:00:00+01:00"
            result: "no"
```
#### Example: Container-flat

```yaml
id: tutorial:s2025
sessions: 
  - id: tutorial:s2025-1
    date_begin_actual: 2025-03-01
    date_end_actual: 2025-04-10
    name: 
      - value: Frühlingssession 2025
        language: de
      - value: Spring Session 2025
        language: en
  - id: tutorial:s2025-2
    date_begin_actual: 2025-06-01
    date_end_actual: 2025-07-10
    name: 
      - value: Sommersession 2025
        language: de
      - value: Summer Session 2025
        language: en
agenda_items:
  - id: tutorial:s2025-1_t1
    name:
      - value: Fahnenfarbe
        language: de
  - id: tutorial:s2025-2_t1
    name: 
      - value: Landeshymne
        language: de
votes:
  - id: tutorial:s2025-1_t1_a1
    is_part_of_agenda_item: tutorial:s2025-1_t1
    is_part_of: tutorial:s2025-1_t1
    question: Soll die Farbe geändert werden?
  - id: tutorial:s2025-1_t1_a2
    is_part_of_agenda_item: tutorial:s2025-1_t1
    is_part_of: tutorial:s2025-1_t1
    question: Soll die Farbe Auberginen-Oliv werden?
  - id: tutorial:s2025-2_t1_a1
    is_part_of_agenda_item: tutorial:s2025-2_t1
    is_part_of: tutorial:s2025-2_t1
    question: Soll die Hymne geändert werden?
```






</div>


## Class: Session 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](#String) | None |
| date_begin_actual | 0..1 <br/> [Date](#Date) | The actual start date of an event or occurrence with time duration.  |
| date_end_actual | 0..1 <br/> [Date](#Date) | The actual end date of an event or occurrence with time duration.  |
| name | * <br/> [MultilingualValue](#MultilingualValue) | None |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | None |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [sessions](#sessions) | range | [Session](#Session) |














### Examples
#### Example: Session-hierarchical__en

```yaml
id: tutorial:s2025-2
date_begin_actual: '2025-06-01'
date_end_actual: '2025-07-10'
name:
- value: Sommersession 2025
  language: de
- value: Summer Session 2025
  language: en
agenda_items:
- id: tutorial:s2025-2_t1
  name:
  - value: Landeshymne
    language: de
  - value: National Anthem
    language: en
  votes:
  - id: tutorial:s2025-2_t1_a1
    question: Soll die Hymne geändert werden?
    datetime_actual: '2025-06-15T10:00:00+01:00'
    result: 'no'

```
#### Example: Session-flat__en

```yaml
id: tutorial:s2025-2
date_begin_actual: 2025-06-01
date_end_actual: 2025-07-10
name:
- value: Sommersession 2025
  language: de
- value: Summer Session 2025
  language: en

```






</div>


## Class: Vote 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](#String) | None |
| is_part_of | 0..1 <br/> [Uriorcurie](#Uriorcurie) | None |
| question | 1 <br/> [String](#String) | None |
| datetime_actual | 0..1 <br/> [Datetime](#Datetime) | The actual date and time of an instantaneous event or occurrence (without time duration).  |
| result | 0..1 <br/> [ResultEnum](#ResultEnum) | None |
| is_part_of_agenda_item | 0..1 <br/> [AgendaItem](#AgendaItem) | None |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AgendaItem](#AgendaItem) | [votes](#votes) | range | [Vote](#Vote) |
| [Container](#Container) | [votes](#votes) | range | [Vote](#Vote) |



















</div>
