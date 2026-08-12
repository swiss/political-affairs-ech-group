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

Die **Rechtstexte** werden auf 4 Ebenen beschrieben: der abstrakte Text (ComplexWork), der Text (Work), die Fassung (Expression) und die Manifestation (Manifestation).

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

Die URL in der SPRQL-Abfrage (`https://fedlex.data.admin.ch/eli/cc/1999/404`) führt im Broswer zum Gesetzestext der Bundesverfassung in der Systematischen Rechtssammlung. (Der Path `/cc` steht für Classified Compilation). Die URI der deutschen Sprachversion `https://fedlex.data.admin.ch/eli/cc/1999/404/de` hingegen beschreibt nicht etwa den deutschen Text der eigentlichen Bundesverfassung sondern repräsentiert nur die "Kopfdaten", also Titel und Abkürzung auf Deutsch. 

Im Datenmodell von JoLux existieren innerhalb eines `jolux:ConsolidationAbstract` verschiedene **Sprachversionen**. Diese sind vom `rdf:type` `jolux:Expression` und sind durch die Eigenschaft `jolux:isRealizedBy` mit dem sprachübergreifenden Eintrag des `jolux:ConsolidationAbstract` verknüpft. 

Der eigentliche Inhalt der Gesetzestexte ist über die "Consolidations-Versionen" der SR Einträge angebunden.

