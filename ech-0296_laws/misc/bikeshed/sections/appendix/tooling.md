Dieser Anhang enthält Hilfsmittel, die die Arbeit mit diesem Standard unterstützen. Sie sind informativer Natur und haben keinen normativen Charakter.

## ReSpec / Bikeshed Konfiguration für eCH Standards ## {#bikeshed-konfiguration}

ReSpec und Bikeshed sind Werkzeuge zur Erstellung von technischen Spezifikationen. Die untenstehenden Tabellen dokumentieren alle Dokumentabschnitte und Beilagen — ihre IDs, Klassen und Quellen.

### Boilerplate-Abschnitte ### {#boilerplate-abschnitte}

eCH-0003 ("Prozessstandard eCH-Dokumente", v11.1.0) definiert die Pflichtstruktur aller eCH-Standards.

<figure class="table" id="tbl-boilerplate">
<table class="simple">
  <thead>
    <tr>
      <th rowspan="2">Abschnitt</th>
      <th rowspan="2">id / class</th>
      <th colspan="2">Quelle</th>
    </tr>
    <tr>
      <th>Bikeshed</th>
      <th>eCH</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Zusammenfassung</strong><br>Abstract</td><td><code>id="abstract"</code></td><td>✓</td><td>✓</td></tr>
    <tr><td><strong>Stand dieses Dokuments</strong><br>Status of This Document</td><td><code>id="sotd"</code></td><td>✓</td><td>✓</td></tr>
    <tr><td><strong>Inhaltsverzeichnis</strong><br>Table of Contents</td><td><code>id="toc"</code></td><td>✓</td><td>✓</td></tr>
    <tr><td><strong>Konformität</strong><br>Conformance</td><td><code>id="conformance"</code></td><td>✓</td><td>✓</td></tr>
    <tr><td><strong>Einleitung</strong><br>Introduction</td><td><code>id="intro"</code></td><td>✗</td><td>✓</td></tr>
    <tr><td><strong>Sicherheitsüberlegungen</strong><br>Security Considerations</td><td><code>id="security"</code></td><td>✗</td><td>✓</td></tr>
    <tr><td><strong>Haftungsausschluss</strong><br>Disclaimer</td><td><code>id="disclaimer"</code></td><td>✗</td><td>✓</td></tr>
    <tr><td><strong>Urheberrechte</strong><br>Copyright</td><td><code>id="copyright"</code></td><td>✗</td><td>✓</td></tr>
    <tr><td><strong>Mitarbeit und Überprüfung</strong><br>Contributors</td><td><code>id="contributors"</code></td><td>✗</td><td>✓</td></tr>
    <tr><td><strong>Index</strong><br>Index of Terms</td><td><code>id="index"</code></td><td>✓</td><td>✓</td></tr>
    <tr><td><strong>Tabellenverzeichnis</strong><br>Table of Tables</td><td><code>id="tot"</code></td><td>✗</td><td>✓</td></tr>
    <tr><td><strong>Änderungen gegenüber Vorversion</strong><br>Changelog</td><td><code>id="changelog"</code></td><td>✗</td><td>✓</td></tr>
    <tr><td><strong>Beilagen</strong><br>Appendices</td><td><code>id="appendices"</code></td><td>—</td><td>—</td></tr>
    <tr><td><strong>Referenzen</strong><br>References</td><td><code>id="references"</code></td><td>✓</td><td>✓</td></tr>
  </tbody>
</table>
<figcaption>Alle Dokumentabschnitte und Beilagen (eCH-0003 Reihenfolge)</figcaption>
</figure>

<figure class="table" id="tbl-metadata">
<table class="simple">
  <thead>
    <tr>
      <th>Schlüssel</th>
      <th>Typ</th>
      <th>Verwendung</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>Title</code></td><td>string</td><td>Dokumenttitel.</td></tr>
    <tr><td><code>Shortname</code></td><td>string</td><td>Kurzbezeichnung für URLs und Querverweise (z.B. <code>akn4ch</code>).</td></tr>
    <tr><td><code>Status</code></td><td>string</td><td><code>UD</code> rendert das Dokument als "Unofficial Proposal Draft".</td></tr>
    <tr><td><code>Editor</code></td><td>string</td><td>Redakteur: Name, Organisation URL, persönliche URL.</td></tr>
    <tr><td><code>Date</code></td><td>string</td><td>Offizielle Publikationsversion (ISO 8601).</td></tr>
    <tr><td><code>Abstract</code></td><td>string</td><td>Kurzbeschreibung des Standards.</td></tr>
    <tr><td><code>Max ToC Depth</code></td><td>number</td><td>Maximale Gliederungstiefe im Inhaltsverzeichnis.</td></tr>
    <tr><td><code>Local Boilerplate</code></td><td>boolean set</td><td>Lokale Überschreibung von Boilerplate-Dateien (z.B. <code>abstract yes, logo yes</code>).</td></tr>
    <tr><td><code>Boilerplate</code></td><td>boolean set</td><td>Deaktivierung von Boilerplate-Abschnitten (z.B. <code>conformance off</code>).</td></tr>
  </tbody>
</table>
<figcaption>Bikeshed Metadaten-Schlüssel für dieses Template</figcaption>
</figure>

### Abschnittstruktur ### {#abschnittstruktur}

In Bikeshed mit Markdown-Modus beginnen Abschnittsüberschriften mit `#` (erzeugt `h2`) für oberste Ebene, `##` für `h3` usw. Explizite HTML-Abschnitte mit `<h2>` sind direkte Top-Level-Abschnitte.

Die Nummerierung beginnt nach Zusammenfassung und Stand des Dokuments mit 1. Abschnitte mit `class=no-num` werden zwar im Inhaltsverzeichnis angezeigt, tragen aber keine Nummer.

### Notizen, Beispiele und Hinweise ### {#notizen-beispiele}

<div class="note">
Notizen erscheinen als graue Boxen mit der Klasse <code>div class=note</code>.
</div>

<div class="example" id="example-akn-minimal">
Beispiele erscheinen als nummerierte Boxen mit der Klasse <code>div class=example</code>.

<pre class=include-code>
path: examples/example-1.xml
highlight: xml
line-numbers:
</pre>
</div>

### Code und Listen ### {#code-und-listen}

Inline-Code verwendet `<code>`. Mehrzeiliger Code verwendet `<pre>`, optional mit Syntaxhervorhebung via `highlight:` (bei `<pre class=include-code>`) oder via CSS-Klasse (`xml`, `js`, `html`, `md`).

### Bilder ### {#bilder}

Bilder werden mit dem `<figure>`-Element eingebunden. Die Beschriftung wird mit `<figcaption>` definiert.

<figure id="fig-gesetzgebungsverfahren">
  <img src="images/legislative-procedure-documents.png" alt="Gesetzgebungsverfahren auf Bundesebene und die dabei entstehenden Dokumenttypen">
  <figcaption>Gesetzgebungsverfahren auf Bundesebene und die dabei entstehenden Dokumenttypen.</figcaption>
</figure>

### Externe Includes ### {#externe-includes}

Bikeshed verwendet `<pre class=include>` zum Einbinden von Markdown- und HTML-Dateien:

```
<pre class=include>
path: datei.md
</pre>
```

Für Code-Dateien steht `<pre class=include-code>` zur Verfügung:

```
<pre class=include-code>
path: datei.xml
highlight: xml
line-numbers:
</pre>
```

### Tabellen ### {#tabellen}

Markdown-Tabellen unterstützen kein `colspan`, `rowspan`, `caption` oder benutzerdefinierte Klassen. HTML-Tabellen können direkt in `.md`-Dateien als rohe HTML-Blöcke eingebettet werden (mit Leerzeile davor und danach). Für nummerierte Tabellen wird `<figure class=table>` mit `<figcaption>` (nach dem schliessenden `</table>`) verwendet. Bikeshed fügt die Beschriftung „Tabelle N – " automatisch ein.

### Referenzen ### {#referenzen-hilfsmittel}

Bibliographieeinträge werden als `<pre class=biblio>` JSON-Block in `bikeshed/index.bs` gepflegt. Zitation: `[[AKN]]` (informativ) oder `[[!AKN]]` (normativ). Normative Referenzen erscheinen unter "Normative References", informative unter "Non-Normative References".
