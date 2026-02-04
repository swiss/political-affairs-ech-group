# Person

## Einführung und Zielsetzung

Das Person-Schema beschreibt natürliche Personen im politischen Kontext mit dem Ziel, eine präzise und gleichzeitig flexible Datenstruktur bereitzustellen. Der Standard ermöglicht es, sowohl hochgradig strukturierte als auch offene Informationen zu erfassen, um unterschiedliche Datenqualitäten und Verfügbarkeiten abzubilden.

**Kernziele:**
- **Präzision**: Unterstützung von zeitlich gültigen Attributen (z.B. Namen, Adressen, Geschlecht)
- **Flexibilität**: Optionale Felder erlauben schrittweise Datenanreicherung
- **Interoperabilität**: Verwendung von Wikidata-IDs und URIs als globale Identifikatoren
- **Mehrsprachigkeit**: Unterstützung mehrsprachiger Inhalte gemäß Schweizer Anforderungen

## Technische Struktur

### Identifikatoren

Das Person-Schema verwendet eine hierarchische Identifikationsstrategie:

1. **Primärer Identifikator (`id`)**:
   - **Präferenz**: Wikidata-ID (z.B. `https://www.wikidata.org/wiki/Q813067`)
   - **Alternative**: Lokaler URI (z.B. `act:person_12345`)
   - **Anforderung**: Eindeutig, persistent, global auflösbar (wenn möglich)

2. **Anzeigenamen**:
   - `label`: Kurzer Anzeigename (z.B. "Beat Jans")
   - `label_long`: Erweiterter Anzeigename mit Titeln (z.B. "Prof. Dr. iur. Andrea Caroni, MPA (Harvard)")

### Temporale Validität

Viele Attribute unterstützen zeitliche Gültigkeit durch `valid_from` und `valid_until`:

- **Name**: Namen können sich ändern (Heirat, Geschlechtsanpassung)
- **Adresse**: Wohn- und Geschäftsadressen ändern sich
- **Geschlecht**: Geschlechtsidentität kann sich entwickeln
- **Staatsbürgerschaft**: Mehrfache Staatsbürgerschaften mit unterschiedlichen Gültigkeitsperioden
- **Beruf**: Berufliche Tätigkeiten mit Start- und Enddatum
- **Wahlkreis**: Wahlkreis kann sich bei Neuwahlen ändern

**Beispiel:**
```yaml
names:
  - name_type: officialLastName
    value: Müller
    valid_from: 1980-01-01
    valid_until: 2010-06-15
  - name_type: officialLastName
    value: Meier-Müller
    valid_from: 2010-06-15
```

### Datentypen und Validierung

| Attribut | Datentyp | Pflicht | Beschreibung |
|----------|----------|---------|--------------|
| `id` | URI | Ja | Eindeutiger Identifikator |
| `label` | string | Ja | Anzeigename |
| `birthyear` | integer | Nein | Geburtsjahr (4-stellig) |
| `birthdate` | date | Nein | Exaktes Geburtsdatum (ISO 8601) |
| `picture` | URI | Nein | Link zu Profilbild (bevorzugt PNG) |
| `names` | Name[] | Nein | Liste strukturierter Namen |
| `addresses` | Address[] | Nein | Wohn- und Geschäftsadressen |
| `languages` | LanguageProficiency[] | Nein | Sprachkenntnisse |
| `ch_citizenship` | Validity | Nein | Schweizer Bürgerrecht (zeitlich) |
| `citizenships` | Citizenship[] | Nein | Weitere Staatsbürgerschaften |
| `genders` | Gender[] | Nein | Geschlechtsidentität(en) |
| `occupations` | Occupation[] | Nein | Berufliche Tätigkeiten |
| `trainings` | Training[] | Nein | Ausbildungen |
| `contacts` | Contact[] | Nein | Kontaktinformationen |
| `electoral_district` | ElectoralDistrict | Nein | Wahlkreis |
| `interest_links_person` | InterestLink[] | Nein | Interessenbindungen |

## Strukturierte Unterklassen

### Name

Namen werden nach eCH-0044 strukturiert erfasst:

```yaml
names:
  - name_type: officialGivenName
    value: Andrea
  - name_type: officialLastName
    value: Caroni
    valid_from: 1980-04-19
  - name_type: callName
    value: Andi
```

**Namenstypen** (`NameTypeEnum`):
- `officialGivenName`: Offizieller Vorname
- `officialLastName`: Offizieller Nachname
- `officialMiddleName`: Offizieller Mittelname
- `callName`: Rufname
- `familyNameOnForeignPassport`: Familienname auf ausländischem Pass

### Adresse

Adressen folgen eCH-0010 Standard:

```yaml
addresses:
  - address_type: businessAddress
    address_URI: https://ld.admin.ch/address/12345
    street_address: Bundesplatz 3
    postal_code: "3003"
    postal_locality: Bern
  - address_type: privateAddress
    postal_locality: Zürich
```

**Adresstypen** (`AddressTypeEnum`):
- `privateAddress`: Privatadresse
- `businessAddress`: Geschäftsadresse
- `localAddress`: Lokale Adresse (z.B. Parlamentsadresse)

### Sprachkenntnisse

```yaml
languages:
  - language: de
    correspondence: true
    native: true
  - language: fr
    correspondence: false
    native: false
```

- `language`: ISO 639-1 Sprachcode (de, fr, it, rm, en)
- `correspondence`: Bevorzugte Korrespondenzsprache
- `native`: Muttersprache

### Geschlecht

```yaml
genders:
  - value: female
    valid_from: 1978-05-23
    pronouns:
      - sie
      - ihr
```

- `value`: Geschlechtscode (male, female, diverse, etc.)
- `pronouns`: Bevorzugte Pronomen (mehrsprachig möglich)
- Unterstützt zeitliche Änderungen

### Staatsbürgerschaft

```yaml
ch_citizenship:
  valid_from: 1980-04-19

citizenships:
  - country: IT
    valid_from: 1980-04-19
  - country: DE
    valid_from: 2005-01-15
    valid_until: 2020-12-31
```

- `ch_citizenship`: Schweizer Bürgerrecht (Validity-Objekt)
- `citizenships`: Weitere Staatsbürgerschaften mit ISO 3166 Ländercodes

### Beruf und Ausbildung

```yaml
occupations:
  - value: Honorarprofessor
    occupation_isco19_code: "2421"
    valid_from: 2010-01-01
    active: true
    paid: true
    enterprise_uid: CHE-123.456.789
    enterprise: Universität St. Gallen

trainings:
  - type: uni
    value: Prof. Dr. iur.
    training_isco19_code: "0421"
  - type: uni
    value: MPA (Harvard)
```

- `occupation_isco19_code`: ISCO-19 Berufsklassifikation
- `enterprise_uid`: UID-Nummer des Unternehmens (eCH-0097)
- `active`: Aktuelle Tätigkeit
- `paid`: Bezahlte Position

**Ausbildungstypen** (`TrainingTypeEnum`):
- `schulabschluss`: Schulabschluss
- `efz`: Eidgenössisches Fähigkeitszeugnis
- `uni`: Universitätsabschluss
- `armee`: Militärdienst
- `zivi`: Zivildienst
- `zischutz`: Zivilschutz

### Kontaktinformationen

```yaml
contacts:
  - type: email
    value: andrea.caroni@parl.ch
  - type: contact_website
    value: http://www.andrea-caroni.ch
  - type: linked-in
    value: https://linkedin.com/in/andrea-caroni
  - type: twitter
    value: https://twitter.com/acaroni
```

**Kontakttypen** (`ContactTypeEnum`):
- `email`: E-Mail-Adresse
- `contact_website`: Persönliche Website
- `linked-in`: LinkedIn-Profil
- `twitter`: Twitter/X-Profil

### Wahlkreis

```yaml
electoral_district:
  district: Appenzell Ausserrhoden
  valid_from: 2015-01-01
  valid_until: 2023-11-30
```

## Datenschutz und Öffentlichkeit

**Grundprinzip**: Nur öffentlich verfügbare Informationen werden erfasst.

**Besondere Schutzbereiche**:
- Geburtsdatum: Optional nur Geburtsjahr angeben
- Privatadresse: Nur wenn öffentlich verfügbar (z.B. Amtsblatt)
- Kontaktdaten: Nur offizielle/öffentliche Kontakte

**Empfehlung**: Siehe separate Datenschutz-Reflexionen (07_privacy_reflections.md)

## Interoperabilität

### Globale Identifikatoren

- **Wikidata**: Primäre Quelle für Personen-IDs
- **eCH-0285**: Kompatibilität mit eCH-Standard für semantische Identifikatoren
- **Linked Open Data**: URIs erlauben Verlinkung mit anderen Datenquellen

### Referenzierung in anderen Schemas

Personen werden in anderen eCH-Standards referenziert:
- **eCH-0293** (Operations): `actor_id` verweist auf Person
- **eCH-0294** (Actors): `person_id` in Memberships und InterestLinks
- **eCH-0295** (Affairs): Autoren, Einreicher, Mitunterzeichner

## Anwendungsbeispiele

### Beispiel 1: Nationalrat mit vollständigen Angaben

```yaml
id: https://www.wikidata.org/wiki/Q493598
label: Andrea Caroni
label_long: Prof. Dr. iur. Andrea Caroni, MPA (Harvard)
birthyear: 1980
birthdate: 1980-04-19
picture: https://www.parlament.ch/[...]
names:
  - name_type: officialGivenName
    value: Andrea
  - name_type: officialLastName
    value: Caroni
    valid_from: 1980-04-19
addresses:
  - address_type: businessAddress
    street_address: Poststrasse 1
    postal_code: "9100"
    postal_locality: Herisau
languages:
  - language: de
    correspondence: true
    native: true
ch_citizenship:
  valid_from: 1980-04-19
genders:
  - value: male
    valid_from: 1980-04-19
    pronouns:
      - er
      - ihm
occupations:
  - value: Honorarprofessor
    valid_from: 2010-01-01
    active: true
    paid: true
trainings:
  - type: uni
    value: Prof. Dr. iur.
  - type: uni
    value: MPA (Harvard)
contacts:
  - type: email
    value: andrea.caroni@parl.ch
  - type: contact_website
    value: http://www.andrea-caroni.ch
electoral_district:
  district: Appenzell Ausserrhoden
  valid_from: 2015-01-01
```

### Beispiel 2: Minimale Angaben

```yaml
id: act:person_local_123
label: Max Muster
names:
  - name_type: officialGivenName
    value: Max
  - name_type: officialLastName
    value: Muster
languages:
  - language: de
    native: true
ch_citizenship:
  valid_from: 1970-01-01
```

### Beispiel 3: Person mit Namensänderung

```yaml
id: https://www.wikidata.org/wiki/Q123456
label: Petra Meier-Schmidt
names:
  - name_type: officialGivenName
    value: Petra
  - name_type: officialLastName
    value: Schmidt
    valid_from: 1975-03-15
    valid_until: 2005-06-20
  - name_type: officialLastName
    value: Meier-Schmidt
    valid_from: 2005-06-20
```

## Praktische Implementierungshinweise

### 1. Schrittweise Datenanreicherung

Start mit Minimum-Daten:
```yaml
id: [Wikidata-ID oder lokale ID]
label: [Anzeigename]
names: [Mindestens Vor- und Nachname]
```

Schrittweise ergänzen:
- Geburtsdaten
- Adressen (wenn öffentlich)
- Sprachkenntnisse
- Berufliche Informationen
- Kontaktdaten

### 2. Validierung

Vor dem Import validieren:
```bash
linkml-validate -s schema.yaml data_person.yaml
```

### 3. Konvertierung

Export in verschiedene Formate:
```bash
# JSON
linkml-convert -s schema.yaml -t json data_person.yaml > person.json

# RDF/Turtle
linkml-convert -s schema.yaml -t rdf data_person.yaml > person.ttl
```

### 4. Best Practices

- **IDs**: Immer Wikidata-IDs verwenden, wenn verfügbar
- **Datenschutz**: Nur öffentliche Informationen erfassen
- **Gültigkeit**: Zeitliche Gültigkeit für veränderliche Attribute nutzen
- **Vollständigkeit**: Nur verfügbare Daten erfassen, keine Platzhalter
- **Konsistenz**: Einheitliche Schreibweise (z.B. Ortsnamen)

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:

{{include:ech-0294_actors/output/docs/Person.md}} 


