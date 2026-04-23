

# Slot: date_end_planned 


_[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer._

_[en] The planned end date of an event or occurrence with time duration._

__





URI: [mcm:dateEndPlanned](https://ld.ech.ch/schema/0292/meta-common/dateEndPlanned)
Alias: date_end_planned

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:dateEndPlanned](https://ld.ech.ch/schema/0292/meta-common/dateEndPlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateEndPlanned |
| native | ops:date_end_planned |




## LinkML Source

<details>
```yaml
name: date_end_planned
description: '[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.

  [en] The planned end date of an event or occurrence with time duration.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:dateEndPlanned
alias: date_end_planned
domain_of:
- IsEventWithDuration
range: date

```
</details>