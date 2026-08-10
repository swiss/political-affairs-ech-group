

## Klasse: IsEventWithDuration 


_Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkommnissen mit Zeitdauer zur Verfügung stellt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_begin_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| date_end_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| date_end_planned | 0..1 <br/> [Date](Date.md) | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |





















</div>