

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




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'remark',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext '
     'zu einem Prozessschritt oder einer Entität.\n'
     '[en] Free-text remark or note for edge cases or additional context on a '
     'process step or an entity.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:remark',
  'owner': 'IsProcessStep',
  'domain_of': ['IsProcessStep'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext zu einem Prozessschritt oder einer Entität.
[en] Free-text remark or note for edge cases or additional context on a process step or an entity.
 | direct |
| SlotDefinition({
  'name': 'local_id',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.\n'
     '[en] Local identifier. For example, a UUID from the council information '
     'system.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:localId',
  'owner': 'IsProcessStep',
  'domain_of': ['HasIdentification'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.
[en] Local identifier. For example, a UUID from the council information system.
 | [HasIdentification](HasIdentification.md) |
| SlotDefinition({
  'name': 'global_uri',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Eine eindeutige, global gültige URI für die Entität.\n'
     '[en] A unique, globally valid URI for the entity.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:globalURI',
  'identifier': True,
  'owner': 'IsProcessStep',
  'domain_of': ['HasIdentification'],
  'range': 'uriorcurie',
  'required': True
}) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität.
[en] A unique, globally valid URI for the entity.
 | [HasIdentification](HasIdentification.md) |
| SlotDefinition({
  'name': 'wikidata_uri',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. '
     'https://www.wikidata.org/wiki/Q39 für die Schweiz.\n'
     '[en] A URI that refers to a Wikidata entity, e.g. '
     'https://www.wikidata.org/wiki/Q39 for Switzerland.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:wikidataUri',
  'owner': 'IsProcessStep',
  'domain_of': ['HasIdentification'],
  'range': 'uriorcurie'
}) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz.
[en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland.
 | [HasIdentification](HasIdentification.md) |
| SlotDefinition({
  'name': 'date_begin_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit '
     'Zeitdauer.\n'
     '[en] The actual start date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateBeginActual',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual start date of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |
| SlotDefinition({
  'name': 'datetime_begin_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder '
     'Vorkommens mit Zeitdauer.\n'
     '[en] The actual start date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeBeginActual',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual start date and time of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |
| SlotDefinition({
  'name': 'date_begin_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit '
     'Zeitdauer.\n'
     '[en] The planned start date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateBeginPlanned',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned start date of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |
| SlotDefinition({
  'name': 'datetime_begin_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder '
     'Vorkommens mit Zeitdauer.\n'
     '[en] The planned start date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeBeginPlanned',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned start date and time of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |
| SlotDefinition({
  'name': 'date_end_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit '
     'Zeitdauer.\n'
     '[en] The actual end date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateEndActual',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual end date of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |
| SlotDefinition({
  'name': 'datetime_end_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder '
     'Vorkommens mit Zeitdauer.\n'
     '[en] The actual end date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeEndActual',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual end date and time of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |
| SlotDefinition({
  'name': 'date_end_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.\n'
     '[en] The planned end date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateEndPlanned',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned end date of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |
| SlotDefinition({
  'name': 'datetime_end_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens '
     'mit Zeitdauer.\n'
     '[en] The planned end date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeEndPlanned',
  'owner': 'IsProcessStep',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned end date and time of an event or occurrence with time duration.
 | [IsEventWithDuration](IsEventWithDuration.md) |



## Mixin Usage

| mixed into | description |
| --- | --- |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:IsProcessStep |
| native | act:IsProcessStep |







