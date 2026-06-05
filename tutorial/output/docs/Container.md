

## Class: Container 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | None |
| sessions | * <br/> [Session](Session.md) | None |
| agenda_items | * <br/> [AgendaItem](AgendaItem.md) | None |
| votes | * <br/> [Vote](Vote.md) | None |

















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