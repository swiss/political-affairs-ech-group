## Status ## {#status}

Der vorliegende Standard befindet sich im Status <em>In Arbeit</em>. Der Gebrauch ist nur innerhalb der Fachgruppe sowie im Expertenausschuss zugelassen.

## Anwendungsgebiet ## {#anwendungsgebiet}

Das Anwendungsprofil eCH-0296 ist eine Lokalisierung des Akoma Ntoso (AKN) [[AKN]] und des European Legislation Identifier (ELI) [[ELI]] Standards für die Schweiz. AKN ist ein XML-Standard für Dokumente in den Bereichen parlamentarische Geschäfte, Gesetzgebung (Legislative) und Rechtsprechung (Judikative). ELI ist ein System für die Identifizierung von Rechtsvorschriften, welches auf einem gemeinsamen Standard beruht.

Die Bereitstellung der Gesetzessammlung in digitaler Form wird in der angestrebten Soll-Architektur des Systems E-Government Schweiz [[eCH-0122]] als Geschäftsfähigkeit mit Voraussetzungscharakter definiert. Durch Herstellung der semantischen und Ermöglichung der technischen Interoperabilität zwischen allen Verwaltungsebenen können der Austausch von Rechtsdaten vereinfacht und Redundanzen eliminiert werden. Die angestrebte Interoperabilität wird erreicht indem alle Verwaltungsebenen ihre Erlasse und Gesetzestexte in strukturierter und maschinenlesbarer Form veröffentlichen. Das Anwendungsprofil eCH-0296 ermöglicht dies, indem es für den Gesetzgebungs- und Publikationsprozess eine einheitliche Sprache und Schnittstellen definiert.

Im Einzelnen unterstützt eCH-0296 folgende Anwendungsfälle:

<dl>
  <dt>Strukturierte Publikation von Erlassen</dt>
  <dd>Einheitliche, maschinenlesbare Abbildung von Gesetzen, Verordnungen und weiteren Erlassen mittels AKN.</dd>
  <dt>Eindeutige Identifikation und Verlinkung</dt>
  <dd>Vergabe persistenter, auflösbarer Identifikatoren für Erlasse und deren Bestandteile mittels ELI, ebenenübergreifend von der Gemeinde bis zum Bund.</dd>
  <dt>Föderierter Zugang zu Rechtssammlungen</dt>
  <dd>Ermöglichung des standardisierten Austauschs und der Aggregation von Erlassdaten zwischen den Verwaltungsebenen und mit europäischen Systemen.</dd>
</dl>

## Aufbau ## {#aufbau}

Der Hauptteil besteht aus drei normativen Modulen, die aufeinander aufbauen:

<dl>
  <dt>Identifier (Kapitel 2)</dt>
  <dd>Regeln zur Bildung von gültigen URIs für Gesetze und andere Dokumente im Gesetzgebungsprozess.</dd>
  <dt>Content (Kapitel 3)</dt>
  <dd>Die unterschiedlichen Dokumententypen und deren Struktur.</dd>
  <dt>Metadata (Kapitel 4)</dt>
  <dd>Daten, welche die Dokumente und Beziehungen unter den Dokumenten weiter beschreiben.</dd>
</dl>

Das vorliegende Kapitel 1 ist rein informativer Natur und verfolgt zwei Ziele:

Einerseits wird Bezug auf die übergeordneten Arbeiten der Fachgruppe Politische Geschäfte genommen, indem es die Begrifflichkeiten rund um den Gesetzgebungs- und Publikationsprozess und die Dokumententypen, die dabei entstehen, definiert.

Andererseits werden die Grundlagen technischer und konzeptioneller Natur vermittelt, die für das Verständnis der normativen Module vorausgesetzt werden.

Darüber hinaus ist jeweils der erste Abschnitt jedes Moduls ebenfalls rein informativer Natur.

## Fachgruppe Politische Geschäfte ## {#fachgruppe}

Das Anwendungsprofil eCH-0296 ist das Ergebnis der Arbeiten der Fachgruppe Politische Geschäfte. In sechs Arbeitsgruppen (Meta, Operations, Actors, Affairs, Laws and Consultations) wurden Datenmodelle, -formate und -protokolle der Domäne Politische Geschäfte für alle Verwaltungsebenen standardisiert.

Im vorliegenden Anwendungsprofil eCH-0296 stehen die im Rahmen des Gesetzgebungs- und Publikationsprozesses erzeugten Dokumententypen, inbesondere Erlasse und Gesetzestexte, und deren Beziehungen untereinander im Vordergrund. Sie respektieren die im Rahmen der Fachgruppe Politische Geschäfte definierten Schemata.

### Begrifflichkeiten ### {#begrifflichkeiten}

Der Begriff Gesetz ist streng genommen vom Begriff Erlass mitumfasst. Wenn man hier also von Erlassen und Gesetzestexten spricht, sind damit alle Stufen (Verfassung, Gesetze und Verordnungen) und Ausgestaltungen (Beschluss, Aufhebung, Änderung, Löschung) gemeint. Wenn im Nachfolgenden der Begriff Erlass verwendet wird, ist damit entweder der Überbegriff oder in Abgrenzung zu Gesetzen im formellen Sinn, jeder Akt eines Parlaments gemeint, der zwar rechtsetzenden Charakter hat, aber ohne materiellen Gehalt entweder ein bereits bestehendes Gesetz in Kraft setzt oder aufhebt.

Wichtig ist, dass es sich bei Gesetzen um Texte mit rechtsetzendem Charakter handelt, die Gegenstand einer juristischen Auslegung sein können, und somit auf einer semantischen Ebene mit Hilfsmaterialien (Erläuternder Bericht, Parlamentarisches Geschäft) unterlegt werden können. Diese Hilfsmaterialien als Produkt von politischen Geschäften gehören deshalb ebenfalls zu den hier definierten Dokumententypen des Gesetzgebungs- und Publikationsprozesses.

Der gesamte Gesetzgebungs- und Publikationsprozess ist ein Wechselspiel unterschiedlicher Akteure. Neben Parlamenten sind bei der Schaffung neuer und der Änderung bestehender Gesetze weitere Stakeholder wie redaktionelle Kommissionen und publizierende Organe beteiligt:

<dl>
  <dt>Übersetzung</dt>
  <dd>Nach einer erfolgreichen Abstimmung über den Schlussabstimmungstext im Parlament muss das Gesetz meist eine redaktionelle Bereinigung durchlaufen und wird für gewöhnlich in weitere Landessprachen übersetzt.</dd>
  <dt>Konsolidierung</dt>
  <dd>Änderungen an einem Gesetz haben meistens Auswirkungen auf weitere Gesetze, was dazu führt, dass diese Auswirkungen in die neuen Fassungen konsolidiert werden müssen.</dd>
  <dt>Inkrafttreten und Referendum</dt>
  <dd>Die meisten Erlasse treten erst zu einem späteren vordefinierten Zeitpunkt in Kraft. Aber auch gültig zustandegekommene Erlasse können – sofern ein Referendum zustande kommt und der Erlass vom Volk abgelehnt wird – noch vor ihrem Inkrafttreten wieder aufgehoben werden.</dd>
  <dt>Ratifikation</dt>
  <dd>Sodann ist an die Ratifikation internationaler Verträge zu denken, die in einem ersten Schritt von der Exekutive oder speziellen Organen ausgehandelt und danach vom Parlament genehmigt werden müssen.</dd>
</dl>

All diese Vorgänge haben zur Folge, dass ein oder mehrere Dokumente publiziert werden, welche wiederum auf andere Dokumente im Gesetzgebungs- und Publikationsprozess Bezug nehmen können. Wie diese Dokumente strukturiert sind, welche Metadaten benötigt werden um Beziehungen untereinander abzubilden, und wie diese Dokumente über einheitlich gebildete und möglichst persistente Links abgerufen werden können, ist Gegenstand dieses Standards.

### Dokumententypen ### {#dokumententypen}

Die folgenden Dokumententypen werden im Nachfolgenden teilweise oder vollständig als Beispiele aufgeführt:

#### Parlamentarische Geschäfte #### {#parlamentarische-geschaefte}


<pre class=include>
path: sections/tables/table-1.html
</pre>


#### Vernehmlassungen und Erläuternde Berichte #### {#vernehmlassungen}


<pre class=include>
path: sections/tables/table-2.html
</pre>


#### Erlasse und Gesetzestexte #### {#erlasse-gesetzestexte}


<pre class=include>
path: sections/tables/table-3.html
</pre>


#### Internationale und -kantonale Verträge #### {#internationale-vertraege}


<pre class=include>
path: sections/tables/table-4.html
</pre>


## Grundlagen ## {#grundlagen}

Die Ausführungen zu den technischen und konzeptionellen Grundlagen werden für das weitere Verständnis der normativen Kapitel vorausgesetzt, sind aber rein informativer Natur.

Alle nachfolgenden Beispiele sind fiktiv und dienen der Illustration. Es handelt sich nicht um gültige AKN4CH Dokumente.

### Technische Grundlagen (XML) ### {#xml-grundlagen}

AKN ist ein XML Standard. Damit ist XML das technologische Fundament für AKN und AKN4CH. Jedes XML Dokument beginnt mit der Zeile <code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;</code> mit Informationen zur XML-Version (1.0) und zum Zeichensatz (UTF-8).

Elemente und Attribute lassen sich in XML grundsätzlich frei definieren, dies im Gegensatz zu HTML wo gewisse Elemente vorausgesetzt werden (Beispiele: <code>&lt;a&gt;</code> oder <code>&lt;p&gt;</code>). AKN gibt ebenfalls standardisierte XML Elemente und Attribute vor, die in vordefinierten Dokumententypen vorkommen dürfen.

AKN4CH geht einen Schritt weiter und definiert eine begrenzte Auswahl an erlaubten AKN Elementen und Attributen sowie Regeln zur Strukturierung der erlaubten Dokumententypen. Ein beliebiges AKN4CH Dokument folgt dabei stets demselben Aufbau:

<div class="example" id="example-1">
<pre class=include-code>
path: examples/example-1.xml
highlight: xml
line-numbers:
</pre>
</div>

Das Root-Element <code>&lt;akomaNtoso&gt;</code> lässt erkennen, dass es sich um ein AKN Dokument handelt.

Das zugehörige Attribut <code>xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"</code> legt den Namespace des Dokumentes fest und bewirkt, dass alle darauffolgenden Elemente und Attribute den Regeln des Akoma Ntoso Standards in der Version 3.0 gehorchen müssen.

Der Präfix <code>xmlns:akn4ch="http://legaldocml.ch/"</code> erweitert den AKN Namespace mit spezifischen Eigenheiten für Schweizer Rechtsdaten: AKN4CH schränkt die Wahlfreiheit innerhalb von AKN weiter ein, indem es die möglichen Dokumententypen, deren Struktur und Metadaten für die Schweiz einheitlich definiert.

Das Element <code>&lt;documentType&gt;</code> gibt es so nicht — es handelt sich um einen Platzhalter für Dokumententypen wie z.B. <code>&lt;act&gt;</code> (für Gesetze) oder <code>&lt;bill&gt;</code> (für Gesetzesentwürfe). Der Dokumententyp bestimmt die Struktur indem es die erlaubten Elemente innerhalb des AKN- und AKN4CH-Namespace definiert.

Das <code>&lt;meta&gt;</code> Element enthält wichtige Metadaten zur Identifizierung, wie URI, Datum, Autor, Land, Nummer, Name, Abkürzung, Sprache und Format, sowie weitere Metadaten zum Gesetzgebungs- und Publikationsprozess.

Das <code>&lt;body&gt;</code> Element enthält die eigentlichen Inhalte des Dokuments, die für den Nutzer sichtbar sind, wie Artikel, Abschnitte und andere Strukturelemente.

Diese XML Dokumente können als Ausgangsformat für andere Dateiformate benutzt werden.

### Konzeptionelle Grundlagen (FRBR) ### {#frbr-grundlagen}

[[FRBROO]] steht für Functional Requirements of Bibliographical Records. Darin wird ein abstraktes Werk und seine sprachlichen Fassungen von einer konkreten Veröffentlichung in einem Format konzeptionell getrennt.

In FRBR werden vier Abstraktionsstufen definiert:

* Work
* Expression
* Manifestation
* Item

Beispiel: Die Bundesverfassung der Schweizerischen Eidgenossenschaft vom 12. September 1848 hat seither zahlreiche Veränderungen erfahren und ist mit der heute gültigen Version vom 18. April 1999 nicht mehr vergleichbar. Zudem sind mehrere sprachliche Versionen und unterschiedliche Dateiformate denkbar.

Sowohl AKN als auch ELI bedienen sich dieses konzeptionellen Modells. AKN4CH Dokumente sind XML Dateien und damit Manifestationen. Jedes AKN4CH Dokument enthält Metadaten zur eindeutigen Identifikation des abstrakten Werks, der sprachlichen Fassung und des Dateiformats: URI, Datum, Autor, Land, Nummer, Name, Abkürzung, Sprache und Format.

<div class="example" id="example-2">
<pre class=include-code>
path: examples/example-2.xml
highlight: xml
line-numbers:
</pre>
</div>

Darüber hinaus gibt <code>&lt;FRBRauthoritative value="true" /&gt;</code> an, ob es sich um die massgebende Fassung handelt, welche Rechtswirkungen entfaltet, wenn es mehrere unterschiedliche Fassungen in unterschiedlichen Sammlungen gibt.
