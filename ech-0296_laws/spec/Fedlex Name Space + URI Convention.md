## Namespace (Fedlex)

Alle URIs des `fedlex` Namespace (u.a. für AS und SR Einträge) beginnen mit `https://fedlex.data.admin.ch/eli/`.

Beispiele:
- Die Einträge für die AS beginnen mit https://fedlex.data.admin.ch/eli/oc/ 
- Die Einträge für die SR beginnen mit https://fedlex.data.admin.ch/eli/cc/

Die URIs von Fedlex werden nach einer `Convention` beschrieben: 

[URIs Templates for Legal Resources in Switzerland](https://fedlex.data.admin.ch/de-CH/home/convention)

Die URIs von Fedlex richten sich nach dem europäischen ELI-Standard (European Legislation Identifier) zur Bezwichnung von Rechtstexten. The [European Legislation Identifier (ELI)](https://eur-lex.europa.eu/eli-register/about.html) is a system to make legislation available online in a standardised format, so that it can be accessed, exchanged and reused across borders.

### Fedlex Vokabular

Das Fedlex Vokabular auf Deutsch ist unter https://fedlex.data.admin.ch/vocabularies/de/ verfügbar. Es wurde mit Hilfe von Skosmos erstellt, einem Open Source Projekt aus Finnland. 

Für die Erstellung der URLS gibt es eine Swagger Dokumentation: [Skosmos API mit Beispielen](https://api.finto.fi/doc/#/)
```
// override this if you'd like to use the rest-api from some other Skosmos server instance.
var rest_base_url = 'rest/v1/';
```

Das Fedlex Vokabular enthält die folgenden Begriffe:
1. Organisationen und Agenten
    * Art der Datenquelle - 6 Concept(s)
    * Arten des Entscheides des Bundesrates * bezüglich eines zu publizierenden Textes. - 3 Concept(s)
    * Betroffenheiten - 31 Concept(s)
    * Eigenschaft skos:notation - 11 Concept(s)
    * Erlassarten - 4 Concept(s)
    * Gliederungseinheiten des Textes - 19 Concept(s)
    * Internationale Organisationen - 283 Concept(s)
    * Internationales Recht - Sachgebiet - 61 Concept(s)
    * Organisationseinheiten - 697 Concept(s)
    * Projekttypen und Ereignisse der Rechtsetzung - 26 Concept(s)
    * Publikationsformate - 19 Concept(s)
    * Rechtsnatur des Vertragsakts - 9 Concept(s)
    * Rollen - 51 Concept(s)
    * Sachregister - 12004 Concept(s)
    * Status der Verträge - 6 Concept(s)
    * Stichwortverzeichnis DE - 7369 Concept(s)
    * Stichwortverzeichnis FR - 7314 Concept(s)
    * Stichwortverzeichnis IT - 8656 Concept(s)

2. Ressourcentypen

    * Dokumententypen des Vernehmlassungsverfahrens - 13 Concept(s)
    * Klassifizierung der sektoriellen Abkommen mit der Europäischen Union - 24 Concept(s)
    * Texttypen - 85 Concept(s)

3. Externe Vokabeln
    * Staaten - 429 Concept(s)


Alle URIs des kontrollierten Vokabulars sind unter dem Pfad `/vocabulary` gebildet. (Nicht `/vocabularies`!) 

Template:

https://fedlex.data.admin.ch/vocabulary/{vocabulary-name}




#### URI of the controlled vocabulary which describes legal institutions

Template:

https://fedlex.data.admin.ch/vocabulary/legal-institution

URI for a all legal institutions in the vocabulary of legal institutions.

#### URI for a concept of a vocabulary

https://fedlex.data.admin.ch/vocabulary/legal-institution/D19

URI for a concept **(skos:Concept)** in the vocabulary of legal institutions, the Swiss national bank (Bundesnahe Betriebe > Schweizerische Nationalbank): 

Template:
https://fedlex.data.admin.ch/vocabulary/{vocabulary-name}/{concept}


## Datenmodell (Jolux)

Das von Fedlex verwendete Datenmodell heisst [JoLux](https://fedlex.data.admin.ch/de-CH/home/models). `jolux` ist ein eigener Namespace für das JOLux Datenmodell basierend auf dem [FRBR-Standard](https://de.wikipedia.org/wiki/Functional_Requirements_for_Bibliographic_Records) (Functional Requirements for Bibliographic Records), einem Entity-Relationship-Modell zur Beschreibung bibliographischer Daten, das für die Beschreibung von Rechtstexten adaptiert wurde. Ursprünglich aus Luxemburg stammend wird das Datenmodell inzwischen von der Schweiz und Luxemburg gemeinsam weiterentwickelt.

### FRBR
Die **Rechtstexte** werden auf 4 Ebenen (FRBR Modell) beschrieben: der abstrakte Text (ComplexWork), der Text (Work), die Fassung (Expression) und die Manifestation (Manifestation).

Auf der abstrakten Ebene (`ComplexWork`) lässt sich ein Text abstrakt darstellen. In unserem Fall erlaubt es diese Gruppe von Klassen einen Grunderlass mit verschiedenen Versionen der Konsolidierung dieses Grunderlasses zu verbinden. Es handelt sich somit um einen `ConsolidationAbstract`.

Beispiele: 

https://fedlex.data.admin.ch/eli/cc/2014/665 

welcher die Abstraktion (d.h. konsolidierte Fassung) eines publizierten AS-Textes darstellt (Classified compilation - Systematische Rechtssammlung)

https://fedlex.data.admin.ch/eli/oc/2014/665 

und sämtliche ursprüngliche Versionen dieses Textes (Official Compilation - Amtliche Sammlung). Den Nutzer interessiert meistens sie letzte gültige Version eines Erlasses. Fehlt diese, ist die Version der Amtlichen Sammlung inhaltlich identisch mit derjenigen der Systematischen Rechtssamlung.

Die Ebene Text (`Work`) repräsentiert eine Dokumentenquelle, unabhängig von ihrer Sprache oder dem Dateiformat. In unserem Fall erlaubt es diese Gruppe von Klassen diese juristischen Quellen (ELI: `LegalResource`) allgemein zu beschreiben. 

"Switzerland publishes several collections of legal resources available in German, French and Italian and in some cases translated to Romanish or English. Most of the information published are documents, but some are just information about a legislative event, such as the starting date of a consultation published in the Federal gazette, or information about consultation events."

Staatsverträge (`Treaty`) sind auch juristische Quellen.

Beispiel: 

https://fedlex.data.admin.ch/eli/oc/2014/665

Die Ebene Fassung (`Expression`) wird verwendet, um die **Sprachversion** der jurischen Quelle wiederzugeben. In der Schweiz wird die Gesetzgebung systematisch auf Deutsch, Französisch und Italienisch, manchmal auch auf Rätoromanisch und Englisch publiziert. Für jede Sprache der juristischen Quelle besteht eine Fassung (Expression).

Beispiel: 

https://fedlex.data.admin.ch/eli/oc/2014/665/de

Die Ebene Manifestation (`Manifestation`) ist diejenige, der Verkörperung ihrer Fassung. Die Manifestationen spiegeln die juristischen Quellen in ihren verschiedenen **Publikationsformaten** wieder: docx, html, pdf (für den Text) **rdf** (für die Metadaten der Texte).

Beispiel: 

https://fedlex.data.admin.ch/eli/oc/2014/665/de/pdf

### Metadaten Abfrage
Die URL in der SPRQL-Abfrage (`https://fedlex.data.admin.ch/eli/cc/1999/404`) führt im Broswer zum Gesetzestext der Bundesverfassung in der Systematischen Rechtssammlung. (Der Path `/cc` steht für Classified Compilation). Die URI der deutschen Sprachversion `https://fedlex.data.admin.ch/eli/cc/1999/404/de` hingegen beschreibt nicht etwa den deutschen Text der eigentlichen Bundesverfassung sondern repräsentiert nur die "Kopfdaten", also Titel und Abkürzung auf Deutsch. 

Im Datenmodell von JoLux existieren innerhalb eines `jolux:ConsolidationAbstract` verschiedene **Sprachversionen**. Diese sind vom `rdf:type` `jolux:Expression` und sind durch die Eigenschaft `jolux:isRealizedBy` mit dem sprachübergreifenden Eintrag des `jolux:ConsolidationAbstract` verknüpft. 

Der eigentliche Inhalt der Gesetzestexte ist über die "Consolidations-Versionen" der SR Einträge angebunden.

## URIs

### Publikationsarten

Gemäss `Convention` ([URIs Templates for Legal Resources in Switzerland](https://fedlex.data.admin.ch/de-CH/home/convention)) gibt es die untenstehenden Publikationsarten. 

Diese sollten dem Bundesgesetz über die Sammlungen des Bundesrechts und das Bundesblatt [(Publikationsgesetz, PublG)](https://www.fedlex.admin.ch/eli/cc/2004/745/de) entsprechen. 

Template:

https://fedlex.data.admin.ch/eli/{collection}

Possible values for `{collection}`:

* `oc` for the Official compilation
* `cc` for the Classified compilation
* `treaty` for the publication of international treaties

* `oe` for reports about ordonnances
* `oldcc` for documents published in the Revised Compilation of Federal Acts and Ordinances 1848-1947 (BS)  
* `fga` for the Federal gazette                                                 
* `cons` for the publication of consultation procedures                         
* `ogc` for documents published in the Swiss Official Gazette of Commerce (SOGC)
* `ob` for documents published in the Official Bulletin of the Federal Assembly 

supporting documents?
* `fgae` for documents published as “reference” in texts published in the fga
* `oce` for documents published as “reference” in texts published in the oc
* `cce` for documents published as "reference” in texts published in the cc

military specific:
  * `mog` for documents published in the Militäramtsblatt (MA) / Feuille officielle militaire (FOM) / Foglio ufficiale militare (FUM)
  * `cmog` for documents published in the Sammelband des Militäramtsblattes (SMA) / Recueil de la Feuille officielle militaire (RFM) / Raccolta del Foglio ufficiale militare (RFM)

#### Legal Resource der Amtlichen Sammlung (oc)

{collection} = oc

Template:

https://fedlex.data.admin.ch/eli/oc/{year}/{natural identifier}


Example:

https://fedlex.data.admin.ch/eli/oc/2020/759

Der {natural identifier} in diesem Fall ist die chronologisch fortlaufende Nummer des Erlasses (YYYY > MM > p) in der AS. Für Texte vor 2000 ist das {volume} optional wie in diesem Fall. Die Verordnung über die Massnahmen im Kulturbereich gemäss Covid-19-Gesetz (Covid-19-Kulturverordnung) erschien in Band 127 der AS (Amtliche Sammlung > Ausgaben der AS > 2020 > Oktober > **127** > AS 2020 4147)

##### Vor 1999
Bei älteren Erlassen (vor 1999) ist der {natural identifier} zusammengesetzt aus {volume} und {page}. Aufgrund mehrerer Sprachversionen ist der {natural identifier} Kombination `{year}/{volume}”_”{page-de}”_”{page-fr}”_”{page-it}`.

Template:
```
https://fedlex.data.admin.ch/eli/{collection}/{year}/{volume}”_”{page-de}”_”{page-fr}”_”{page-it}
```

Example:

https://fedlex.data.admin.ch/eli/fga/1994/2_1_1_1

Die Endung `2_1_1_1` deutet auf "aligned language versions" für den Eintrag BBl 1994 II S. 1 hin.

Wenn 2_1_1_1 nicht "aligned" wäre, ergibt dich die Seitennummer aus der Scanreihenfolge durch das Schweizerische Bundesarchiv (gescannte Dokumentversion). Es wird dabei nur die vorliegende Sprachversion indiziert

BBl 1994 I 569, Jahresbericht des Bundesrates über die Tätigkeiten der Schweiz im Europarat 1993 vom 19. Januar 1994:

https://fedlex.data.admin.ch/eli/fga/1994/1_569__

BBl vom 3.Oktober 1940, S. 1083 (auf Französisch):

https://fedlex.data.admin.ch/eli/fga/1940/1__1083_

Remark: the language of the text is indicated in the metadata jolux:langage in the related Expression.


##### Zwischen 1948 und 1999

Template:

https://fedlex.data.admin.ch/eli/oc/{year}/{page-de}”_”{page-fr}”_”{page-it}

Example: AS 1996 1506, Verordnung vom 22. Mai 1996 über Finanzhilfen nach dem Gleichstellungsgesetz

https://fedlex.data.admin.ch/eli/oc/1996/1506_1506_1506

Die Texte sind verfügbar auf der [Webseite des Schweizerischen Bundesarchivs](https://www.amtsdruckschriften.bar.admin.ch/setLanguage.do?lang=DE&currWebPage=searchHome).

##### Zwischen 1848 und 1947

Template:

https://fedlex.data.admin.ch/eli/{collection}/{volume-number}”_”{page-de}”_”{page-fr}”_”{page-it}

Examples:
https://fedlex.data.admin.ch/eli/oc/VII/342_337_325 (From 1848 to 1874 the volume is indicated with Roman numbers)
https://fedlex.data.admin.ch/eli/oc/III/183_182_182 (From 1874 to 1947 the volume is indicated with Arabic numbers)

#### Legal Resources der Systemarischen Rechtssamlung (cc)

URI for a basic act of the classified compilation (Consolidation). The URI is made of the URI of the basic act published in the Official compilation; the collection identifier is changed from “oc” to “cc”.

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{natural identifier}

Example:

When the URI of a basic act in the Official compilation is:

https://fedlex.data.admin.ch/eli/oc/2020/759

the URI of its compilation in the Classified compilation is:

https://fedlex.data.admin.ch/eli/cc/2020/759

##### Main act
In most cases Classified compilations and their URIs are derived from the basic act published in the Official compilation when the Official Compilation (Amtliche Sammlung) is considered **the main act**. In this case the URIs of the Classified compilations (Systematische Sammlung) are the same followed by a sequential number starting at 2.

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{natural identifier}“-”{order number starting at 2}

Examples:

URI of the basic act in the Official compilation:

https://fedlex.data.admin.ch/eli/oc/2004/25

URI of the main act and following in Classified compilation:

https://fedlex.data.admin.ch/eli/cc/2004/25
https://fedlex.data.admin.ch/eli/cc/2004/25-2


If the basic act of the Classified compilation has been published in another collection than the Official compilation, the collection of the basic act is indicated at the end of the URI (e.g. fga).

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{natural identifier}“_”{collection of the basic act}

Example:

https://fedlex.data.admin.ch/eli/cc/2004/232_fga


In some cases, the basic act of a Classified compilation has not been published. The URIs are then identified by their {historicaldossierID}.

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{historicaldossierID}_cc

Example:

https://fedlex.data.admin.ch/eli/cc/1929/0029_cc

##### Version at point in time

URI for a Classified compilation with indication of the version
{point in time} = date of the version of the Classified compilation as YYYYMMDD.

Template:

URI of the Classified compilation/{point in time}

Example of URI for the version of a classified compilation on the 1/11/2015:

https://fedlex.data.admin.ch/eli/cc/2015/659/20151101

#### Legal resource des Bundesblatts (fga)

{collection} = fga

##### Seit 2000
Template:
```
https://fedlex.data.admin.ch/eli/fga/{year}/{natural identifier}
```

Example :

https://fedlex.data.admin.ch/eli/fga/2020/1

##### Vor 2000
See oc.

### Sprachen
URIs for linguistic versions of LegalResource (Expression)
{language} = iso code (ISO-639-1) of the languages: “de”, “fr”, “it”, “rm”, “en”

The URIs of linguistic versions of a legal resource are based on a concatenation of the URI of the legal resource and the iso code of the language.

Template:

{URI of the legal resource}/{language}

Example of URI for the German version of the legal resource published in the Official compilation:

https://fedlex.data.admin.ch/eli/oc/2007/928/de

Example of URI for the German version of a Classified compilation:

https://fedlex.data.admin.ch/eli/cc/2007/928/de

### File format (Manifestation)

{user-format}: code of the functional format of the file.

Format can have the following values: “html”, “pdf-x”, “pdf-a”, “pdf-a-an”, “docx”, “docx-an” where “an” stands for “anonymized version”, “x” stands for “print version” and “a” for “display version” (see the property skos:notation of the controlled vocabulary for more details https://fedlex.data.admin.ch/vocabulary/user-format).

The URI of legal resource in a specific linguistic version and a specific format is the concatenation of the URI of the linguistic version followed by the code of the format of the publication.

Template:

{work uri}/{language}/{user-format}

Example of URI for the **html** publication of the German version the basic act on legal publications:

https://fedlex.data.admin.ch/eli/oc/2007/928/de

Example of URI for the signed **pdf** of the German version of a consolidated compilation:

https://fedlex.data.admin.ch/eli/oc/2007/928/de/pdf-a

#### Version of a Manifestation
If there is a need to change a file described by a Manifestation, for traceability reason, the former document will be related to the Manifestation through the property `jolux#wasExemplifiedBy`, when the newest version will be related to the Manifestation through the property `jolux#isExemplifiedBy` (is vs.was).

Use cases: a new version of provisional consolidation is published. The description of the consolidation (Consolidation) and the description of the linguistic versions (Expression) and files (Manifestation) are unchanged, the former version of the provisional consolidation now related with the property jolux#wasExemplifiedBy to the Manifestation.

See an example with the Manifestation:

https://fedlex.data.admin.ch/eli/cc/27/317_321_377/20210501/fr/pdf-a

### Gliederung

#### URI for appendices, annexes or parts of a legal resource (LegalResource)
{part} = The code “app” is used for each part of the document, except the main part.

Template:

{work uri}/{part type}/{order number}

Example of URI for annex 2 of a legal resource:

https://fedlex.data.admin.ch/eli/oc/2017/663/annex/2

URI for subdivision of a legal resource (`LegalResourceSubdivision`) {subdivision type}: The subdivision types are the same as the ones used in the `xml/AkomaNtoso` document. 

See the property skos:notation of the controlled vocabulary https://fedlex.data.admin.ch/vocabulary/subdivision-type to have the codes for the subdivision types.

See also the website of the Federal Chencellery (Bundeskanzlei) with a [Documentation for the propoer publication](https://www.bk.admin.ch/bk/de/home/dokumentation/begleitende-rechtssetzung/dokumentation-rechtsetzungsbegleitung.html) of laws for useful background information.

Two types of subdivision hierarchies can be described for the same text:

1. a hierarchy of articles and sub-elements of articles,

2. a hierarchy of documents made of chapters, sections, titles…

The two hierarchies are independent from each other which allows to insert new sections in a document without impact on the identification of the articles and their sub-levels and reciprocally.

#### Subdivision: articles and subdivisions of articles
Template:

{work uri}/{subdivision type}”_”{id of the subdivision}/{subdivision type}”_”{id of the subdivision}

Examples of URI for the article 1 of a legal resource:

https://fedlex.data.admin.ch/eli/oc/2021/137/art_1

#### Subdivisions: chapters, titles, sections:
The code “tit” is used on each of the levels, which can be chapters, sections, titles…

Template:

{work uri}/{subdivision type}”_”{id of the level section}/{subdivision type}”_”{id of the level section}/

Example of URI for the level 1 of a legal resource:

https://fedlex.data.admin.ch/eli/oc/2021/153/lvl_I
Texts available at the national archives

For pre-1999 texts these are only available in the national archives. For the Federal gazette there is one scanned text for each legislative resource. For the Official compilation there is one scanned text for each weekly publication of the official journal. For the Official compilation the scanned version of the text has been structured as an XML document.

### URI for collections, edition, language and format

To display whole collections, we add the path `collection` inbetween `eli` and `{collection}`. After that `{year}/{edition number}` and `{language}` (optional).

Template:

https://fedlex.data.admin.ch/eli/collection/{collection}/{year}/{edition number}/{language}

Example: URI of the Official **compilation** of 2010:

https://fedlex.data.admin.ch/eli/collection/oc/2010

Example: URI of the edition of the Official compilation in week 23 from year 2010 (edition of a collection (Memorial)):

https://fedlex.data.admin.ch/eli/collection/oc/2010/23

Example: URI of the Italian edition of the official compilation in week 23 from year 2010 (linguistic version of an edition (Expression)):

https://fedlex.data.admin.ch/eli/collection/oc/2010/23/it

Example: URI of the Italian edition of the official compilation in week 23 from the year 2018 in the language Italian with the file format PDF (a specific file format (Manifestation)):

https://fedlex.data.admin.ch/eli/collection/oc/2010/23/it/pdf-a

#### URI for edition of the complete legislation
Edition abstract
URI for the edition family (EditionAbstract)
https://fedlex.data.admin.ch/eli/edition/{edition type}

{edition type} : “national” or “international”

Examples :

https://fedlex.data.admin.ch/eli/edition/national
https://fedlex.data.admin.ch/eli/edition/international
Edition

#### URI for the edition (Edition)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302 https://fedlex.data.admin.ch/eli/edition/international/20220302
URI for the expression of an edition (Expression)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{language}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de https://fedlex.data.admin.ch/eli/edition/international/20220302/fr
URI for the manifestation of an edition (Manifestation)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{language}/{format}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/pdf-a https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/pdf-a
Remark: indicate “pdf-a” format even if the pdf is in a zip file.

#### Binder
URI for a binder in a given language (Edition)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{edition language}/{binder number}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/3 https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/2
URI for the expression of a binder (Expression)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{edition language}/{binder number}/{language}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/3/de https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/2/fr
URI for the manifestation of a binder (Manifestation)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{edition language}/{binder number}/{language}/{format}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/3/de/pdf-a https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/2/fr/pdf-a
URI for the compendium (Compendium)

#### Compendium is an ad-hoc compilation of legal resources.
Template:

https://fedlex.data.admin.ch/{collection}/{compendium}/{year}{serial number}

Example:

https://fedlex.data.admin.ch/fga/compendium/2021/1
URI for the linguistic version of a compendium with indication of the language (Expression)
Template:

https://fedlex.data.admin.ch/eli/compendium/{year}/{serial number}/{language}

Example of the German version of a compendium:

https://fedlex.data.admin.ch/fga/compendium/2021/1/de
URI for the linguistic version of a compendium in a specific file format (Manifestation)
Template:

https://fedlex.data.admin.ch/eli/compendium/{year}/{serial number}/{language}/{user format}

Example:

https://fedlex.data.admin.ch/fga/compendium/2021/1/de/pdf-x

### URI for legal analysis (LegalAnalysis)
The URI of the legal resource analysis is based on the URI of the legal resource which is analysed. Legal resource impact describes the legal impact of a legal resource on another legal resource (initial version or consolidated version). 

Before 1/1/2021, the legal impacts are described from text to text with a comment on the impacted articles. Since 1/1/2021, the legal impacts are described from `articles` or `titles` of legal resources to articles or titles of the impacted legal resource.

Template:

{uri the legal resource which is analysed}/legal-analysis

Example: Analysis of the legal impact of a legislation:

https://fedlex.data.admin.ch/eli/oc/2021/115/legal-analysis

AS 2021 115 Verordnung 3 über Massnahmen zur Bekämpfung des Coronavirus (Covid-19) (Covid-19-Verordnung 3) (Liste der Erkrankungen, die Personen zu besonders gefährdeten Personen machen) has one URI for legal resource impact (LegalResourceImpact): Anhang 7 der Covid-19-Verordnung 3 vom 19. Juni 2020 wird gemäss Beilage gestützt auf Artikel 27a Absatz 12 der Covid-19-Verordnung 3 geändert." 

The URI of the impact is based on the URI of the legal analysis of the legal resource:

Template:

{uri of the legal analysis of the legal resource}/LegalResourceImpact/{impact number}

Example of the URI for a legal impact of a legislation:

https://fedlex.data.admin.ch/eli/oc/2021/115/legal-analysis/LegalResourceImpact/1


### URI for citation (Citation)
Citation describes the citation from legal resource to another legal resource. Before 1/1/2021, the citations are described from text to text with a comment on the cited article. Since 1/1/2021, the citations are described from articles of legal resource to articles of the cited legal resource.

The URI of the citation is based on the URI of the version of legislation which cites.

Template:

{uri of the subdivision of the legal resource which cites}/{point in time}/citation/{citation number}

Example of the URI of a citation made from the version of the 1/1/2020 of a consolidated text:

https://fedlex.data.admin.ch/eli/cc/2002/452/text/20180701/citation/10
URI for treaty (TreatyProcess)
Starting from January 1st, 2021
Template:

https://fedlex.data.admin.ch/eli/treaty/{year}/{treaty number - 4 digits}

Example:

https://fedlex.data.admin.ch/eli/treaty/2021/0242
Before January 1st, 2021

Before 1/1/2021 the existing treaty identifiers will be reused adding a “/” before the treaty number. Identifier as 2018234 becomes 2018/0234, identifier as 99992335 will become 9999/2335.

Example 1:

https://fedlex.data.admin.ch/eli/treaty/2018/1072
Example 2:

https://fedlex.data.admin.ch/eli/treaty/9999/6088
URI of treaties considered as annexes:
Template:

{uri of the parent treaty}1{annex number - 3 digits}

Example:

https://fedlex.data.admin.ch/eli/treaty/1978/00261001
URI of treaties considered as modifications:
Template:

{uri of the parent treaty}2{modification number - 3 digits}

Example:

https://fedlex.data.admin.ch/eli/treaty/1923/00112012
URI of treaties based on European conventions:
Template:

https://fedlex.data.admin.ch/eli/treaty/1234/{convention number}

Example:

https://fedlex.data.admin.ch/eli/treaty/1234/18037
Creation of new treaties from decision of joint committee:
Template:

https://fedlex.data.admin.ch/eli/treaty/1357/{decision number}

Example:

https://fedlex.data.admin.ch/eli/treaty/1357/18424

### URI for draft legislation
#### URI for Legislative Project (InitialDraft)
Legislative projects make it possible to group the various tasks and publications that mark the process of publishing a law. This type of resource does not exist today, it should be created based on the migrated publication dossiers. The linked publication dossiers will all be attached to a single legislative project. Consultations will also be related to the legislative project.

Template:

https://fedlex.data.admin.ch/eli/dl/proj/{year}/{legislative_process_identifier}

Example:

https://fedlex.data.admin.ch/eli/dl/proj/2022/15

#### URI for the tasks of Legislative Project (LegislativeTask and their sub-classes)
The stage of the process that take place throughout the creation of a new law (consultation, parliament...) have the URI of the legislative project in which they register followed by a number.

{task type}: for the possible values see the property skos:notation of the vocabulary https://fedlex.data.admin.ch/vocabulary/type-projet

Template:

{URI of the legislative project}/{task type}”_”{sequence of the task}/{task type}”_”{sequence of the task}

Remark: {sequence of the task} is facultative if the task opens only once.

Example for a consultation:

https://fedlex.data.admin.ch/eli/dl/proj/6020/6/cons_1
Example for the subtask of a consultation, the publication of position statements:

https://fedlex.data.admin.ch/eli/dl/proj/6020/6/cons_1/cons-open

#### URI for the text of a legislative project (DraftDocument)
Uri for the abstract of the text of a legislative project (DraftDocumentAbstract).
Template:

{URI of the legislative project}/{task type}”_”{sequence of the task}/{document identifier}

Example:

https://fedlex.data.admin.ch/eli/dl/proj/6020/34/cons_1/doc_1

#### URI for the document related to the text of a legislative task (DraftRelatedDocument)
For the abstract of a document related to a legislative task (DraftRelatedDocumentAbstract)
Template:

{URI of the legislative project}/{task type}”_”{sequence of the task}/{document identifier}

Example of a document provided for a consultation.

https://fedlex.data.admin.ch/eli/dl/proj/6020/34/cons_1/doc_2

