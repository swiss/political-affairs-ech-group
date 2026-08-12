# ELI implementation guide 

## Capture requirements for HTTP URIs

### Exmaple

URI template for European Union legislation         `eli/{typedoc}/{year}/{naturalnumber}/oj`


### Appraoches
The first step that publishers of legal information should take when approaching the implementation of the first ELI pillar (i.e. HTTP URIs) is to get a detailed understanding of user needs and, if necessary, up- date the business case (cf. ‘Organisation and policy’, Step 1). Many techniques are available for gathering user requirements. In order to gain a complete overview of the requirements that are relevant for the implementation of ELI HTTP URIs, publishers of legal information might consider the following approaches.

- Interviews: publishers of legal information should gather detailed information on what type of tasks users carry out with legal information, and understand how they cite legal information and what type of information they expect to find online. Interviews are very useful in this regard because they allow an in-depth analysis to be carried out and new requirements uncovered.

- Questionnaires: questionnaires are useful when publishers of legal information need to gather a large number of requirements from a wide audience, including users in remote locations that cannot be interviewed individually. It is advisable to complement the results gathered via questionnaires with more in-depth approaches.

- Prototyping: this technique allows requirements to be gathered that will help publishers of legal information to build the initial version of the HTTP URI. The development of a prototype on HTTP URIs will help users provide feedback that will be used to refine the HTTP URI implementation. This process should continue until the HTTP URI template meets the critical mass of user needs.

- Use cases: use cases are useful to describe how and for what purpose HTTP URIs for each type of content are used. Examples of use cases for HTTP URIs might include: consultation of legislation as it stood at a specific point in time; access to the consolidated version of specific piece of legislation; references to legal information in social media.

### Characteristics of legal domain
On top of gathering user requirements, publishers of legal information should take into account needs that are more related to the `characteristics of legal information` and to the environment where the HTTP
URIs will be developed, such as the following:
- Whether there is a single authority that attributes the identifiers or whether the `attribution of identifiers` is done in a decentralised manner. 
  - e.g., Germany             : since there are 16 Bundesländer that promulgate legislation, the attribution of identifiers is decentralised.
- The fact that legal information might not all have an identifier to be used to `uniquely identify legal` information, which means that alternative options should be considered:
  - e.g. Luxembourg           : Règlement grand-ducal du 2 février 2015 portant organisation de la Conférence nationale des élèves is identified uniquely with an ELI-compliant HTTP URI by adding a sequential number (cf. `n7`): http://eli.legilux.public.lu/eli/etat/leg/rgd/2015/02/02/n7 (1).
  - e.g. Norway               : Before Lovdata (2) existed not all regulations had numbers. As a result, when Lovdata came into existence it introduced numbers to legislation in a systematic way. Where numbers did not exist (i.e. for regulations and statutes published before 1982) Lovdata retroactively assigned them, and from 1982 all regulations got an official number published in the Legal Gazette.
- The fact that legislation may be published in different websites, with different domain names. 
  - e.g., in Italy            : basic acts are published on the Gazzetta Ufficiale website, while consolidations can be browsed on the Normattiva website. Domain-agnostic URIs (e.g. http: // data. country. `eu/eli/`, etc.) may help in this situation.
- The need to identify whether legislation is published as an `individual resource`, or in the context of an official journal, or both. 
  - e.g., Italy               : provides ELI for both of the following. For information on the different URI template components, please see the Italy page of the ELI website: http://eur-lex.europa.eu/eli-register/italy.html.
  - Official journal          : `/eli/gu/2015/1/13/9/sg/html`    -> gu
  - Individual resource       : `/eli/Decreto/2013/65/art4`      -> Decreto (`individual resource`)
- Take into account `when consolidation takes place` (when applicable).
  - e.g., France                     : consolidates legislation immediately after the amending act has been adopted and has put in place a specific database for it, which is called ‘LEGI’. Ireland instead consolidates legislation on a case-by-case basis, and mostly for large acts.
- The existence of `more than one calendar`. This is the case for Ireland and the United Kingdom where, prior to 1922 and 1963 respectively, the regnal years were used to identify the year that legislation was
published. To overcome such a challenge, these countries decided to redirect URIs with a calendar year before these dates to a URI based on the Gregorian calendar. Although such an approach worked for the majority of the cases, there were a small number of items of legislation held on the United Kingdom website where this redirection could not have been done unambiguously. For such cases a list of candidates is given in response to the user, who then has to choose the right legislation.
- The existence of `legacy identifiers`. It may be that when publishers of legal information implement ELI they already assign identifiers to legal information. When this is the case these identifiers can continue to be supported. For example, in the past Ireland went through two iterations of URI patterns. The first implemented pattern was not user friendly and it had to be replaced around 2004. The second URI pattern was a user-friendly pattern that had some resemblance to the current ELI URI schema. As there are still a large number of websites that link to the eISB (the electronic Irish Statute Book) using the old pattern, redirection is planned from the old to the new HTTP ELI pattern.

## Considerations
When designing ELI URI schemas it is important to make a distinction between the (abstract) legal resources and their realisations. In this way it will be possible to identify a reference to legislation independently of the version, language, representation format, etc.

e.g.  Luxembourg            : `/eli/etat/leg/loi/{YYYY}/(MM)/{DD}/{naturalnumber}`

identifies  the  abstract  basic  act  ‘Loi  1974  04  16’.  

When  Legilux (Official Journal and classified compilation) of Luxembourg receives a request for this kind of resource, it returns: 
- the Legilux page of the latest `consolidated` version of an act;  
- if  no  consolidated  version  exists,  the  OJ  page  of  the  `base  act`  identified by `eli/etat/leg/loi/2011/04/08/n2/jo` (note that the `jo` path is used as the main publication system for base acts and modifying acts, not for consolidations)
- and  always  includes  the  not-yet-integrated  `amendments`, if any (e.g. `eli/etat/rgd/2011/04/08/n2/republication/20140331/jo`)

When  designing  the  ELI  URI  template(s),  publishers  of  legal  information should follow the following steps:
- identify how legal information is cited (Good practice 6);
- ensure that each legal resource is identified uniquely (Good practice 7);
-  take  into  account  the  type  of  content  to  be  published  (e.g.  statutory  instruments  vs  acts,  basic  acts  vs  consolidated  texts,  official  journals)  and the concepts of the ELI ontology (legal resource, legal expression and format) (Good practice 8); 
- identify subparts of legal information (Good practice 9); 
- follow good practices for HTTP URIs (Good practice 10); and 
- test URI templates (Good practice 11).

Key Good Practices include:  
- avoiding using more elements than necessary to identify legal information in a unique way; 
- staying as close as possible to existing citation practice;
- implementing the FRBR hierarchy in the URI scheme;
- avoiding using elements that tend to change in HTTP URIs.


### Timeline
e.g. Luxembourg: base act -> modifying act 1 -> consolidation 1 -> mofiying act 2 -> consolidation 2

`base acts` and `modifying acts` contain:
agent + type                : `etat` -> Staat? + `leg` -> administrative branch?
YYYY + MM + DD              : -> the creation date?
n#                          : n + `sequence number`

`consolidated acts` contain additionally:
rgd                         : before -> indicating Consolidation ?
 + consolide                : indicating Consolidation


### Citation
In addition to design, ELI URI schemas usually match the types of legal resources, but it is also important to take into account how people will  use  URIs.  

People  should  find  identifiers  of  legal  information  that  are  
easy  to  use,  thus  the  closer  identifiers  are  to  the  way  the  legislation   is  cited  the  easier  it  is  to  understand  them,  remember  them  and  use  them. 

commonly used in citation practices are: 
- year, 
- type of legislation, 
- identifier and 
- version. 

See the following French example.
- Vue le décret n° 2014-1169 du 10 octobre 2014 modifiant diverses dispositions réglementaires du code de la défense
- ELI HTTP URI: http://www.legifrance.gouv.fr/eli/decret/2014/10/10/
DEFD1415169D/jo/texte

A  relevant  standard  for  ELI  implementation  is  the  specification  of  the  URI  described  in  the  Internet  Engineering  Taskforce  `Request  for  Comment 3986`, `Uniform Resource Identifier (URI): generic syntax`. 
Further guidance on how to effectively use URIs in the context of the semantic web is given by W3C in the document Cool URIs for the semantic web. 
Additional principles that should be applied in designing URI templates  are described in the document 10 rules for persistent URIs (https://joinup.ec.europa.eu/community/semic/document/10-rules-persistent-uris)


Examples for Switzerland
- Gesetze (act)
  - zitiert wird meistens die aktuell gültige Fassung des Systematischen Rechts
  - werden einzelne Bestimmungen zitiert, dann meist unter Angabe der genauen Fundstelle (Art., Abs., Satz)
- Gesetzesvorlagen / Entwürfe (bill)
  - wird eine Gesetzesvorlage zitiert, so erhält sie einen Präfix `n` (z.B. nDSG) oder `rev` (z.B. revDSG)
  - Die Artikelanzahl, Inhalt und Reihenfolge können sich zwischen Versionen ändern
  - Vernehmlassungsvorlagen enthalten den Präfix `VE-` zur Kennzeichnung eines Vorentwurfs
- Erläuternde Berichte
  - Die Botschaft des Bundesrates oder der erläuternde Bericht zu einer Vernehmlassungsvorlage oder zu einem Gesetzgebungsprojekt (grundsätzlich vom Bundesrat, seltener durch Kommission) wird unter Angabe der `BBl YYYY p` Referenznummer (p = Seitenzahl)
- Motionen, Interpellationen und parlamentarische Initiativen sind allesamt Parlamentsgeschäfte in der Curia Vista Datenbank auffindbar mit Hilfe der `YY.x` Referenznummer (x = Geschäftsnummer, fortlaufend)

### Unique Resources 
If one HTTP URI resolves to more than one piece of legislation, a request for that HTTP URI will receive in response all the pieces of legislation resolved by that URI. This is called the URI homonym problem and can lead to confusion and interoperability conflicts as it might not be clear what resource is associated with a URI.

Examples for Switzerland:
- official and condolidated compilation -> default URL resolving to the consolidated version
- e.g. two laws created on the same day by the same jurisdiction
- not specifying `bill` and `act`; currently:
  -  only `year`, `naturalnumber` for acts in `oc` 
  -  `year`, `naturalnumber` for bills 
     -  Vernehmlassungen implementieren den `ELI-DL standard` (e.g. `eli/dl/proj/2024/65/cons_1`), verweisen aber auf Ebene Projekt, nicht Gesetz (kann auch Botschaft gemeint sein; `project`, `bill` or `report`)
        -   `cons` ?
     -  Initiativen können auch Gesetzesentwürfe sein (`eli/fga/2025/3069/de` = `BBl 2025 3069`) und haben zusätzlich die Parlamentsnummer (e.g. 25.078) angehängt
- long-term persistence of already minted URIs

### FRBR (Work, Expression, Manifestation)
ELI  describes  legal  information  based  on the well-established  FRBR  model and distinguishes between the concepts of:
- `work` (or ‘legal resource’)          -> intellectual or artistic creation;
- `expression` (or ‘legal expression)   -> the (language as) intellectual or  artistic  realisation  of a work, typically in a text, a sequence of signs; and
- `manifestation` or format             -> materialisation of one of the expressions in a file. 

Each  time  a  ‘work’  is  realised  it  takes  the  form  of  an  ‘expression’.  The physical embodiment of an expression is a ’format’, or ‘manifestation’.

Different  language  versions  of  legislation  can  be  considered  to  be  different  ‘expressions’,  whereas  different  formats  can  be  considered to be different ‘manifestations’ of the same ‘work’ following the  ELI  ontology.  (the  use  of technology-specific extensions like .asp, .aspx and .jsp in URIs should be avoided as this is prone to change; meaningful format indicators like HTML, RDF and PDF should be allowed.)


In line with the commonly known best practices for linked data, such a structure enables the retrieval of various resource representations via content negotiation.

### Links and References
The  ability  to  establish  the relationship between different pieces of information, such asestablishing the link between basic acts and related amendments, is keyfor supporting  a  good  understanding  of  the  evolution  of  a  given  law.  

Publishers  of  legal  information  should  design  the  ELI metadata  schema  making  explicit  relationships  between  acts.  Examples  of relationships  that can be expressed using the ELI metadata schema include 
- citations,
- amendments, 
- consolidations, 
- commencement

Examples of available ELI metadata include: 
- `changes`, to indicate legal modifications between two acts, along with  more  precise  properties  such  as  `repeals`,  `amends`  or  `commences`.
- `consolidates`, defined as a link between a consolidated resource and the amendments it incorporates; 
- `related to`, a generic property defined as a link to ‘a somehow related other document, not necessarily a legal resource’;
- `transposes`, defined as a link between a piece of national legislation and a transposed EU directive;  

### Publishing workflows
The use of Akoma Ntoso as an XML representation format for the documents  can  help  streamline  the  workflow.  Such  an  XML  schema  can  store metadata in the document header, and the ELI/XML schema can be integrated in an Akoma Ntoso proprietary metadata field.

### URI as state for web applications
URIs can be used for storing state, encoding intent, and making an entire setup shareable.

The basic parts are:
- path to file    : `/path/to/myfile.html`
- parameters      : `?key1=value1&key2=value2` or `?tags=frontend,react,hooks` or `?filters=status:active,owner:me,priority:high` or `?debug=true&analytics=false`
- anchor          : `#SomewhereInTheDocument`
- fragment        : `id` or `:~:text=`

parameters can have multiple values or a nested / strctured data and/or a specific purpose:
- highlighting    : github.com/mgajdo/text.md`#L108-L136`
- filter + sort   : store.com/laptops?brand=dell+hp&price=500-1500&rating=4&sort=price-asc
- location        : google.com/maps/@22.443842,-74.220744,19z
- file            : figma.com/file/abc123/MyDesign?node-id=123:456

Switching back or forth in navigation should reflect the intent: new page or same page?

Good design only includes non-default values in URL.


### AKN on URIs


## Implementation

### Base URL Model
The general ELI URL components are `/eli/{jurisdiction}/{agent}/{sub-agent}/{year}/{month}/{day}/{type}/{natural identifier}/{level 1…}/{point in time}/{version}/{language}` and can be roughly translated into five parts:
- agents                    : `{jurisdiction}/{agent}/{sub-agent}`
- identifier                : `{year}/{month}/{day}/{type}/{natural identifier}`
- subdivision               : `{level 1…}/{level 2…}/etc.` for the document structure
- versioning                : `{point in time}/{version}` 
- langauge                  : `{language}`

### European Model
EU ELI URI template         : `eli/{typedoc}/{year}/{naturalnumber}/{start-date}/{subdivision*}oj`
- identifiers               : `{typedoc}/{year}/{naturalmnumber}`
- publication               : where `/oj` means Official Journal and is at the end of the URI (cf. Swiss Model)

The `identifiers` part is the main part with typedoc determining the type of law (e.g. regulation). The `year` and `naturalnumber` (e.g. consecutive number of legislation project) are used to differentiate between (published) versions.

In case of ambiguity, i.e. when two or more acts of the same typedoc could be published with the same natural number in the same year (e.g. < 2015 for OJ-L). In order to avoid conflicts the natural_number will include a `sequence number`:
- `naturalnumber` + `sequence numbers` : e. g.`eli/dec/2014/445(1)/oj` in which case the sequence number is `(1)`. 

The `{naturalnumber}` together with `{start-date}` is only used for classified compilations and it indicates the `day of entry into force` of the last amendment. 


There can be multiple subdivisions (art. + par.) e.g. `eli/dir/2000/31/art_1/par_2/oj`
- subdivisions:             :`eli/{typedoc}/{year}/{naturalnumber}{/subdivision*}/oj`

e.g.,  the  United  Kingdom  has  developed  a  URI  model  that  
considers  the  `section`  parameter.  
- sections                  : `/id/{type}/{year}/{number}/{section}/[]`

e.g. Scotland 2014, Nr. 2   : `/id/asp/2014/2`
Section 3                   : `/id/asp/2014/2/section/3`


Production  workflow  is  based  on  XML  structures:
-> more granular levels by processing the XML records. assign unique identifiers  to  each  XML  element  
-> important to integrate it into the  design  of  HTTP  URIs  from  the  beginning.

All of these templates can be used in combination with a `{language}` and `{format}`:
- base + language           : e.g.`/eli/dir/2000/31/oj/fra`
- base + langauge + format  : e.g. `/eli/dir/2000/31/oj/fra/pdf`

### Swiss Model (SLI or AKN-CH)
Fedlex currently has an additional part `publication` shoved inbetween `eli` and the `identifiers` part instead of `oj` at the end (`base`)and has `agent` part omitted, therefore not taking into account federal states. The different publications are using abbreviations (e.g. `oc` or `cc`).
- base                      : `eli/oc/2024/65`

For the Swiss Legal Identifier (SLI or Swiss E) or country-specific AKN (AKN-CH) we propose the following URI:

#### base                   : `eli` + `publication`
- publication               : e.g. `oc`, `cc`, `fga` and new `cons` or `bill`

#### agents                 : `publication` + `/eli/{jurisdiction}/{agent}/{sub-agent}`
- jurisdiction              : `CH`, if explicit resolves to federal law
                            -> canton: `CH` + two digit code e.g., `/eli/CH/ZH` or `/eli/CH/BL` for ZH or BL cantonal law
                            -> municipality: `CH` + canton + BFS number for municipality e.g., `/eli/CH/ZH/{BFS}`
                            -> each organisation may omit the jurisdictions higher up 
- agent + subagent          : optional  -> responsible ministry or government branch, e.g. `/eli/CH/leg/` or `/eli/CH//exe` or `/eli/CH/jud/`   

#### identifiers            : `agents` + `{year}/{month}/{day}/{type}/{natural identifier}`
year + mm + dd              : year is mandatory
type                        : optional -> law, decree, bill (cons?)
natural identifier          : mandatory, if required

#### subdivisions           : optional


#### versioning             : `agents` + `reference` + `subdivisions` + `{point in time}/{version}/{language}/`



### Metadata
Metadata  provides  the  means  for  describing,  classifying,  linking,  finding  legal information as well as connecting it to other pieces of information and  enabling  users  to  access  and  reuse  it.  

It  includes,  for  example: 
- title,  
- date of adoption, 
- date of signature, and 
- author 
of a given piece of legisla-
tion.  

For example, if users are mainly interested in consulting in-force legislation, an option could be to focus on  applying  ELI-compliant  metadata  to  this  collection  first.

Map  the  data  model  already  managed  by  the  publisher  to  the  ELI  application  profile.  This  prepares  the  data  conversion  of  the  existing  metadata to the ELI application profile and the publication of ELI metadata.  Metadata  that  is  already  managed  by  legal  publishers  may  be  stored in a content management system, in a specific application or in the XML of documents. The publishers should map:
- existing  metadata  fields  with  the  corresponding  fields  in  the  ELI application profile to describe the equivalence between the 
two data models;
- values  of  the  metadata  in  the  existing  information  system  with  their  value  in  the  controlled  vocabularies  selected  or  created for the ELI publication.

The  publisher  will  have  to  carry  out  data  conversion  from the existing metadata to the ELI metadata. To do so the publisher should make sure the following elements are available.  
- Mappings between existing metadata schemas and the ELI ontology elements used as part of the ELI application profile. 
- Mappings between  existing  metadata  values  and  values  of  the  controlled vocabularies used as part of the ELI application profile. 
- Data conversion rules that might be needed.
- If all the above is available, the work of the publisher will be toprepare the scripts which will execute the data conversion. The output of the scripts will be used to add RDFa tags in web pages. (see XML serialisation of ELI and the associated conversion stylesheet).

## Testing + Webserver
When  designing  URI  templates,  publishers  of  legal  information  may  face  a  number  of  challenges,  such  as  being  able  to  correctly  identify  subparts of legislation, being able to uniquely identify legislation that does not have a unique identifier or being able to handle dates where more than one type of calendar year applies. These difficulties may not immediately  be  apparent  during  the  design  phase  of  ELI  HTTP  URIs  and it may not be possible to foresee all possible scenarios.

The tests should reveal issues related to the correspondence between URIs and: 
- the way legislation is cited; 
- identification of consolidated acts (when applicable); and 
- resolution mechanisms. 

Tests should also include simulations of probable scenarios that can happen during the publication process, such as: 
- 1. create a new legal act; 
- 2. update  the  content  of  an  act  by  altering  its  structure;  
- 3. replace  an  act;  
- 4. amend an act; 
- 5. consolidate an act. 

The tests should be designed to match  the  context  of  each  implementer.  For  example,  the  Publications  Office had to find a way to assign unique and persistent URIs to legislation that did not have an identifier, such as corrigenda (`eli/{typedoc}/{year}/{naturalnumber}/corrigendum/{pub_date}/oj`).

Publishers of legal information should design HTTP URIs in such a way that  they  resolve  to  legislation.  Resolution  means  that  if  an  HTTP  request  is  issued  (either  by  a  human  using  a  web  browser  or  by  a  machine/an application) to a web server, this returns a representation of 
the resource, either: 
- the metadata of the legal resource (in either a human-readable or a 
machine-readable way); 
- the  legal  resource  document  itself  (in  one  of  its  available  formats, e.g. HTML, PDF, XML).

Publishing the data using an `API` with proper documentation allows data consumers to retrieve the subset of the data they are interested in. This is usually a very large project, requiring a lot of resources and with other impacts on the information system. 

Opening the data in a `SPARQL` endpoint  is an alternative to creat-
ing  an  API. (This  is  closer  to  the  original  ELI  metadata work  since  it does not require that a new data model or the inputs and outputs of the API be specified.).

Publishers who want an API need to do the following:
- Create a web application capable of rendering machine-readable metadata for legislation that should conform to the ELI-compliant  metadata  schema.  
- API data model should  follow  the  principles  of  linked  data  and  the  ELI  data  model.  The JSON-LD syntax (1) provides a good way to create API based on JSON and still linked-data compatible.
- Publish  API  documentation.  An  example  of  such  documentation is the one provided by the Publications Office, which can be 
found at http://data.europa.eu/eli. 

