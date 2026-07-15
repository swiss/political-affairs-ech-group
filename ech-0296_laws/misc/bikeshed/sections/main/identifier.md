## Einleitung ## {#identifier-einleitung}

### ELI HTTP URI Vorlage ### {#eli-uri-vorlage}

Der digitale Austausch von Rechtsdaten zwischen Verwaltungsebenen erfordert Kenntnisse über den Speicherort und Eigenheiten des Rechtssystems. Kenntnis über den Speicherort erlangt man

AKN4CH folgt dem ELI Standard und nutzt zur Identifikation von Rechtstexten HTTP URIs. Die URIs werden formell über maschinenlesbare URI-Schematafeln beschrieben ([[RFC6570]]).

Die Implementierung von ELI URIs ist nur einer von vier Pfeilern des ELI Standards. Pfeiler 2-4 setzen eine Beschreibung der Rechtsdaten mit Metadaten voraus. Siehe dazu Kapitel Metadaten.

ELI URIs bestehen aus hierarchisch aufgebauten Komponenten, die entsprechend den nationalen Anforderungen ausgewählt werden können. Komponenten werden in der Regel durch "/" voneinander getrennt, wodurch sie in ihrer Gesamtheit einen Pfad bilden, der sowohl aus Endnutzer- als auch aus rechtlicher Perspektive eine semantische Bedeutung tragen kann. ELI empfiehlt die Nutzung der vorgeschlagenen Referenz-Komponenten, welche – mit Ausnahme der ersten "eli" Komponente – optional sind und in keiner vordefinierten Reihenfolge aneinandergereiht werden können.

Das folgende Beispiel macht sich alle der vorgeschlagenen Referenz-Komponenten in der vorgeschlagenen Reihenfolge zu Nutze:

<div class="example" id="example-4">
<pre class=include-code>
path: examples/example-4.txt
</pre>
</div>

Die Referenz-Komponenten lassen sich in vier Gruppen aufteilen: Jurisdiction, Reference, Subdivision und Point in time. Zusätzlich wird zwischen einer massgebenden und konsolidierten (Version) sowie unterschiedlichen sprachlichen Fassungen (Language) unterschieden. Insbesondere Gliederungsebenen innerhalb eines Dokuments (Subdivision) und der Umgang mit Korrigenda (Subtype) werden hier ausgeblendet, da bei AKN4CH die Dokumentenperspektive im Vordergrund steht.

Für die Festlegung der AKN4CH URI-Vorlage stehen vor allem folgende Komponenten-Gruppen im Vordergrund:

<dl>
  <dt>Jurisdiction (i.w.S.)</dt>
  <dd>Bei mehreren publizierenden Stellen muss zunächst klargestellt werden, welchem Gemeinwesen ein Rechtstext zugeordnet wird (Jurisdiction i.e.S.) und, sofern notwendig, welcher Akteur diesen erlassen hat (Agent bzw. Subagent).</dd>
  <dt>Reference</dt>
  <dd>Zum Zweck der eindeutigen Identifikation muss ein Rechtstext referenzierbar sein. Wie das zu geschehen hat, ist von Land zu Land unterschiedlich und hängt stark von der Publikationspraxis ab. Denkbar sind Zeitangaben, Dokumententyp, Themen-Codes (Domain) und – falls notwendig – weitere Unterscheidungsmerkmale (Natural identifier).</dd>
</dl>

### URI-Vorlage und ELI Referenz-Komponenten ### {#eli-referenz-komponenten}

Die folgende Tabelle beschreibt die Komponenten des ELI URI für die Schweiz:

<figure class="table" id="table-eli-komponenten">
<table class="data">
  <thead>
    <tr>
      <th>Komponente</th>
      <th>Beschreibung</th>
      <th>Beispielwert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>jurisdiction</code></td>
      <td>Zuständiger Staat oder Kanton</td>
      <td><code>ch</code>, <code>ch-zh</code>, <code>ch-ge</code></td>
    </tr>
    <tr>
      <td><code>type</code></td>
      <td>Typ des Rechtsdokuments</td>
      <td><code>cc</code> (konsolidiert), <code>oc</code> (Amtsblatt), <code>fga</code>, <code>dl</code></td>
    </tr>
    <tr>
      <td><code>year</code></td>
      <td>Erlassjahr</td>
      <td><code>1999</code>, <code>2024</code></td>
    </tr>
    <tr>
      <td><code>natural_id</code></td>
      <td>Natürliche Identifikationsnummer</td>
      <td><code>404</code>, <code>123</code></td>
    </tr>
    <tr>
      <td><code>language</code></td>
      <td>Sprachcode (ISO 639-1)</td>
      <td><code>de</code>, <code>fr</code>, <code>it</code>, <code>rm</code></td>
    </tr>
  </tbody>
</table>
<figcaption>ELI URI Referenz-Komponenten für die Schweiz</figcaption>
</figure>
