---
title: "eCH-0292 Metaprozesse zu politischen Geschäften"
lang: de
toc: false
---

|**Name**|**Metaprozesse zu politischen Geschäften**|
|---|---|
|**eCH-Nummer**|eCH-0292|
|**Kategorie**|Standard|
|**Reifegrad**|Definiert|
|**Version**|0.1.0|
|**Status**|In Arbeit|
|**Beschluss am**||
|**Ausgabedatum**||
|**Ersetzt Version**||
|**Voraussetzungen**||
|**Beilagen**|-|
|**Sprachen**|Deutsch (Original) - English (Datamodel)|
|**Autoren**|Fachgruppe Politische Geschäfte: Florin Hasler, Moret Michel, Benedikt Hitz, Jonas Schär, Daniela Koller, Simon Graf, Fabian Davolio, Martin Gadjos|
|**Herausgeber / Vertrieb**|Verein eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Abstrakt


\newpage

# Inhaltsverzeichnis

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Rechtsklick &gt; „Felder aktualisieren“, um das Inhaltsverzeichnis zu erzeugen.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```


\newpage

# Design Principles

The following design principles apply to all data models developed by the eCH Specialist Group Political Affairs.

## Data Exchange Focus

The eCH Specialist Group Political Affairs focuses on **data exchange** between different systems. Therefore, the data schema is designed to facilitate interoperability and data sharing. It is not intended to model the internal workings of any specific system.

## Identifiers and URIs

There is always the possibility to identify an entity with either an internal/local identifier (`ID`) or a global `URI`. The design principle is to always have both, so that data can be linked globally but also work in isolated systems.

## Normalization

The data schema follows a pragmatic approach to normalization. The basic principle is to avoid redundancy where possible. The main reason for not fully normalizing the data schema is that there is no single authority for many entities in the political domain. Therefore, some redundancy is accepted to allow for easier data integration and historical tracking.

## Versioning

There is no general versioning of entities in the data schema. The main reason for this is that versioning can lead to significant complexity in data management and querying. However, versioning can be implemented for specific entities where it makes sense and is required by the use case. In such a case, the versioning mechanism is part of the data model for that specific entity.

An example of this would be the occupation of a person. Each occupation can have a start and end date, allowing to track changes over time without versioning the person entity itself.

## Local References

Some entities are referenced "locally" in addition to linking to the full entity. This is done to have useful local data without too much query complexity. This will also generate some form of versioning implicitly, as the local reference will not change when the full entity changes.

An example of this would be that a motion links to the person who submitted it. In addition to the link to the full person entity, the information of e.g. the political party at the time of the submission or the role of the person is stored "locally" in the motion entity. This way, even if the person changes party and/or role later on, the motion still contains the correct information at the time of submission.

### Example of Local Reference

The following example shows a motion with a local reference to the submitter (person) and the actual person entity. The motion contains the correct information about the submitter at the time of submission, even if the person changes party and/or role later on.

This is a **simplified example**, in a real use case there would be more information about the motion and the person.

```yaml
motion:
  id: ex:m1
  date: 2012-04-01
  title: "Motion 1"
  submitter: # local reference to person, class PersonReference
    id: ex:p1
    name: "John Doe"
    party: "Party A"
    role: "Member of Parliament"
```

```yaml
person:
  id: ex:p1
  name: "John Doe"
  parties: 
    - party: "Party B"
      valid_from: 2016-01-01
    - party: "Party A"
      valid_from: 1990-01-01
      valid_through: 2015-12-31
  roles: 
    - role: "Minister"
      valid_from: 2019-01-01
    - role: "Member of Parliament"
      valid_from: 2010-07-01
      valid_through: 2018-12-31
```

\newpage

# Common Data Elements

One of the outputs of the eCH-0292 subgroup is a set of **common data elements** that can be used across all the standards developed by the eCH Specialist Group Political Affairs without duplication.

## Defining Common Data Elements

The common data elements are defined in the `schema_common.yaml` file. The classes and their slots defined in this file will mainly be used as **mixins** in the specific standards. With this approach, a class that declares a mixin can use all the slots defined in the mixin class without having to redefine them. This allows for a consistent definition of common data elements across all standards.

## Using Common Data Elements

The common data elements can be used by importing the `schema_common.yaml` file into the LinkML schema of a specific standard. This happens in the `import` section of the LinkML schema:

```yaml
imports:
  - linkml:types
  - ../../ech-0292_meta/input/schema_common
```

Afterwards, all the elements defined in the `schema_common.yaml` file can be used in the specific standard:

```yaml
classes:
    Person:
        description: A person with identifiers, names, addresses, citizenships, and occupations.
        mixins:
            - HasIdentification #import from schema_common.yaml
            - HasCreationModificationDates #import from schema_common.yaml
```

\newpage

# Data Publishing

* Stabilität Location (Permant Identifier, DOI, ARK) 
* Format(e)?
  * minimale Formate?
  * CSV, JSON, XML, ...
  * Linked Data RDF
  * API Direkt Ratssystem / Indirekt Datenplattform
  * ZIP Packages? Regeln zu Bennenung
* Umwandlung nach eCH durch Pipeline
* Periodizität
* Plattformen?

* Übergang ins Archiv?

https://www.w3.org/Provider/Style/URI

GAP (https://www.go-fair.org/fair-principles/):
* Daten werden nicht publiziert. FAIR
* Zugang wird eingeschränkt, wie geht man mit Throttling, Robots um? Data Delivery Contracts -> API Keys 
* Daten sind nicht einfach auffindbar. (Gleiche Stichwörter in Datenplattformen.) FAIR
* Fehlende Metadaten: FAIR 
  * Eigenene Identität (Erst publizierend / Aggregator)
  * Attribute: Exekutive vs Legeslative
  * Attribute: Kompetenzen
  * Attribute: Lizenzen
* Daten werden als obsolet markiert, versionisiert, geändert (Korrekturen). 
* Future: Data Streams sind nicht vorhanden.
* Datenelemente / Inhalte -> Identifikatoren! UUID vs echten Identifikatoren FAIR
* Authentizität und Signierung

\newpage

# Richtext Definition

+ Unicode

| Zweck        | Element                                         | HTML                                                              | Bemerkung                                                                                                                            |
| ------------ | ----------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Gliederung   | Paragraph                                       | `<p>`                                                            | CSS-Styles, Klassen und in-line Definitionen sind nicht erlaubt.                                                                     |
| Gliederung   | Titel                                           | `<h2>`–`<h4>`                                                   | Nur `<h2>`, `<h3>` und `<h4>` sind erlaubt. H1 wird meist als eigenes Titeldatenfeld mitgeliefert.                                |
| Elemente     | Tabelle Kopf Inhalt                             | `<table>` `<thead>` `<tbody>` `<tr>` `<td>`                  | Styles sind auch in Tabellen nicht erlaubt. Ein angehängtes `<figure>` ist erlaubt.                                                 |
| Elemente     | Bild                                            | `<img>`                                                          | Bilder in einem Text müssen inline mit BASE64 geliefert werden. Externe Links sind nicht erlaubt.                                    |
| Elemente     | Links                                           | `<a href>`                                                       | Keine Einschränkungen; es muss darauf geachtet werden, dass es sich um öffentlich zugängliche und langfristig stabile Links handelt. |
| Elemente     | Geordnete Liste / Ungeordnete Liste             | `<ol>` `<ul>` `<li>`                                           | Die Attribute `list-style-types` und `start` sind erlaubt.                                                                           |
| Formatierung | Kursiv / Fett / Unterstrichen / Durchgestrichen | `<i>` `<em>` `<b>` `<strong>` `<u>` `<s>` `<sub>` `<sup>` | Alle Elemente sind erlaubt. `<em>` und `<strong>` werden `<i>` und `<b>` vorgezogen, da sie semantisch statt typografisch sind.  |
| Formatierung | Allgemein                                       | —                                                                 | CSS-Styles, Klassen und Inline-Definitionen sind nicht erlaubt.                                                                      |
| Formatierung | Schriftgrösse                                   | `<span style="font-size: 18px;">`                                | Nicht erlaubt.                                                                                                                       |
| Formatierung | Schriftfarbe                                    | `<mark class=*>` `<span style="color: rgb(184, 49, 47);">`      | Nicht erlaubt.                                                                                                                       |
| Formatierung | Schriftart                                      | `<span style="font-family: Impact, Charcoal, sans-serif;">`      | Nicht erlaubt.                                                                                                                       |
| Formatierung | Einrücken                                       | `<p style="margin-left: 20px">`                                  | Nicht erlaubt.                                                                                                                       |
| Formatierung | Ausrichtung                                     | `<p style="text-align: center;">`                                | Nicht erlaubt.                                                                                                                       |

\newpage

# Documents as a last-resort fallback

The schemas of this eCH expert group are designed to publish information as structured data whenever possible.

Documents should therefore not be used as the normal way to convey information. They may be added to the data model only as a last resort, when the relevant information cannot yet be represented in a structured form.

This fallback supports the gradual transition from legacy documents to a fully data-modelled approach.

# Modelling of the document structure (FRBR)

As in other data models, we propose adopting the Functional Requirements for Bibliographic Records (FRBR) model. This approach is also used by ELI, which this eCH expert group uses for legal texts.

The hierarchy of classes makes it possible to represent different versions of a document and to extend them later, for example with regard to language and format.

The model distinguishes between a Work, an Expression, and a Manifestation. The following definitions and examples are based on Wikipedia:

## Work

Abstract: A work is a "distinct intellectual or artistic creation." For example, Beethoven's Ninth Symphony is a work, regardless of who performs it.

The work is the main container for one document. It holds different expressions and manifestions for different versions of the same document. But it shall not be used to mix documents with different content. 

It holds the unique identifier for this work and a document category for a high-level overview. The document categories are defined by this standard.

Attached to the Work is one or multiple expressions as described below.



### Klasse: Work []{#Work}


_FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten Sprachfassung oder einem Dateiformat._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| document_category | 0..1 <br/> [DocumentCategoryEnum](#DocumentCategoryEnum) | Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch 'other' verwendet.  |
| expressions | * <br/> [Expression](#Expression) | Die Sprachfassungen (Expressions) eines Works.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| WorkContainer | works | range | [Work](#Work) |



















</div>

### Dokumentenkategorien (document_category)

### Enum: DocumentCategoryEnum []{#DocumentCategoryEnum}




_Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards 0292-0297 referenziert werden. Mehrsprachige Labels (DE/FR/IT/RM/EN) sind über `annotations` (Konvention `label_xx`) abgebildet; Erstvorschläge für FR/IT/RM stehen unter Plenum-Review._




<div data-search-exclude markdown="1">

URI: [meta:DocumentCategoryEnum](https://ch.paf.link/schema/meta/DocumentCategoryEnum)

#### Zulässige Werte
| Wert | Beschreibung | Zusätzliche Info |
|----------------------|----------------------------------------------------------|--------------------|
| meeting_planning ([meta:vocabulary/document_category/MeetingPlanning](meta:vocabulary/document_category/MeetingPlanning)) | Planung von Sitzungen und Sessionen. Beispiele: Einladung, Sitzplan, Zeitbudget, Fristen für Einzelanträge.  | Title: Meeting planning<br>|
| meeting_documents ([meta:vocabulary/document_category/MeetingDocuments](meta:vocabulary/document_category/MeetingDocuments)) | Unterlagen zu den Geschäften einer Sitzung. Beispiele: Traktandenliste, Sessionsprogramm, Vorstossliste.  | Title: Meeting documents<br>|
| protocol ([meta:vocabulary/document_category/Protocol](meta:vocabulary/document_category/Protocol)) | Aufzeichnung des Verlaufs einer Sitzung. Beispiele: Wortprotokoll, Beschlussprotokoll, Rednerliste, Videoaufzeichnung.  | Title: Protocol<br>|
| voting_result ([meta:vocabulary/document_category/VotingResult](meta:vocabulary/document_category/VotingResult)) | Ergebnisse von Abstimmungen und Wahlen. Beispiele: Abstimmungsprotokoll, Wahlprotokoll.  | Title: Voting result<br>|
| legislative_documents ([meta:vocabulary/document_category/LegislativeDocuments](meta:vocabulary/document_category/LegislativeDocuments)) | Dokumente des Gesetzgebungsverfahrens. Beispiele: Erlassentwurf, erläuternder Bericht, beschlossener Erlass, konsolidierte Fassung.  | Title: Legislative documents<br>|
| consultation_documents ([meta:vocabulary/document_category/ConsultationDocuments](meta:vocabulary/document_category/ConsultationDocuments)) | Unterlagen zur Eröffnung einer Vernehmlassung. Beispiele: Einladung, Adressatenliste, Fragebogen, synoptische Darstellung (Fahne).  | Title: Consultation documents<br>|
| consultation_results ([meta:vocabulary/document_category/ConsultationResults](meta:vocabulary/document_category/ConsultationResults)) | Ergebnisse einer Vernehmlassung. Beispiele: Stellungnahme einer Organisation oder Person, Ergebnisbericht.  | Title: Consultation results<br>|
| media_release ([meta:vocabulary/document_category/MediaRelease](meta:vocabulary/document_category/MediaRelease)) | Medienmitteilungen.  | Title: Media release<br>|
| group_documents ([meta:vocabulary/document_category/GroupDocuments](meta:vocabulary/document_category/GroupDocuments)) | Unterlagen einer Gruppe wie Kommission oder Partei. Beispiele: Statuten, Jahresbericht, Kommissionszuteilung.  | Title: Group documents<br>|
| member_directory ([meta:vocabulary/document_category/MemberDirectory](meta:vocabulary/document_category/MemberDirectory)) | Mitgliederlisten. Beispiele: Mitglieder der Räte, Kommissionsmitglieder, Mitglieder von Freundschaftsgruppen.  | Title: Member directory<br>|
| person_documents ([meta:vocabulary/document_category/PersonDocuments](meta:vocabulary/document_category/PersonDocuments)) | Unterlagen zu einzelnen Personen. Beispiele: Porträt eines Ratsmitglieds, Liste der persönlichen Mitarbeitenden.  | Title: Person documents<br>|
| interest_disclosure ([meta:vocabulary/document_category/InterestDisclosure](meta:vocabulary/document_category/InterestDisclosure)) | Register der Interessenbindungen von Ratsmitgliedern. Beispiel: Register der Interessenbindungen des Nationalrats.  | Title: Interest disclosure<br>|
| other ([meta:vocabulary/document_category/Other](meta:vocabulary/document_category/Other)) | Dokument, das keiner Kategorie zugeordnet werden kann oder dessen Kategorie unbekannt ist. Default, wenn `document_category` nicht gesetzt ist.  | Title: Other<br>|







</div>


## Expression

Abstract: An expression is "the specific intellectual or artistic form that a work takes each time it is 'realized.'" An audiobook and a text edition of a book are different expressions of the same work. For music, this includes both writing down the sheet music and performing it. Each draft of the score is an expression. The professionally recorded 1996 London Philharmonic performance of Beethoven's Ninth is another expression.

Typically per language on distinct expression is created. An expression holds additionally to the attributes of the work, the title and description in the according language of the expression.

Attached to the Expression is one or multiple Manifestation as decribed below.



### Klasse: Expression []{#Expression}


_FRBR Expression: eine konkrete Sprachfassung eines Works._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| expression_language | 1 <br/> String | Sprachcode im ISO 639-1-Format.  |
| expression_title | 1 <br/> String | Titel der Sprachfassung.  |
| expression_description | 0..1 <br/> String | Beschreibender Text zur Sprachfassung.  |
| manifestations | * <br/> [Manifestation](#Manifestation) | Die Dateiformen (Manifestations) einer Expression.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Work](#Work) | expressions | range | [Expression](#Expression) |



















</div>

## Manifestation

Abstract: A manifestation is "the physical embodiment of an expression of a work. As an entity, manifestation represents all the physical objects that bear the same characteristics, in respect to both intellectual content and physical form." The recordings of the 1996 performance released on vinyl are one manifestation. The same performance released on CD is another manifestation.

With the manifestion the final URL to the actual document is added. There can be one more more manifestations, which are differing in the differnt formats (e.g. PDF, DOCX, HTML) of the document provided.

Both the Expression and the Manifestation carry creation and modification dates via the common mixin `HasCreationModificationDates`. All FRBR entities are identified via the common mixin `HasIdentification`.




### Klasse: Manifestation []{#Manifestation}


_FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL adressierbar._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| format | 0..1 <br/> String | Das Dateiformat der Manifestation (z.B. pdf, html).  |
| manifestation_url | 0..1 <br/> Uri | URL, unter der die Dateiform abgerufen werden kann.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Expression](#Expression) | manifestations | range | [Manifestation](#Manifestation) |



















</div>


### Klasse: HasIdentification []{#HasIdentification}


_Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügung stellt. Sie wird für Entitäten verwendet, die aus sich heraus identifiziert sind; deren `global_uri` ist der Identifikator und daher obligatorisch._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.  |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität.  |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans.  |



#### Mixin-Verwendung

[Work](#Work), [Expression](#Expression), [Manifestation](#Manifestation), WorkContainer





















</div>


### Klasse: HasCreationModificationDates []{#HasCreationModificationDates}


_Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderungsdaten einer Entität zur Verfügung stellt._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde.  |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.  |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde.  |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.  |



#### Mixin-Verwendung

[Expression](#Expression), [Manifestation](#Manifestation)





















</div>

\newpage

list of topics/categories for affairs that can be mapped to any organization's list
see: https://github.com/swiss/political-affairs-ech-group/blob/main/ech-0297_consultations/misc/2026-06-19-session.md

for next version

