# Enum: AgendaItemTypeEnum 




_[en] Type of agenda item, distinguishing individual items from grouped items._

_[de] Art des Traktandums, unterscheidet einzelne von gruppierten Traktanden._

__



URI: [ops:agenda_item_type_enum](https://ch.paf.link/schema/operations/agenda_item_type_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| item | ops:enum/agenda_item_type/item | [en] Individual agenda item (Traktandum) |
| group | ops:enum/agenda_item_type/group | [en] Group of agenda items (Traktandengruppe) |




## Slots

| Name | Description |
| ---  | --- |
| [agenda_item_type](agenda_item_type.md) | [en] Type of agenda item, distinguishing individual items from groups |





## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: agenda_item_type_enum
description: '[en] Type of agenda item, distinguishing individual items from grouped
  items.

  [de] Art des Traktandums, unterscheidet einzelne von gruppierten Traktanden.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  item:
    text: item
    description: '[en] Individual agenda item (Traktandum)

      [de] Einzelnes Traktandum

      '
    meaning: ops:enum/agenda_item_type/item
  group:
    text: group
    description: '[en] Group of agenda items (Traktandengruppe)

      [de] Traktandengruppe

      '
    meaning: ops:enum/agenda_item_type/group

```
</details>