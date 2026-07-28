# tutorial

[en] This is a dummy schema for a parliamentary affairs system, including sessions, agenda items, and votes. It is used to demonstrate the use of LinkML for defining data models. In this model, a session contains multiple agenda items and each agenda item can have multiple votes.
[de] Dies ist ein Dummy-Schema für ein System von parlamentarischen Angelegenheiten, das Sitzungen, Tagesordnungspunkte und Abstimmungen umfasst. Es wird verwendet, um die Verwendung von LinkML zur Definition von Datenmodellen zu demonstrieren. In diesem Modell enthält eine Sitzung mehrere Tagesordnungspunkte und jeder Tagesordnungspunkt kann mehrere Abstimmungen haben.


URI: https://ch.paf.link/schema/tutorial

Name: tutorial



## Classes

| Class | Description |
| --- | --- |
| [AgendaItem](AgendaItem.md) |  |
| [Container](Container.md) |  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |
| [HasTemporalValidity](HasTemporalValidity.md) | A mixin class that provides slots for modeling a temporal validity of informa... |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | A mixin class that provides slots for modeling instantaneous events or occurr... |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [Session](Session.md) |  |
| [Vote](Vote.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) | Abbreviation (can be multilingual) |
| [agenda_items](agenda_items.md) |  |
| [date_actual](date_actual.md) | The actual date of an instantaneous event or occurrence (without time duratio... |
| [date_begin_actual](date_begin_actual.md) | The actual start date of an event or occurrence with time duration |
| [date_begin_planned](date_begin_planned.md) | The planned start date of an event or occurrence with time duration |
| [date_created](date_created.md) | The date when an entity was created |
| [date_end_actual](date_end_actual.md) | The actual end date of an event or occurrence with time duration |
| [date_end_planned](date_end_planned.md) | The planned end date of an event or occurrence with time duration |
| [date_modified](date_modified.md) | The date when an entity was last modified |
| [date_planned](date_planned.md) | The planned date of an instantaneous event or occurrence (without time durati... |
| [datetime_actual](datetime_actual.md) | The actual date and time of an instantaneous event or occurrence (without tim... |
| [datetime_begin_actual](datetime_begin_actual.md) | The actual start date and time of an event or occurrence with time duration |
| [datetime_begin_planned](datetime_begin_planned.md) | The planned start date and time of an event or occurrence with time duration |
| [datetime_created](datetime_created.md) | The date and time when an entity was created |
| [datetime_end_actual](datetime_end_actual.md) | The actual end date and time of an event or occurrence with time duration |
| [datetime_end_planned](datetime_end_planned.md) | The planned end date and time of an event or occurrence with time duration |
| [datetime_modified](datetime_modified.md) | The date and time when an entity was last modified |
| [datetime_planned](datetime_planned.md) | The planned date and time of an instantaneous event or occurrence (without ti... |
| [global_uri](global_uri.md) | A unique, globally valid URI for the entity |
| [group_label](group_label.md) | Name of the body/group at time of linking |
| [id](id.md) |  |
| [is_active](is_active.md) | Indicates whether the information is currently valid |
| [is_part_of](is_part_of.md) |  |
| [is_part_of_agenda_item](is_part_of_agenda_item.md) |  |
| [label](label.md) | Assign a label to a structured piece of information (e |
| [label_long](label_long.md) | Assign an extended label to a structured piece of information (e |
| [language](language.md) | Language code in ISO 639-1 format (two lowercase letters, e |
| [local_id](local_id.md) | Local identifier |
| [multilingual_value](multilingual_value.md) | A multilingual value with language specification |
| [name](name.md) |  |
| [question](question.md) |  |
| [remark](remark.md) | Free-text remark or note for edge cases or additional context on a process st... |
| [result](result.md) |  |
| [sessions](sessions.md) |  |
| [text](text.md) |  |
| [valid_from](valid_from.md) | The date from which the information is valid |
| [valid_through](valid_through.md) | The date until which the information is valid, inclusive |
| [value](value.md) | The value of an information besides other attributes such as type, language, ... |
| [votes](votes.md) |  |
| [wikidata_uri](wikidata_uri.md) | A URI that refers to a Wikidata entity, e |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ResultEnum](ResultEnum.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
