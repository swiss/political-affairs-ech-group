

## Class: IsEventWithDuration 


_A mixin class that provides slots for modeling events or occurrences with time duration._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | The actual start date of an event or occurrence with time duration.  |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual start date and time of an event or occurrence with time duration.  |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | The planned start date of an event or occurrence with time duration.  |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned start date and time of an event or occurrence with time duration.  |
| date_end_actual | 0..1 <br/> [Date](Date.md) | The actual end date of an event or occurrence with time duration.  |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual end date and time of an event or occurrence with time duration.  |
| date_end_planned | 0..1 <br/> [Date](Date.md) | The planned end date of an event or occurrence with time duration.  |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned end date and time of an event or occurrence with time duration.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |





















</div>