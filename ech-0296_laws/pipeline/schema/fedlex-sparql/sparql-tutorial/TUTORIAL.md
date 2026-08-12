# Fedlex Tutorial

Das folgende Beispiel wurde übernommen aus: [Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/). 

Mehr Tutorials zu Linked Data aus der Schweiz hier: https://zazuko.com/get-started/.

## Usage
Following the instructions below will return the (meta-)data of the Federal Constitution of the Swiss Confederation from the Fedlex SPARQL Endpoint in HTML format. 

1. Insert your SPARQL query inside `sparql_query.txt`.
2. (optional) Add you custom endpoint and assign a variable in `sparql_endpoints.txt`. Adapt the variable to your endpoint in `main.py` line 11. The default endpoint is `F=https://fedlex.data.admin.ch/sparqlendpoint`.
4. Run `python main.py` inside the shell at the root directory of the project to run the program.

Files:
- `query.py` contains the logic
- `display_result.py` renders the code as HTML
- `sparql_endpoints.txt` input file containing available SPARQL Endpoints. (Default is set to Fedlex.)
- `sparql_query.txt` input file containing the SPARQL query to the endpoint in question.

You can also run SPARQL querys directly in any `.sparqlbook` file in VS Code without the files above:
- First install [Sparql Notebook Extension](https://marketplace.visualstudio.com/items?itemName=Zazuko.sparql-notebook) (Documentation)
- Connect to a remote server by clicking the + button in the SPARQL Connections panel in the VS Code extension. 
- Fedlex Endpoint: Fill in the server URL and optional credentials: https://fedlex.data.admin.ch/sparqlendpoint
- Run the cell: Click on the traingle left of a cell inside the editor.
- This connection is used throughout the entire notebook, except when a cell defines its own endpoint.
- Right click a `.sparqlbook`file and select Export to Markdown.

## SPARQL API

Die API von Fedlex ist auch über einen SPARQL Endpoint verfügbar:
- [API Endpoint](https://fedlex.data.admin.ch/sparqlendpoint)
- [SPARQL Playground](https://fedlex.data.admin.ch/de-CH/sparql) von Casemates mit vordefinierten Abfragen für **Fedlex**. 

Die Website https://fedlex.admin.ch und alle dort angzeigten Daten sind in Form von **Linked Data**, d.h. Triples im Datenformat RDF (Resource Description Framework) in einem Triple Store gespeichert und mit Hilfe des SPARQL Endpoints  maschinenlesbar. Im Gegensatz zu relationalen Datenbanken werden die Daten in Triple Stores als  **Triples** (daher mit Tabellen nicht visualisierbar) gespeichert. 

Die URI bzw. die URL der Bundesverfassung `https://fedlex.data.admin.ch/eli/cc/1999/404` verweist auf den Gesetzestext. Im [Metadaten-Explorer](https://fedlex.data.admin.ch/de-CH/metadata) kann man die damit verknüpften Linked Data Triples durchsuchen. 

Eine Abfrage der Linked Data Triples der Bundesverfassung über den Metadaten-Explorers weist stets folgende URL auf:
- die Sprache als path `/de-CH` 
- der Gesetzestext als Parameter: `/metadata?value=`

Die zusammengesetzte URL: https://fedlex.data.admin.ch/de-CH/metadata?value=https://fedlex.data.admin.ch/eli/cc/1999/404

Die Metadaten werden in der Sprache des semantischen Webs RDF veröffentlicht. Dazu werden verschiedene Ontologien genutzt, unter anderem das ELI-Modell («European Legislation Identifier»). Neben vordefinierten Suchen und strukturierten Suchen über Webformulare werden die RDF-Daten auch über einen sog. SPARQL-Endpoint für Abfragen zur Verfügung gestellt.

Jolux Vokabular und Namespaces, die mit Jolux verknüpft sind:
* [Download Jolux Ontology](https://fedlex.data.admin.ch/filestore/resources/jolux_ontology.zip) (.zip file)
* `skos` : [SKOS Vokabular](http://www.w3.org/2004/02/skos/core#)
* `rdf` : [RDF Vokabular](http://www.w3.org/1999/02/22-rdf-syntax-ns#)

Eine SPARQL Abfrage ist nichts anderes als ein POST-Request an den entsprechenden Triple Store Datenbank Server. Wir benutzen dazu das Web-Interface:

![Virtuoso SPARQL Query Editor abrufbar unter: https://fedlex.data.admin.ch/sparqlendpoint](<Screenshot 2024-04-27 at 14.04.54.png>) (Web-Interface)

## SPARQL queries

SPARQL Queries folgen einem grundlegenden Aufbau, der immer gleich lautet:

```
SELECT * WHERE 
{
    ?subject ?predicate ?object.   
}
```

Triples folgen der grammatikalischen Struktur **Subjekt -> Prädikat -> Objekt**.  Einzelne Positionen der Triples können bewusst undefiniert gelassen und mit der Variable `?`bezeichnet werden. 

Das Ziel unserer ersten Query in der Bundesverfassung ist es Triples suchen, in denen die Bundesverfassung als **Subjekt** erscheint. Alle Triples müssen dieses Muster erfüllen:

```
SELECT DISTINCT ?Prädikat ?Objekt WHERE {
    
    <https://fedlex.data.admin.ch/eli/cc/1999/404> ?Prädikat ?Objekt .
} 
```

In SPARQL ist die `URI der Bundesverfassung` das **Subjekt** der SPARQL-Abfrage. Wir setzen das `Prädikat` und `Objekt` als Variablen ein (`?`). `SELECT` beschreibt welche Variablen zurückgegeben werden sollen und mit `DISTINCT` werden doppelte Ergebnisse aussortiert. Die Aussage endet mit einem Punkt und die Abfrage gibt alle Elemente zurück, die das definierte Pattern erfüllen. 

Eine ausführliche Anleitung zum Pattern Matching ist [hier](https://programminghistorian.org/en/lessons/retired/graph-databases-and-SPARQL#rdf-in-brief) zu finden. 

Das Ergebnis ist eine Tabelle mit allen Prädikaten und den entsprechenden Objekten (unsere Variabeln), die in allen abgespeicherten Triples mit der Bundesverfassung als Subjekt vorkommen.

![alt text](<Screenshot 2024-04-27 at 14.17.45.png>)

Als **Objekte** sehen wir URIs (Objekte die dereferenzierbar und ihrerseits mit Prädikaten beschrieben sind) und **Literals** (Strings die eine bestimmte Information (z.B. Datum) transportieren).

Die Bundesverfassung ist vom Typ `rdf:type` `jolux:ConsolidationAbstract` (**Objekt**), der einen SR-Eintrag (Gesetz auf abstrakter Ebene) darstellt. 

Das **Prädikat** `classifiedByTaxonomyEntry` im  [Vokabular](https://fedlex.data.admin.ch/vocabularies/de/) (Begriffsverzeichnis) der Bundeskanzlei beschreibt der SR-Eintrag. Es ist die zuverlässigste Quelle zum Abfragen der SR-Nummer eines SR-Eintrags.

Mehr Informationen zu SPARQL:
- [SPARQL-Tutorial 1](https://jena.apache.org/tutorials/sparql.html) 
- [SPARQL Tutorial 2](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial) from Wikidata