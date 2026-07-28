

## Class: Session 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | None |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | The actual start date of an event or occurrence with time duration.  |
| date_end_actual | 0..1 <br/> [Date](Date.md) | The actual end date of an event or occurrence with time duration.  |
| name | * <br/> [MultilingualValue](MultilingualValue.md) | None |
| agenda_items | * <br/> [AgendaItem](AgendaItem.md) | None |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [sessions](sessions.md) | range | [Session](Session.md) |














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