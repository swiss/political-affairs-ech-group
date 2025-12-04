

# Slot: agenda_item_description 


_[en] Subtitle or detailed description of the agenda item._

_[de] Untertitel oder ausführliche Beschreibung des Traktandums._

__





URI: [ops:agenda_item_description](https://ch.paf.link/schema/operations/agenda_item_description)
Alias: agenda_item_description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |






## Properties

* Range: [MultilingualString](MultilingualString.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:agenda_item_description |
| native | ops:agenda_item_description |




## LinkML Source

<details>
```yaml
name: agenda_item_description
description: '[en] Subtitle or detailed description of the agenda item.

  [de] Untertitel oder ausführliche Beschreibung des Traktandums.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: agenda_item_description
domain_of:
- AgendaItem
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>