\newpage

# Einleitung

Dieses Kapitel ist rein informativer Natur. Es ordnet den Standard in die Arbeiten der Fachgruppe ein, klärt die Begriffe rund um den Gesetzgebungs- und Publikationsprozess und vermittelt die technischen und konzeptionellen Grundlagen, die für die normativen Kapitel vorausgesetzt werden. Auch der jeweils erste Abschnitt der normativen Kapitel ist informativ.

## Anwendungsgebiet

Der Standard eCH-0296 ist eine Lokalisierung von Akoma Ntoso (AKN) und des European Legislation Identifier (ELI) für die Schweiz. AKN ist ein XML-Standard für Dokumente aus parlamentarischen Geschäften, Gesetzgebung und Rechtsprechung; ELI ist ein System zur Identifikation von Rechtsvorschriften auf gemeinsamer Grundlage.

Die Bereitstellung der Gesetzessammlung in digitaler Form ist in der Soll-Architektur von E-Government Schweiz (eCH-0122) eine Geschäftsfähigkeit mit Voraussetzungscharakter. Wenn alle Verwaltungsebenen ihre Erlasse strukturiert und maschinenlesbar veröffentlichen, lässt sich der Austausch von Rechtsdaten vereinfachen und Redundanz vermeiden. eCH-0296 schafft dafür eine einheitliche Sprache und einheitliche Schnittstellen.

Drei Anwendungsfälle stehen im Vordergrund:

- **Strukturierte Publikation von Erlassen** — einheitliche, maschinenlesbare Abbildung von Gesetzen, Verordnungen und weiteren Erlassen mittels AKN.
- **Eindeutige Identifikation und Verlinkung** — persistente, auflösbare Identifikatoren für Erlasse und ihre Bestandteile mittels ELI, von der Gemeinde bis zum Bund.
- **Föderierter Zugang zu Rechtssammlungen** — standardisierter Austausch und Aggregation von Erlassdaten zwischen den Verwaltungsebenen und mit europäischen Systemen.

## Aufbau des Standards

Der normative Teil besteht aus drei aufeinander aufbauenden Modulen:

- **Identifikation** — Regeln zur Bildung gültiger URIs für Erlasse und weitere Dokumente des Gesetzgebungsprozesses.
- **Inhalt** — die Dokumententypen und ihre Struktur.
- **Metadaten** — Angaben, welche die Dokumente und ihre Beziehungen untereinander beschreiben.

## Begrifflichkeiten

Der Begriff Gesetz ist vom Begriff Erlass mitumfasst. Wenn hier von Erlassen und Gesetzestexten die Rede ist, sind alle Stufen (Verfassung, Gesetze, Verordnungen) und alle Ausgestaltungen (Beschluss, Aufhebung, Änderung, Löschung) gemeint. Der Begriff Erlass steht entweder als Überbegriff oder — in Abgrenzung zum Gesetz im formellen Sinn — für jeden Akt eines Parlaments, der rechtsetzenden Charakter hat, aber ohne materiellen Gehalt ein bestehendes Gesetz in Kraft setzt oder aufhebt.

Gesetze sind Texte mit rechtsetzendem Charakter, die Gegenstand juristischer Auslegung sein können und deshalb auf semantischer Ebene mit Hilfsmaterialien unterlegt werden — mit dem erläuternden Bericht oder dem parlamentarischen Geschäft. Diese Hilfsmaterialien entstehen aus politischen Geschäften und gehören deshalb ebenfalls zu den Dokumententypen dieses Standards.

Am Gesetzgebungs- und Publikationsprozess sind neben den Parlamenten weitere Akteure beteiligt, etwa redaktionelle Kommissionen und publizierende Organe. Vier Vorgänge prägen den Prozess:

- **Übersetzung** — nach der Schlussabstimmung durchläuft ein Erlass in der Regel eine redaktionelle Bereinigung und wird in weitere Landessprachen übersetzt.
- **Konsolidierung** — Änderungen an einem Erlass wirken sich meist auf weitere Erlasse aus; diese Wirkungen sind in die neuen Fassungen zu konsolidieren.
- **Inkrafttreten und Referendum** — die meisten Erlasse treten erst zu einem späteren Zeitpunkt in Kraft; kommt ein Referendum zustande und wird der Erlass abgelehnt, kann er noch vor dem Inkrafttreten wieder aufgehoben werden.
- **Ratifikation** — internationale Verträge werden zunächst von der Exekutive oder besonderen Organen ausgehandelt und danach vom Parlament genehmigt.

Aus all diesen Vorgängen gehen Dokumente hervor, die ihrerseits auf andere Dokumente des Prozesses Bezug nehmen. Wie diese Dokumente strukturiert sind, welche Metadaten ihre Beziehungen abbilden und wie sie über einheitlich gebildete, möglichst persistente Links abrufbar sind, ist Gegenstand dieses Standards.

## Dokumententypen

Die folgenden Dokumententypen dienen im weiteren Verlauf als Beispiele.

**Parlamentarische Geschäfte**

| FGA-Nummer | Titel | URI | Bemerkung |
|---|---|---|---|
| FGA 2026/802 | Schlussabstimmungstext | [fedlex.admin.ch/eli/fga/2026/802/de](https://www.fedlex.admin.ch/eli/fga/2026/802/de) | Vorlage der Redaktionskommission mit Referendumsfrist |
| — | Gesetzesentwürfe und Normenkonzepte | — | Frühe Legislaturphase, Dokumentenstruktur in Entwurfsform |
| — | Anträge | — | Parlamentarische Anträge und Eingaben |
| — | Fahnen (synoptische Darstellungen) | — | Gegenüberstellung von Textfassungen |
| — | Kommissionsberichte | — | Berichte der parlamentarischen Kommissionen |

**Vernehmlassungen und erläuternde Berichte**

| Nummer | Titel | URI | Bemerkung |
|---|---|---|---|
| Proj. 2024/79 | Kommunikationsplattformengesetz — Vernehmlassungsverfahren | [fedlex.data.admin.ch/…/cons_1](https://fedlex.data.admin.ch/eli/dl/proj/2024/79/cons_1) | Projektübersicht und Vernehmlassungsdokumentation |
| VE-KomPG | Vorentwurf zum Kommunikationsplattformengesetz | [fedlex.admin.ch/…/doc_1/de](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/dl/proj/2024/79/cons_1/doc_1/de/pdf-a/fedlex-data-admin-ch-eli-dl-proj-2024-79-cons_1-doc_1-de-pdf-a.pdf) | Vorgeschlagener Gesetzestext zur öffentlichen Vernehmlassung |
| AS 2024/79 | Erläuternder Bericht zum Vorentwurf | [fedlex.admin.ch/…/doc_5/de](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/dl/proj/2024/79/cons_1/doc_5/de/pdf-a/fedlex-data-admin-ch-eli-dl-proj-2024-79-cons_1-doc_5-de-pdf-a.pdf) | Detaillierte Begründung zum Vorentwurf |
| RFA 2024/79 | Regulierungsfolgenabschätzung | [bakom.admin.ch/…RFA.pdf](https://www.bakom.admin.ch/dam/de/sd-web/qe9rNgmwX2CZ/Regulierungsfolgenabsch%C3%A4tzung%20(RFA)%20zur%20Regulierung%20von%20sehr%20grossen%20Kommunikationsplattformen%20und%20sehr%20grossen%20Online-Suchmaschinen.pdf) | Kostenwirkungsanalyse und Machbarkeitsstudie |

**Erlasse und Gesetzestexte**

| SR-Nummer | Name | URI | Bemerkung |
|---|---|---|---|
| SR 101 | Bundesverfassung der Schweizerischen Eidgenossenschaft | [fedlex.admin.ch/eli/cc/1999/404/de](https://www.fedlex.admin.ch/eli/cc/1999/404/de) | Generelle Struktur auf Stufe Verfassung, Mehrsprachigkeit |
| SR 131.213 | Verfassung des Kantons Luzern | [ai.clex.ch/…LUZV-100](https://ai.clex.ch/download?ID=LUZV-100) | Kantonsverfassung — verwendet § statt Art. |
| SR 220 | Obligationenrecht (OR) | [fedlex.admin.ch/eli/cc/1911/3470/de](https://www.fedlex.admin.ch/eli/cc/1911/3470/de) | Kodifikation — 5. Titel des Zivilgesetzbuches |
| SR 171.10 | Parlamentsgesetz (ParlG) | [fedlex.admin.ch/eli/cc/1975/856/de](https://www.fedlex.admin.ch/eli/cc/1975/856/de) | Gesetz neueren Datums |
| SR 741.21 | Signalisationsverordnung (SSV) | [fedlex.admin.ch/eli/cc/1962/3631/de](https://www.fedlex.admin.ch/eli/cc/1962/3631/de) | Verordnung mit Tabellen und Bildern |

**Internationale und interkantonale Verträge**

| SR-Nummer | Titel | URI | Art |
|---|---|---|---|
| SR 0.101 | Charta der Vereinten Nationen | [fedlex.admin.ch/eli/cc/1945/…](https://www.fedlex.admin.ch/eli/cc/1945/214_224_245/de) | Multilateraler völkerrechtlicher Vertrag |
| SR 0.101.1 | Allgemeine Erklärung der Menschenrechte | [fedlex.admin.ch/eli/cc/1948/13/de](https://www.fedlex.admin.ch/eli/cc/1948/13/de) | Menschenrechtsinstrument (UNO) |
| SR 0.101.2 | Konvention zum Schutze der Menschenrechte und Grundfreiheiten (EMRK) | [fedlex.admin.ch/eli/cc/1950/194/de](https://www.fedlex.admin.ch/eli/cc/1950/194/de) | Menschenrechtsvertrag (Europarat) |
| SR 0.111 | Wiener Übereinkommen über das Recht der Verträge | [fedlex.admin.ch/eli/cc/1980/1566/de](https://www.fedlex.admin.ch/eli/cc/1980/1566/de) | Völkerrechtlicher Vertrag über Vertragsrecht |
| SR 0.142.112.681 | Abkommen über die Freizügigkeit (Schweiz–EU) | [fedlex.admin.ch/eli/cc/1999/300/de](https://www.fedlex.admin.ch/eli/cc/1999/300/de) | Bilateraler Vertrag |
| iSR 5.3-21 | Vereinbarung über die Harmonisierung der Informatik in der Strafjustiz (VHIS) | — | Interkantonale Vereinbarung |
| iSR 5.3-8 | Konkordat über die Sicherheitsunternehmen | — | Interkantonales Konkordat |

## Technische Grundlagen (XML)

AKN ist ein XML-Standard; XML ist damit das technische Fundament dieses Anwendungsprofils. Elemente und Attribute lassen sich in XML frei definieren — anders als in HTML, wo bestimmte Elemente vorgegeben sind. AKN gibt standardisierte Elemente und Attribute vor, die in vordefinierten Dokumententypen vorkommen dürfen; dieser Standard geht einen Schritt weiter und definiert eine begrenzte Auswahl erlaubter Elemente sowie Regeln zur Strukturierung der Dokumententypen.

Ein Dokument folgt stets demselben Aufbau:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0" xmlns:akn4ch="http://legaldocml.ch/">
    <documentType>
        <meta>
            <!-- Metadata -->
        </meta>
        <body>
            <!-- Content -->
        </body>
    </documentType>
</akomaNtoso>
```

Das Wurzelelement `akomaNtoso` weist das Dokument als AKN-Dokument aus. Das Attribut `xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"` legt den Namensraum fest: Alle enthaltenen Elemente und Attribute folgen den Regeln von Akoma Ntoso 3.0. Der Präfix `xmlns:akn4ch="http://legaldocml.ch/"` erweitert diesen Namensraum um die schweizerischen Eigenheiten.

`documentType` ist ein Platzhalter für den tatsächlichen Dokumententyp — etwa `act` für Erlasse oder `bill` für Entwürfe. Der Dokumententyp bestimmt die Struktur, indem er die erlaubten Elemente festlegt. Das Element `meta` enthält die Metadaten zur Identifikation (URI, Datum, Autor, Land, Nummer, Name, Abkürzung, Sprache, Format) sowie weitere Angaben zum Gesetzgebungs- und Publikationsprozess. Das Element `body` enthält den eigentlichen, für die Lesenden sichtbaren Inhalt.

## Konzeptionelle Grundlagen (FRBR)

FRBR — Functional Requirements for Bibliographic Records — trennt ein abstraktes Werk und seine sprachlichen Fassungen von der konkreten Veröffentlichung in einem bestimmten Format. Vier Abstraktionsstufen werden unterschieden: Work, Expression, Manifestation und Item.

Die Bundesverfassung vom 12. September 1848 etwa hat seither zahlreiche Änderungen erfahren und ist mit der heute geltenden Fassung vom 18. April 1999 nicht mehr vergleichbar; hinzu kommen mehrere sprachliche Fassungen und unterschiedliche Dateiformate.

Sowohl AKN als auch ELI bedienen sich dieses Modells. Ein Dokument nach diesem Standard ist eine XML-Datei und damit eine Manifestation. Es enthält Metadaten zur eindeutigen Identifikation des abstrakten Werks, der sprachlichen Fassung und des Dateiformats:

```xml
<identification>
    <FRBRWork>
        <!-- Metadaten zum abstrakten Werk: URI, Datum, Autor, Land, Nummer, Name, Abkürzung -->
        <FRBRauthoritative value="true"/>
    </FRBRWork>
    <FRBRExpression>
        <!-- Metadaten zur sprachlichen Fassung: URI, Datum, Autor, Sprache -->
        <FRBRlanguage language="de"/>
    </FRBRExpression>
    <FRBRManifestation>
        <!-- Metadaten zur Veröffentlichung: URI, Datum, Autor, Format -->
        <FRBRformat value="xml"/>
    </FRBRManifestation>
</identification>
```

`FRBRauthoritative` gibt an, ob es sich um die massgebende Fassung handelt, die Rechtswirkungen entfaltet — was dann zählt, wenn dieselbe Fassung in mehreren Sammlungen vorliegt.

Alle Beispiele in diesem Standard sind fiktiv und dienen der Illustration; es handelt sich nicht um gültige Dokumente.

## Aufbau einer Lieferung

Ein Dokument nach diesem Standard ist ein `FedlexDocument` — das Wurzelelement `akn:akomaNtoso` mit genau einem Erlass darin.

{{include:ech-0296_laws/output/docs/FedlexDocument.md}}
