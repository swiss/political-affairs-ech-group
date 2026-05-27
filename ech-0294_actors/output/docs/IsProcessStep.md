

# Class: IsProcessStep 


_[de] Eine Mixin-Klasse für einen einzelnen Schritt in einem_

_mehrstufigen Prozess (z. B. Bearbeitungsschritt eines Geschäfts oder_

_Phasen­schritt einer Konsultation). Kombiniert Identifikations- und_

_Zeitdauer-Slots und ergänzt einen freien Bemerkungs-Slot. Konkrete_

_Step-Klassen ergänzen ihre eigenen typ-spezifischen Slots._

_[en] A mixin class for a single step in a multi-stage process (e.g.,_

_a deliberation step of an affair or a phase step of a consultation)._

_Combines identification and event-duration slots and adds a free-text_

_remark slot. Concrete step classes add their own type-specific slots._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| remark | 0..1 <br/> [String](String.md) | [de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext zu einem Prozessschritt oder einer Entität. [en] Free-text remark or note for edge cases or additional context on a process step or an entity.  |
| local_id | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer. [en] The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |



### Mixin Usage

| mixed into | description |
| --- | --- |





















</div>