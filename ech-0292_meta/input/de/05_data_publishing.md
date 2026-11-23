\newpage

# Datenpublikation

Dieses Kapitel enthält **Empfehlungen** für die Publikation von Daten nach den Standards der Fachgruppe Politische Geschäfte. Es ist nicht normativ: Ratsinformationssysteme, Budgets und rechtliche Grundlagen unterscheiden sich zwischen Bund, Kantonen und Gemeinden zu stark, als dass eine einheitliche Pflicht sinnvoll wäre. Die Empfehlungen richten sich in erster Linie an

* **Parlamentsdienste und Ratssekretariate**, welche die Daten als Erste publizieren, und
* **Herstellerinnen und Hersteller von Ratsinformationssystemen**, welche Exporte und Schnittstellen in ihre Produkte einbauen.

Die Empfehlungen sind mit `DP-nn` nummeriert, damit in Ausschreibungen, Pflichtenheften oder Konformitätserklärungen auf einzelne Punkte verwiesen werden kann. Sie übernehmen, wo möglich, bewährte Regeln bestehender Standards, namentlich eCH-0200 (DCAT-AP CH), eCH-0205 (Linked Open Data), der deutschen Spezifikation OParl für Ratsinformationssysteme und der W3C *Data on the Web Best Practices* (DWBP). Zusammen sollen sie die Daten im Sinne der FAIR-Prinzipien auffindbar, zugänglich, interoperabel und wiederverwendbar machen.

Ob und in welchem Umfang Daten veröffentlicht werden, entscheidet die publizierende Stelle auf Basis der für sie geltenden Rechtsgrundlagen. Die Empfehlungen dieses Kapitels betreffen nur das *Wie* der Publikation. Für Personendaten gelten zusätzlich die Hinweise zum Datenschutz in eCH-0294.

## Wahl des Publikationsformates

Das Datenformat ist zweitrangig. Entscheidend ist, dass die publizierten Daten die **Begriffe und die Struktur des LinkML-Schemas** übernehmen. Das LinkML-Schema ist das Ausgangsformat; JSON, XML und RDF sind daraus abgeleitete, gleichwertige Serialisierungen.

* **DP-01 Schema-Begriffe verwenden:** Klassen, Slots und Enumerationswerte sollen mit den Namen des Schemas publiziert werden, nicht mit systeminternen Feldnamen oder Übersetzungen. Nur so können Nutzerinnen und Nutzer Daten verschiedener Räte ohne individuelle Zuordnung zusammenführen.
* **DP-02 JSON oder XML, gleichwertig:** Publiziert werden soll mindestens eine der vom Schema abgeleiteten Serialisierungen (JSON gemäss generiertem JSON Schema oder XML gemäss generiertem XSD). RDF kann zusätzlich angeboten werden. CSV eignet sich als ergänzende, vereinfachte Sicht, ersetzt die strukturierte Publikation aber nicht.
* **DP-03 Gegen das Schema validieren:** Publizierte Daten sollen vor der Freigabe automatisiert gegen das generierte JSON Schema bzw. XSD geprüft werden. Die verwendete Version des Standards soll in den Daten oder Metadaten angegeben sein.
* **DP-04 Technische Konventionen:** Zeichenkodierung UTF-8 ohne BOM; Datumswerte nach ISO 8601 (`JJJJ-MM-TT`), Zeitstempel immer mit Zeitzone (UTC oder Offset); Werte sprachneutral (Dezimalpunkt, keine formatierten Zahlen). Leere optionale Felder sollen weggelassen statt mit Platzhaltern gefüllt werden.

## Identifikatoren und URIs

Gemäss den Designprinzipien trägt jede Entität eine lokale Id (`local_id`) und eine globale URI (`global_uri`). Es ist von Vorteil wenn die URIs semantisch Hilfestellung geben um welches Datenobjekt es sich handelt. Dies hilft bei der Arbeit mit den Daten. Darüberhinaus sind UUIDs nicht ideal um von Menschen zu Überprüfen ob die richtigen Daten herangezogen werden.

Für die Publikation heisst das:

* **DP-06 Systemunabhängige Identifikatoren:** Identifikatoren, die in URIs verwendet werden, sollen persistent und vom aktuell eingesetzten System unabhängig sein. Geeignet sind fachliche Identifikatoren (z. B. Geschäftsnummer), sofern diese nachweislich stabil sind und einen Systemwechsel überdauern. Interne Datenbankschlüssel des Ratsinformationssystems eignen sich nicht. Fachliche Nummern, die nicht Teil der URI sind, sollen trotzdem als eigene Angabe mitgeliefert werden, weil Nutzerinnen und Nutzer danach suchen. Ein einmal vergebener Identifikator darf nicht für eine andere Entität wiederverwendet werden.
* **DP-07 Stabile URIs ohne Implementierungsdetails:** URIs sollen nur Bestandteile enthalten, die sich nie ändern („Cool URIs don't change"). Sie sollen keine Produktnamen, Dateiendungen von Skripten (`.php`, `.aspx`), Sitzungs-Ids oder Verwaltungseinheiten enthalten, die bei einer Reorganisation wegfallen. Massgebend ist die Körperschaft (z. B. Kanton, Gemeinde, Rat), nicht das Departement oder die Herstellerin bzw. der Hersteller. Daten werden nicht unter `ld.ech.ch` publiziert (dort liegen nur Schema und Vokabulare), sondern unter einer Domain der publizierenden Stelle, idealerweise einer bestehenden Linked-Data-Domain wie `ld.zh.ch`, `ld.bs.ch` oder `ld.stadt-zuerich.ch`. Ein Systemwechsel darf die URIs nicht verändern. Das URI-Konzept der Fachgruppe (`docs/common/naming.md`) schlägt Muster vor, z. B. `https://ld.bs.ch/gc/meeting/2026/session/<fachidentifikator>` für eine Sitzung des Grossen Rats Basel-Stadt.
* **DP-08 Eine kanonische URI je Entität:** Jede Entität soll genau eine kanonische URI haben. Andere Schreibweisen (Gross-/Kleinschreibung, Schrägstrich am Ende, führende Nullen) sollen mit HTTP 301 auf die kanonische URI umleiten. Die URI soll sprachunabhängig sein; die Sprache wird über Content Negotiation oder separate Darstellungen (`MultilingualUri`) gewählt.
* **DP-09 URIs bleiben auflösbar:** Eine URI soll auch nach Löschung, Archivierung oder Systemwechsel auflösbar bleiben – entweder zur Ressource selbst, per Umleitung oder zu einer Information, was mit der Ressource geschehen ist (HTTP 410 *Gone* für gelöschte Entitäten).

## Zugang
Siehe auch https://github.com/swiss/api-guidelines.

* **DP-13 Systemunabhängige Publikation:** Wo möglich, sollen die Daten unabhängig vom Ratsinformationssystem und vom Webauftritt publiziert werden. Dann überdauern Daten und URIs einen Produktwechsel oder eine Neugestaltung der Website, Lastspitzen der Nutzung belasten den Ratsbetrieb nicht, und es bleibt nachvollziehbar, welche Daten zu welchem Zeitpunkt publiziert waren.

* **DP-14 Anonymer, offener Zugang:** Öffentliche Daten sollen ohne Registrierung und ohne API-Schlüssel abrufbar sein. Ein Schlüssel oder eine Datenliefervereinbarung kann für erhöhte Kontingente oder zugesicherte Verfügbarkeit angeboten werden, soll aber keine Voraussetzung für den Zugang sein. Die Schnittstelle soll ausschliesslich lesend, zustandslos und über HTTPS erreichbar sein und CORS (`Access-Control-Allow-Origin: *`) erlauben, damit Webanwendungen Dritter sie direkt nutzen können.

* **DP-15 Lastbegrenzung transparent machen:** Ist eine Lastbegrenzung (Throttling) nötig, sollen die Limiten dokumentiert und Überschreitungen mit HTTP 429 und `Retry-After` beantwortet werden. Datenendpunkte sollen nicht per `robots.txt` von Suchmaschinen und Crawlern ausgeschlossen werden; diese gehören ausdrücklich zum vorgesehenen Nutzerkreis.

* **DP-12 Gesamtbezug der Daten:** Daten sollen sowohl als Gesamtbezug (Bulk Download oder Datendump ein komprimiertes Paket je Datensatz unter einer stabilen URL) als auch über eine Schnittstelle (API) für Einzelabfragen angeboten werden. Wer nur eines anbieten kann, soll den Gesamtbezug priorisieren, weil er ohne Programmieraufwand nutzbar ist und Lastspitzen vermeidet.


## Aktualisierung, Korrekturen und Löschungen

Politische Daten ändern sich laufend, und Nutzerinnen und Nutzer müssen ihre Kopien nachführen können, ohne jeweils den gesamten Bestand neu zu laden.

* **DP-18 Änderungszeitpunkt pflegen:** Bei jeder Änderung einer Entität soll `datetime_modified` (bzw. `date_modified`) nachgeführt werden (Mixin `HasCreationModificationDates`). Dieser Wert ist die Grundlage für jede inkrementelle Synchronisation und darf nicht ausbleiben.

* **DP-19 Abfrage nach Änderungen:** Die Schnittstelle soll Filter auf Erstellungs- und Änderungszeitpunkt anbieten (z. B. `modified_since`), damit nur Änderungen seit dem letzten Abruf geholt werden müssen.

* **DP-20 Löschungen sichtbar machen:** Entitäten sollen nicht einfach verschwinden. Eine gelöschte oder zurückgezogene Entität soll als solche markiert weiter ausgeliefert werden (Identifikator, Typ und Löschzeitpunkt), zumindest in Abfragen nach Änderungen. Ihre URI antwortet mit HTTP 410 (DP-09). Nur so erfahren Nutzerinnen und Nutzer, dass sie den Datensatz in ihrer Kopie entfernen müssen.

## Metadaten und Auffindbarkeit

* **DP-24 Katalogisierung nach DCAT-AP CH:** Jeder Datensatz soll mit Metadaten nach eCH-0200 (DCAT-AP CH) beschrieben und in einem Katalog verzeichnet werden (opendata.swiss). Pflichtangaben sind dort u. a. Titel, Beschreibung, Identifikator, publizierende Stelle, Kontakt und Lizenz.
* **DP-25 Publizierende Stelle eindeutig ausweisen:** Die Metadaten sollen festhalten,
  * wer die Daten publiziert, mit einer stabilen Kontaktadresse, die laufend bearbeitet wird;
  * welche Staatsebene (Bund, Kanton, Gemeinde) und welche Gewalt (Legislative, Exekutive) die Daten betreffen;
  * ab welchem Zeitpunkt die Daten vollständig vorliegen (ältere Bestände sind oft lückenhaft).

## Lizenz

* **DP-29 Offene Lizenz:** Daten sollen unter einer offenen Lizenz publiziert werden, welche die Weiterverwendung einschliesslich kommerzieller Nutzung erlaubt. Empfohlen sind CC0 bzw. die entsprechenden Nutzungsbedingungen von opendata.swiss (`terms_open`, `terms_by`). eCH-0205 empfiehlt CC0, weil sie die Verknüpfung mit anderen Daten (z. B. Wikidata) am wenigsten einschränkt. Für die Bundesverwaltung gilt zusätzlich Art. 10 EMBAG.
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
* **DP-37 Nach der Archivierung weiterleiten:** Die URIs archivierter Entitäten sollen weiterhin auflösbar sein und auf das Archiv bzw. eine Information zum Zugang verweisen (DP-09). Ist absehbar, dass eine Ressource nur befristet online bleibt (z. B. Ton- und Videoaufnahmen von Sitzungen), soll die geplante Verfügbarkeit in den Metadaten angegeben werden (`dcatap:availability` nach eCH-0200), zusammen mit dem Hinweis, wo die Ressource danach zu finden ist. Wird ein publiziertes Vokabular oder Schema ersetzt, soll die alte Version abrufbar bleiben, solange Daten darauf verweisen.


## Offene Punkte

Folgende Fragen sind in der Fachgruppe noch zu klären:

* Ein kontrolliertes Vokabular für die Rolle der publizierenden Stelle (erstpublizierend/aggregierend, Staatsebene, Gewalt) existiert in eCH-0200 noch nicht. Zu prüfen ist, ob die Fachgruppe ein eigenes Vokabular definiert oder auf eCH-0200 wartet.
* Das Schema kennt derzeit kein eigenes Merkmal für gelöschte bzw. zurückgezogene Entitäten (DP-20). Zu prüfen ist ein gemeinsames Element in den Common Data Elements.
* Die Angaben zur Kompetenz (Zuständigkeit) einer Körperschaft sind noch nicht modelliert.
* Verfahren zur Signierung strukturierter Daten (DP-35).
* Beispiele für mögliche Pipelines (aus Ratssystemen) angeben.

## Referenzen

* eCH-0200 DCAT-Anwendungsprofil für Datenportale in der Schweiz (DCAT-AP CH), V3.0.1: <https://www.ech.ch/de/ech/ech-0200/3.0.1>
* eCH-0205 Linked Open Data, V1.0: <https://www.ech.ch/de/ech/ech-0205/1.0>
* eCH-0160 Archivische Ablieferungsschnittstelle, V1.3.0: <https://www.ech.ch/de/ech/ech-0160/1.3.0>
* OParl 1.1, Spezifikation: <https://oparl.org/spezifikation/online-ansicht/>
* W3C, Data on the Web Best Practices: <https://www.w3.org/TR/dwbp/>
* W3C, Cool URIs don't change: <https://www.w3.org/Provider/Style/URI>
* W3C, Cool URIs for the Semantic Web: <https://www.w3.org/TR/cooluris/>
* Fachgruppe Politische Geschäfte, Naming Conventions and URI Concept: `docs/common/naming.md`
* GO FAIR, FAIR Principles: <https://www.go-fair.org/fair-principles/>
* Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG), Art. 10: <https://www.fedlex.admin.ch/eli/cc/2023/682/de>
* Frictionless Data Package: <https://datapackage.org/standard/data-package/>
* LINDAS, Namespace-Governance: <https://schema.ld.admin.ch/governance/namespaces>
