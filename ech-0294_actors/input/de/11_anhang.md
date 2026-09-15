\newpage

# Anhang A – Referenzen & Bibliographie

Wo eine Version genannt ist, ist es diejenige, gegen die dieser Standard erarbeitet wurde.

## Standards der Fachgruppe „Politische Geschäfte"

Die Standards der Fachgruppe entstehen gemeinsam und verweisen aufeinander. Sie stehen zurzeit alle im Status „In Arbeit" (Stand: 10. August 2026); eine Version ist deshalb nicht angegeben.

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0292|eCH-0292: Metaprozesse zu politischen Geschäften – gemeinsame Datenelemente: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0293|eCH-0293: Öffentlicher Ratsbetrieb: [https://www.ech.ch/de/ech/ech-0293](https://www.ech.ch/de/ech/ech-0293)|
|eCH-0295|eCH-0295: Parlamentarische Geschäfte: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0296|eCH-0296: Erlasse und Gesetzestexte: [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|eCH-0297|eCH-0297: Öffentliche Konsultationen: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Weitere eCH-Standards

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0011|eCH-0011: Datenstandard Personendaten, Version 9.0.0 (Genehmigt, 27.07.2023). Grundlage der Namenstypen in `NameTypeEnum` (`personNameData`): [https://www.ech.ch/de/ech/ech-0011/9.0.0](https://www.ech.ch/de/ech/ech-0011/9.0.0)|
|eCH-0108|eCH-0108: Datenstandard: Unternehmensstammdaten und Unternehmensregister, Version 6.0.0 (Genehmigt, 04.04.2024). Definiert das Austauschformat der UID (`organization_uid`) und ist der Standard, zu dem die Rechtsform-Codeliste in `LegalFormEnum` konform ist: [https://www.ech.ch/de/ech/ech-0108/6.0.0](https://www.ech.ch/de/ech/ech-0108/6.0.0)|

## Codelisten und weitere Quellen

| | |
|------------------|----------------------------------------------------------------------------------|
|I14Y|Interoperabilitätsplattform des Bundesamts für Statistik. Bezugsquelle der Codelisten für Rechtsform (`LegalFormEnum`) und Geschlecht (`GenderCodeEnum`): [https://www.i14y.admin.ch](https://www.i14y.admin.ch)|
|LINDAS|Linked Data Service der Schweizerischen Bundesverwaltung. Identifikatoren der Schweizer Raumeinheiten (Land, Kanton, Bezirk, Gemeinde) für `spatial` und `ElectoralDistrict`: [https://ld.admin.ch](https://ld.admin.ch)|
|NOGA|Allgemeine Systematik der Wirtschaftszweige des Bundesamts für Statistik. Ermöglicht Auswertungen über die UID referenzierter Organisationen.|
|Wikidata|Freie Wissensdatenbank. Entitäts-IRI (`http://www.wikidata.org/entity/Q…`) in `wikidata_uri`: [https://www.wikidata.org](https://www.wikidata.org)|
|ISO 639-1|ISO (International Organization for Standardization). Sprachcodes, verwendet im Slot `language` von `MultilingualValue`.|
|schema.org|Gemeinsames Vokabular für strukturierte Daten. Quelle mehrerer `slot_uri`-Zuordnungen: [https://schema.org](https://schema.org)|
|LinkML|Modellierungssprache, in der dieser Standard definiert ist: [https://linkml.io](https://linkml.io)|

\newpage

# Anhang B – Mitarbeit & Überprüfung

Fachgruppe Politische Geschäfte, Subgruppe Politische Akteure:

| | |
|---|---|
|Julie Silberstein|Bundesamt für Statistik|
|Laurence Brandenberger|Universität Zürich, IPZ|
|Daniela Koller|Kanton Thurgau|
|Thomas Roth||
|Stefan Oderbolz|EBP|
|Fabian Davolio|Parlamentsdienste|
|Orhan Saeedi|Kanton Basel-Stadt|
|Christian Gutknecht|Glue AG|
|Michael Luggen|Bundeskanzlei|

<!-- TODO Fachgruppe: Organisationen ergänzen bzw. korrigieren; Versionsverlauf
     unten mit den effektiven Entwurfsständen und Review-Runden vervollständigen. -->

| Version | Datum | Ersteller | Bemerkung |
|---|---|---|---|
| 1.0.0 | 2026-08-10 | Fachgruppe Politische Geschäfte | Einreichung als Vorschlag |

# Anhang C – Abkürzungen und Glossar

| | |
|---|---|
|DSG|Bundesgesetz über den Datenschutz, in Kraft seit 1. September 2023.|
|I14Y|Interoperabilitätsplattform des Bundesamts für Statistik; Bezugsquelle mehrerer Codelisten.|
|IRI|Internationalized Resource Identifier. Erweiterung der URI auf den vollen Unicode-Zeichenvorrat.|
|JSON-LD|JSON for Linking Data. Serialisierung von verknüpften Daten in JSON.|
|LINDAS|Linked Data Service der Schweizerischen Bundesverwaltung.|
|LinkML|Linked Data Modeling Language. Modellierungssprache, in der dieser Standard definiert ist.|
|NOGA|Allgemeine Systematik der Wirtschaftszweige des Bundesamts für Statistik.|
|RDF|Resource Description Framework. Datenmodell für verknüpfte Daten; hier als Turtle (.ttl) ausgeliefert.|
|UID|Unternehmens-Identifikationsnummer. Eindeutiger Schlüssel eines Schweizer Unternehmens gemäss Bundesamt für Statistik.|
|URI|Uniform Resource Identifier. Eindeutiger Bezeichner einer Ressource.|
|XSD|XML Schema Definition. Empfehlung des W3C zum Definieren von Strukturen für XML-Dokumente.|

# Anhang D – Änderungen gegenüber Vorversion

Dies ist die erste Version.

\newpage

# Anhang E – Abbildungsverzeichnis

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \h \z \c "Abbildung" </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Rechtsklick &gt; „Felder aktualisieren“, um das Abbildungsverzeichnis zu erzeugen.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

# Anhang F – Tabellenverzeichnis

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \h \z \c "Tabelle" </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Rechtsklick &gt; „Felder aktualisieren“, um das Tabellenverzeichnis zu erzeugen.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```
