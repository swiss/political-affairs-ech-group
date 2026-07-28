

## Class: AgendaItem 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | None |
| name | * <br/> [MultilingualValue](MultilingualValue.md) | None |
| votes | * <br/> [Vote](Vote.md) | None |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Session](Session.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |
| [Vote](Vote.md) | [is_part_of_agenda_item](is_part_of_agenda_item.md) | range | [AgendaItem](AgendaItem.md) |
| [Container](Container.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |














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