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
| [MultilingualString](MultilingualString.md) |  |
| [Session](Session.md) |  |
| [Vote](Vote.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [agenda_items](agenda_items.md) |  |
| [end_date](end_date.md) | [en] The end date of the session |
| [id](id.md) |  |
| [language](language.md) | [en] Language code in ISO 639-1 format [de] Sprachcode im ISO 639-1-Format |
| [name](name.md) |  |
| [question](question.md) |  |
| [result](result.md) |  |
| [sessions](sessions.md) |  |
| [start_date](start_date.md) | [en] The start date of the session |
| [text](text.md) |  |
| [vote_time](vote_time.md) | [en] The date and time when the vote was cast |
| [votes](votes.md) |  |


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
