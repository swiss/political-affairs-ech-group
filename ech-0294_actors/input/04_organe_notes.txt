# Gruppen und Organe (Groups)

## Einführung und Zielsetzung

Das Group-Schema beschreibt politische Gruppen, Organisationen und Körperschaften im schweizerischen politischen System. Ein Organ ist in dieser Definition eine Ansammlung von Personen, die durch einen Typ und weitere Attribute charakterisiert wird.

**Kernziele:**
- **Strukturierung**: Einheitliche Erfassung aller politischen Akteure (Legislative, Exekutive, Judikative, Zivilgesellschaft)
- **Hierarchien**: Abbildung von Organisationsstrukturen (Parteien, Kommissionen, Departemente)
- **Föderalismus**: Unterstützung aller föderalen Ebenen (Bund, Kantone, Gemeinden)
- **Mehrsprachigkeit**: Multilinguale Namen und Abkürzungen

## Anwendungszwecke

Das Schema unterstützt verschiedene Einsatzszenarien:

1. **Organisation innerhalb eines Parlamentssystems**: Parlamente, Kommissionen, Fraktionen
2. **Publikation an die Öffentlichkeit**: Transparente Darstellung politischer Strukturen
3. **Systeme mit politischen Personen**: Zuordnung von Personen zu Gruppen (Memberships)
4. **Analysen**: Untersuchungen von Gruppenzusammensetzungen und Netzwerken
5. **Parteilisten**: Verwaltung von Wahllisten (z.B. UNIBE Parteilisten-Datenbank)

## Technische Struktur

### Identifikatoren

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `id` | URI | Ja | Lokaler Identifikator |
| `uri` | URI | Nein | Global gültiger Identifikator (z.B. politics.ld.admin.ch/party/1) |

**Beispiel:**
```yaml
id: act:sp_basel_stadt
uri: https://politics.ld.admin.ch/party/sp_basel_stadt
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `id` | URI | Eindeutiger Identifikator |
| `group_type` | GroupTypeEnum | Art der Gruppe (siehe Klassifikation unten) |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `uri` | URI | Global auflösbare URI (eCH-0285 kompatibel) |
| `type_label` | string | Spezifischer lokaler Typ-Name (wenn Enum nicht ausreicht) |
| `valid_from` | date | Beginn der Gültigkeit |
| `valid_until` | date | Ende der Gültigkeit |
| `name` | MultilingualString[] | Name (mehrsprachig) |
| `abbreviation` | MultilingualString[] | Abkürzung (mehrsprachig) |
| `description` | MultilingualString[] | Beschreibung |
| `landing_page` | URI | URL mit weiteren Informationen |
| `parent_groups` | string[] | Übergeordnete Gruppen (0..n) |
| `spatial` | string | Räumliche Referenz (Gemeinde-/Kantonsnummer) |
| `contacts` | Contact[] | Kontaktinformationen |
| `addresses` | Address[] | Adressen |
| `url_statutes` | URI | URL zu Statuten (speziell für Parteien) |
| `party_color` | string | Parteifarbe (speziell für Parteien) |
| `datetime_updated` | datetime | Letzte Aktualisierung |
| `datetime_created` | datetime | Erstellung |

## Klassifikation: GroupTypeEnum

### Legislative

#### parliament (Parlament)
Parlamente auf allen föderalen Ebenen.

**Beispiele:**
- Bundesversammlung (Bund)
- Nationalrat
- Ständerat
- Grosser Rat (Kanton)
- Kantonsrat
- Gemeindeparlament

```yaml
group_type: parliament
name:
  - text: Nationalrat
    language: de
  - text: Conseil national
    language: fr
  - text: Consiglio nazionale
    language: it
spatial: https://ld.admin.ch/country/1  # Schweiz
```

#### commission (Kommission)
Ständige oder Ad-hoc-Kommissionen.

**Untertypen:**
- Ständige Kommissionen (z.B. Finanzkommission)
- Ad-hoc-Kommissionen
- Aufsichtskommissionen (Geschäftsprüfungskommission, GPK)
- Sachkommissionen
- PUK (Parlamentarische Untersuchungskommission)
- Rechnungsprüfungskommission

```yaml
group_type: commission
name:
  - text: Geschäftsprüfungskommission des Nationalrats
    language: de
type_label: Ständige Aufsichtskommission
parent_groups:
  - act:nationalrat
```

#### delegation (Delegation)
Parlamentarische Delegationen.

```yaml
group_type: delegation
name:
  - text: Delegation für internationale Finanzfragen
    language: de
```

#### faction (Fraktion)
Parlamentsfraktionen.

```yaml
group_type: faction
name:
  - text: SP-Fraktion
    language: de
abbreviation:
  - text: SP
    language: de
parent_groups:
  - act:nationalrat
```

#### parliamentary_bureau (Parlamentsbüro)
Organisatorisches Leitungsgremium.

```yaml
group_type: parliamentary_bureau
name:
  - text: Büro des Nationalrats
    language: de
```

#### presidency (Präsidium)
Präsidium des Parlaments.

```yaml
group_type: presidency
name:
  - text: Präsidium der Bundesversammlung
    language: de
```

### Exekutive

#### government (Regierung)
Regierung als Gesamtorgan.

**Beispiele:**
- Bundesrat
- Regierungsrat (Kantone)
- Stadtrat / Gemeinderat

```yaml
group_type: government
name:
  - text: Bundesrat
    language: de
  - text: Conseil fédéral
    language: fr
spatial: https://ld.admin.ch/country/1
```

#### department (Departement)
Verwaltungsdepartemente.

```yaml
group_type: department
name:
  - text: Eidgenössisches Departement des Innern
    language: de
abbreviation:
  - text: EDI
    language: de
parent_groups:
  - act:bundesrat
```

#### office (Amt)
Ämter innerhalb von Departementen.

```yaml
group_type: office
name:
  - text: Bundesamt für Gesundheit
    language: de
abbreviation:
  - text: BAG
    language: de
parent_groups:
  - act:edi
```

#### extraparliamentary_commission (Außerparlamentarische Kommission)
APK mit Regierungsauftrag.

**Beispiele:**
- Bankrat der Schweizerischen Nationalbank
- Eidgenössische Finanzmarktaufsicht (FINMA)

```yaml
group_type: extraparliamentary_commission
name:
  - text: Bankrat der SNB
    language: de
```

#### workgroup (Arbeitsgruppe)
Ad-hoc-Arbeitsgruppen.

```yaml
group_type: workgroup
name:
  - text: Arbeitsgruppe Klimapolitik
    language: de
valid_from: 2024-01-01
valid_until: 2024-12-31
```

### Judikative

#### court (Gericht)
Gerichte aller Instanzen.

**Beispiele:**
- Bundesgericht
- Kantonsgericht
- Bezirksgericht

```yaml
group_type: court
name:
  - text: Bundesgericht
    language: de
  - text: Tribunal fédéral
    language: fr
  - text: Tribunale federale
    language: it
spatial: https://ld.admin.ch/country/1
```

### Zivilgesellschaft

#### party (Partei)
Politische Parteien auf allen föderalen Ebenen.

**Wichtig:** Jede föderale Ebene wird als eigene Gruppe geführt.

```yaml
group_type: party
name:
  - text: SP Schweiz
    language: de
abbreviation:
  - text: SP
    language: de
url_statutes: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
party_color: "#FF0000"
spatial: https://ld.admin.ch/country/1
```

**Hierarchie-Beispiel:**
```yaml
# SP Schweiz (Bund)
- id: act:sp_schweiz
  group_type: party
  name: [{text: "SP Schweiz", language: de}]
  spatial: https://ld.admin.ch/country/1

# SP Basel-Stadt (Kanton)
- id: act:sp_basel_stadt
  group_type: party
  name: [{text: "SP Basel-Stadt", language: de}]
  parent_groups: [act:sp_schweiz]
  spatial: https://ld.admin.ch/canton/12

# SP Riehen (Gemeinde)
- id: act:sp_riehen
  group_type: party
  name: [{text: "SP Riehen", language: de}]
  parent_groups: [act:sp_basel_stadt]
  spatial: https://ld.admin.ch/municipality/2703
```

#### list (Liste)
Wahllisten, können Teil einer Partei sein oder unabhängig.

```yaml
group_type: list
name:
  - text: Liste 1 - SP
    language: de
parent_groups:
  - act:sp_basel_stadt  # Optional: Zugehörigkeit zur Partei
```

#### interest_group (Interessengruppe)
Lobbyorganisationen und Interessenverbände.

```yaml
group_type: interest_group
name:
  - text: Economiesuisse
    language: de
```

#### association (Verein)
Vereine und Verbände.

```yaml
group_type: association
name:
  - text: Pro Natura
    language: de
```

#### petition_carrier (Petitionsträger)
Träger von Petitionen oder Volksinitiativen.

```yaml
group_type: petition_carrier
name:
  - text: Komitee für bezahlbare Krankenkassen
    language: de
```

### Andere Organe

#### control_body (Kontrollorgan)
Kontroll- und Aufsichtsorgane.

**Beispiele:**
- Eidgenössische Finanzkontrolle (EFK)
- AB-BA (Aufsichtsbehörde)

```yaml
group_type: control_body
name:
  - text: Eidgenössische Finanzkontrolle
    language: de
abbreviation:
  - text: EFK
    language: de
```

#### parliamentary_services (Parlamentsdienste)
Unterstützungsdienste des Parlaments.

```yaml
group_type: parliamentary_services
name:
  - text: Parlamentsdienste der Bundesversammlung
    language: de
```

#### university (Universität)
Universitäten und Hochschulen (als ausgelagerte Träger öffentlicher Aufgaben).

```yaml
group_type: university
name:
  - text: Universität Zürich
    language: de
abbreviation:
  - text: UZH
    language: de
```

## Hierarchien und parent_groups

Das Attribut `parent_groups` erlaubt die Abbildung von Organisationsstrukturen:

### Parteihierarchie (Föderalismus)

```yaml
# National
- id: act:fdp_schweiz
  parent_groups: []

# Kantonal
- id: act:fdp_zuerich
  parent_groups: [act:fdp_schweiz]

# Kommunal
- id: act:fdp_winterthur
  parent_groups: [act:fdp_zuerich]
```

### Verwaltungshierarchie

```yaml
# Departement
- id: act:edi
  parent_groups: [act:bundesrat]

# Amt
- id: act:bag
  parent_groups: [act:edi]

# Abteilung
- id: act:bag_abteilung_gesundheitspolitik
  parent_groups: [act:bag]
```

### Kommissionshierarchie

```yaml
# Hauptkommission
- id: act:sik_nr
  name: [{text: "Sicherheitspolitische Kommission NR", language: de}]
  parent_groups: [act:nationalrat]

# Subkommission
- id: act:sik_nr_sub_cyber
  name: [{text: "Subkommission Cybersicherheit", language: de}]
  parent_groups: [act:sik_nr]
```

## Räumliche Referenz (spatial)

Das Attribut `spatial` verknüpft Gruppen mit Gemeinden, Kantonen oder dem Bund:

**Formate:**
- Gemeinde: `https://ld.admin.ch/municipality/[BFS-Nr]`
- Kanton: `https://ld.admin.ch/canton/[Kantonsnr]`
- Bund: `https://ld.admin.ch/country/1`

**Beispiele:**
```yaml
# Gemeinde Zürich (BFS 261)
spatial: https://ld.admin.ch/municipality/261

# Kanton Zürich
spatial: https://ld.admin.ch/canton/1

# Bund
spatial: https://ld.admin.ch/country/1
```

## Mehrsprachigkeit

Namen und Abkürzungen sind mehrsprachig erfassbar:

```yaml
name:
  - text: Bundesversammlung
    language: de
  - text: Assemblée fédérale
    language: fr
  - text: Assemblea federale
    language: it
  - text: Assamblea federala
    language: rm

abbreviation:
  - text: BVers
    language: de
  - text: AsFed
    language: fr
```

## Partei-spezifische Attribute

### url_statutes
Link zu den Parteistatuten (PDF oder Webseite).

```yaml
url_statutes: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
```

### party_color
Parteifarbe als Hexadezimalwert.

```yaml
party_color: "#FF0000"  # SP
party_color: "#0066CC"  # FDP
party_color: "#008000"  # Grüne
party_color: "#FF6600"  # SVP
party_color: "#FF9900"  # CVP/Mitte
```

## Interoperabilität

### Verknüpfung mit Memberships

Gruppen werden über Memberships mit Personen verbunden:

```yaml
# Container-Struktur
groups:
  - id: act:sp_basel_stadt
    group_type: party
    name: [{text: "SP Basel-Stadt", language: de}]

memberships:
  - id: act:membership_jans_sp
    person_id: https://www.wikidata.org/wiki/Q813067
    group_id: act:sp_basel_stadt
    role: Mitglied
    valid_from: 1990-01-01
```

### Verknüpfung mit eCH-0293 (Operations)

Gruppen werden in Operations als `actor_id` referenziert:

```yaml
# eCH-0293 Meeting
actor_id: act:nationalrat
actor_name: Nationalrat
```

## Anwendungsbeispiele

### Beispiel 1: Nationalrat

```yaml
id: act:nationalrat
uri: https://politics.ld.admin.ch/parliament/nationalrat
group_type: parliament
name:
  - text: Nationalrat
    language: de
  - text: Conseil national
    language: fr
  - text: Consiglio nazionale
    language: it
abbreviation:
  - text: NR
    language: de
  - text: CN
    language: fr
landing_page: https://www.parlament.ch/de/organe/nationalrat
spatial: https://ld.admin.ch/country/1
datetime_created: 2024-01-01T00:00:00Z
```

### Beispiel 2: Geschäftsprüfungskommission

```yaml
id: act:gpk_nr
group_type: commission
name:
  - text: Geschäftsprüfungskommission des Nationalrats
    language: de
abbreviation:
  - text: GPK-N
    language: de
type_label: Ständige Aufsichtskommission
parent_groups:
  - act:nationalrat
landing_page: https://www.parlament.ch/de/organe/kommissionen/aufsichtskommissionen/gpk
```

### Beispiel 3: Partei mit Hierarchie

```yaml
# Bundesebene
- id: act:gruene_schweiz
  group_type: party
  name:
    - text: Grüne Schweiz
      language: de
    - text: Les Verts Suisses
      language: fr
  abbreviation:
    - text: GPS
      language: de
  party_color: "#84B414"
  url_statutes: https://www.gruene.ch/statuten
  spatial: https://ld.admin.ch/country/1

# Kantonsebene
- id: act:gruene_bern
  group_type: party
  name:
    - text: Grüne Kanton Bern
      language: de
  parent_groups:
    - act:gruene_schweiz
  spatial: https://ld.admin.ch/canton/2
  landing_page: https://www.gruenebern.ch
```

### Beispiel 4: Bundesrat

```yaml
id: act:bundesrat
uri: https://politics.ld.admin.ch/government/bundesrat
group_type: government
name:
  - text: Bundesrat
    language: de
  - text: Conseil fédéral
    language: fr
  - text: Consiglio federale
    language: it
spatial: https://ld.admin.ch/country/1
landing_page: https://www.admin.ch/gov/de/start/bundesrat.html
contacts:
  - type: email
    value: info@gs-uvek.admin.ch
  - type: contact_website
    value: https://www.admin.ch/gov/de/start/bundesrat.html
addresses:
  - address_type: businessAddress
    street_address: Bundeshaus West
    postal_code: "3003"
    postal_locality: Bern
```

### Beispiel 5: Fraktion

```yaml
id: act:sp_fraktion_nr
group_type: faction
name:
  - text: SP-Fraktion im Nationalrat
    language: de
abbreviation:
  - text: SP
    language: de
parent_groups:
  - act:nationalrat
  - act:sp_schweiz  # Verbindung zur Partei
landing_page: https://www.sp-ps.ch/fraktion
```

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:

{{include:ech-0294_actors/output/docs/Group.md}}
