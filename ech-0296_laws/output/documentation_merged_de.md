---
title: "eCH-0296 Erlasse und Gesetzestexte"
lang: de
toc: false
---

|**Name**|**Erlasse und Gesetzestexte**|
|---|---|
|**eCH-Nummer**|eCH-0296|
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
|**Autoren**|Fachgruppe Politische Geschäfte: Martin Gajdos, Benedikt Hitz-Gamper, Michael Luggen, Florin Hasler, Christian Gutknecht|
|**Herausgeber / Vertrieb**|Verein eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Abstrakt

Der Standard eCH-0296 ist eine Lokalisierung von Akoma Ntoso (AKN) und des European Legislation Identifier (ELI) für die Schweiz. Er definiert, wie Erlasse und Gesetzestexte strukturiert abgebildet, eindeutig identifiziert und mit Metadaten beschrieben werden — von der Gemeinde über den Kanton bis zum Bund.

Der Standard richtet sich an publizierende Organe der Rechtssammlungen, an Softwareanbieterinnen und Softwareanbieter von Gesetzgebungs- und Publikationssystemen sowie an Stellen, die Rechtsdaten weiterverarbeiten oder aggregieren.

eCH-0296 ist Teil einer Familie von Standards für politische Daten und arbeitet eng mit eCH-0292 (Gemeinsame Datenelemente), eCH-0293 (Öffentlicher Ratsbetrieb), eCH-0294 (Politische Akteure), eCH-0295 (Parlamentarische Geschäfte) und eCH-0297 (Öffentliche Konsultationen) zusammen.

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



### Klasse: FedlexDocument []{#FedlexDocument}


_Wurzelelement eines Fedlex AkomaNtoso-Dokuments (akn:akomaNtoso). Muss genau ein akn:act-Element enthalten, keine weiteren Kinder (FLX-RT-001). Trägt die AkomaNtoso-Namespace-Deklaration und den Fedlex-Erweiterungs-Namespace._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| act_ref | 1 <br/> [Act](#Act) | Der Erlass (akn:act). Muss das einzige Kind von akn:akomaNtoso sein (FLX-RT-001). |






















</div>

\newpage

# Identifikation

## ELI-URI-Vorlage

Der Standard folgt ELI und identifiziert Rechtstexte über HTTP-URIs. Die URIs werden formell über maschinenlesbare URI-Vorlagen nach RFC 6570 beschrieben. Die Umsetzung von ELI-URIs ist nur einer von vier Pfeilern des ELI-Standards; die Pfeiler 2 bis 4 setzen eine Beschreibung der Rechtsdaten mit Metadaten voraus — siehe das Kapitel Metadaten.

ELI-URIs bestehen aus hierarchisch aufgebauten Komponenten, die nach nationalen Anforderungen ausgewählt werden. Die Komponenten werden durch „/" getrennt und bilden zusammen einen Pfad, der aus Sicht der Endnutzenden wie aus rechtlicher Sicht eine semantische Bedeutung tragen kann. Mit Ausnahme der ersten Komponente `eli` sind alle optional. Das folgende Muster nutzt sämtliche vorgeschlagenen Referenzkomponenten in der vorgeschlagenen Reihenfolge:

```
/eli/{jurisdiction}/{agent}/{subagent}/{year}/{month}/{day}/{type}/{subtype}/{domain}/{natural identifier}/{level 1…}/{point in time}/{version}/{language}
```

Die Referenzkomponenten lassen sich in vier Gruppen aufteilen: Jurisdiction, Reference, Subdivision und Point in time. Zusätzlich wird zwischen der massgebenden und der konsolidierten Fassung (Version) sowie zwischen den sprachlichen Fassungen (Language) unterschieden. Gliederungsebenen innerhalb eines Dokuments (Subdivision) und der Umgang mit Korrigenda (Subtype) bleiben hier ausgeblendet, weil die Dokumentenperspektive im Vordergrund steht.

Zwei Komponentengruppen sind für die schweizerische URI-Vorlage massgebend:

- **Jurisdiction im weiteren Sinn** — bei mehreren publizierenden Stellen ist zunächst zu klären, welchem Gemeinwesen ein Rechtstext zugeordnet wird und, wo nötig, welcher Akteur ihn erlassen hat (Agent beziehungsweise Subagent).
- **Reference** — zur eindeutigen Identifikation muss ein Rechtstext referenzierbar sein. Wie das geschieht, ist von Land zu Land verschieden und hängt stark von der Publikationspraxis ab; denkbar sind Zeitangaben, Dokumententyp, Themen-Codes (Domain) und weitere Unterscheidungsmerkmale (Natural identifier).

## Referenzkomponenten für die Schweiz

| Komponente | Beschreibung | Beispielwert |
|---|---|---|
| `jurisdiction` | Zuständiger Staat oder Kanton | `ch`, `ch-zh`, `ch-ge` |
| `type` | Typ des Rechtsdokuments | `cc` (konsolidiert), `oc` (Amtsblatt), `fga`, `dl` |
| `year` | Erlassjahr | `1999`, `2024` |
| `natural_id` | Natürliche Identifikationsnummer | `404`, `123` |
| `language` | Sprachcode (ISO 639-1) | `de`, `fr`, `it`, `rm` |

## Identifikation im Dokument

Der FRBR-Block `akn:identification` trägt die drei Ebenen Work, Expression und Manifestation. Jede Ebene führt ihre eigene URI, ihre Daten und ihre Autoren; die Ebene Expression ergänzt die Sprache, die Ebene Manifestation das Format.



### Klasse: Identification []{#Identification}


_FRBR-Identifikationsblock (akn:identification) mit Work-, Expression- und Manifestations-Beschreibungen. Das @source-Attribut referenziert die verantwortliche Organisation als Dokument-internen Anker (z.B. '#ch.bk')._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](#AnchorRef) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| frbr_work | 0..1 <br/> [FRBRWork](#FRBRWork) | FRBR-Work-Ebenen-Beschreibung (akn:FRBRWork). |
| frbr_expression | 0..1 <br/> [FRBRExpression](#FRBRExpression) | FRBR-Expression-Ebenen-Beschreibung (akn:FRBRExpression). |
| frbr_manifestation | 0..1 <br/> [FRBRManifestation](#FRBRManifestation) | FRBR-Manifestations-Ebenen-Beschreibung (akn:FRBRManifestation). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActMeta](#ActMeta) | identification_ref | range | [Identification](#Identification) |














#### Beispiele
##### Beispiel Identification: sr101 excerpt 1 1

```yaml
identification_ref:
  source: '#ch.bk'
  frbr_work:
    frbr_this:
      value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
    frbr_uri:
      value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
    frbr_dates:
    - date_value: '2000-01-01'
      frbr_date_name: jolux:dateEntryInForce
    - date_value: '1999-04-18'
      frbr_date_name: jolux:dateDocument
    - date_value: '2024-03-03'
      frbr_date_name: jolux:dateApplicability
    frbr_authors:
    - href: '#ch.bk'
      as_role: '#publisher'
    - href: '#ch.bk'
      as_role: '#rightsHolder'
    frbr_country:
      value: CH
    frbr_number:
      value: '101'
    frbr_names:
    - xml_lang: de
      value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April
        1999
      short_form: BV
    - xml_lang: fr
      value: Constitution fédérale de la Confédération suisse du 18 avril 1999
      short_form: Cst.
    - xml_lang: it
      value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
      short_form: Cost.
    - xml_lang: rm
      value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
      short_form: Cst.
    frbr_authoritative:
      value: 'true'
  frbr_expression:
    frbr_this:
      value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
    frbr_uri:
      value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
    frbr_dates:
    - date_value: '2000-01-01'
      frbr_date_name: jolux:dateEntryInForce
    - date_value: '1999-04-18'
      frbr_date_name: jolux:dateDocument
    frbr_authors:
    - href: '#ch.bk'
      as_role: '#publisher'
    frbr_language:
      language_value: de
  frbr_manifestation:
    frbr_this:
      value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
    frbr_uri:
      value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
    frbr_dates:
    - date_value: '2024-03-03'
      frbr_date_name: jolux:dateApplicability
    frbr_authors:
    - href: '#ch.bk'
      as_role: '#publisher'
    frbr_format:
      value: xml

```
##### Beispiel Identification: bgoe excerpt 1 1

```yaml
identification_ref:
  source: '#ch.bk'
  frbr_work:
    frbr_this:
      value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
    frbr_uri:
      value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
    frbr_dates:
    - date_value: '2006-07-01'
      frbr_date_name: jolux:dateEntryInForce
    - date_value: '2004-12-17'
      frbr_date_name: jolux:dateDocument
    - date_value: '2023-11-01'
      frbr_date_name: jolux:dateApplicability
    frbr_authors:
    - href: '#ch.bk'
      as_role: '#publisher'
    - href: '#ch.bk'
      as_role: '#rightsHolder'
    frbr_country:
      value: CH
    frbr_number:
      value: '152.3'
    frbr_names:
    - xml_lang: de
      value: >-
        Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung
        (Öffentlichkeitsgesetz, BGÖ)
      short_form: BGÖ
    - xml_lang: fr
      value: >-
        Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans l'administration
        (Loi sur la transparence, LTrans)
      short_form: LTrans
    - xml_lang: it
      value: >-
        Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
        (Legge sulla trasparenza, LTras)
      short_form: LTras
    - xml_lang: rm
      value: >-
        Lescha federala dals 17 da december 2004 davart il princip da la transparenza
        da l'administraziun (Lescha da transparenza, LTrans)
      short_form: LTrans
    - xml_lang: en
      value: >-
        Federal Act of 17 December 2004 on Freedom of Information in the Administration
        (Freedom of Information Act, FoIA)
      short_form: FoIA
    frbr_authoritative:
      value: 'true'
  frbr_expression:
    frbr_this:
      value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
    frbr_uri:
      value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
    frbr_dates:
    - date_value: '2006-07-01'
      frbr_date_name: jolux:dateEntryInForce
    - date_value: '2023-11-01'
      frbr_date_name: jolux:dateApplicability
    frbr_authors:
    - href: '#ch.bk'
      as_role: '#publisher'
    frbr_language:
      language_value: de
  frbr_manifestation:
    frbr_this:
      value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
    frbr_uri:
      value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
    frbr_dates:
    - date_value: '2023-11-01'
      frbr_date_name: jolux:dateApplicability
    frbr_authors:
    - href: '#ch.bk'
      as_role: '#publisher'
    frbr_format:
      value: xml
      fedlex_generator: 2024-q4-rel-1.6.5

```






</div>



### Klasse: FRBRWork []{#FRBRWork}


_FRBR-Work-Ebene (akn:FRBRWork): der abstrakte Erlass unabhängig von Sprache und Version. Enthält ELI-URIs, Fedlex/JoLux-Daten, Autoren, Ländercode (CH), SR-Nummer und mehrsprachige Namen mit Kurzformen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| frbr_this | 0..1 <br/> [UriValueType](#UriValueType) | Kanonische ELI-URI dieser FRBR-Entität (akn:FRBRthis/@value). |
| frbr_uri | 0..1 <br/> [UriValueType](#UriValueType) | Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value). |
| frbr_dates | * <br/> [FRBRDate](#FRBRDate) | Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für verschiedene Ereignistypen.  |
| frbr_authors | * <br/> [FRBRAuthor](#FRBRAuthor) | Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor). |
| frbr_country | 0..1 <br/> [ValueType](#ValueType) | Ländercode für diesen Erlass (akn:FRBRcountry/@value), z.B. 'CH'. |
| frbr_number | 0..1 <br/> [ValueType](#ValueType) | SR-Nummer (akn:FRBRnumber/@value), z.B. '101'. |
| frbr_names | * <br/> [FRBRName](#FRBRName) | Mehrsprachige Namenseinträge des FRBR-Works (akn:FRBRname). Ein Eintrag pro Sprache. |
| frbr_authoritative | 0..1 <br/> [ValueType](#ValueType) | Ob dies die massgebliche Version ist (akn:FRBRauthoritative/@value). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Identification](#Identification) | frbr_work | range | [FRBRWork](#FRBRWork) |














#### Beispiele
##### Beispiel FRBRWork: sr101 excerpt 1 1

```yaml
frbr_work:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
  frbr_dates:
  - date_value: '2000-01-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '1999-04-18'
    frbr_date_name: jolux:dateDocument
  - date_value: '2024-03-03'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  - href: '#ch.bk'
    as_role: '#rightsHolder'
  frbr_country:
    value: CH
  frbr_number:
    value: '101'
  frbr_names:
  - xml_lang: de
    value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April 1999
    short_form: BV
  - xml_lang: fr
    value: Constitution fédérale de la Confédération suisse du 18 avril 1999
    short_form: Cst.
  - xml_lang: it
    value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
    short_form: Cost.
  - xml_lang: rm
    value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
    short_form: Cst.
  frbr_authoritative:
    value: 'true'

```
##### Beispiel FRBRWork: bgoe excerpt 1 1

```yaml
frbr_work:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
  frbr_dates:
  - date_value: '2006-07-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '2004-12-17'
    frbr_date_name: jolux:dateDocument
  - date_value: '2023-11-01'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  - href: '#ch.bk'
    as_role: '#rightsHolder'
  frbr_country:
    value: CH
  frbr_number:
    value: '152.3'
  frbr_names:
  - xml_lang: de
    value: >-
      Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung
      (Öffentlichkeitsgesetz, BGÖ)
    short_form: BGÖ
  - xml_lang: fr
    value: >-
      Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans l'administration
      (Loi sur la transparence, LTrans)
    short_form: LTrans
  - xml_lang: it
    value: >-
      Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
      (Legge sulla trasparenza, LTras)
    short_form: LTras
  - xml_lang: rm
    value: >-
      Lescha federala dals 17 da december 2004 davart il princip da la transparenza
      da l'administraziun (Lescha da transparenza, LTrans)
    short_form: LTrans
  - xml_lang: en
    value: >-
      Federal Act of 17 December 2004 on Freedom of Information in the Administration
      (Freedom of Information Act, FoIA)
    short_form: FoIA
  frbr_authoritative:
    value: 'true'

```






</div>



### Klasse: FRBRExpression []{#FRBRExpression}


_FRBR-Expression-Ebene (akn:FRBRExpression): eine sprachspezifische Version des Erlasses. Identifiziert durch einen ELI-URI mit Sprachcode._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| frbr_this | 0..1 <br/> [UriValueType](#UriValueType) | Kanonische ELI-URI dieser FRBR-Entität (akn:FRBRthis/@value). |
| frbr_uri | 0..1 <br/> [UriValueType](#UriValueType) | Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value). |
| frbr_dates | * <br/> [FRBRDate](#FRBRDate) | Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für verschiedene Ereignistypen.  |
| frbr_authors | * <br/> [FRBRAuthor](#FRBRAuthor) | Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor). |
| frbr_language | 0..1 <br/> [LanguageType](#LanguageType) | Sprachcode dieser Expression (akn:FRBRlanguage/@language). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Identification](#Identification) | frbr_expression | range | [FRBRExpression](#FRBRExpression) |














#### Beispiele
##### Beispiel FRBRExpression: sr101 excerpt 1 1

```yaml
frbr_expression:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
  frbr_dates:
  - date_value: '2000-01-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '1999-04-18'
    frbr_date_name: jolux:dateDocument
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  frbr_language:
    language_value: de

```
##### Beispiel FRBRExpression: bgoe excerpt 1 1

```yaml
frbr_expression:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
  frbr_dates:
  - date_value: '2006-07-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '2023-11-01'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  frbr_language:
    language_value: de

```






</div>



### Klasse: FRBRManifestation []{#FRBRManifestation}


_FRBR-Manifestations-Ebene (akn:FRBRManifestation): ein spezifisches Dateiformat der Expression. Für Fedlex XML-Dateien ist der Formatwert 'xml'. Das optionale Attribut fedlex:generator ist nur hier erlaubt (FLX-XF-002)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| frbr_this | 0..1 <br/> [UriValueType](#UriValueType) | Kanonische ELI-URI dieser FRBR-Entität (akn:FRBRthis/@value). |
| frbr_uri | 0..1 <br/> [UriValueType](#UriValueType) | Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value). |
| frbr_dates | * <br/> [FRBRDate](#FRBRDate) | Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für verschiedene Ereignistypen.  |
| frbr_authors | * <br/> [FRBRAuthor](#FRBRAuthor) | Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor). |
| frbr_format | 0..1 <br/> [FormatType](#FormatType) | Dateiformat dieser Manifestation (akn:FRBRformat/@value), typischerweise 'xml'. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Identification](#Identification) | frbr_manifestation | range | [FRBRManifestation](#FRBRManifestation) |














#### Beispiele
##### Beispiel FRBRManifestation: bgoe excerpt 1 1

```yaml
frbr_manifestation:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
  frbr_dates:
  - date_value: '2023-11-01'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  frbr_format:
    value: xml
    fedlex_generator: 2024-q4-rel-1.6.5

```
##### Beispiel FRBRManifestation: sr101 excerpt 1 1

```yaml
frbr_manifestation:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
  frbr_dates:
  - date_value: '2024-03-03'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  frbr_format:
    value: xml

```






</div>



### Klasse: FRBRDate []{#FRBRDate}


_Ein Datumseintrag einer FRBR-Entität (akn:FRBRdate). Das @name-Attribut verwendet Fedlex/JoLux-Vokabular: jolux:dateEntryInForce, jolux:dateDocument, jolux:dateApplicability._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_value | 0..1 <br/> Date | Ein ISO-8601-Datumswert (akn:FRBRdate/@date). |
| frbr_date_name | 0..1 <br/> String | Datumstyp (akn:FRBRdate/@name), mit Fedlex/JoLux-Vokabular, z.B. 'jolux:dateEntryInForce', 'jolux:dateDocument', 'jolux:dateApplicability'.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](#FRBRWork) | frbr_dates | range | [FRBRDate](#FRBRDate) |
| [FRBRExpression](#FRBRExpression) | frbr_dates | range | [FRBRDate](#FRBRDate) |
| [FRBRManifestation](#FRBRManifestation) | frbr_dates | range | [FRBRDate](#FRBRDate) |














#### Beispiele
##### Beispiel FRBRDate: sr101 excerpt 1 2

```yaml
frbr_dates:
- date_value: '1999-04-18'
  frbr_date_name: jolux:dateDocument

```
##### Beispiel FRBRDate: bgoe excerpt 1 2

```yaml
frbr_dates:
- date_value: '2023-11-01'
  frbr_date_name: jolux:dateApplicability

```
##### Beispiel FRBRDate: sr101 excerpt 1 3

```yaml
frbr_dates:
- date_value: '2024-03-03'
  frbr_date_name: jolux:dateApplicability

```
##### Beispiel FRBRDate: bgoe excerpt 1 3

```yaml
frbr_dates:
- date_value: '2023-11-01'
  frbr_date_name: jolux:dateApplicability

```
##### Beispiel FRBRDate: bgoe excerpt 1 1

```yaml
frbr_dates:
- date_value: '2023-11-01'
  frbr_date_name: jolux:dateApplicability

```
##### Beispiel FRBRDate: sr101 excerpt 1 1

```yaml
frbr_dates:
- date_value: '2024-03-03'
  frbr_date_name: jolux:dateApplicability

```






</div>



### Klasse: FRBRAuthor []{#FRBRAuthor}


_Ein Autoren- oder Rechteinhaber-Eintrag einer FRBR-Entität (akn:FRBRauthor). @href referenziert die Organisation; @as referenziert die Rolle (beide als Dokument-interne Anker)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| href | 0..1 <br/> String | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| as_role | 0..1 <br/> [AnchorRef](#AnchorRef) | Rolle des Autors (akn:FRBRauthor/@as), als Anker-Referenz, z.B. '#publisher', '#rightsHolder'.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](#FRBRWork) | frbr_authors | range | [FRBRAuthor](#FRBRAuthor) |
| [FRBRExpression](#FRBRExpression) | frbr_authors | range | [FRBRAuthor](#FRBRAuthor) |
| [FRBRManifestation](#FRBRManifestation) | frbr_authors | range | [FRBRAuthor](#FRBRAuthor) |














#### Beispiele
##### Beispiel FRBRAuthor: sr101 excerpt 1 2

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#rightsHolder'

```
##### Beispiel FRBRAuthor: sr101 excerpt 1 1

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#publisher'

```
##### Beispiel FRBRAuthor: bgoe excerpt 1 1

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#publisher'

```
##### Beispiel FRBRAuthor: bgoe excerpt 1 2

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#rightsHolder'

```






</div>



### Klasse: FRBRName []{#FRBRName}


_Ein mehrsprachiger Namenseintrag des FRBR-Works (akn:FRBRname). Enthält den offiziellen Langtitel und eine optionale Abkürzung. Ein Eintrag pro Sprache._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| xml_lang | 0..1 <br/> String | XML-Sprachattribut (xml:lang), z.B. 'de', 'fr', 'it', 'rm', 'en'. |
| value | 0..1 <br/> String | Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet. |
| short_form | 0..1 <br/> String | Kurzform-Abkürzung des Gesetzesnamens (@shortForm), z.B. 'BV' (Deutsch), 'Cst.' (Französisch).  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](#FRBRWork) | frbr_names | range | [FRBRName](#FRBRName) |














#### Beispiele
##### Beispiel FRBRName: bgoe excerpt 1 4

```yaml
frbr_names:
- xml_lang: rm
  value: >-
    Lescha federala dals 17 da december 2004 davart il princip da la transparenza
    da l'administraziun (Lescha da transparenza, LTrans)
  short_form: LTrans

```
##### Beispiel FRBRName: sr101 excerpt 1 3

```yaml
frbr_names:
- xml_lang: it
  value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
  short_form: Cost.

```
##### Beispiel FRBRName: bgoe excerpt 1 3

```yaml
frbr_names:
- xml_lang: it
  value: >-
    Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
    (Legge sulla trasparenza, LTras)
  short_form: LTras

```
##### Beispiel FRBRName: sr101 excerpt 1 2

```yaml
frbr_names:
- xml_lang: fr
  value: Constitution fédérale de la Confédération suisse du 18 avril 1999
  short_form: Cst.

```
##### Beispiel FRBRName: bgoe excerpt 1 2

```yaml
frbr_names:
- xml_lang: fr
  value: >-
    Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans l'administration
    (Loi sur la transparence, LTrans)
  short_form: LTrans

```
##### Beispiel FRBRName: bgoe excerpt 1 5

```yaml
frbr_names:
- xml_lang: en
  value: >-
    Federal Act of 17 December 2004 on Freedom of Information in the Administration
    (Freedom of Information Act, FoIA)
  short_form: FoIA

```
##### Beispiel FRBRName: bgoe excerpt 1 1

```yaml
frbr_names:
- xml_lang: de
  value: >-
    Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung
    (Öffentlichkeitsgesetz, BGÖ)
  short_form: BGÖ

```
##### Beispiel FRBRName: sr101 excerpt 1 4

```yaml
frbr_names:
- xml_lang: rm
  value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
  short_form: Cst.

```
##### Beispiel FRBRName: sr101 excerpt 1 1

```yaml
frbr_names:
- xml_lang: de
  value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April 1999
  short_form: BV

```






</div>

## Element-Identifikatoren

Innerhalb eines Dokuments trägt jedes Hierarchieelement, jeder Artikel, jeder Unterabschnitt und jeder Absatz ein `@eId`. Es folgt der AKN-Namenskonvention und bildet den Pfad im Dokument ab (`ti_1`, `ch_1`, `art_1`, `art_1-para_1`) — es ist also bewusst kein zufälliger Identifikator. Die Fedlex-Schematron-Regeln verlangen seine Anwesenheit, nicht aber seine Eindeutigkeit: Reale Dokumente der Systematischen Rechtssammlung enthalten mehrfach vergebene `@eId`.

## Typ: ELIURI []{#ELIURI}




_Ein European Legislation Identifier (ELI) URI, wie von Fedlex verwendet._



<div data-search-exclude markdown="1">

URI: [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI)

### Typ-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Base | `str` |
| Type URI | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |










</div>

## Typ: EIdType []{#EIdType}




_Eindeutiger Element-Identifier innerhalb eines AkomaNtoso-Dokuments (@eId). Folgt der AKN-eId-Konvention, z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'. Gemäss Fedlex Schematron Pflicht bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen._




<div data-search-exclude markdown="1">

URI: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

### Typ-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Base | `str` |
| Type URI | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |










</div>

## Typ: AnchorRef []{#AnchorRef}




_Eine Dokument-interne Referenz im Format '#id', die auf ein eId oder TLC-Element zeigt._



<div data-search-exclude markdown="1">

URI: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

### Typ-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Base | `str` |
| Type URI | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |










</div>

\newpage

# Inhalt

Der Erlass selbst ist das Element `akn:act`. Es trägt den Erlasstyp im Attribut `@name`, dazu die Metadaten, den Vorspann, eine allfällige Präambel und den Hauptteil.



### Klasse: Act []{#Act}


_Das Erlasselement (akn:act). Hauptinhaltselement eines AkomaNtoso-Dokuments. Das @name-Attribut gibt den Erlasstyp an (z.B. 'publicLaw')._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| act_name | 0..1 <br/> [ActTypeEnum](#ActTypeEnum) | Erlasstyp (@name-Attribut von akn:act), z.B. 'publicLaw'. |
| meta | 0..1 <br/> [ActMeta](#ActMeta) | Metadaten-Abschnitt des Erlasses (akn:meta). |
| preface_ref | 0..1 <br/> [Preface](#Preface) | Vorspann des Erlasses (akn:preface). |
| preamble_ref | 0..1 <br/> [Preamble](#Preamble) | Präambel des Erlasses (akn:preamble). |
| body | 0..1 <br/> [ActBody](#ActBody) | Hauptteil des Erlasses (akn:body). |
| components_ref | 0..1 <br/> [Components](#Components) | Die diesem Erlass beiliegenden Dokumente (akn:components). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FedlexDocument](#FedlexDocument) | act_ref | range | [Act](#Act) |














#### Beispiele
##### Beispiel Act: sr101 excerpt 1

```yaml
act_ref:
  act_name: constitution
  meta:
    identification_ref:
      source: '#ch.bk'
      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
        frbr_dates:
        - date_value: '2000-01-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '1999-04-18'
          frbr_date_name: jolux:dateDocument
        - date_value: '2024-03-03'
          frbr_date_name: jolux:dateApplicability
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_country:
          value: CH
        frbr_number:
          value: '101'
        frbr_names:
        - xml_lang: de
          value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April
            1999
          short_form: BV
        - xml_lang: fr
          value: Constitution fédérale de la Confédération suisse du 18 avril 1999
          short_form: Cst.
        - xml_lang: it
          value: Costituzione federale della Confederazione Svizzera del 18 aprile
            1999
          short_form: Cost.
        - xml_lang: rm
          value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl
            1999
          short_form: Cst.
        frbr_authoritative:
          value: 'true'
      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
        frbr_dates:
        - date_value: '2000-01-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '1999-04-18'
          frbr_date_name: jolux:dateDocument
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        frbr_language:
          language_value: de
      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
        frbr_dates:
        - date_value: '2024-03-03'
          frbr_date_name: jolux:dateApplicability
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        frbr_format:
          value: xml
    references_ref:
      source: '#ch.bk'
      tlc_organizations:
      - eId: ch.bk
        href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
        show_as: Bundeskanzlei
      tlc_roles:
      - eId: publisher
        href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
        show_as: Editeur
      - eId: rightsHolder
        href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
        show_as: Détenteur des droits
  preface_ref:
    preface_paragraphs:
    - doc_number: '101'
    - doc_title:
        inline_content:
        - element_type: TextRun
          text: Bundesverfassung
        - element_type: Br
        - element_type: TextRun
          text: der Schweizerischen Eidgenossenschaft
  body:
    titles:
    - eId: tit_1
      num:
        inline_content:
        - element_type: TextRun
          text: '1. Titel: '
      heading:
        inline_content:
        - element_type: TextRun
          text: Allgemeine Bestimmungen
      articles:
      - eId: art_1
        num:
          inline_content:
          - element_type: B
            inline_content:
            - element_type: TextRun
              text: Art. 1
        heading:
          inline_content:
          - element_type: TextRun
            text: Schweizerische Eidgenossenschaft
        paragraphs:
        - eId: art_1/para
          content_ref:
            block_paragraphs:
            - inline_content:
              - element_type: TextRun
                text: >-
                  Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz,
                  Obwalden und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt
                  und Basel-Landschaft, Schaffhausen, Appenzell Ausserrhoden und Appenzell
                  Innerrhoden, St. Gallen, Graubünden, Aargau, Thurgau, Tessin, Waadt,
                  Wallis, Neuenburg, Genf und Jura bilden die Schweizerische Eidgenossenschaft.

```
##### Beispiel Act: bgoe excerpt 1

```yaml
act_ref:
  act_name: publicLaw
  meta:
    identification_ref:
      source: '#ch.bk'
      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
        frbr_dates:
        - date_value: '2006-07-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '2004-12-17'
          frbr_date_name: jolux:dateDocument
        - date_value: '2023-11-01'
          frbr_date_name: jolux:dateApplicability
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_country:
          value: CH
        frbr_number:
          value: '152.3'
        frbr_names:
        - xml_lang: de
          value: >-
            Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der
            Verwaltung (Öffentlichkeitsgesetz, BGÖ)
          short_form: BGÖ
        - xml_lang: fr
          value: >-
            Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans
            l'administration (Loi sur la transparence, LTrans)
          short_form: LTrans
        - xml_lang: it
          value: >-
            Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
            (Legge sulla trasparenza, LTras)
          short_form: LTras
        - xml_lang: rm
          value: >-
            Lescha federala dals 17 da december 2004 davart il princip da la transparenza
            da l'administraziun (Lescha da transparenza, LTrans)
          short_form: LTrans
        - xml_lang: en
          value: >-
            Federal Act of 17 December 2004 on Freedom of Information in the Administration
            (Freedom of Information Act, FoIA)
          short_form: FoIA
        frbr_authoritative:
          value: 'true'
      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
        frbr_dates:
        - date_value: '2006-07-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '2023-11-01'
          frbr_date_name: jolux:dateApplicability
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        frbr_language:
          language_value: de
      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
        frbr_dates:
        - date_value: '2023-11-01'
          frbr_date_name: jolux:dateApplicability
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        frbr_format:
          value: xml
          fedlex_generator: 2024-q4-rel-1.6.5
    references_ref:
      source: '#ch.bk'
      tlc_organizations:
      - eId: ch.bk
        href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
        show_as: Bundeskanzlei
      tlc_roles:
      - eId: publisher
        href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
        show_as: Editeur
      - eId: rightsHolder
        href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
        show_as: Détenteur des droits
      tlc_references:
      - name_attr: language
        href: http://publications.europa.eu/resource/authority/language/DEU
        show_as: de
      - name_attr: format
        href: https://fedlex.data.admin.ch/vocabulary/user-format/xml
        show_as: xml
  preface_ref:
    preface_paragraphs:
    - doc_number: '152.3 '
    - doc_title:
        inline_content:
        - element_type: TextRun
          text: Bundesgesetz
        - element_type: Br
        - element_type: TextRun
          text: über das Öffentlichkeitsprinzip der Verwaltung
  body:
    articles:
    - eId: art_1
      num:
        inline_content:
        - element_type: B
          inline_content:
          - element_type: TextRun
            text: Art. 1
      heading:
        inline_content:
        - element_type: TextRun
          text: Zweck und Gegenstand
      paragraphs:
      - eId: art_1/para
        content_ref:
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: >-
                Dieses Gesetz soll die Transparenz über den Auftrag, die Organisation
                und die Tätigkeit der Verwaltung fördern. Zu diesem Zweck trägt es
                zur Information der Öffentlichkeit bei, indem es den Zugang zu amtlichen
                Dokumenten gewährleistet.
    - eId: art_2
      num:
        inline_content:
        - element_type: B
          inline_content:
          - element_type: TextRun
            text: Art. 2
      heading:
        inline_content:
        - element_type: TextRun
          text: Persönlicher Geltungsbereich
      paragraphs:
      - eId: art_2/para_1
        num:
          inline_content:
          - element_type: TextRun
            text: '1'
        content_ref:
          block_lists:
          - eId: art_2/para_1/lst
            list_introduction:
              eId: art_2/para_1/listintro
              inline_content:
              - element_type: TextRun
                text: ' Dieses Gesetz gilt für:'
            items:
            - eId: art_2/para_1/lbl_a
              num:
                inline_content:
                - element_type: TextRun
                  text: 'a. '
              block_paragraphs:
              - inline_content:
                - element_type: TextRun
                  text: die Bundesverwaltung;
            - eId: art_2/para_1/lbl_b
              num:
                inline_content:
                - element_type: TextRun
                  text: 'b. '
              block_paragraphs:
              - inline_content:
                - element_type: TextRun
                  text: >-
                    Organisationen und Personen des öffentlichen oder privaten Rechts,
                    die nicht der Bundesverwaltung angehören, soweit sie Erlasse oder
                    erstinstanzliche Verfügungen im Sinne von Artikel 5 des Bundesgesetzes
                    vom 20. Dezember 1968 über das Verwaltungsverfahren erlassen;
  components_ref:
    component_list:
    - doc_ref:
        doc_name: annex
        preface_ref:
          containers:
          - container_name: headerOfAnnex
            blocks:
            - block_name: heading
              inline_content:
              - element_type: TextRun
                text: Anhang
        main_body:
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: (Art. 22)
          levels:
          - eId: annex_u1/lvl_u1
            heading:
              inline_content:
              - element_type: TextRun
                text: Änderung bisherigen Rechts
            content_ref:
              block_paragraphs:
              - inline_content:
                - element_type: TextRun
                  text: 'Die nachstehenden Gesetze werden wie folgt geändert:'
              - inline_content:
                - element_type: TextRun
                  text: …
                - element_type: AuthorialNote
                  block_paragraphs:
                  - inline_content:
                    - element_type: TextRun
                      text: Die Änderungen können unter
                    - element_type: Ref
                      href: https://fedlex.data.admin.ch/eli/oc/2006/355
                      inline_content:
                      - element_type: TextRun
                        text: AS
                      - element_type: B
                        inline_content:
                        - element_type: TextRun
                          text: '2006'
                      - element_type: TextRun
                        text: '2319'
                    - element_type: TextRun
                      text: konsultiert werden.

```






</div>

### Enum: ActTypeEnum []{#ActTypeEnum}




_Art des Erlasses, ausgedrückt im @name-Attribut von akn:act._



<div data-search-exclude markdown="1">

URI: [laws:ActTypeEnum](https://ld.ech.ch/schema/0296/laws/ActTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| publicLaw |  Ein Erlass des öffentlichen Rechts |
| privateAct |  Ein Erlass des Privatrechts |
| amendment |  Eine Änderung |
| constitution |  Eine Verfassung |







</div>

## Vorspann und Präambel



### Klasse: Preface []{#Preface}


_Der Vorspann des Erlasses (akn:preface) mit Dokumentnummer und -titel. Fedlex Schematron verlangt akn:docNumber (FLX-PF-001) und akn:docTitle (FLX-PF-002) innerhalb eines akn:p-Elements._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| preface_paragraphs | * <br/> [PrefaceP](#PrefaceP) | Die akn:p-Absätze des Vorspanns, die docNumber/docTitle umschliessen. |
| containers | * <br/> [Container](#Container) | Behälter des Vorspanns (akn:container). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](#Act) | preface_ref | range | [Preface](#Preface) |
| [Doc](#Doc) | preface_ref | range | [Preface](#Preface) |














#### Beispiele
##### Beispiel Preface: sr101 excerpt 1 1

```yaml
preface_ref:
  preface_paragraphs:
  - doc_number: '101'
  - doc_title:
      inline_content:
      - element_type: TextRun
        text: Bundesverfassung
      - element_type: Br
      - element_type: TextRun
        text: der Schweizerischen Eidgenossenschaft

```
##### Beispiel Preface: bgoe excerpt 1 1

```yaml
preface_ref:
  preface_paragraphs:
  - doc_number: '152.3 '
  - doc_title:
      inline_content:
      - element_type: TextRun
        text: Bundesgesetz
      - element_type: Br
      - element_type: TextRun
        text: über das Öffentlichkeitsprinzip der Verwaltung

```






</div>



### Klasse: PrefaceP []{#PrefaceP}


_Ein Vorspann-Absatz (akn:p), der Dokumentnummer und/oder -titel umschliesst. Fedlex verlangt akn:docNumber und akn:docTitle innerhalb eines akn:p des Vorspanns (FLX-PF-001/002)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| doc_number | 0..1 <br/> String | Dokumentnummer im Vorspann (akn:docNumber). Pflicht gemäss FLX-PF-001. Typischerweise die SR-Nummer, z.B. '101'.  |
| doc_title | 0..1 <br/> [MixedText](#MixedText) | Dokumenttitel im Vorspann (akn:docTitle). Pflicht gemäss FLX-PF-002. Kann Inline-Markup und akn:br für Zeilenumbrüche enthalten.  |
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |

###### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- doc_number
- doc_title
- inline_content










#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preface](#Preface) | preface_paragraphs | range | [PrefaceP](#PrefaceP) |














#### Beispiele
##### Beispiel PrefaceP: sr101 excerpt 1 1

```yaml
preface_paragraphs:
- doc_number: '101'

```
##### Beispiel PrefaceP: sr101 excerpt 1 2

```yaml
preface_paragraphs:
- doc_title:
    inline_content:
    - element_type: TextRun
      text: Bundesverfassung
    - element_type: Br
    - element_type: TextRun
      text: der Schweizerischen Eidgenossenschaft

```
##### Beispiel PrefaceP: bgoe excerpt 1 1

```yaml
preface_paragraphs:
- doc_number: '152.3 '

```
##### Beispiel PrefaceP: bgoe excerpt 1 2

```yaml
preface_paragraphs:
- doc_title:
    inline_content:
    - element_type: TextRun
      text: Bundesgesetz
    - element_type: Br
    - element_type: TextRun
      text: über das Öffentlichkeitsprinzip der Verwaltung

```






</div>



### Klasse: Preamble []{#Preamble}


_Die Präambel des Erlasses (akn:preamble) mit einleitenden Fliesstext-Absätzen vor dem Hauptteil._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_paragraphs | * <br/> [BlockParagraph](#BlockParagraph) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](#Act) | preamble_ref | range | [Preamble](#Preamble) |



















</div>

## Gesetzeshierarchie

Die Gliederung eines Erlasses ist rekursiv: Buch, Titel, Teil, Kapitel, Unterkapitel, Abschnitt und Unterabschnitt können ineinander verschachtelt werden, bis auf der untersten Ebene der Artikel steht. Welche Ebene in welcher vorkommen darf, ist nicht durch die Struktur selbst, sondern durch die Fedlex-Regeln bestimmt.

Eine Eigenheit ist `akn:level`: Seine erlaubten Kinder sind diejenigen des nächsten Vorfahren, der selbst kein `level` ist. Das lässt sich in einem XSD nicht ausdrücken und wird deshalb über Schematron geprüft (FLX-HR-001-lv).



### Klasse: ActBody []{#ActBody}


_Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie. Erlaubte direkte Kinder: book, title, part, chapter, subchapter, section, subsection, level, article, transitional, proviso. Keine anderen Elemente erlaubt (FLX-BD-001)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| books | * <br/> [Book](#Book) | Buch-Kindelemente (akn:book). |
| titles | * <br/> [Title](#Title) | Titel-Kindelemente (akn:title). |
| parts | * <br/> [Part](#Part) | Teil-Kindelemente (akn:part). |
| chapters | * <br/> [Chapter](#Chapter) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](#Subchapter) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](#Section) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |
| transitionals | * <br/> [Transitional](#Transitional) | Übergangsbestimmungs-Elemente (akn:transitional). |
| provisos | * <br/> [Proviso](#Proviso) | Vorbehalt-Elemente (akn:proviso). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](#Act) | body | range | [ActBody](#ActBody) |



















</div>



### Klasse: Book []{#Book}


_Buch-Ebene eines Erlasses (akn:book). Erlaubte Kinder: title, part, chapter, subchapter, section, subsection, level (FLX-HR-001-bk). Benötigt eindeutiges @eId (FLX-HR-002-bk)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| titles | * <br/> [Title](#Title) | Titel-Kindelemente (akn:title). |
| parts | * <br/> [Part](#Part) | Teil-Kindelemente (akn:part). |
| chapters | * <br/> [Chapter](#Chapter) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](#Subchapter) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](#Section) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | books | range | [Book](#Book) |
| [Title](#Title) | books | range | [Book](#Book) |
| [Level](#Level) | books | range | [Book](#Book) |



















</div>



### Klasse: Title []{#Title}


_Titel-Ebene eines Erlasses (akn:title). Erlaubte Kinder: book, part, chapter, subchapter, section, subsection, level (FLX-HR-001-ti). Benötigt eindeutiges @eId (FLX-HR-002-ti)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| books | * <br/> [Book](#Book) | Buch-Kindelemente (akn:book). |
| parts | * <br/> [Part](#Part) | Teil-Kindelemente (akn:part). |
| chapters | * <br/> [Chapter](#Chapter) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](#Subchapter) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](#Section) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | titles | range | [Title](#Title) |
| [Book](#Book) | titles | range | [Title](#Title) |
| [Level](#Level) | titles | range | [Title](#Title) |














#### Beispiele
##### Beispiel Title: Titel mit Nummer, Überschrift und Artikeln

```yaml
titles:
- eId: tit_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1. Titel: '
  heading:
    inline_content:
    - element_type: TextRun
      text: Allgemeine Bestimmungen
  articles:
  - eId: art_1
    num:
      inline_content:
      - element_type: B
        inline_content:
        - element_type: TextRun
          text: Art. 1
    heading:
      inline_content:
      - element_type: TextRun
        text: Schweizerische Eidgenossenschaft
    paragraphs:
    - eId: art_1/para
      content_ref:
        block_paragraphs:
        - inline_content:
          - element_type: TextRun
            text: >-
              Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz,
              Obwalden und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt
              und Basel-Landschaft, Schaffhausen, Appenzell Ausserrhoden und Appenzell
              Innerrhoden, St. Gallen, Graubünden, Aargau, Thurgau, Tessin, Waadt,
              Wallis, Neuenburg, Genf und Jura bilden die Schweizerische Eidgenossenschaft.

```






</div>



### Klasse: Part []{#Part}


_Teil-Ebene eines Erlasses (akn:part). Erlaubte Kinder: chapter, subchapter, section, subsection, level (FLX-HR-001-pt). Benötigt eindeutiges @eId (FLX-HR-002-pt)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| chapters | * <br/> [Chapter](#Chapter) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](#Subchapter) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](#Section) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | parts | range | [Part](#Part) |
| [Book](#Book) | parts | range | [Part](#Part) |
| [Title](#Title) | parts | range | [Part](#Part) |
| [Level](#Level) | parts | range | [Part](#Part) |



















</div>



### Klasse: Chapter []{#Chapter}


_Kapitel-Ebene eines Erlasses (akn:chapter). Erlaubte Kinder: subchapter, section, subsection, level, sowie direkt article (FLX-HR-001-ch). Benötigt eindeutiges @eId (FLX-HR-002-ch)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| subchapters | * <br/> [Subchapter](#Subchapter) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](#Section) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | chapters | range | [Chapter](#Chapter) |
| [Book](#Book) | chapters | range | [Chapter](#Chapter) |
| [Title](#Title) | chapters | range | [Chapter](#Chapter) |
| [Part](#Part) | chapters | range | [Chapter](#Chapter) |
| [Level](#Level) | chapters | range | [Chapter](#Chapter) |



















</div>



### Klasse: Subchapter []{#Subchapter}


_Unterkapitel-Ebene (akn:subchapter). Erlaubte Kinder: section, subsection, level, sowie direkt article (FLX-HR-001-sh). Benötigt eindeutiges @eId (FLX-HR-002-sh)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| sections | * <br/> [Section](#Section) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | subchapters | range | [Subchapter](#Subchapter) |
| [Book](#Book) | subchapters | range | [Subchapter](#Subchapter) |
| [Title](#Title) | subchapters | range | [Subchapter](#Subchapter) |
| [Part](#Part) | subchapters | range | [Subchapter](#Subchapter) |
| [Chapter](#Chapter) | subchapters | range | [Subchapter](#Subchapter) |
| [Level](#Level) | subchapters | range | [Subchapter](#Subchapter) |



















</div>



### Klasse: Section []{#Section}


_Abschnitt-Ebene (akn:section). Erlaubte Kinder: subsection, level, sowie direkt article (FLX-HR-001-sc). Benötigt eindeutiges @eId (FLX-HR-002-sc)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | sections | range | [Section](#Section) |
| [Book](#Book) | sections | range | [Section](#Section) |
| [Title](#Title) | sections | range | [Section](#Section) |
| [Part](#Part) | sections | range | [Section](#Section) |
| [Chapter](#Chapter) | sections | range | [Section](#Section) |
| [Subchapter](#Subchapter) | sections | range | [Section](#Section) |
| [Level](#Level) | sections | range | [Section](#Section) |



















</div>



### Klasse: Subsection []{#Subsection}


_Unterabschnitt-Ebene (akn:subsection). Erlaubte Kinder: level, sowie direkt article (FLX-HR-001-ss). Benötigt eindeutiges @eId (FLX-HR-002-ss)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | subsections | range | [Subsection](#Subsection) |
| [Book](#Book) | subsections | range | [Subsection](#Subsection) |
| [Title](#Title) | subsections | range | [Subsection](#Subsection) |
| [Part](#Part) | subsections | range | [Subsection](#Subsection) |
| [Chapter](#Chapter) | subsections | range | [Subsection](#Subsection) |
| [Subchapter](#Subchapter) | subsections | range | [Subsection](#Subsection) |
| [Section](#Section) | subsections | range | [Subsection](#Subsection) |
| [Level](#Level) | subsections | range | [Subsection](#Subsection) |



















</div>



### Klasse: Level []{#Level}


_Transparente Strukturebene (akn:level). Ein level ist 'transparent': erlaubte Kinder entsprechen denen des nächsten nicht-level-Vorfahren (FLX-HR-001-lv). Ein level mit akn:content ist nur erlaubt, wenn der Inhalt ein Änderungselement (akn:mod) enthält (FLX-HR-003). fedlex:role='marginal' kennzeichnet es als Randnote (FLX-XF-004). Benötigt eindeutiges @eId (FLX-HR-002-lv, FLX-HR-004)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| fedlex_role | 0..1 <br/> [FedlexRoleEnum](#FedlexRoleEnum) | Wenn gesetzt, muss der Wert 'marginal' sein (FLX-XF-004). Der Wert 'reference' ist bei level nicht erlaubt; er ist für subheading reserviert (FLX-XF-005).  |
| content_ref | 0..1 <br/> [Content](#Content) | Inhaltselement innerhalb eines Absatzes (akn:content). |
| books | * <br/> [Book](#Book) | Buch-Kindelemente (akn:book). |
| titles | * <br/> [Title](#Title) | Titel-Kindelemente (akn:title). |
| parts | * <br/> [Part](#Part) | Teil-Kindelemente (akn:part). |
| chapters | * <br/> [Chapter](#Chapter) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](#Subchapter) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](#Section) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](#Subsection) | Unterabschnitt-Kindelemente (akn:subsection). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | levels | range | [Level](#Level) |
| [Book](#Book) | levels | range | [Level](#Level) |
| [Title](#Title) | levels | range | [Level](#Level) |
| [Part](#Part) | levels | range | [Level](#Level) |
| [Chapter](#Chapter) | levels | range | [Level](#Level) |
| [Subchapter](#Subchapter) | levels | range | [Level](#Level) |
| [Section](#Section) | levels | range | [Level](#Level) |
| [Subsection](#Subsection) | levels | range | [Level](#Level) |
| [Transitional](#Transitional) | levels | range | [Level](#Level) |
| [Proviso](#Proviso) | levels | range | [Level](#Level) |
| [MainBody](#MainBody) | levels | range | [Level](#Level) |



















</div>

## Artikel und Absätze



### Klasse: Article []{#Article}


_Ein Artikel, die primäre legislative Einheit (akn:article). Constraints (FLX-ART-*): - akn:num ist obligatorisch (FLX-ART-001) - nur Überschriften-Elemente (num, heading, subheading) sowie akn:paragraph und akn:subdivision sind als Kinder erlaubt (FLX-ART-002) - benötigt eindeutiges @eId (FLX-ART-003)_




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 1 <br/> [MixedText](#MixedText) | Die Artikelnummer (z.B. 'Art. 1'). In jedem Artikel obligatorisch (FLX-ART-001). |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| paragraphs | * <br/> [Paragraph](#Paragraph) | Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts. |
| subdivisions | * <br/> [Subdivision](#Subdivision) | Unterabschnitt-Kindelemente (akn:subdivision) innerhalb eines Artikels. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | articles | range | [Article](#Article) |
| [Book](#Book) | articles | range | [Article](#Article) |
| [Title](#Title) | articles | range | [Article](#Article) |
| [Part](#Part) | articles | range | [Article](#Article) |
| [Chapter](#Chapter) | articles | range | [Article](#Article) |
| [Subchapter](#Subchapter) | articles | range | [Article](#Article) |
| [Section](#Section) | articles | range | [Article](#Article) |
| [Subsection](#Subsection) | articles | range | [Article](#Article) |
| [Level](#Level) | articles | range | [Article](#Article) |
| [Transitional](#Transitional) | articles | range | [Article](#Article) |
| [Proviso](#Proviso) | articles | range | [Article](#Article) |














#### Beispiele
##### Beispiel Article: Artikel mit fett ausgezeichneter Nummer

```yaml
articles:
- eId: art_1
  num:
    inline_content:
    - element_type: B
      inline_content:
      - element_type: TextRun
        text: Art. 1
  heading:
    inline_content:
    - element_type: TextRun
      text: Schweizerische Eidgenossenschaft
  paragraphs:
  - eId: art_1/para
    content_ref:
      block_paragraphs:
      - inline_content:
        - element_type: TextRun
          text: >-
            Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz, Obwalden
            und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt und Basel-Landschaft,
            Schaffhausen, Appenzell Ausserrhoden und Appenzell Innerrhoden, St. Gallen,
            Graubünden, Aargau, Thurgau, Tessin, Waadt, Wallis, Neuenburg, Genf und
            Jura bilden die Schweizerische Eidgenossenschaft.

```
##### Beispiel Article: Article with numbered paragraphs

```yaml
articles:
- eId: art_2
  num:
    inline_content:
    - element_type: B
      inline_content:
      - element_type: TextRun
        text: Art. 2
  heading:
    inline_content:
    - element_type: TextRun
      text: Persönlicher Geltungsbereich
  paragraphs:
  - eId: art_2/para_1
    num:
      inline_content:
      - element_type: TextRun
        text: '1'
    content_ref:
      block_lists:
      - eId: art_2/para_1/lst
        list_introduction:
          eId: art_2/para_1/listintro
          inline_content:
          - element_type: TextRun
            text: ' Dieses Gesetz gilt für:'
        items:
        - eId: art_2/para_1/lbl_a
          num:
            inline_content:
            - element_type: TextRun
              text: 'a. '
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: die Bundesverwaltung;
        - eId: art_2/para_1/lbl_b
          num:
            inline_content:
            - element_type: TextRun
              text: 'b. '
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: >-
                Organisationen und Personen des öffentlichen oder privaten Rechts,
                die nicht der Bundesverwaltung angehören, soweit sie Erlasse oder
                erstinstanzliche Verfügungen im Sinne von Artikel 5 des Bundesgesetzes
                vom 20. Dezember 1968 über das Verwaltungsverfahren erlassen;

```






</div>



### Klasse: Subdivision []{#Subdivision}


_Ein Unterabschnitt in einem Artikel, der zusammengehörige Absätze gruppiert (akn:subdivision). Constraints (FLX-SD-*): - nur Überschriften-Elemente und akn:paragraph als Kinder erlaubt (FLX-SD-001) - nur als direktes Kind von akn:article erlaubt, keine Verschachtelung (FLX-SD-002) - benötigt eindeutiges @eId (FLX-SD-003)_




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](#MixedText) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| paragraphs | * <br/> [Paragraph](#Paragraph) | Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Article](#Article) | subdivisions | range | [Subdivision](#Subdivision) |



















</div>



### Klasse: Paragraph []{#Paragraph}


_Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph). Constraints (FLX-PR-*): - nur Überschriften-Elemente und akn:content als Kinder erlaubt (FLX-PR-001) - nur als direktes Kind von akn:article oder akn:subdivision erlaubt (FLX-PR-002) - benötigt eindeutiges @eId (FLX-PR-003)_




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| content_ref | 0..1 <br/> [Content](#Content) | Inhaltselement innerhalb eines Absatzes (akn:content). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Article](#Article) | paragraphs | range | [Paragraph](#Paragraph) |
| [Subdivision](#Subdivision) | paragraphs | range | [Paragraph](#Paragraph) |
| [Transitional](#Transitional) | paragraphs | range | [Paragraph](#Paragraph) |
| [Proviso](#Proviso) | paragraphs | range | [Paragraph](#Paragraph) |














#### Beispiele
##### Beispiel Paragraph: Absatz mit Aufzählung statt Fliesstext

```yaml
paragraphs:
- eId: art_2/para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    block_lists:
    - eId: art_2/para_1/lst
      list_introduction:
        eId: art_2/para_1/listintro
        inline_content:
        - element_type: TextRun
          text: ' Dieses Gesetz gilt für:'
      items:
      - eId: art_2/para_1/lbl_a
        num:
          inline_content:
          - element_type: TextRun
            text: 'a. '
        block_paragraphs:
        - inline_content:
          - element_type: TextRun
            text: die Bundesverwaltung;
      - eId: art_2/para_1/lbl_b
        num:
          inline_content:
          - element_type: TextRun
            text: 'b. '
        block_paragraphs:
        - inline_content:
          - element_type: TextRun
            text: >-
              Organisationen und Personen des öffentlichen oder privaten Rechts, die
              nicht der Bundesverwaltung angehören, soweit sie Erlasse oder erstinstanzliche
              Verfügungen im Sinne von Artikel 5 des Bundesgesetzes vom 20. Dezember
              1968 über das Verwaltungsverfahren erlassen;

```
##### Beispiel Paragraph: Paragraph with running text

```yaml
paragraphs:
- eId: art_1/para
  content_ref:
    block_paragraphs:
    - inline_content:
      - element_type: TextRun
        text: >-
          Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz, Obwalden
          und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt und Basel-Landschaft,
          Schaffhausen, Appenzell Ausserrhoden und Appenzell Innerrhoden, St. Gallen,
          Graubünden, Aargau, Thurgau, Tessin, Waadt, Wallis, Neuenburg, Genf und
          Jura bilden die Schweizerische Eidgenossenschaft.

```






</div>



### Klasse: Transitional []{#Transitional}


_Eine Übergangsbestimmung im Hauptteil eines Erlasses (akn:transitional). Als Hauptteil-Element auf oberster Ebene erlaubt (FLX-BD-001). Struktur wie Artikel._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |
| paragraphs | * <br/> [Paragraph](#Paragraph) | Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | transitionals | range | [Transitional](#Transitional) |



















</div>



### Klasse: Proviso []{#Proviso}


_Ein Vorbehalt im Hauptteil eines Erlasses (akn:proviso). Als Hauptteil-Element auf oberster Ebene erlaubt (FLX-BD-001). Erscheint typischerweise nach den Hauptartikeln._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](#MixedText) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](#Article) | Artikel-Kindelemente (akn:article). |
| paragraphs | * <br/> [Paragraph](#Paragraph) | Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](#ActBody) | provisos | range | [Proviso](#Proviso) |



















</div>

## Blockinhalte

Auf der untersten Ebene stehen die Inhaltsblöcke: Absätze, Listen und Tabellen.



### Klasse: Content []{#Content}


_Der Inhalt eines Absatzes (akn:content). Enthält Block-Elemente: akn:p (Fliesstext), akn:blockList (Aufzählungen), akn:table. Wenn in einem akn:level, muss ein akn:mod-Element enthalten sein (FLX-HR-003)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_paragraphs | * <br/> [BlockParagraph](#BlockParagraph) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| block_lists | * <br/> [BlockList](#BlockList) | Auflistungs-Elemente (akn:blockList) innerhalb von Content. |
| tables | * <br/> [Table](#Table) | Tabellen-Elemente (akn:table) innerhalb von Content. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Level](#Level) | content_ref | range | [Content](#Content) |
| [Paragraph](#Paragraph) | content_ref | range | [Content](#Content) |
| [MainBody](#MainBody) | content_ref | range | [Content](#Content) |














#### Beispiele
##### Beispiel Content: bgoe excerpt 1 1

```yaml
content_ref:
  block_lists:
  - eId: art_2/para_1/lst
    list_introduction:
      eId: art_2/para_1/listintro
      inline_content:
      - element_type: TextRun
        text: ' Dieses Gesetz gilt für:'
    items:
    - eId: art_2/para_1/lbl_a
      num:
        inline_content:
        - element_type: TextRun
          text: 'a. '
      block_paragraphs:
      - inline_content:
        - element_type: TextRun
          text: die Bundesverwaltung;
    - eId: art_2/para_1/lbl_b
      num:
        inline_content:
        - element_type: TextRun
          text: 'b. '
      block_paragraphs:
      - inline_content:
        - element_type: TextRun
          text: >-
            Organisationen und Personen des öffentlichen oder privaten Rechts, die
            nicht der Bundesverwaltung angehören, soweit sie Erlasse oder erstinstanzliche
            Verfügungen im Sinne von Artikel 5 des Bundesgesetzes vom 20. Dezember
            1968 über das Verwaltungsverfahren erlassen;

```
##### Beispiel Content: sr101 excerpt 1 1

```yaml
content_ref:
  block_paragraphs:
  - inline_content:
    - element_type: TextRun
      text: >-
        Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz, Obwalden
        und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt und Basel-Landschaft,
        Schaffhausen, Appenzell Ausserrhoden und Appenzell Innerrhoden, St. Gallen,
        Graubünden, Aargau, Thurgau, Tessin, Waadt, Wallis, Neuenburg, Genf und Jura
        bilden die Schweizerische Eidgenossenschaft.

```






</div>



### Klasse: BlockParagraph []{#BlockParagraph}


_Ein Fliesstext-Absatz in Content (akn:p). Kann gemischten Inhalt mit Inline-Markup enthalten (XmlContent-Typ). Hinweis: akn:br ist hier nicht erlaubt, nur in Überschriften (FLX-TXT-001)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preamble](#Preamble) | block_paragraphs | range | [BlockParagraph](#BlockParagraph) |
| [Content](#Content) | block_paragraphs | range | [BlockParagraph](#BlockParagraph) |
| [BlockListItem](#BlockListItem) | block_paragraphs | range | [BlockParagraph](#BlockParagraph) |
| [TableCell](#TableCell) | block_paragraphs | range | [BlockParagraph](#BlockParagraph) |
| [AuthorialNote](#AuthorialNote) | block_paragraphs | range | [BlockParagraph](#BlockParagraph) |
| [MainBody](#MainBody) | block_paragraphs | range | [BlockParagraph](#BlockParagraph) |














#### Beispiele
##### Beispiel BlockParagraph: bgoe excerpt 1 1

```yaml
block_paragraphs:
- inline_content:
  - element_type: TextRun
    text: >-
      Dieses Gesetz soll die Transparenz über den Auftrag, die Organisation und die
      Tätigkeit der Verwaltung fördern. Zu diesem Zweck trägt es zur Information der
      Öffentlichkeit bei, indem es den Zugang zu amtlichen Dokumenten gewährleistet.

```
##### Beispiel BlockParagraph: sr101 excerpt 1 1

```yaml
block_paragraphs:
- inline_content:
  - element_type: TextRun
    text: >-
      Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz, Obwalden
      und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt und Basel-Landschaft,
      Schaffhausen, Appenzell Ausserrhoden und Appenzell Innerrhoden, St. Gallen,
      Graubünden, Aargau, Thurgau, Tessin, Waadt, Wallis, Neuenburg, Genf und Jura
      bilden die Schweizerische Eidgenossenschaft.

```






</div>



### Klasse: BlockList []{#BlockList}


_Eine Auflistung von nummerierten oder buchstabierten Punkten (akn:blockList), optional eingeleitet durch ein akn:listIntroduction-Element._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| list_introduction | 0..1 <br/> [MixedText](#MixedText) | Optionaler Einleitungstext vor einer Auflistung (akn:listIntroduction). |
| items | * <br/> [BlockListItem](#BlockListItem) | Punkte einer Auflistung (akn:item). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Content](#Content) | block_lists | range | [BlockList](#BlockList) |
| [BlockListItem](#BlockListItem) | block_lists | range | [BlockList](#BlockList) |
| [TableCell](#TableCell) | block_lists | range | [BlockList](#BlockList) |



















</div>



### Klasse: BlockListItem []{#BlockListItem}


_Ein einzelner Punkt in einer Auflistung (akn:item). Trägt ein num-Label und Block-Inhalt direkt: Fliesstext-Absätze (akn:p) und optional verschachtelte Listen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](#MixedText) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| block_paragraphs | * <br/> [BlockParagraph](#BlockParagraph) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| block_lists | * <br/> [BlockList](#BlockList) | Auflistungs-Elemente (akn:blockList) innerhalb von Content. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [BlockList](#BlockList) | items | range | [BlockListItem](#BlockListItem) |



















</div>



### Klasse: Table []{#Table}


_Ein Tabellen-Element innerhalb von Content (akn:table). Enthält Zeilen (akn:tr) mit Zellen (akn:td). Entspricht dem HTML-Tabellenmodell._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| border | 0..1 <br/> String | Das @border-Attribut auf akn:table (HTML-artige Darstellung). |
| table_rows | * <br/> [TableRow](#TableRow) | Zeilen in einer Tabelle (akn:tr). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Content](#Content) | tables | range | [Table](#Table) |



















</div>



### Klasse: TableRow []{#TableRow}


_Eine Zeile in einer AkomaNtoso-Tabelle (akn:tr)._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| table_cells | * <br/> [TableCell](#TableCell) | Zellen in einer Tabellenzeile (akn:td). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Table](#Table) | table_rows | range | [TableRow](#TableRow) |



















</div>



### Klasse: TableCell []{#TableCell}


_Eine Zelle in einer Tabellenzeile (akn:td). Enthält Block-Inhalt: Fliesstext-Absätze (akn:p) und Auflistungen (akn:blockList)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| colspan | 0..1 <br/> String | Das @colspan-Attribut auf akn:td (HTML-artige Darstellung). |
| block_paragraphs | * <br/> [BlockParagraph](#BlockParagraph) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| block_lists | * <br/> [BlockList](#BlockList) | Auflistungs-Elemente (akn:blockList) innerhalb von Content. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [TableRow](#TableRow) | table_cells | range | [TableCell](#TableCell) |



















</div>

## Anhänge

Ein Erlass kann Dokumente mitführen, die nicht Teil seines Artikeltextes sind — im Bundesrecht regelmässig einen Anhang. Solche Dokumente stehen in `akn:components` und sind je ein eigenes `akn:doc` mit eigenem Vorspann und eigenem Hauptteil. Beim Öffentlichkeitsgesetz enthält der Anhang die Änderung bisherigen Rechts, beim Datenschutzgesetz ebenso.

Zwei Eigenheiten sind dabei festzuhalten. Erstens wiederholt der Anhang in den Fedlex-Dateien die Identifikation des Erlasses unverändert — dieselben ELI-URIs, dieselben Daten und Namen. Er ist also nicht eigenständig identifiziert, sondern Teil desselben Werks. Zweitens nutzt sein Vorspann nicht die Absatzstruktur des Erlasses, sondern die generischen Behälter `akn:container` und `akn:block`. Deren `@name` ist in AKN frei wählbar; dieser Standard führt die Werte, die Fedlex tatsächlich verwendet, als Aufzählung: `headerOfAnnex` für den Behälter, `heading` und `num` für den Block.

Der Hauptteil eines Anhangs (`akn:mainBody`) kennt die Gesetzeshierarchie nicht. Er nimmt Absätze und Ebenen unmittelbar auf — und darin wieder dieselben Inhalts- und Auszeichnungselemente wie der Erlass selbst, bis hin zur Fussnote mit Verweis auf die Amtliche Sammlung.



### Klasse: Components []{#Components}


_Behälter für die Dokumente, die einem Erlass beiliegen (akn:components) — etwa seinen Anhang._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| component_list | * <br/> [Component](#Component) | Die beiliegenden Dokumente (akn:component). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](#Act) | components_ref | range | [Components](#Components) |



















</div>



### Klasse: Component []{#Component}


_Ein einzelnes beiliegendes Dokument (akn:component)._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| doc_ref | 0..1 <br/> [Doc](#Doc) | Das beiliegende Dokument selbst (akn:doc). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Components](#Components) | component_list | range | [Component](#Component) |



















</div>



### Klasse: Doc []{#Doc}


_Ein beiliegendes Dokument (akn:doc). Das @name-Attribut nennt die Art; Fedlex verwendet 'annex'. Es führt einen eigenen Identifikationsblock, der in den Fedlex-Dateien die URIs des zugehörigen Erlasses wiederholt._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| doc_name | 0..1 <br/> [DocNameEnum](#DocNameEnum) | Art des beiliegenden Dokuments (akn:doc/@name). |
| meta | 0..1 <br/> [ActMeta](#ActMeta) | Metadaten-Abschnitt des Erlasses (akn:meta). |
| preface_ref | 0..1 <br/> [Preface](#Preface) | Vorspann des Erlasses (akn:preface). |
| main_body | 0..1 <br/> [MainBody](#MainBody) | Hauptteil des beiliegenden Dokuments (akn:mainBody). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Component](#Component) | doc_ref | range | [Doc](#Doc) |



















</div>

### Enum: DocNameEnum []{#DocNameEnum}




_Arten beiliegender Dokumente, die Fedlex in akn:doc/@name verwendet._



<div data-search-exclude markdown="1">

URI: [laws:DocNameEnum](https://ld.ech.ch/schema/0296/laws/DocNameEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| annex |  Ein Anhang zum Erlass. |







</div>



### Klasse: MainBody []{#MainBody}


_Hauptteil eines beiliegenden Dokuments (akn:mainBody). Anders als der Erlasskörper nimmt er Absätze und Ebenen unmittelbar auf, ohne die Gesetzeshierarchie._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_paragraphs | * <br/> [BlockParagraph](#BlockParagraph) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| levels | * <br/> [Level](#Level) | Transparente Level-Kindelemente (akn:level). |
| content_ref | 0..1 <br/> [Content](#Content) | Inhaltselement innerhalb eines Absatzes (akn:content). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Doc](#Doc) | main_body | range | [MainBody](#MainBody) |



















</div>



### Klasse: Container []{#Container}


_Ein generischer Behälter (akn:container), dessen @name den Zweck nennt._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| container_name | 0..1 <br/> [ContainerNameEnum](#ContainerNameEnum) | Zweck des Behälters (akn:container/@name). |
| blocks | * <br/> [Block](#Block) | Blöcke innerhalb des Behälters (akn:block). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preface](#Preface) | containers | range | [Container](#Container) |














#### Beispiele
##### Beispiel Container: sr101 excerpt

```yaml
# Auszug aus SR 101, Bundesverfassung der Schweizerischen Eidgenossenschaft,
# Fassung vom 3. März 2024. Werte übernommen aus der Fedlex-Datei
# misc/spec/input/examples/federal/SR-101-03032024-DE.xml -- gekürzt auf den
# vollständigen Metadatenblock, den Vorspann und den ersten Artikel, damit die
# Beispiele im Dokument lesbar bleiben.
act_ref:
  act_name: constitution

  meta:
    identification_ref:
      # Der Anker zeigt auf die Organisation, die in references deklariert ist.
      source: "#ch.bk"

      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
        # Drei Datumsangaben desselben Werks, unterschieden über @name aus dem
        # Fedlex/JoLux-Vokabular: Inkrafttreten, Erlassdatum, Nachführungsstand.
        frbr_dates:
          - date_value: "2000-01-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "1999-04-18"
            frbr_date_name: jolux:dateDocument
          - date_value: "2024-03-03"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
          - href: "#ch.bk"
            as_role: "#rightsHolder"
        frbr_country:
          value: CH
        frbr_number:
          value: "101"
        # Die SR-Nummer wird nicht übersetzt, der Titel schon: je Sprache ein
        # Eintrag mit Kurzform.
        frbr_names:
          - xml_lang: de
            value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April 1999
            short_form: BV
          - xml_lang: fr
            value: Constitution fédérale de la Confédération suisse du 18 avril 1999
            short_form: Cst.
          - xml_lang: it
            value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
            short_form: Cost.
          - xml_lang: rm
            value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
            short_form: Cst.
        frbr_authoritative:
          value: "true"

      # Die Expression ist die sprachliche Fassung: dieselbe URI mit Sprachanteil.
      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
        frbr_dates:
          - date_value: "2000-01-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "1999-04-18"
            frbr_date_name: jolux:dateDocument
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        frbr_language:
          language_value: de

      # Die Manifestation ist die konkrete Datei -- hier das XML.
      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
        frbr_dates:
          - date_value: "2024-03-03"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        frbr_format:
          value: xml

    # Stellen und Rollen stehen einmal hier; die Elemente oben verweisen mit
    # dokumentinternen Ankern darauf.
    references_ref:
      source: "#ch.bk"
      tlc_organizations:
        - eId: ch.bk
          href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
          show_as: Bundeskanzlei
      tlc_roles:
        - eId: publisher
          href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
          show_as: Editeur
        - eId: rightsHolder
          href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
          show_as: Détenteur des droits

  preface_ref:
    preface_paragraphs:
      - doc_number: "101"
      - doc_title:
          inline_content:
            - element_type: TextRun
              text: Bundesverfassung
            - element_type: Br
            - element_type: TextRun
              text: der Schweizerischen Eidgenossenschaft

  body:
    titles:
      - eId: tit_1
        num:
          inline_content:
            - element_type: TextRun
              text: "1. Titel: "
        heading:
          inline_content:
            - element_type: TextRun
              text: Allgemeine Bestimmungen
        articles:
          - eId: art_1
            # Die Artikelnummer ist im Original fett ausgezeichnet: ein B-Element
            # mit einem Textlauf darin, nicht eine Zeichenkette "Art. 1".
            num:
              inline_content:
                - element_type: B
                  inline_content:
                    - element_type: TextRun
                      text: Art. 1
            heading:
              inline_content:
                - element_type: TextRun
                  text: Schweizerische Eidgenossenschaft
            paragraphs:
              - eId: art_1/para
                content_ref:
                  block_paragraphs:
                    - inline_content:
                        - element_type: TextRun
                          text: >-
                            Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz,
                            Obwalden und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt
                            und Basel-Landschaft, Schaffhausen, Appenzell Ausserrhoden und
                            Appenzell Innerrhoden, St. Gallen, Graubünden, Aargau, Thurgau,
                            Tessin, Waadt, Wallis, Neuenburg, Genf und Jura bilden die
                            Schweizerische Eidgenossenschaft.

```
##### Beispiel Container: bgoe excerpt

```yaml
# Auszug aus SR 152.3, Bundesgesetz über das Öffentlichkeitsprinzip der
# Verwaltung (Öffentlichkeitsgesetz, BGÖ), Fassung vom 1. November 2023.
# Werte übernommen aus der Fedlex-Auslieferung
# https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
#
# Zweites Beispiel neben der Bundesverfassung: ein gewöhnliches Bundesgesetz
# (act_name: publicLaw statt constitution), mit Aufzählung im Absatz und den
# Referenzeinträgen für Sprache und Format, welche die Verfassungsdatei nicht
# führt.
act_ref:
  act_name: publicLaw

  meta:
    identification_ref:
      source: "#ch.bk"

      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
        frbr_dates:
          - date_value: "2006-07-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "2004-12-17"
            frbr_date_name: jolux:dateDocument
          - date_value: "2023-11-01"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
          - href: "#ch.bk"
            as_role: "#rightsHolder"
        frbr_country:
          value: CH
        # Anders als die Verfassung trägt das Gesetz eine gegliederte SR-Nummer.
        frbr_number:
          value: "152.3"
        frbr_names:
          - xml_lang: de
            value: Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung (Öffentlichkeitsgesetz, BGÖ)
            short_form: BGÖ
          - xml_lang: fr
            value: Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans l'administration (Loi sur la transparence, LTrans)
            short_form: LTrans
          - xml_lang: it
            value: Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione (Legge sulla trasparenza, LTras)
            short_form: LTras
          - xml_lang: rm
            value: Lescha federala dals 17 da december 2004 davart il princip da la transparenza da l'administraziun (Lescha da transparenza, LTrans)
            short_form: LTrans
          - xml_lang: en
            value: Federal Act of 17 December 2004 on Freedom of Information in the Administration (Freedom of Information Act, FoIA)
            short_form: FoIA
        frbr_authoritative:
          value: "true"

      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
        frbr_dates:
          - date_value: "2006-07-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "2023-11-01"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        frbr_language:
          language_value: de

      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
        frbr_dates:
          - date_value: "2023-11-01"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        # Fedlex vermerkt am Format zusätzlich, welche Werkzeugversion die Datei
        # erzeugt hat -- ein Attribut aus dem Fedlex-Namensraum.
        frbr_format:
          value: xml
          fedlex_generator: 2024-q4-rel-1.6.5

    references_ref:
      source: "#ch.bk"
      tlc_organizations:
        - eId: ch.bk
          href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
          show_as: Bundeskanzlei
      tlc_roles:
        - eId: publisher
          href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
          show_as: Editeur
        - eId: rightsHolder
          href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
          show_as: Détenteur des droits
      # Sprache und Format zeigen auf kontrollierte Vokabulare: das der EU für
      # die Sprache, das von Fedlex für das Dateiformat.
      tlc_references:
        - name_attr: language
          href: http://publications.europa.eu/resource/authority/language/DEU
          show_as: de
        - name_attr: format
          href: https://fedlex.data.admin.ch/vocabulary/user-format/xml
          show_as: xml

  preface_ref:
    preface_paragraphs:
      - doc_number: "152.3 "
      - doc_title:
          inline_content:
            - element_type: TextRun
              text: Bundesgesetz
            - element_type: Br
            - element_type: TextRun
              text: über das Öffentlichkeitsprinzip der Verwaltung

  body:
    articles:
      - eId: art_1
        num:
          inline_content:
            - element_type: B
              inline_content:
                - element_type: TextRun
                  text: Art. 1
        heading:
          inline_content:
            - element_type: TextRun
              text: Zweck und Gegenstand
        paragraphs:
          # Ein einziger Absatz bleibt unnummeriert; die eId endet auf "para".
          - eId: art_1/para
            content_ref:
              block_paragraphs:
                - inline_content:
                    - element_type: TextRun
                      text: >-
                        Dieses Gesetz soll die Transparenz über den Auftrag, die Organisation und
                        die Tätigkeit der Verwaltung fördern. Zu diesem Zweck trägt es zur
                        Information der Öffentlichkeit bei, indem es den Zugang zu amtlichen
                        Dokumenten gewährleistet.

      - eId: art_2
        num:
          inline_content:
            - element_type: B
              inline_content:
                - element_type: TextRun
                  text: Art. 2
        heading:
          inline_content:
            - element_type: TextRun
              text: Persönlicher Geltungsbereich
        paragraphs:
          # Mehrere Absätze werden nummeriert, und der Absatz führt statt eines
          # Fliesstextes eine Aufzählung mit Einleitungssatz.
          - eId: art_2/para_1
            num:
              inline_content:
                - element_type: TextRun
                  text: "1"
            content_ref:
              block_lists:
                - eId: art_2/para_1/lst
                  list_introduction:
                    eId: art_2/para_1/listintro
                    inline_content:
                      - element_type: TextRun
                        text: " Dieses Gesetz gilt für:"
                  items:
                    - eId: art_2/para_1/lbl_a
                      num:
                        inline_content:
                          - element_type: TextRun
                            text: "a. "
                      block_paragraphs:
                        - inline_content:
                            - element_type: TextRun
                              text: die Bundesverwaltung;
                    - eId: art_2/para_1/lbl_b
                      num:
                        inline_content:
                          - element_type: TextRun
                            text: "b. "
                      block_paragraphs:
                        - inline_content:
                            - element_type: TextRun
                              text: >-
                                Organisationen und Personen des öffentlichen oder privaten Rechts,
                                die nicht der Bundesverwaltung angehören, soweit sie Erlasse oder
                                erstinstanzliche Verfügungen im Sinne von Artikel 5 des
                                Bundesgesetzes vom 20. Dezember 1968 über das
                                Verwaltungsverfahren erlassen;

  # Der Anhang des Erlasses: ein eigenes Dokument mit eigenem Vorspann und
  # Hauptteil. Sein Identifikationsblock, der in der Fedlex-Datei die URIs des
  # Erlasses unveraendert wiederholt, ist hier weggelassen.
  components_ref:
    component_list:
    - doc_ref:
        doc_name: annex
        preface_ref:
          containers:
          - container_name: headerOfAnnex
            blocks:
            - block_name: heading
              inline_content:
              - element_type: TextRun
                text: Anhang
        main_body:
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: (Art. 22)
          levels:
          - eId: annex_u1/lvl_u1
            heading:
              inline_content:
              - element_type: TextRun
                text: Änderung bisherigen Rechts
            content_ref:
              block_paragraphs:
              - inline_content:
                - element_type: TextRun
                  text: 'Die nachstehenden Gesetze werden wie folgt geändert:'
              - inline_content:
                - element_type: TextRun
                  text: …
                - element_type: AuthorialNote
                  block_paragraphs:
                  - inline_content:
                    - element_type: TextRun
                      text: Die Änderungen können unter
                    - element_type: Ref
                      href: https://fedlex.data.admin.ch/eli/oc/2006/355
                      inline_content:
                      - element_type: TextRun
                        text: AS
                      - element_type: B
                        inline_content:
                        - element_type: TextRun
                          text: '2006'
                      - element_type: TextRun
                        text: '2319'
                    - element_type: TextRun
                      text: konsultiert werden.

```






</div>

### Enum: ContainerNameEnum []{#ContainerNameEnum}




_Zwecke, die Fedlex in akn:container/@name verwendet._



<div data-search-exclude markdown="1">

URI: [laws:ContainerNameEnum](https://ld.ech.ch/schema/0296/laws/ContainerNameEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| headerOfAnnex |  Kopfbereich eines Anhangs. |







</div>



### Klasse: Block []{#Block}


_Ein generischer Block (akn:block), dessen @name den Zweck nennt; trägt gemischten Inhalt._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_name | 0..1 <br/> [BlockNameEnum](#BlockNameEnum) | Zweck des Blocks (akn:block/@name). |
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | blocks | range | [Block](#Block) |



















</div>

### Enum: BlockNameEnum []{#BlockNameEnum}




_Zwecke, die Fedlex in akn:block/@name verwendet._



<div data-search-exclude markdown="1">

URI: [laws:BlockNameEnum](https://ld.ech.ch/schema/0296/laws/BlockNameEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| heading |  Die Überschrift des umgebenden Behälters. |
| num |  Die Nummer des umgebenden Behälters. |







</div>

\newpage

# Textauszeichnung

Innerhalb eines Absatzes, einer Überschrift, einer Nummer oder einer Tabellenzelle steht Text nicht für sich: Er ist mit Verweisen, Hervorhebungen, Fussnoten und Platzhaltern durchsetzt, und zwar in der Reihenfolge, in der er gelesen wird. Dieser gemischte Inhalt wird nicht als undurchsichtige Zeichenkette abgelegt, sondern als geordnete Liste eigener Klassen. Ein Textstück und ein Auszeichnungselement sind dabei gleichrangige Geschwister — dafür steht `TextRun`, der einen reinen Zeichenlauf trägt.

Diese Modellierung ist aufwendiger als ein einzelnes Textfeld, aber sie ist die Voraussetzung dafür, dass ein Verweis auf einen anderen Erlass maschinell auffindbar bleibt und eine Fussnote ihren eigenen Inhalt behält, statt im Fliesstext aufzugehen.



### Klasse: MixedText []{#MixedText}


_Wiederverwendbarer Halter für gemischten Inhalt: eine geordnete Folge aus Text und Inline-Markup. Range für num, heading, subheading, listIntroduction, docTitle; der umschliessende Elementname kommt vom referenzierenden Slot._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [PrefaceP](#PrefaceP) | doc_title | range | [MixedText](#MixedText) |
| [Book](#Book) | num | range | [MixedText](#MixedText) |
| [Book](#Book) | heading | range | [MixedText](#MixedText) |
| [Book](#Book) | subheading | range | [MixedText](#MixedText) |
| [Title](#Title) | num | range | [MixedText](#MixedText) |
| [Title](#Title) | heading | range | [MixedText](#MixedText) |
| [Title](#Title) | subheading | range | [MixedText](#MixedText) |
| [Part](#Part) | num | range | [MixedText](#MixedText) |
| [Part](#Part) | heading | range | [MixedText](#MixedText) |
| [Part](#Part) | subheading | range | [MixedText](#MixedText) |
| [Chapter](#Chapter) | num | range | [MixedText](#MixedText) |
| [Chapter](#Chapter) | heading | range | [MixedText](#MixedText) |
| [Chapter](#Chapter) | subheading | range | [MixedText](#MixedText) |
| [Subchapter](#Subchapter) | num | range | [MixedText](#MixedText) |
| [Subchapter](#Subchapter) | heading | range | [MixedText](#MixedText) |
| [Subchapter](#Subchapter) | subheading | range | [MixedText](#MixedText) |
| [Section](#Section) | num | range | [MixedText](#MixedText) |
| [Section](#Section) | heading | range | [MixedText](#MixedText) |
| [Section](#Section) | subheading | range | [MixedText](#MixedText) |
| [Subsection](#Subsection) | num | range | [MixedText](#MixedText) |
| [Subsection](#Subsection) | heading | range | [MixedText](#MixedText) |
| [Subsection](#Subsection) | subheading | range | [MixedText](#MixedText) |
| [Level](#Level) | num | range | [MixedText](#MixedText) |
| [Level](#Level) | heading | range | [MixedText](#MixedText) |
| [Level](#Level) | subheading | range | [MixedText](#MixedText) |
| [Article](#Article) | num | range | [MixedText](#MixedText) |
| [Article](#Article) | heading | range | [MixedText](#MixedText) |
| [Article](#Article) | subheading | range | [MixedText](#MixedText) |
| [Subdivision](#Subdivision) | num | range | [MixedText](#MixedText) |
| [Subdivision](#Subdivision) | heading | range | [MixedText](#MixedText) |
| [Subdivision](#Subdivision) | subheading | range | [MixedText](#MixedText) |
| [Paragraph](#Paragraph) | num | range | [MixedText](#MixedText) |
| [Paragraph](#Paragraph) | heading | range | [MixedText](#MixedText) |
| [Transitional](#Transitional) | num | range | [MixedText](#MixedText) |
| [Transitional](#Transitional) | heading | range | [MixedText](#MixedText) |
| [Proviso](#Proviso) | num | range | [MixedText](#MixedText) |
| [Proviso](#Proviso) | heading | range | [MixedText](#MixedText) |
| [BlockList](#BlockList) | list_introduction | range | [MixedText](#MixedText) |
| [BlockListItem](#BlockListItem) | num | range | [MixedText](#MixedText) |



















</div>



### Klasse: InlineElement []{#InlineElement}


_Abstrakte Basis für ein modelliertes Inline-Markup-Element in gemischtem Inhalt._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [PrefaceP](#PrefaceP) | inline_content | range | [InlineElement](#InlineElement) |
| [BlockParagraph](#BlockParagraph) | inline_content | range | [InlineElement](#InlineElement) |
| [MixedText](#MixedText) | inline_content | range | [InlineElement](#InlineElement) |
| [Ref](#Ref) | inline_content | range | [InlineElement](#InlineElement) |
| [B](#B) | inline_content | range | [InlineElement](#InlineElement) |
| [I](#I) | inline_content | range | [InlineElement](#InlineElement) |
| [Sup](#Sup) | inline_content | range | [InlineElement](#InlineElement) |
| [Span](#Span) | inline_content | range | [InlineElement](#InlineElement) |
| [Inline](#Inline) | inline_content | range | [InlineElement](#InlineElement) |
| [Placeholder](#Placeholder) | inline_content | range | [InlineElement](#InlineElement) |
| [Block](#Block) | inline_content | range | [InlineElement](#InlineElement) |



















</div>



### Klasse: TextRun []{#TextRun}


_Ein einfacher Textabschnitt in gemischtem Inhalt. Wird als Textknoten eines mixed-complexType ausgegeben, nicht als Element._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| text | 0..1 <br/> String | Die Zeichendaten eines TextRun; wird als Textknoten in gemischtem Inhalt ausgegeben. |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: Ref []{#Ref}


_Eine Inline-Referenz (akn:ref). Trägt @href, und bei internen SR-Querverweisen die Fedlex-Erweiterungsattribute fedlex:rs und fedlex:rs-uri._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| href | 0..1 <br/> String | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| fedlex_rs | 0..1 <br/> String | Fedlex-Erweiterungsattribut fedlex:rs auf akn:ref: die SR-Nummer des referenzierten Erlasses (z.B. '641.20').  |
| fedlex_rs_uri | 0..1 <br/> [ELIURI](#ELIURI) | Fedlex-Erweiterungsattribut fedlex:rs-uri auf akn:ref: die ELI-URI des SR-Eintrags des referenzierten Erlasses.  |
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: AuthorialNote []{#AuthorialNote}


_Eine Fussnote des Autors (akn:authorialNote). Rekursiv in Block-Inhalt: enthält ein oder mehrere akn:p-Absätze, die selbst Inline-Inhalt tragen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_paragraphs | * <br/> [BlockParagraph](#BlockParagraph) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: Inline []{#Inline}


_Ein benanntes präsentationsbezogenes Inline (akn:inline), z.B. name='man-font-style-normal'._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| name_attr | 0..1 <br/> String | Das @name-Attribut auf akn:inline, z.B. 'man-font-style-normal'. |
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: Placeholder []{#Placeholder}


_Ein Platzhalter für entfernten Inhalt (akn:placeholder) mit dem Erweiterungsattribut fedlex:message (z.B. 'E40S10-TAB')._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| fedlex_message | 0..1 <br/> String | Fedlex-Erweiterungsattribut fedlex:message auf akn:placeholder, das entfernten Inhalt kennzeichnet (z.B. 'E40S10-TAB').  |
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: Span []{#Span}


_Generischer Inline-Bereich (akn:span)._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: B []{#B}


_Fett-Inline-Markup (akn:b)._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: I []{#I}


_Kursiv-Inline-Markup (akn:i)._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: Sup []{#Sup}


_Hochgestelltes Inline-Markup (akn:sup)._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| inline_content | * <br/> [InlineElement](#InlineElement) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>



### Klasse: Br []{#Br}


_Ein Zeilenumbruch (akn:br). In der (derzeit deaktivierten) Regel FLX-TXT-001 ist br auf Überschriften-Elemente beschränkt._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| element_type | 0..1 <br/> String | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](#InlineElement) |






















</div>

## Typ: XmlContent []{#XmlContent}




_Gemischter XML-Inhalt: Text mit optionalem Inline-Markup. Erlaubte Inline-Elemente: akn:ref, akn:span, akn:b, akn:i, akn:sup, akn:authorialNote, akn:mod, akn:ins, akn:del. Hinweis: akn:br ist nur in Überschriften-Elementen erlaubt (FLX-TXT-001)._




<div data-search-exclude markdown="1">

URI: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

### Typ-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Base | `str` |
| Type URI | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |










</div>

\newpage

# Metadaten

Der Metadatenblock `akn:meta` versammelt alles, was ein Dokument beschreibt, ohne Teil seines Textes zu sein: die FRBR-Identifikation (siehe Kapitel Identifikation) und die Referenzen auf die beteiligten Stellen und Rollen.



### Klasse: ActMeta []{#ActMeta}


_Metadaten-Abschnitt des Erlasses (akn:meta). Enthält die FRBR-Identifikation (Work-, Expression-, Manifestations-Ebene) sowie benannte Referenz-Definitionen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| identification_ref | 0..1 <br/> [Identification](#Identification) | FRBR-Identifikationsblock (akn:identification). |
| references_ref | 0..1 <br/> [References](#References) | Referenzen-Abschnitt der Metadaten (akn:references). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](#Act) | meta | range | [ActMeta](#ActMeta) |
| [Doc](#Doc) | meta | range | [ActMeta](#ActMeta) |














#### Beispiele
##### Beispiel ActMeta: sr101 excerpt 1 1

```yaml
meta:
  identification_ref:
    source: '#ch.bk'
    frbr_work:
      frbr_this:
        value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
      frbr_uri:
        value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
      frbr_dates:
      - date_value: '2000-01-01'
        frbr_date_name: jolux:dateEntryInForce
      - date_value: '1999-04-18'
        frbr_date_name: jolux:dateDocument
      - date_value: '2024-03-03'
        frbr_date_name: jolux:dateApplicability
      frbr_authors:
      - href: '#ch.bk'
        as_role: '#publisher'
      - href: '#ch.bk'
        as_role: '#rightsHolder'
      frbr_country:
        value: CH
      frbr_number:
        value: '101'
      frbr_names:
      - xml_lang: de
        value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April
          1999
        short_form: BV
      - xml_lang: fr
        value: Constitution fédérale de la Confédération suisse du 18 avril 1999
        short_form: Cst.
      - xml_lang: it
        value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
        short_form: Cost.
      - xml_lang: rm
        value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
        short_form: Cst.
      frbr_authoritative:
        value: 'true'
    frbr_expression:
      frbr_this:
        value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
      frbr_uri:
        value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
      frbr_dates:
      - date_value: '2000-01-01'
        frbr_date_name: jolux:dateEntryInForce
      - date_value: '1999-04-18'
        frbr_date_name: jolux:dateDocument
      frbr_authors:
      - href: '#ch.bk'
        as_role: '#publisher'
      frbr_language:
        language_value: de
    frbr_manifestation:
      frbr_this:
        value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
      frbr_uri:
        value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
      frbr_dates:
      - date_value: '2024-03-03'
        frbr_date_name: jolux:dateApplicability
      frbr_authors:
      - href: '#ch.bk'
        as_role: '#publisher'
      frbr_format:
        value: xml
  references_ref:
    source: '#ch.bk'
    tlc_organizations:
    - eId: ch.bk
      href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
      show_as: Bundeskanzlei
    tlc_roles:
    - eId: publisher
      href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
      show_as: Editeur
    - eId: rightsHolder
      href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
      show_as: Détenteur des droits

```
##### Beispiel ActMeta: bgoe excerpt 1 1

```yaml
meta:
  identification_ref:
    source: '#ch.bk'
    frbr_work:
      frbr_this:
        value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
      frbr_uri:
        value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
      frbr_dates:
      - date_value: '2006-07-01'
        frbr_date_name: jolux:dateEntryInForce
      - date_value: '2004-12-17'
        frbr_date_name: jolux:dateDocument
      - date_value: '2023-11-01'
        frbr_date_name: jolux:dateApplicability
      frbr_authors:
      - href: '#ch.bk'
        as_role: '#publisher'
      - href: '#ch.bk'
        as_role: '#rightsHolder'
      frbr_country:
        value: CH
      frbr_number:
        value: '152.3'
      frbr_names:
      - xml_lang: de
        value: >-
          Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung
          (Öffentlichkeitsgesetz, BGÖ)
        short_form: BGÖ
      - xml_lang: fr
        value: >-
          Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans
          l'administration (Loi sur la transparence, LTrans)
        short_form: LTrans
      - xml_lang: it
        value: >-
          Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
          (Legge sulla trasparenza, LTras)
        short_form: LTras
      - xml_lang: rm
        value: >-
          Lescha federala dals 17 da december 2004 davart il princip da la transparenza
          da l'administraziun (Lescha da transparenza, LTrans)
        short_form: LTrans
      - xml_lang: en
        value: >-
          Federal Act of 17 December 2004 on Freedom of Information in the Administration
          (Freedom of Information Act, FoIA)
        short_form: FoIA
      frbr_authoritative:
        value: 'true'
    frbr_expression:
      frbr_this:
        value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
      frbr_uri:
        value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
      frbr_dates:
      - date_value: '2006-07-01'
        frbr_date_name: jolux:dateEntryInForce
      - date_value: '2023-11-01'
        frbr_date_name: jolux:dateApplicability
      frbr_authors:
      - href: '#ch.bk'
        as_role: '#publisher'
      frbr_language:
        language_value: de
    frbr_manifestation:
      frbr_this:
        value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
      frbr_uri:
        value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
      frbr_dates:
      - date_value: '2023-11-01'
        frbr_date_name: jolux:dateApplicability
      frbr_authors:
      - href: '#ch.bk'
        as_role: '#publisher'
      frbr_format:
        value: xml
        fedlex_generator: 2024-q4-rel-1.6.5
  references_ref:
    source: '#ch.bk'
    tlc_organizations:
    - eId: ch.bk
      href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
      show_as: Bundeskanzlei
    tlc_roles:
    - eId: publisher
      href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
      show_as: Editeur
    - eId: rightsHolder
      href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
      show_as: Détenteur des droits
    tlc_references:
    - name_attr: language
      href: http://publications.europa.eu/resource/authority/language/DEU
      show_as: de
    - name_attr: format
      href: https://fedlex.data.admin.ch/vocabulary/user-format/xml
      show_as: xml

```






</div>

## Referenzen auf Akteure und Rollen

Personen, Organisationen und Rollen werden nicht im Text selbst beschrieben, sondern einmal im Abschnitt `akn:references` deklariert; die Elemente des Dokuments verweisen anschliessend über einen dokumentinternen Anker darauf (`href="#ch.bk"`). So bleibt die Angabe an einer Stelle, auch wenn sie im Dokument mehrfach vorkommt.



### Klasse: References []{#References}


_Benannte Referenz-Definitionen für das gesamte Dokument (akn:references). Definiert Organisationen, Rollen und andere Entitäten, die über Anker (@href='#eId') referenziert werden._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](#AnchorRef) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| tlc_organizations | * <br/> [TLCOrganization](#TLCOrganization) | Benannte Organisations-Referenzen im Dokument (akn:TLCOrganization). |
| tlc_roles | * <br/> [TLCRole](#TLCRole) | Benannte Rollen-Referenzen im Dokument (akn:TLCRole). |
| tlc_references | * <br/> [TLCReference](#TLCReference) | Generische benannte Referenzen im Dokument (akn:TLCReference). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActMeta](#ActMeta) | references_ref | range | [References](#References) |














#### Beispiele
##### Beispiel References: sr101 excerpt 1 1

```yaml
references_ref:
  source: '#ch.bk'
  tlc_organizations:
  - eId: ch.bk
    href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
    show_as: Bundeskanzlei
  tlc_roles:
  - eId: publisher
    href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
    show_as: Editeur
  - eId: rightsHolder
    href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
    show_as: Détenteur des droits

```
##### Beispiel References: bgoe excerpt 1 1

```yaml
references_ref:
  source: '#ch.bk'
  tlc_organizations:
  - eId: ch.bk
    href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
    show_as: Bundeskanzlei
  tlc_roles:
  - eId: publisher
    href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
    show_as: Editeur
  - eId: rightsHolder
    href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
    show_as: Détenteur des droits
  tlc_references:
  - name_attr: language
    href: http://publications.europa.eu/resource/authority/language/DEU
    show_as: de
  - name_attr: format
    href: https://fedlex.data.admin.ch/vocabulary/user-format/xml
    show_as: xml

```






</div>



### Klasse: TLCOrganization []{#TLCOrganization}


_Eine benannte Organisation als Referenz im Dokument (akn:TLCOrganization). Beispiel: die Bundeskanzlei (ch.bk)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| href | 0..1 <br/> String | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| show_as | 0..1 <br/> String | Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [References](#References) | tlc_organizations | range | [TLCOrganization](#TLCOrganization) |














#### Beispiele
##### Beispiel TLCOrganization: Deklaration der publizierenden Stelle

```yaml
tlc_organizations:
- eId: ch.bk
  href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
  show_as: Bundeskanzlei

```






</div>



### Klasse: TLCRole []{#TLCRole}


_Eine benannte Rolle als Referenz im Dokument (akn:TLCRole). Beispiele: publisher, rightsHolder._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| href | 0..1 <br/> String | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| show_as | 0..1 <br/> String | Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [References](#References) | tlc_roles | range | [TLCRole](#TLCRole) |














#### Beispiele
##### Beispiel TLCRole: sr101 excerpt 1 2

```yaml
tlc_roles:
- eId: rightsHolder
  href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
  show_as: Détenteur des droits

```
##### Beispiel TLCRole: bgoe excerpt 1 2

```yaml
tlc_roles:
- eId: rightsHolder
  href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
  show_as: Détenteur des droits

```
##### Beispiel TLCRole: Role publisher as an anchor

```yaml
tlc_roles:
- eId: publisher
  href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
  show_as: Editeur

```






</div>



### Klasse: TLCReference []{#TLCReference}


_Eine generische benannte Referenz im Dokument (akn:TLCReference). Für Referenzen, die nicht TLCOrganization oder TLCRole entsprechen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](#EIdType) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| name_attr | 0..1 <br/> String | Das @name-Attribut auf akn:inline, z.B. 'man-font-style-normal'. |
| href | 0..1 <br/> String | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| show_as | 0..1 <br/> String | Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [References](#References) | tlc_references | range | [TLCReference](#TLCReference) |



















</div>

### Enum: FedlexRoleEnum []{#FedlexRoleEnum}




_Erlaubte Werte für das Fedlex-Erweiterungsattribut fedlex:role (FLX-XF-003). 'marginal' nur bei akn:level-Elementen (FLX-XF-004). 'reference' nur bei akn:subheading-Elementen (FLX-XF-005)._




<div data-search-exclude markdown="1">

URI: [laws:FedlexRoleEnum](https://ld.ech.ch/schema/0296/laws/FedlexRoleEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| marginal |  Kennzeichnet ein level als Randnote. Nur bei akn:level erlaubt (FLX-XF-004). |
| reference |  Kennzeichnet eine Unterüberschrift als Referenzüberschrift. Nur bei akn:subheading erlaubt (FLX-XF-005).  |







</div>

## Werte, Sprache und Format

Mehrere AKN-Elemente tragen ihren Inhalt nicht als Text, sondern in einem Attribut — `value`, `href`, `language` oder `format`. Dafür stehen eigene kleine Klassen, damit die Attributform im Modell sichtbar bleibt.



### Klasse: ValueType []{#ValueType}


_Einfacher Halter mit einem einzelnen @value-Attribut (AKN valueType). Wiederverwendet für FRBRcountry, FRBRnumber, FRBRauthoritative usw._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| value | 0..1 <br/> String | Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](#FRBRWork) | frbr_country | range | [ValueType](#ValueType) |
| [FRBRWork](#FRBRWork) | frbr_number | range | [ValueType](#ValueType) |
| [FRBRWork](#FRBRWork) | frbr_authoritative | range | [ValueType](#ValueType) |



















</div>



### Klasse: UriValueType []{#UriValueType}


_Halter mit einem @value-Attribut vom Typ ELI-URI (AKN valueType). Wiederverwendet für FRBRthis und FRBRuri._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| value_uri | 0..1 <br/> [ELIURI](#ELIURI) | Ein @value-Attribut vom Typ ELI-URI (akn:FRBRthis/@value, akn:FRBRuri/@value). |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](#FRBRWork) | frbr_this | range | [UriValueType](#UriValueType) |
| [FRBRWork](#FRBRWork) | frbr_uri | range | [UriValueType](#UriValueType) |
| [FRBRExpression](#FRBRExpression) | frbr_this | range | [UriValueType](#UriValueType) |
| [FRBRExpression](#FRBRExpression) | frbr_uri | range | [UriValueType](#UriValueType) |
| [FRBRManifestation](#FRBRManifestation) | frbr_this | range | [UriValueType](#UriValueType) |
| [FRBRManifestation](#FRBRManifestation) | frbr_uri | range | [UriValueType](#UriValueType) |



















</div>



### Klasse: LanguageType []{#LanguageType}


_Halter mit einem einzelnen @language-Attribut (akn:FRBRlanguage)._



<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| language_value | 0..1 <br/> [DocumentLanguageEnum](#DocumentLanguageEnum) | Das @language-Attribut von akn:FRBRlanguage, z.B. 'de'. |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRExpression](#FRBRExpression) | frbr_language | range | [LanguageType](#LanguageType) |



















</div>



### Klasse: FormatType []{#FormatType}


_Halter für akn:FRBRformat: ein @value (typischerweise 'xml') plus das optionale Erweiterungsattribut fedlex:generator (FLX-XF-002)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| value | 0..1 <br/> String | Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet. |
| fedlex_generator | 0..1 <br/> String | Fedlex-Erweiterungsattribut fedlex:generator bei akn:FRBRformat[@value='xml']. Identifiziert das Werkzeug, das die XML-Datei erzeugt hat. Nur bei FRBRformat erlaubt (FLX-XF-002).  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRManifestation](#FRBRManifestation) | frbr_format | range | [FormatType](#FormatType) |



















</div>

### Enum: DocumentLanguageEnum []{#DocumentLanguageEnum}




_Sprachcodes für schweizerische Bundesdokumente._



<div data-search-exclude markdown="1">

URI: [laws:DocumentLanguageEnum](https://ld.ech.ch/schema/0296/laws/DocumentLanguageEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| de |  Deutsch |
| fr |  Französisch |
| it |  Italienisch |
| rm |  Rätoromanisch |
| en |  Englisch |







</div>

\newpage

# Anhang A – Referenzen & Bibliographie

## Standards der Fachgruppe „Politische Geschäfte"

Die folgenden Standards der Fachgruppe befinden sich alle in Arbeit; sie werden hier ohne Versionsangabe zitiert.

|Standard|Beschreibung|
|---|---|
|eCH-0292|eCH-0292: Metaprozesse zu politischen Geschäften – gemeinsame Datenelemente: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0293|eCH-0293: Öffentlicher Ratsbetrieb: [https://www.ech.ch/de/ech/ech-0293](https://www.ech.ch/de/ech/ech-0293)|
|eCH-0294|eCH-0294: Politische Akteure: [https://www.ech.ch/de/ech/ech-0294](https://www.ech.ch/de/ech/ech-0294)|
|eCH-0295|eCH-0295: Parlamentarische Geschäfte: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0297|eCH-0297: Öffentliche Konsultationen: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Weitere eCH-Standards

|Standard|Beschreibung|
|---|---|
|eCH-0122|E-Government-Architektur Schweiz: [https://www.ech.ch/de/ech/ech-0122](https://www.ech.ch/de/ech/ech-0122)|
|eCH-0003|Prozessstandard eCH-Dokumente – Namenskonventionen und Pflichtstruktur der eCH-Standards: [https://www.ech.ch/de/ech/ech-0003](https://www.ech.ch/de/ech/ech-0003)|

## Grundlagenstandards

|Quelle|Beschreibung|
|---|---|
|AKN|Legal Document Markup Language (LegalDocML) – Akoma Ntoso Version 3.0, OASIS Standard: [http://docs.oasis-open.org/legaldocml/akn-core/v1.0/](http://docs.oasis-open.org/legaldocml/akn-core/v1.0/)|
|ELI|European Legislation Identifier, Europäische Kommission: [https://op.europa.eu/en/web/eu-vocabularies/eli](https://op.europa.eu/en/web/eu-vocabularies/eli)|
|FRBRoo|FRBRoo – Object Oriented Definition and Mapping of the FRBR, IFLA: [http://iflastandards.info/ns/fr/frbr/frbroo/](http://iflastandards.info/ns/fr/frbr/frbroo/)|
|RFC 6570|URI Template, IETF: [https://www.rfc-editor.org/rfc/rfc6570](https://www.rfc-editor.org/rfc/rfc6570)|
|Fedlex|Systematische Rechtssammlung und ELI-URIs des Bundes: [https://www.fedlex.admin.ch](https://www.fedlex.admin.ch)|

## Quellen und Werkzeuge

Die Prüfregeln dieses Anwendungsprofils stammen aus dem Fedlex-Schematron (`AKN-fedlex-*.sch`); die zulässigen Elemente aus dem AKN-3.0-Schema (`akomantoso30.xsd`). Beide sowie das Referenzmaterial der Fachgruppe liegen im Ordner `misc/` dieses Standards.

\newpage

# Anhang B – Zuordnung zu Akoma Ntoso

Jede Klasse und jeder Slot dieses Standards trägt die Entsprechung im Akoma-Ntoso-Vokabular am Element selbst — als `exact_mappings`, `close_mappings` und die weiteren Mapping-Angaben, die LinkML dafür vorsieht. Die folgende Tabelle ist daraus erzeugt und nicht von Hand geführt; wer eine Klasse an ein anderes Element bindet, ändert das Schema.

Aus derselben Quelle entsteht ein Mapping-Set nach SSSOM (Simple Standard for Sharing Ontology Mappings) als `output/mappings/ech-0296_laws.sssom.tsv`. Es hält zu jeder Zeile fest, wie eng die Entsprechung ist (`exactMatch`, `closeMatch`, `narrowMatch`, `broadMatch`) und worauf sie beruht, und lässt sich mit den Werkzeugen der Mapping Commons prüfen und weiterverarbeiten. Dieselben Angaben stehen als `skos:exactMatch`-Tripel im RDF-Export des Schemas (`output/schema.ttl`).

Die Zuordnung zum European Legislation Identifier steht noch aus. Sie kommt an dieselbe Stelle — als weiterer Eintrag bei den betroffenen Elementen — und erscheint dann ohne weiteres Zutun in dieser Tabelle und im Mapping-Set.

| Element in diesem Standard | Art | Beziehung | Entspricht |
|---|---|---|---|
| `FedlexDocument` | Klasse | exactMatch | `akn:akomaNtoso` |
| `Act` | Klasse | exactMatch | `akn:act` |
| `ActMeta` | Klasse | exactMatch | `akn:meta` |
| `Identification` | Klasse | exactMatch | `akn:identification` |
| `FRBRWork` | Klasse | exactMatch | `akn:FRBRWork` |
| `FRBRWork` | Klasse | closeMatch | `eli:LegalResource` |
| `FRBRExpression` | Klasse | exactMatch | `akn:FRBRExpression` |
| `FRBRExpression` | Klasse | closeMatch | `eli:LegalExpression` |
| `FRBRManifestation` | Klasse | exactMatch | `akn:FRBRManifestation` |
| `FRBRManifestation` | Klasse | closeMatch | `eli:Format` |
| `FRBRDate` | Klasse | exactMatch | `akn:FRBRdate` |
| `FRBRAuthor` | Klasse | exactMatch | `akn:FRBRauthor` |
| `FRBRName` | Klasse | exactMatch | `akn:FRBRname` |
| `FRBRName` | Klasse | closeMatch | `eli:title` |
| `References` | Klasse | exactMatch | `akn:references` |
| `TLCOrganization` | Klasse | exactMatch | `akn:TLCOrganization` |
| `TLCRole` | Klasse | exactMatch | `akn:TLCRole` |
| `TLCReference` | Klasse | exactMatch | `akn:TLCReference` |
| `Preface` | Klasse | exactMatch | `akn:preface` |
| `PrefaceP` | Klasse | exactMatch | `akn:p` |
| `Preamble` | Klasse | exactMatch | `akn:preamble` |
| `ActBody` | Klasse | exactMatch | `akn:body` |
| `Book` | Klasse | exactMatch | `akn:book` |
| `Title` | Klasse | exactMatch | `akn:title` |
| `Part` | Klasse | exactMatch | `akn:part` |
| `Chapter` | Klasse | exactMatch | `akn:chapter` |
| `Subchapter` | Klasse | exactMatch | `akn:subchapter` |
| `Section` | Klasse | exactMatch | `akn:section` |
| `Subsection` | Klasse | exactMatch | `akn:subsection` |
| `Level` | Klasse | exactMatch | `akn:level` |
| `Article` | Klasse | exactMatch | `akn:article` |
| `Subdivision` | Klasse | exactMatch | `akn:subdivision` |
| `Paragraph` | Klasse | exactMatch | `akn:paragraph` |
| `Transitional` | Klasse | exactMatch | `akn:transitional` |
| `Proviso` | Klasse | exactMatch | `akn:proviso` |
| `Content` | Klasse | exactMatch | `akn:content` |
| `BlockParagraph` | Klasse | exactMatch | `akn:p` |
| `BlockList` | Klasse | exactMatch | `akn:blockList` |
| `BlockListItem` | Klasse | exactMatch | `akn:item` |
| `Table` | Klasse | exactMatch | `akn:table` |
| `TableRow` | Klasse | exactMatch | `akn:tr` |
| `TableCell` | Klasse | exactMatch | `akn:td` |
| `Ref` | Klasse | exactMatch | `akn:ref` |
| `B` | Klasse | exactMatch | `akn:b` |
| `I` | Klasse | exactMatch | `akn:i` |
| `Sup` | Klasse | exactMatch | `akn:sup` |
| `Span` | Klasse | exactMatch | `akn:span` |
| `Br` | Klasse | exactMatch | `akn:br` |
| `Inline` | Klasse | exactMatch | `akn:inline` |
| `Placeholder` | Klasse | exactMatch | `akn:placeholder` |
| `AuthorialNote` | Klasse | exactMatch | `akn:authorialNote` |
| `Components` | Klasse | exactMatch | `akn:components` |
| `Component` | Klasse | exactMatch | `akn:component` |
| `Doc` | Klasse | exactMatch | `akn:doc` |
| `MainBody` | Klasse | exactMatch | `akn:mainBody` |
| `Container` | Klasse | exactMatch | `akn:container` |
| `Block` | Klasse | exactMatch | `akn:block` |
| `preface_paragraphs` | Slot | exactMatch | `akn:p` |
| `frbr_this` | Slot | exactMatch | `akn:FRBRthis` |
| `frbr_uri` | Slot | exactMatch | `akn:FRBRuri` |
| `frbr_authors` | Slot | closeMatch | `eli:passed_by` |
| `frbr_country` | Slot | exactMatch | `akn:FRBRcountry` |
| `frbr_country` | Slot | closeMatch | `eli:jurisdiction` |
| `frbr_number` | Slot | exactMatch | `akn:FRBRnumber` |
| `frbr_number` | Slot | closeMatch | `eli:number` |
| `frbr_authoritative` | Slot | exactMatch | `akn:FRBRauthoritative` |
| `frbr_authoritative` | Slot | closeMatch | `eli:legal_value` |
| `frbr_language` | Slot | exactMatch | `akn:FRBRlanguage` |
| `frbr_language` | Slot | closeMatch | `eli:language` |
| `frbr_format` | Slot | exactMatch | `akn:FRBRformat` |
| `frbr_format` | Slot | closeMatch | `eli:format` |
| `doc_number` | Slot | exactMatch | `akn:docNumber` |
| `doc_title` | Slot | exactMatch | `akn:docTitle` |
| `num` | Slot | exactMatch | `akn:num` |
| `heading` | Slot | exactMatch | `akn:heading` |
| `subheading` | Slot | exactMatch | `akn:subheading` |
| `list_introduction` | Slot | exactMatch | `akn:listIntroduction` |
| `components_ref` | Slot | exactMatch | `akn:components` |
| `component_list` | Slot | exactMatch | `akn:component` |
| `doc_ref` | Slot | exactMatch | `akn:doc` |
| `main_body` | Slot | exactMatch | `akn:mainBody` |
| `containers` | Slot | exactMatch | `akn:container` |
| `blocks` | Slot | exactMatch | `akn:block` |


