# political-affairs-ech-group

- eCH-0292: [Metaprozesse zu politischen Geschäften (meta)](https://github.com/swiss/political-affairs-ech-group/tree/main/ech-0292_meta)
- eCH-0293: [Öffentlicher Ratsbetrieb (operations)](https://github.com/swiss/political-affairs-ech-group/tree/main/ech-0293_operations)
- eCH-0294: [Politische Akteure: Personen, Gruppen und Organe (actors)](https://github.com/swiss/political-affairs-ech-group/tree/main/ech-0294_actors)
- eCH-0295: [Parlamentarische Geschäfte (affairs)](https://github.com/swiss/political-affairs-ech-group/tree/main/ech-0295_affairs)
- 
- * eCH-0296: [Erlasse und Gesetzestexte (laws)](https://github.com/swiss/political-affairs-ech-group/tree/main/ech-0296_laws)

- eCH-0297: [Öffentliche Konsultationen (consultations)](https://github.com/swiss/political-affairs-ech-group/tree/main/ech-0297_consultations)

## Meta
  * Schema Evolution nachvollziebar machen
    * Procedure bei Änderungen                          -> Rolle von AkomaNtoso?
  * Vokabular
    * Rollenbezeichnungen
      * Parlament / Legislative
        * Zweikammersystem Bund
        * Kommissionen
        * Einzelne Parlamentarier
      * Regierungsrat / Exekutive
    * Begrifssklärungen / Prozess-Äquivalente (Kanton)
      * Exekutive z.B. Bundesrat <> Regierungsrat
      * Legislative z.B. Bundesversammlung <> Kantonsrat

## Gesetze
  * Gesetzesentwürfe (bill) und Gesetze (act)
    * Varianten zu Entscheiden                          -> affairs
    * Struktur des G.Entwurfs                           -> laws
  * Verknüpfung [von Vernehmlassungen] zu Gesetzen      -> consultations
  
## Fragen
  * hat ein Änderungserlass eine andere Struktur? 
  * Spezialfall Aufhebungsbeschluss (oder Aufhebungserlass)?

## Rechtsquellen
für den Ablauf eines Gesetzgebungsprojektes relevant: 
- ParlG         -> Gesetzgebungsprozess
- ParlVV
- VlG           -> Vernehmlassungen
- VlV
- PublG         -> Publikation
- PublV
- Verordnung der Bundesversammlung über die Redaktionskommission

## URL convention 
- URL: https://fedlex.data.admin.ch/de-CH/home/convention

Datenmodell   (>1999) : https://fedlex.data.admin.ch/eli/{collection}/{year}/{naturalIdentifier}/{workURI}/{language}/{user-format}
  - collection        : e.g. fga, oc, cc etc.
  - year
  - naturalIdentifier : sequencial number
  - workURI           : -> ?
  - language          : de, fr, it, en
  - format            : .html, .pdf, etc.


# Event Driven Architecture (PROV-O)
source: https://paf.link/

The paf.link schema is an `event-based` RDF (see "RDF 1.1 Concepts and Abstract Syntax") data schema for describing public affairs (paf) which allows to model generic them to the full extent. It can be adapted to specific public administrations on different public levels by using an application profile (e.g. ch.paf.link).

It is based on the `PROV-O` and extends it based on a number of design principles. PROV-O was developed by the World Wide Web Consortium (W3C) as a standard for expressing and exchanging provenance information in RDF. PROV-O defines a set of classes, properties, and relationships that enable the representation of provenance information across diverse domains and applications. The schema can also be used with JSON and XML implementations.

## Layer 1 - links
Central elements:
- `agents` and (responsibility for an activity taking place or for the existence of an entity)
- `activities` (processes or events)
  - Activities  chained in temporal succession are used to build an activity stream that can also branch and reunite.
  -  prov:startedAtTime and prov:endedAtTime with values of type xsd:dateTime or xsd:date. 
  -  If an activity is instantaneous, only the start time is given. This means that an activity without end time is considered to be instantaneous.
- `entities`   (documents or processes)
  - Entities can be used as input information for a certain activity or can be created as output information representing the result of a specific activity (e.g. voting result of a voting activity). Such output information in turn can act as input information for later activities.
  - As identifiers of specific public affairs (Parlamentsnummer, z.B. 25.078) are very fundamental, this information is modelled by using identifier entities with class `paf:IdentifierEntity` as subclass of prov:Entity. 

Such `identifier entities` are very atomic and only contain the following information:
- the identifier itself (as string link via schema:identifier) which in addition should also be part of the URI of such entities and
- an additional class showing the kind of identifier (e.g. identifier of the national parliament).
- Every activity that acts upon a specific affair should use the corresponding identifier entity as part of the input entities (prov:used). 
- It is very common, that activities act upon multiple identifiers at the same time meaning that at least parts of a public affair can have multiple different identifiers from different systems.

All activities, entities and agents should be linked together. This will allow to design queries that can find all information:

The most important links are:
- Activities should be linked in temporal succession via prov:wasInformedBy. In PROV-O, entities, activities and agents are connected backwards in time. So items that happen later, link to their predecessors and not vice versa.
  - Activities should have a time specification via prov:startedAtTime and optionally prov:endedAtTime.
- Activities should have at least one `agent` linked via a qualified association (prov:qualifiedAssociation).
- Activities link to the `entities` via prov:used.
  - If it is important to show that an entity was created by a specific activity, the entity should link to the activity via prov:wasGeneratedBy.

For complete traceability, elements should not be deleted or changed but instead a new element should be created via corresponding activities.Otherwise, activities that used these entities before, could lead to other results. If a change/correction is necessary, a `paf:EntityChangeActivity` is carried out that uses the old entity as input and creates the changed/corrected entity as output.

## Layer 2 - activity archetypes

### proposal + decision (Antrag + Entscheidung)
  - activities
    - paf:ProposalActivity    : This activity contains as the sum of all input entities the actual proposal.
    - paf:DecisionActivity    : This activity contains as the sum of all input entities the content of the decision (what is decided upon) and as output entity the actual vote on the decision.
  - agents
    - paf:ProposalSubmitter   : The agent (person or group) which submits the proposal.
    - paf:ProposalReceiver    : The agent (person or group) which receives the proposal. 
    - paf:DecisionMaker       : The agent (person or group) which issues the decision
  - entities
    - paf:ProposalEntity      : This is the entity that contains the content of the proposal.
    - paf:DecisionEntity: This is the entity that contains the content that is decided upon (can differ from the proposal).
    - paf:DecisionResultEntity: This is the entity that contains the result

### consultation + comment (Vernehmlassung + Stellungnahme)
- activities
  - paf:ConsultationActivity  : This activity contains as the sum of all input entities the actual consultation with all necessary information.
  - paf:CommentActivity       : This activity contains as input entity a comment on the consultation.
- agents
  - paf:ConsultationSubmitter : The agent (person or group) which submits the consultation
  - paf:ConsultationReceiver  : The agent (person or group) which receives the consultation
  - paf:CommentMaker          : The agent (person or group) which issues the comment.
  - Entities
    - paf:ConsultationEntity: This is the entity that contains the content of the consultation.
    - paf:CommentEntity: This is the entity that contains a comment to the consultation.

### information & acknowledgement (Information +	Quittierung)

### order + conmpletion 
Catch-all category:
- Task-Assignment & Task-Fulfillment
- Mandate & Resolution Activities
- Todo & Done Activities
- Action & Reaction Activities

## Layer 3 - Procedural requests
- motion
- postulate

The list of all postulates are available as list (report). You can get information about the status of motions and postulates (e.g. why it has not yet been answered by the executive branch). A proposal (and decision) on how to handle a motion or postulate can have connected IDs referring to the original postulate:
- id            : 21.3654   
- proposal	    : "Postulatsbericht vom 9. Juni 2023 «Lagebeurteilung Beziehungen Schweiz–EU». Der Bundesrat erachtet das Anliegen der Postulate und der Motion als erfüllt und beantragt deren Abschreibung."@de
- submitter     : <https://ld.admin.ch/office/I.1.2>
- conn_id       : 13.3151



# examples

## 1a - (Vor-)Entwurf zum Bundesgesetz über Kommunikationsplattformen und Suchmaschine (KomPG) - Vernehmlassungsvorlage des Bundesrats (VE-KomPG)
URLs:
- URL_WORK (neu)    : https://www.fedlex.admin.ch/eli/cons/2024/65/cons
  
- URL_WORK (alt)    : https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/dl/proj/2024/65/cons_1/doc_1/de/pdf-a/fedlex-data-admin-ch-eli-dl-proj-2024-65-cons_1-doc_1-de-pdf-a.pdf

Sprachen (expressions)
- de (neu)          : https://www.fedlex.admin.ch/eli/cons/2024/65/cons/de
- fr
- it
- en

Formate (manifestations)
- html (neu)        : https://www.fedlex.admin.ch/eli/cons/2024/65/cons/de.html
- pdf (neu)         : https://www.fedlex.admin.ch/eli/cons/2024/65/cons/de.pdf
- etc.

Dokumente: 
-  Vernehmlassungsvorlage
   -  Art. 1
   -  etc.
-  Erläuternder Bericht

## 1b - Erläuternder Bericht des Bundesrats zum Bundesgesetz über Kommunikationsplattformen und Suchmaschine (KomPG) zur Eröffnung des Vernehmlassungsverfahrens - 
URLs:
- URL_WORK (neu)        : https://fedlex.data.admin.ch/eli/cons/2024/65

- URL_DL_PROJECT (alt)  : https://fedlex.data.admin.ch/eli/dl/proj/2024/65/cons_1
- URL_PDF (alt)         : https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/dl/proj/2024/65/cons_1/doc_1/de/pdf-a/fedlex-data-admin-ch-eli-dl-proj-2024-65-cons_1-doc_1-de-pdf-a.pdf

ID:
-  2024/65

Datum:
- Beschluss: 08.10.2025
- Publikation: 29.10.2025
- Eröffnung: 30.10.2025
- Aktualisierung: 29.10.2025
- Frist: 16.02.2026
≈
Sprachen (expressions)
- de (neu)              : https://fedlex.data.admin.ch/eli/cons/2024/65/de
- fr
- it
- en

Formate (manifestations):
- xml                   : https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/fga/2025/3136/de/xml/fedlex-data-admin-ch-eli-fga-2025-3136-de-xml.xml
- html                  : https://fedlex.data.admin.ch/eli/cons/2024/65/de
- doc
- pdf

Behörde: 
- Bundesrat

Dokumente: 
-  Vernehmlassungsvorlage - Vorentwurf zum Bundesgesetz über Kommunikationsplattformen und Suchmaschinen (VE-KomPG)
   -  Art. 1
   -  etc.
-  # Erläuternder Bericht
   - 1 Ausgangslage
   - 2 Vorverfahren, insbesondere Vernehmlassungsverfahren
   - 3 Rechtsvergleich mit dem europäischen Recht
   - 4 Grundzüge der Vorlage
   - 5 Erläuterungen zu einzelnen Artikeln
   - 6 Auswirkungen
   - 7 Rechtliche Aspekte
-  Begleitschreiben 
-  Begleitschreiben-2 
-  Adressatenliste 
-  Diverses 
-  Antwortformular



## 1 - Erläuternder Bericht des Bundesrats zum Bundesgesetz über Kommunikationsplattformen und Suchmaschine (KomPG) - Eröffnung des Vernehmlassungsverfahrens
URLs:
- URL_WORK (neu)        : https://fedlex.data.admin.ch/eli/cons/2024/65

- URL_DL_PROJECT (alt)  : https://fedlex.data.admin.ch/eli/dl/proj/2024/65/cons_1
- URL_PDF (alt)         : https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/dl/proj/2024/65/cons_1/doc_1/de/pdf-a/fedlex-data-admin-ch-eli-dl-proj-2024-65-cons_1-doc_1-de-pdf-a.pdf

ID:
-  2024/65

Datum:
- Beschluss: 08.10.2025
- Publikation: 29.10.2025
- Eröffnung: 30.10.2025
- Aktualisierung: 29.10.2025
- Frist: 16.02.2026
≈
Sprachen (expressions)
- de (neu)              : https://fedlex.data.admin.ch/eli/cons/2024/65/de
- fr
- it
- en

Formate (manifestations):
- xml                   : https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/fga/2025/3136/de/xml/fedlex-data-admin-ch-eli-fga-2025-3136-de-xml.xml
- html                  : https://fedlex.data.admin.ch/eli/cons/2024/65/de
- doc
- pdf

Behörde: 
- Bundesrat

Dokumente: 
-  Vernehmlassungsvorlage - Vorentwurf zum Bundesgesetz über Kommunikationsplattformen und Suchmaschinen (VE-KomPG)
   -  Art. 1
   -  etc.
-  # Erläuternder Bericht
   - 1 Ausgangslage
   - 2 Vorverfahren, insbesondere Vernehmlassungsverfahren
   - 3 Rechtsvergleich mit dem europäischen Recht
   - 4 Grundzüge der Vorlage
   - 5 Erläuterungen zu einzelnen Artikeln
   - 6 Auswirkungen
   - 7 Rechtliche Aspekte
-  Begleitschreiben 
-  Begleitschreiben-2 
-  Adressatenliste 
-  Diverses 
-  Antwortformular

## 2b - Entwurf zum Bundesgesetz über das bäuerliche Bodenrecht (BGBB) - Änderungserlass (des Bundesrats, beauftragt durch Kommission des Ständerats)
URLs:
- URL_EXPRESSION    : https://www.fedlex.admin.ch/eli/fga/2025/3136/de

- URL_PROJECT       : https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20250079

Datum:
- Medienmitteilung: 08.10.2025 
- Frist: bis Ende 2025 

Datenmodell:
-  Motion 22.4253 «Entkopplung des bäuerlichen Bodenrechts von der AP22+» 
-  Auftrag der Kommission für Wirtschaft und Abgaben des Ständerats (WAK-S) an den Bundesrat 
-  Entwurf zur Anpassung des BGBB 
-  Botschaft zu einer Teilrevision des BGBB zuhanden des Parlaments verabschiedet.

Mitglieder:
- Für die Ausarbeitung der Vorlage hat das WBF eine externe Begleitgruppe einberufen. In dieser waren die kantonalen Landwirtschaftsämter (KOLAS), der Schweizer Bauernverband, der Schweizer Bäuerinnen- und Landfrauenverband, die Junglandwirte-Kommission, die Kleinbauernvereinigung, die Schweizerische Arbeitsgemeinschaft für die Berggebiete, die Schweizerische Gesellschaft für Agrarrecht, der Verein zum Schutz des landwirtschaftlichen Grundeigentums und die landwirtschaftlichen Treuhänder vertreten.



## 3 - Botschaft zur Volksinitiative «Ja zur tierversuchsfreien Zukunft»
URL: https://www.fedlex.admin.ch/eli/fga/2025/3069/de