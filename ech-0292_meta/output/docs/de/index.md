# meta

Dieses Schema modelliert Meta-Themen für die eCH Standards 0293-0297. In einem ersten Schritt werden FRBR-Entitäten modelliert, um die Verwaltung von Dokumenten und deren Übersetzungen zu ermöglichen.


URI: https://ch.paf.link/schema/meta

Name: meta



## Klassen

| Klasse | Beschreibung |
| --- | --- |
| [Date](Date.md) | Ein Datum mit Typangabe (z |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |
| [Manifestation](Manifestation.md) | FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL a... |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |
| [WorkContainer](WorkContainer.md) | Container für die Dokumente (FRBR Works) dieses Schemas |



## Slots

| Slot | Beschreibung |
| --- | --- |
| [date_type](date_type.md) | Bedeutung des Datums (z |
| [dates](dates.md) | Datumsangaben zum Element, jeweils mit Typangabe |
| [document_category](document_category.md) | Kategorie des Dokuments |
| [documents](documents.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind |
| [expression_description](expression_description.md) | Beschreibender Text zur Sprachfassung |
| [expression_language](expression_language.md) | Sprachcode im ISO 639-1-Format |
| [expression_title](expression_title.md) | Titel der Sprachfassung |
| [expressions](expressions.md) | Die Sprachfassungen (Expressions) eines Works |
| [format](format.md) | Das Dateiformat der Manifestation (z |
| [id](id.md) | Eindeutiger Identifikator des Elements |
| [manifestation_url](manifestation_url.md) | URL, unter der die Dateiform abgerufen werden kann |
| [manifestations](manifestations.md) | Die Dateiformen (Manifestations) einer Expression |
| [works](works.md) | Die im Container enthaltenen Dokumente (FRBR Works) |
| [xdate](xdate.md) | Der Datumswert selbst |


## Enums

| Aufzählung | Beschreibung |
| --- | --- |
| [DateTypesEnum](DateTypesEnum.md) | Bedeutung einer Datumsangabe |
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
