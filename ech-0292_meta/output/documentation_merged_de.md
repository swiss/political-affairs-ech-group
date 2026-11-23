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

## Common Data Elements

Elements that are needed in multiple standards of the eCH Specialist Group Political Affairs are defined once in a common schema and imported into the individual standards. This avoids duplication and ensures consistency across the different standards. These elements are called **Common Data Elements** (CDEs) and are defined in the subgroup **eCH-0292: Metaprozesse zu politischen Geschäften**. The CDEs are not part of the eCH-0292 standard itself, but are documented there.

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

# Datenpublikation

Dieses Kapitel enthält **Empfehlungen** für die Publikation von Daten nach den Standards der Fachgruppe Politische Geschäfte. Es ist nicht normativ: Ratsinformationssysteme, Budgets und rechtliche Grundlagen unterscheiden sich zwischen Bund, Kantonen und Gemeinden zu stark, als dass eine einheitliche Pflicht sinnvoll wäre. Die Empfehlungen richten sich in erster Linie an

* **Parlamentsdienste und Ratssekretariate**, welche die Daten als Erste publizieren, und
* **Herstellerinnen und Hersteller von Ratsinformationssystemen**, welche Exporte und Schnittstellen in ihre Produkte einbauen.

Die Empfehlungen sind mit `DP-nn` nummeriert, damit in Ausschreibungen, Pflichtenheften oder Konformitätserklärungen auf einzelne Punkte verwiesen werden kann. Sie übernehmen, wo möglich, bewährte Regeln bestehender Standards, namentlich eCH-0200 (DCAT-AP CH), eCH-0205 (Linked Open Data), der deutschen Spezifikation OParl für Ratsinformationssysteme und der W3C *Data on the Web Best Practices* (DWBP).

## Struktur und Begriffe des Schemas

Das Datenformat ist zweitrangig. Entscheidend ist, dass die publizierten Daten die **Begriffe und die Struktur des LinkML-Schemas** übernehmen. Das LinkML-Schema ist das Ausgangsformat; JSON, XML und RDF sind daraus abgeleitete, gleichwertige Serialisierungen.

* **DP-01 Schema-Begriffe verwenden:** Klassen, Slots und Enumerationswerte sollen mit den Namen des Schemas publiziert werden, nicht mit systeminternen Feldnamen oder Übersetzungen. Nur so können Nutzerinnen und Nutzer Daten verschiedener Räte ohne individuelle Zuordnung zusammenführen.
* **DP-02 JSON oder XML, gleichwertig:** Publiziert werden soll mindestens eine der vom Schema abgeleiteten Serialisierungen (JSON gemäss generiertem JSON Schema oder XML gemäss generiertem XSD). RDF kann zusätzlich angeboten werden. CSV eignet sich als ergänzende, vereinfachte Sicht, ersetzt die strukturierte Publikation aber nicht.
* **DP-03 Gegen das Schema validieren:** Publizierte Daten sollen vor der Freigabe automatisiert gegen das generierte JSON Schema bzw. XSD geprüft werden. Die verwendete Version des Standards soll in den Daten oder Metadaten angegeben sein.
* **DP-04 Technische Konventionen:** Zeichenkodierung UTF-8 ohne BOM; Datumswerte nach ISO 8601 (`JJJJ-MM-TT`), Zeitstempel immer mit Zeitzone (UTC oder Offset); Werte sprachneutral (Dezimalpunkt, keine formatierten Zahlen). Leere optionale Felder sollen weggelassen statt mit Platzhaltern gefüllt werden.
* **DP-05 Umwandlung über eine Pipeline ist zulässig:** Kann ein Ratsinformationssystem die Struktur nicht nativ ausgeben, ist eine nachgelagerte Umwandlung (Pipeline) gleichwertig. Die Zuordnung der Quellfelder zum Schema soll dokumentiert und die Pipeline nach Möglichkeit offen zugänglich sein, damit Dritte Abweichungen nachvollziehen können.

## Identifikatoren und URIs

Gemäss den Designprinzipien trägt jede Entität eine lokale Id (`local_id`) und eine globale URI (`global_uri`). Für die Publikation heisst das:

* **DP-06 Bestehende Identifikatoren übernehmen:** Wo die Quelle bereits fachliche Identifikatoren führt (Geschäftsnummer, Personennummer, Sitzungsnummer), sollen diese als `local_id` und als Teil der URI weiterverwendet werden. Neu erzeugte UUIDs sollen nur verwendet werden, wenn kein stabiler fachlicher Identifikator existiert. Ein einmal vergebener Identifikator darf nicht für eine andere Entität wiederverwendet werden.
* **DP-07 Stabile URIs ohne Implementierungsdetails:** URIs sollen nur Bestandteile enthalten, die sich nie ändern („Cool URIs don't change"). Sie sollen keine Produktnamen, Dateiendungen von Skripten (`.php`, `.aspx`), Datenbankschlüssel, Sitzungs-Ids oder Verwaltungseinheiten enthalten, die bei einer Reorganisation wegfallen. Massgebend ist die Körperschaft (z. B. Kanton, Gemeinde, Rat), nicht das Departement oder die Herstellerin bzw. der Hersteller. Ein Systemwechsel darf die URIs nicht verändern; dafür eignet sich ein eigener, vom Produkt unabhängiger Hostname.
* **DP-08 Eine kanonische URI je Entität:** Jede Entität soll genau eine kanonische URI haben. Andere Schreibweisen (Gross-/Kleinschreibung, Schrägstrich am Ende, führende Nullen) sollen mit HTTP 301 auf die kanonische URI umleiten. Die URI soll sprachunabhängig sein; die Sprache wird über Content Negotiation oder separate Darstellungen (`MultilingualUri`) gewählt.
* **DP-09 URIs bleiben auflösbar:** Eine URI soll auch nach Löschung, Archivierung oder Systemwechsel auflösbar bleiben – entweder zur Ressource selbst, per Umleitung oder zu einer Information, was mit der Ressource geschehen ist (HTTP 410 *Gone* für gelöschte Entitäten).
* **DP-10 Persistente Identifikatoren für Dokumente:** Für Erlasse soll ELI verwendet werden (siehe eCH-0296). Für Dokumente und Datenstände, die langfristig zitierbar sein müssen, kann zusätzlich ein persistenter Identifikator wie DOI oder ARK vergeben werden. Er ergänzt die `global_uri`, ersetzt sie aber nicht.
* **DP-11 Verknüpfung mit Wikidata:** Wo bekannt, soll `wikidata_uri` mitgeliefert werden. Sie erleichtert die Verknüpfung derselben Person oder Körperschaft über föderale Ebenen hinweg.

## Zugang

* **DP-12 Gesamtbezug und Schnittstelle:** Daten sollen sowohl als Gesamtbezug (Bulk Download, ein komprimiertes Paket je Datensatz unter einer stabilen URL) als auch über eine Schnittstelle (API) für Einzelabfragen angeboten werden. Wer nur eines anbieten kann, soll den Gesamtbezug priorisieren, weil er ohne Programmieraufwand nutzbar ist und Lastspitzen vermeidet.
* **DP-13 Direkt oder über eine Datenplattform:** Die Schnittstelle kann direkt vom Ratsinformationssystem oder indirekt über eine Datenplattform (z. B. kantonales OGD-Portal) bereitgestellt werden. Bei indirekter Bereitstellung sollen die URIs dennoch auf die Körperschaft lauten (DP-07), damit ein späterer Wechsel des Bereitstellungswegs die Identifikatoren nicht verändert.
* **DP-14 Anonymer, offener Zugang:** Öffentliche Daten sollen ohne Registrierung und ohne API-Schlüssel abrufbar sein. Ein Schlüssel kann für erhöhte Kontingente angeboten werden, soll aber keine Voraussetzung für den Zugang sein. Die Schnittstelle soll ausschliesslich lesend, zustandslos und über HTTPS erreichbar sein und CORS (`Access-Control-Allow-Origin: *`) erlauben, damit Webanwendungen Dritter sie direkt nutzen können.
* **DP-15 Lastbegrenzung transparent machen:** Ist eine Lastbegrenzung (Throttling) nötig, sollen die Limiten dokumentiert und Überschreitungen mit HTTP 429 und `Retry-After` beantwortet werden. Datenendpunkte sollen nicht per `robots.txt` von Suchmaschinen und Crawlern ausgeschlossen werden; diese gehören ausdrücklich zum vorgesehenen Nutzerkreis.
* **DP-16 Schnittstelle dokumentieren und stabil halten:** Die Schnittstelle soll maschinenlesbar dokumentiert sein (z. B. OpenAPI). Listen sollen stabil sortiert und seitenweise mit Link auf die nächste Seite ausgeliefert werden. Konditionale Abfragen (`ETag`, `Last-Modified`, `If-Modified-Since`) und Komprimierung sollen unterstützt werden. Inkompatible Änderungen sollen nur mit neuer Version, Ankündigung und festem Abschaltdatum der alten Version erfolgen.
* **DP-17 Verständliche Fehler:** Fehler sollen mit dem passenden HTTP-Statuscode und einer kurzen, maschinenlesbaren Fehlermeldung beantwortet werden; nicht verfügbare Daten sollen als solche erkennbar sein (z. B. HTTP 503 bei Wartung statt einer leeren Liste).

## Aktualisierung, Korrekturen und Löschungen

Politische Daten ändern sich laufend, und Nutzerinnen und Nutzer müssen ihre Kopien nachführen können, ohne jeweils den gesamten Bestand neu zu laden.

* **DP-18 Änderungszeitpunkt pflegen:** Bei jeder Änderung einer Entität soll `datetime_modified` (bzw. `date_modified`) nachgeführt werden (Mixin `HasCreationModificationDates`). Dieser Wert ist die Grundlage für jede inkrementelle Synchronisation und darf nicht ausbleiben.
* **DP-19 Abfrage nach Änderungen:** Die Schnittstelle soll Filter auf Erstellungs- und Änderungszeitpunkt anbieten (z. B. `modified_since`), damit nur Änderungen seit dem letzten Abruf geholt werden müssen.
* **DP-20 Löschungen sichtbar machen:** Entitäten sollen nicht einfach verschwinden. Eine gelöschte oder zurückgezogene Entität soll als solche markiert weiter ausgeliefert werden (Identifikator, Typ und Löschzeitpunkt), zumindest in Abfragen nach Änderungen. Ihre URI antwortet mit HTTP 410 (DP-09). Nur so erfahren Nutzerinnen und Nutzer, dass sie den Datensatz in ihrer Kopie entfernen müssen.
* **DP-21 Korrektur und Veränderung unterscheiden:** Eine **Korrektur** (Tippfehler, falsch erfasstes Datum) überschreibt den bisherigen Wert und aktualisiert den Änderungszeitpunkt. Eine **Veränderung in der Wirklichkeit** (Parteiwechsel, Umbenennung einer Kommission) wird dagegen nicht überschrieben, sondern über zeitliche Gültigkeiten (`valid_from`/`valid_through`) abgebildet, wie in den Designprinzipien beschrieben. Damit bleibt der historische Zustand erhalten, ohne dass eine allgemeine Versionierung nötig ist.
* **DP-22 Aktualisierungsrhythmus angeben:** Die Periodizität der Aktualisierung (z. B. täglich, nach jeder Sitzung, laufend) soll in den Metadaten angegeben werden und der Realität entsprechen. Gesamtbezüge sollen mit Stichtag versehen werden.
* **DP-23 Datenströme (Ausblick):** Für Anwendungen, die zeitnah reagieren müssen (z. B. Abstimmungsresultate während der Sitzung), können Änderungen zusätzlich als Feed oder Strom angeboten werden (z. B. Atom mit Tombstones nach RFC 6721, WebSub oder Server-Sent Events). Die Abfrage nach Änderungen (DP-19) bleibt die Mindestvariante.

## Metadaten und Auffindbarkeit

* **DP-24 Katalogisierung nach DCAT-AP CH:** Jeder Datensatz soll mit Metadaten nach eCH-0200 (DCAT-AP CH) beschrieben und in einem Katalog verzeichnet werden (opendata.swiss und/oder I14Y). Pflichtangaben sind dort u. a. Titel, Beschreibung, Identifikator, publizierende Stelle, Kontakt und Lizenz.
* **DP-25 Publizierende Stelle eindeutig ausweisen:** Die Metadaten sollen festhalten,
  * wer die Daten publiziert, mit einer stabilen Kontaktadresse, die laufend bearbeitet wird;
  * ob es sich um die **erstpublizierende Stelle** oder um eine **aggregierende Stelle** handelt, die Daten Dritter sammelt und weitergibt (mit Verweis auf die Quelle);
  * welche Staatsebene (Bund, Kanton, Gemeinde) und welche Gewalt (Legislative, Exekutive) die Daten betreffen;
  * ab welchem Zeitpunkt die Daten vollständig vorliegen (ältere Bestände sind oft lückenhaft).
* **DP-26 Herkunft des Systems angeben:** Die Schnittstelle soll angeben, mit welchem Produkt (Herstellerin bzw. Hersteller, Produkt, Version) und nach welcher Version des Standards die Daten erzeugt wurden. Das erleichtert die Fehlersuche bei systematischen Abweichungen.
* **DP-27 Einheitliche Schlagwörter:** Für die Kataloge sollen die Schlagwörter aus Sicht der Nutzerinnen und Nutzer gewählt und zwischen den Räten einheitlich verwendet werden (mindestens die Bezeichnung des Rats, „Parlament", die Nummer des eCH-Standards und der Datentyp, z. B. „Abstimmungen"). Wo möglich, sollen Themen und Körperschaften mit Wikidata verknüpft werden.
* **DP-28 Menschenlesbare Darstellung verlinken:** Zu jeder Entität soll, wo vorhanden, die Webseite der Entität im Ratsinformationssystem verlinkt sein, damit Nutzerinnen und Nutzer die Daten mit der offiziellen Darstellung abgleichen können.

## Lizenz

* **DP-29 Offene Lizenz:** Daten sollen unter einer offenen Lizenz publiziert werden, welche die Weiterverwendung einschliesslich kommerzieller Nutzung erlaubt. Empfohlen sind CC0 oder CC BY 4.0 bzw. die entsprechenden Nutzungsbedingungen von opendata.swiss (`terms_open`, `terms_by`). eCH-0205 empfiehlt CC0, weil sie die Verknüpfung mit anderen Daten (z. B. Wikidata) am wenigsten einschränkt. Für die Bundesverwaltung gilt zusätzlich Art. 10 EMBAG.
* **DP-30 Lizenz einmal angeben, Abweichungen ausweisen:** Die Lizenz soll maschinenlesbar (als URI aus dem Vokabular von eCH-0200) auf Ebene des Datensatzes angegeben werden und gilt dann für alle enthaltenen Entitäten. Abweichende Lizenzen einzelner Dokumente (z. B. Fotos, Gutachten Dritter) sollen am Dokument selbst angegeben werden. Ändert die Lizenz, soll der Zeitpunkt der Änderung festgehalten werden.

## Pakete und Benennung

* **DP-31 Gesamtbezug als Paket:** Ein Gesamtbezug soll als ZIP-Paket mit einer Beschreibungsdatei (Manifest) ausgeliefert werden, die mindestens die Version des Standards, den Stichtag, die enthaltenen Dateien mit Prüfsummen und die Lizenz nennt. Als Vorlage kann das Frictionless *Data Package* (`datapackage.json`) dienen.
* **DP-32 Dateinamen:** Datei- und Ordnernamen sollen nur Kleinbuchstaben, Ziffern sowie `-`, `_` und `.` enthalten, keine Leerzeichen und Umlaute, und ein Datum im Format `JJJJ-MM-TT` tragen, z. B. `kr-zh_votings_2026-11-23.json.zip`. Der Name eines Datensatzes soll über Aktualisierungen hinweg gleich bleiben; der jeweils aktuelle Stand soll zusätzlich unter einer gleichbleibenden URL (`…/latest`) erreichbar sein.

## Authentizität

* **DP-33 Prüfsummen:** Zu jeder Datei, insbesondere zu Dokumenten und Gesamtbezügen, soll eine Prüfsumme (SHA-256 oder stärker) publiziert werden. MD5 und SHA-1 sollen nicht mehr verwendet werden.
* **DP-34 Signierte Dokumente:** Wo Dokumente rechtlich massgebend sind (z. B. amtliche Publikationen), soll die signierte Fassung als Manifestation verfügbar sein und als massgebend gekennzeichnet werden, wie dies die Fedlex für die amtlichen Sammlungen tut.
* **DP-35 Signierte Daten (Ausblick):** Eine Signierung strukturierter Daten (z. B. signierte Gesamtbezüge oder signierte Manifeste) ist sinnvoll, sobald Daten Dritter weitergereicht werden und ihre Herkunft geprüft werden muss. Die Fachgruppe legt dafür noch kein Verfahren fest.

## Archivierung

* **DP-36 Übergang ins Archiv planen:** Daten und Dokumente, die nicht mehr aktiv gepflegt werden, sollen nach eCH-0160 an das zuständige Archiv abgeliefert werden. Die Ablieferung soll die URIs und Identifikatoren mitführen, damit die Verknüpfungen im Archiv erhalten bleiben.
* **DP-37 Nach der Archivierung weiterleiten:** Die URIs archivierter Entitäten sollen weiterhin auflösbar sein und auf das Archiv bzw. eine Information zum Zugang verweisen (DP-09). Wird ein publiziertes Vokabular oder Schema ersetzt, soll die alte Version abrufbar bleiben, solange Daten darauf verweisen.

## Offene Punkte

Folgende Fragen sind in der Fachgruppe noch zu klären:

* Ein kontrolliertes Vokabular für die Rolle der publizierenden Stelle (erstpublizierend/aggregierend, Staatsebene, Gewalt) existiert in eCH-0200 noch nicht. Zu prüfen ist, ob die Fachgruppe ein eigenes Vokabular definiert oder auf eCH-0200 wartet.
* Das Schema kennt derzeit kein eigenes Merkmal für gelöschte bzw. zurückgezogene Entitäten (DP-20). Zu prüfen ist ein gemeinsames Element in den Common Data Elements.
* Die Angaben zur Kompetenz (Zuständigkeit) einer Körperschaft sind noch nicht modelliert.
* Verfahren zur Signierung strukturierter Daten (DP-35).

## Referenzen

* eCH-0200 DCAT-Anwendungsprofil für Datenportale in der Schweiz (DCAT-AP CH), V3.0.1: <https://www.ech.ch/de/ech/ech-0200/3.0.1>
* eCH-0205 Linked Open Data, V1.0: <https://www.ech.ch/de/ech/ech-0205/1.0>
* eCH-0160 Archivische Ablieferungsschnittstelle, V1.3.0: <https://www.ech.ch/de/ech/ech-0160/1.3.0>
* OParl 1.1, Spezifikation: <https://oparl.org/spezifikation/online-ansicht/>
* W3C, Data on the Web Best Practices: <https://www.w3.org/TR/dwbp/>
* W3C, Cool URIs don't change: <https://www.w3.org/Provider/Style/URI>
* GO FAIR, FAIR Principles: <https://www.go-fair.org/fair-principles/>
* Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG), Art. 10: <https://www.fedlex.admin.ch/eli/cc/2023/682/de>
* Frictionless Data Package: <https://datapackage.org/standard/data-package/>
* LINDAS, Namespace-Governance: <https://schema.ld.admin.ch/governance/namespaces>

\newpage

# Richtext-Definition

In einigen Anwendungsfällen im Rahmen der politischen Geschäfte werden Texte strukturiert übermittelt. In diesem Fall enthalten die Texte verschiedene Formatierungselemente, welche repräsentiert werden sollen. Im Grundsatz werden Formatierungen mit HTML-Elementen ausgedrückt. Es sollen aber nicht alle Möglichkeiten von HTML erlaubt werden, sondern nur solche, welche grundsätzliche Formatierungen erlauben. Schriftart, -grösse und -farbe sind grundsätzlich nicht erlaubt, um Inkompatibilitäten zu vermeiden.

Dieses Kapitel zeigt auf, welche Elemente von HTML in diesen sogenannten "Richtext"-Feldern erlaubt sind.

## Erlaubte Codepages
Im Grundsatz ist in allen Standards dieser eCH-Gruppe nur Unicode erlaubt.

## Auflistung der erlaubten und nicht erlaubten Elemente


| Zweck        | Element                                         | HTML                                                              | Bemerkung                                                                                                                            |
| ------------ | ----------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Gliederung   | Paragraph                                       | `<p>`                                                            | CSS-Styles, Klassen und Inline-Definitionen sind nicht erlaubt.                                                                      |
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
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: HasIdentification |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: HasIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: HasIdentification |
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
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: HasIdentification |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: HasIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: HasIdentification |
| expression_language | 1 <br/> String | Sprachcode im ISO 639-1-Format.  |
| expression_title | 1 <br/> String | Titel der Sprachfassung.  |
| expression_description | 0..1 <br/> String | Beschreibender Text zur Sprachfassung.  |
| manifestations | * <br/> [Manifestation](#Manifestation) | Die Dateiformen (Manifestations) einer Expression.  |
| date_created | 0..1 <br/> Date | Datum der Erstpublikation der Sprachfassung. <br/><br/>Vererbung: HasCreationModificationDates |
| datetime_created | 0..1 <br/> Datetime | Datum und Uhrzeit der Erstpublikation der Sprachfassung. <br/><br/>Vererbung: HasCreationModificationDates |
| date_modified | 0..1 <br/> Date | Datum der letzten Revision der Sprachfassung. <br/><br/>Vererbung: HasCreationModificationDates |
| datetime_modified | 0..1 <br/> Datetime | Datum und Uhrzeit der letzten Revision der Sprachfassung. <br/><br/>Vererbung: HasCreationModificationDates |





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
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: HasIdentification |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: HasIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: HasIdentification |
| format | 0..1 <br/> String | Das Dateiformat der Manifestation (z.B. pdf, html).  |
| manifestation_url | 0..1 <br/> Uri | URL, unter der die Dateiform abgerufen werden kann.  |
| date_created | 0..1 <br/> Date | Datum der Erstpublikation der Dateiform. <br/><br/>Vererbung: HasCreationModificationDates |
| datetime_created | 0..1 <br/> Datetime | Datum und Uhrzeit der Erstpublikation der Dateiform. <br/><br/>Vererbung: HasCreationModificationDates |
| date_modified | 0..1 <br/> Date | Datum der letzten Revision der Dateiform. <br/><br/>Vererbung: HasCreationModificationDates |
| datetime_modified | 0..1 <br/> Datetime | Datum und Uhrzeit der letzten Revision der Dateiform. <br/><br/>Vererbung: HasCreationModificationDates |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Expression](#Expression) | manifestations | range | [Manifestation](#Manifestation) |



















</div>

