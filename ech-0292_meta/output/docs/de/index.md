# meta

Dieses Schema modelliert Meta-Themen für die eCH Standards 0293-0297. In einem ersten Schritt werden FRBR-Entitäten modelliert, um die Verwaltung von Dokumenten und deren Übersetzungen zu ermöglichen.


URI: https://ch.paf.link/schema/meta

Name: meta



## Klassen

| Klasse | Beschreibung |
| --- | --- |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |
| [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum... |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderu... |
| [HasIdentification](HasIdentification.md) | Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügu... |
| [HasReferenceIdentification](HasReferenceIdentification.md) | Eine Mixin-Klasse, welche die Slots bereitstellt, mit denen eine Referenz die... |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |
| [IsEventWithDuration](IsEventWithDuration.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkom... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen... |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |
| [Manifestation](Manifestation.md) | FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL a... |
| [MultilingualUri](MultilingualUri.md) | Eine URI zusammen mit der Sprache der Ressource, auf die sie verweist |
| [MultilingualValue](MultilingualValue.md) | Ein mehrsprachiger String mit Angabe der Sprache |
| [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum... |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |
| [WorkContainer](WorkContainer.md) | Container für die Dokumente (FRBR Works) dieses Schemas |



## Slots

| Slot | Beschreibung |
| --- | --- |
| [abbreviation](abbreviation.md) | Abkürzung (kann mehrsprachig sein) |
| [date_actual](date_actual.md) | Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommnissen (ohne... |
| [date_begin_actual](date_begin_actual.md) | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdaue... |
| [date_begin_planned](date_begin_planned.md) | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_created](date_created.md) | Das Datum, an dem eine Entität erstellt wurde |
| [date_end_actual](date_end_actual.md) | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_end_planned](date_end_planned.md) | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_modified](date_modified.md) | Das Datum, an dem eine Entität zuletzt geändert wurde |
| [date_planned](date_planned.md) | Das geplante Datum eines instantanen Ereignisses oder Vorkommnissen (ohne Zei... |
| [datetime_actual](datetime_actual.md) | Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses oder Vor... |
| [datetime_begin_actual](datetime_begin_actual.md) | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnis... |
| [datetime_begin_planned](datetime_begin_planned.md) | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen ... |
| [datetime_created](datetime_created.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde |
| [datetime_end_actual](datetime_end_actual.md) | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnisse... |
| [datetime_end_planned](datetime_end_planned.md) | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mi... |
| [datetime_modified](datetime_modified.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde |
| [datetime_planned](datetime_planned.md) | Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkomm... |
| [document_category](document_category.md) | Kategorie des Dokuments |
| [documents](documents.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind |
| [expression_description](expression_description.md) | Beschreibender Text zur Sprachfassung |
| [expression_language](expression_language.md) | Sprachcode im ISO 639-1-Format |
| [expression_title](expression_title.md) | Titel der Sprachfassung |
| [expressions](expressions.md) | Die Sprachfassungen (Expressions) eines Works |
| [format](format.md) | Das Dateiformat der Manifestation (z |
| [global_uri](global_uri.md) | Eine eindeutige, global gültige URI für die Entität |
| [group_label](group_label.md) | Name des Gremiums zum Zeitpunkt der Verknüpfung |
| [is_active](is_active.md) | Gibt an, ob die Information aktuell gültig ist |
| [label](label.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw |
| [label_long](label_long.md) | Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu ver... |
| [language](language.md) | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z |
| [local_id](local_id.md) | Lokaler Identifikator |
| [manifestation_url](manifestation_url.md) | URL, unter der die Dateiform abgerufen werden kann |
| [manifestations](manifestations.md) | Die Dateiformen (Manifestations) einer Expression |
| [multilingual_value](multilingual_value.md) | Ein mehrsprachiger Wert mit Angabe der Sprache |
| [remark](remark.md) | Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext zu ei... |
| [valid_from](valid_from.md) | Das Datum, ab dem die Information gültig ist |
| [valid_through](valid_through.md) | Das Datum, bis und mit dem die Information gültig ist |
| [value](value.md) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Spr... |
| [wikidata_uri](wikidata_uri.md) | Eine URI, die auf eine Wikidata-Entität verweist, z |
| [works](works.md) | Die im Container enthaltenen Dokumente (FRBR Works) |


## Enums

| Aufzählung | Beschreibung |
| --- | --- |
| [DocumentCategoryEnum](DocumentCategoryEnum.md) | Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards 0292-0... |


## Typen

| Typ | Beschreibung |
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

| Subset | Beschreibung |
| --- | --- |
