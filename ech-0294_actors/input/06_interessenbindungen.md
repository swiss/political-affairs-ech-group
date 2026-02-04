# Interessenbindungen (Interest Links)

## Einführung und Zielsetzung

Das InterestLink-Schema erfasst Interessenbindungen, Interessenkonflikte und Verflechtungen von Personen im politischen Kontext mit Organisationen. Der Standard orientiert sich an den Transparenzanforderungen für Parlamentsmitglieder gemäß [Bundesversammlung - Interessenbindungen](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

**Kernziele:**
- **Transparenz**: Offenlegung von potenziellen Interessenkonflikten
- **Strukturierte Erfassung**: Einheitliche Klassifikation nach Art der Interessenbindung
- **Auswertbarkeit**: Verknüpfung mit UID-Register für statistische Analysen (NOGA-Codes)
- **Zeitliche Nachvollziehbarkeit**: Dokumentation von Start und Ende der Bindung

## Technische Struktur

### Identifikatoren und Referenzen

Das InterestLink-Schema verknüpft Personen mit Organisationen:

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `id` | URI | Ja | Eindeutiger Identifikator der Interessenbindung |
| `person_id` | string | Ja | Referenz zur Person (act:person_123 oder Wikidata-ID) |

**Beispiel:**
```yaml
id: act:interest_link_12345
person_id: https://www.wikidata.org/wiki/Q493598
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `id` | URI | Eindeutiger Identifikator |
| `person_id` | string | Referenz zur Person |
| `interest_type` | InterestTypeEnum | Art der Interessenbindung (siehe unten) |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `organization_label` | string | Name/Bezeichnung der Organisation |
| `organization_uid` | string | UID-Nummer der Organisation (eCH-0097) |
| `organization_address` | string | Adresse der Organisation |
| `legal_form` | string | Rechtsform (AG, GmbH, Verein, Stiftung, etc.) |
| `valid_from` | date | Beginn der Interessenbindung |
| `valid_until` | date | Ende der Interessenbindung |
| `paid` | boolean | Gibt an, ob die Position bezahlt ist |
| `committee` | string | Gremium (Stiftungsrat, Verwaltungsrat, etc.) |
| `function_role` | string | Funktion/Rolle in der Organisation |
| `datetime_updated` | datetime | Letzte Aktualisierung des Datensatzes |
| `datetime_created` | datetime | Erstellung des Datensatzes |

## Klassifikation: InterestTypeEnum

Interessenbindungen werden in drei Hauptkategorien klassifiziert:

### 1. professional_activity (Berufliche Tätigkeit)

Berufliche Tätigkeiten außerhalb des politischen Mandats.

**Beispiele:**
- Anstellung in einem Unternehmen
- Selbstständige Tätigkeit
- Beratungsmandate
- Verwaltungsratsmandate in Privatunternehmen

```yaml
interest_type: professional_activity
organization_label: Swisscom AG
organization_uid: CHE-116.281.426
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
paid: true
```

### 2. political_office (Politische Ämter)

Politische Ämter und Mandate auf anderen föderalen Ebenen oder in anderen Körperschaften.

**Beispiele:**
- Mitgliedschaft in kantonalen oder kommunalen Parlamenten
- Regierungsräte
- Kommissionsmitgliedschaften
- Ämter in außerparlamentarischen Kommissionen

```yaml
interest_type: political_office
organization_label: Gemeinderat Herisau
organization_address: Rathaus, 9100 Herisau
function_role: Gemeinderat
valid_from: 2018-01-01
paid: true
```

### 3. association (Vereinsmitgliedschaft)

Mitgliedschaften in Vereinen, Verbänden und Interessenorganisationen.

**Beispiele:**
- Branchenverbände
- Berufsverbände
- Lobbyorganisationen
- Gemeinnützige Vereine
- Stiftungen

```yaml
interest_type: association
organization_label: Schweizerischer Gewerbeverband
organization_uid: CHE-105.967.319
legal_form: Verein
function_role: Vorstandsmitglied
paid: false
```

## Organisation-UID und NOGA-Codes

Die `organization_uid` ermöglicht die Verknüpfung mit dem eidgenössischen Unternehmensregister:

**Vorteile:**
- Automatische Zuordnung von NOGA-Codes (Branchenklassifikation)
- Statistische Auswertungen nach Wirtschaftszweigen
- Eindeutige Identifikation der Organisation
- Verknüpfung mit Unternehmensdaten (Rechtsform, Adresse, etc.)

**Format:** eCH-0097 konform (CHE-XXX.XXX.XXX)

```yaml
organization_uid: CHE-116.281.426  # Swisscom AG
```

**Nachschlagen:** https://www.uid.admin.ch/

## Temporale Validität

Interessenbindungen ändern sich im Laufe der Zeit:

```yaml
# Beispiel: Wechsel von Positionen
- id: act:interest_link_001
  person_id: https://www.wikidata.org/wiki/Q493598
  interest_type: professional_activity
  organization_label: Credit Suisse
  committee: Verwaltungsrat
  valid_from: 2015-01-01
  valid_until: 2020-12-31
  paid: true

- id: act:interest_link_002
  person_id: https://www.wikidata.org/wiki/Q493598
  interest_type: professional_activity
  organization_label: UBS AG
  organization_uid: CHE-357.686.674
  committee: Verwaltungsrat
  valid_from: 2021-01-01
  paid: true
```

## Gremien und Funktionen

### Typische Gremien (`committee`)

Nach Schweizer Recht und Praxis:

- **Verwaltungsrat** (VR): Oberstes Führungsorgan einer AG
- **Stiftungsrat**: Oberstes Organ einer Stiftung
- **Vorstand**: Geschäftsführendes Organ eines Vereins
- **Aufsichtsrat**: Kontrollgremium
- **Beirat**: Beratendes Gremium
- **Geschäftsleitung**: Operative Führung

### Typische Funktionen (`function_role`)

- Präsident/Präsidentin
- Vizepräsident/Vizepräsidentin
- Mitglied
- Delegierter
- Geschäftsführer/Geschäftsführerin
- Berater/Beraterin

## Bezahlung (paid)

Das Attribut `paid` gibt an, ob die Position vergütet ist:

- `true`: Bezahlte Position (Entschädigung, Honorar, Lohn)
- `false`: Ehrenamtliche/unbezahlte Position

**Wichtig:** Bereits kleine Entschädigungen (z.B. Sitzungsgelder) gelten als bezahlt.

## Interoperabilität

### Verknüpfung mit Person-Schema

Interessenbindungen werden in zwei Formen referenziert:

1. **In der Container-Struktur:**
```yaml
# Container-Ebene
id: act:example_container
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni
    # ... weitere Person-Attribute

interest_links:
  - id: act:interest_link_001
    person_id: https://www.wikidata.org/wiki/Q493598
    interest_type: professional_activity
    organization_label: Universität St. Gallen
```

2. **Direkt bei der Person:**
```yaml
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni
    interest_links_person:
      - id: act:interest_link_001
        interest_type: professional_activity
        organization_label: Universität St. Gallen
```

### Verknüpfung mit UID-Register

Die UID ermöglicht Abfragen im Unternehmensregister:

```yaml
organization_uid: CHE-116.281.426
```

Liefert automatisch:
- Firmenname
- Rechtsform
- Adresse
- NOGA-Code (Branche)
- Handelsregistereintrag

## Anwendungsbeispiele

### Beispiel 1: Verwaltungsratsmandat in AG

```yaml
id: act:interest_link_caroni_001
person_id: https://www.wikidata.org/wiki/Q493598
interest_type: professional_activity
organization_label: Swiss Re AG
organization_uid: CHE-101.458.980
organization_address: Mythenquai 50/60, 8022 Zürich
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
valid_from: 2018-04-01
paid: true
datetime_created: 2024-01-15T10:30:00Z
datetime_updated: 2024-01-15T10:30:00Z
```

### Beispiel 2: Politisches Amt auf kantonaler Ebene

```yaml
id: act:interest_link_riniker_001
person_id: https://www.wikidata.org/wiki/Q77074968
interest_type: political_office
organization_label: Grosser Rat des Kantons Aargau
organization_address: Regierungsgebäude, 5001 Aarau
function_role: Grossrätin
valid_from: 2009-01-01
valid_until: 2019-12-31
paid: true
```

### Beispiel 3: Vereinsmitgliedschaft (ehrenamtlich)

```yaml
id: act:interest_link_jans_001
person_id: https://www.wikidata.org/wiki/Q813067
interest_type: association
organization_label: Pro Natura Basel
legal_form: Verein
function_role: Vorstandsmitglied
valid_from: 2010-01-01
paid: false
```

### Beispiel 4: Stiftungsrat

```yaml
id: act:interest_link_luisier_001
person_id: https://www.wikidata.org/wiki/Q24699807
interest_type: professional_activity
organization_label: Fondation pour le développement durable
legal_form: Stiftung
committee: Stiftungsrat
function_role: Präsidentin
valid_from: 2020-06-01
paid: false
```

### Beispiel 5: Mehrere Interessenbindungen einer Person

```yaml
id: act:container_example
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni
    interest_links_person:
      - id: act:interest_001
        interest_type: professional_activity
        organization_label: Universität St. Gallen
        organization_uid: CHE-105.817.549
        function_role: Honorarprofessor
        paid: true
        valid_from: 2015-01-01

      - id: act:interest_002
        interest_type: association
        organization_label: FDP Schweiz
        legal_form: Verein
        function_role: Mitglied
        paid: false
        valid_from: 2000-01-01

      - id: act:interest_003
        interest_type: professional_activity
        organization_label: Rechtsanwaltskanzlei Caroni
        legal_form: Einzelunternehmen
        function_role: Inhaber
        paid: true
        valid_from: 2008-01-01
```

## Auswertungsmöglichkeiten

### Nach Interessentyp

Statistische Auswertung nach Art der Interessenbindung:
- Anzahl beruflicher Tätigkeiten pro Person
- Anteil politischer Ämter auf verschiedenen Ebenen
- Vereinsmitgliedschaften nach Partei

### Nach Branche (NOGA-Code)

Über die UID-Verknüpfung:
- Welche Wirtschaftszweige sind im Parlament vertreten?
- Häufung von Mandaten in bestimmten Branchen
- Verflechtungen zwischen Politik und Wirtschaft

### Nach Bezahlung

- Anteil bezahlter vs. ehrenamtlicher Tätigkeiten
- Durchschnittliche Anzahl bezahlter Mandate
- Kumulation von Einkommen

### Zeitliche Entwicklung

- Beginn/Ende von Interessenbindungen
- Wechsel zwischen Organisationen
- Dauer von Mandaten

## Referenzen

**Weiterführende Dokumentation:**
- [Bundesversammlung - Interessenbindungen Nationalrat](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf)
- [UID-Register](https://www.uid.admin.ch/)
- [eCH-0097: Unternehmens-Identifikationsnummer](https://www.ech.ch/de/ech/ech-0097)
- [NOGA-Codes (Branchenklassifikation)](https://www.bfs.admin.ch/bfs/de/home/statistiken/industrie-dienstleistungen/nomenklatur/noga.html)

Siehe vollständige LinkML-Schema-Dokumentation:

{{include:ech-0294_actors/output/docs/InterestLink.md}}
