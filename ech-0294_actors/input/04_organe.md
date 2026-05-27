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
| `global_uri` | URI | Ja | Global gültiger Identifikator (z.B. `politics.ld.admin.ch/party/...`) |
| `local_id` | string | Nein | Lokaler Identifikator im publizierenden System |
| `wikidata_uri` | URI | Nein | Wikidata-Entität der Gruppe, falls vorhanden |

**Beispiel:**
```yaml
global_uri: https://politics.ld.admin.ch/party/sp_basel_stadt
local_id: act:sp_basel_stadt
```

### Datenmodell (LinkML-Auszug)

```yaml
global_uri: https://politics.ld.admin.ch/party/sp_basel_stadt
local_id: act:sp_basel_stadt
group_type:
  group_type_enum: party
label: SP Basel-Stadt
abbreviation:
  - value: SP
    language: de
parent_groups:
  - https://politics.ld.admin.ch/party/sp_schweiz
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `global_uri` | URI | Eindeutiger globaler Identifikator |
| `group_type` | GroupType | Art der Gruppe (`group_type_enum`, optional `label`) |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `local_id` | string | Lokaler Identifikator |
| `wikidata_uri` | URI | Wikidata-Referenz |
| `label` | string | Anzeigename der Gruppe |
| `valid_from` | date | Beginn der Gültigkeit |
| `valid_through` | date | Ende der Gültigkeit |
| `abbreviation` | MultilingualValue[] | Abkürzung (mehrsprachig, `value`/`language`) |
| `description` | MultilingualValue[] | Beschreibung (mehrsprachig) |
| `landing_page` | URI | URL mit weiteren Informationen |
| `parent_groups` | string[] | Übergeordnete Gruppen (0..n) |
| `spatial` | string | Räumliche Referenz (Gemeinde-/Kantonsnummer) |
| `contacts` | Contact[] | Kontaktinformationen |
| `addresses` | Address[] | Adressen |
| `statutes_url` | URI | URL zu Statuten (speziell für Parteien) |
| `party_color` | string | Parteifarbe (speziell für Parteien) |
| `datetime_modified` | datetime | Letzte Aktualisierung |
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
group_type:
  group_type_enum: parliament
label: Nationalrat
description:
  - value: Conseil national
    language: fr
  - value: Consiglio nazionale
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
group_type:
  group_type_enum: commission
  label: Ständige Aufsichtskommission
label: Geschäftsprüfungskommission des Nationalrats
parent_groups:
  - act:nationalrat
```

#### delegation (Delegation)
Parlamentarische Delegationen.

```yaml
group_type:
  group_type_enum: delegation
label: Delegation für internationale Finanzfragen
```

#### faction (Fraktion)
Parlamentsfraktionen.

```yaml
group_type:
  group_type_enum: faction
label: SP-Fraktion
abbreviation:
  - value: SP
    language: de
parent_groups:
  - act:nationalrat
```

#### parliamentary_bureau (Parlamentsbüro)
Organisatorisches Leitungsgremium.

```yaml
group_type:
  group_type_enum: parliamentary_bureau
label: Büro des Nationalrats
```

#### presidency (Präsidium)
Präsidium des Parlaments.

```yaml
group_type:
  group_type_enum: presidency
label: Präsidium der Bundesversammlung
```

### Exekutive

#### government (Regierung)
Regierung als Gesamtorgan.

**Beispiele:**
- Bundesrat
- Regierungsrat (Kantone)
- Stadtrat / Gemeinderat

```yaml
group_type:
  group_type_enum: government
label: Bundesrat
description:
  - value: Conseil fédéral
    language: fr
spatial: https://ld.admin.ch/country/1
```

#### department (Departement)
Verwaltungsdepartemente.

```yaml
group_type:
  group_type_enum: department
label: Eidgenössisches Departement des Innern
abbreviation:
  - value: EDI
    language: de
parent_groups:
  - act:bundesrat
```

#### office (Amt)
Ämter innerhalb von Departementen.

```yaml
group_type:
  group_type_enum: office
label: Bundesamt für Gesundheit
abbreviation:
  - value: BAG
    language: de
parent_groups:
  - act:edi
```

#### extraparliamentary_commission (Ausserparlamentarische Kommission)
APK mit Regierungsauftrag.

**Beispiele:**
- Bankrat der Schweizerischen Nationalbank
- Eidgenössische Finanzmarktaufsicht (FINMA)

```yaml
group_type:
  group_type_enum: extraparliamentary_commission
label: Bankrat der SNB
```

#### workgroup (Arbeitsgruppe)
Ad-hoc-Arbeitsgruppen.

```yaml
group_type:
  group_type_enum: workgroup
label: Arbeitsgruppe Klimapolitik
valid_from: 2024-01-01
valid_through: 2024-12-31
```

### Judikative

#### court (Gericht)
Gerichte aller Instanzen.

**Beispiele:**
- Bundesgericht
- Kantonsgericht
- Bezirksgericht

```yaml
group_type:
  group_type_enum: court
label: Bundesgericht
description:
  - value: Tribunal fédéral
    language: fr
  - value: Tribunale federale
    language: it
spatial: https://ld.admin.ch/country/1
```

### Zivilgesellschaft

#### party (Partei)
Politische Parteien auf allen föderalen Ebenen.

Jede föderale Ebene wird als eigene Gruppe geführt.

```yaml
group_type:
  group_type_enum: party
label: SP Schweiz
abbreviation:
  - value: SP
    language: de
statutes_url: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
party_color: "#FF0000"
spatial: https://ld.admin.ch/country/1
```

**Hierarchie-Beispiel:**
```yaml
# SP Schweiz (Bund)
- global_uri: act:sp_schweiz
  group_type:
    group_type_enum: party
  label: SP Schweiz
  spatial: https://ld.admin.ch/country/1

# SP Basel-Stadt (Kanton)
- global_uri: act:sp_basel_stadt
  group_type:
    group_type_enum: party
  label: SP Basel-Stadt
  parent_groups: [act:sp_schweiz]
  spatial: https://ld.admin.ch/canton/12

# SP Riehen (Gemeinde)
- global_uri: act:sp_riehen
  group_type:
    group_type_enum: party
  label: SP Riehen
  parent_groups: [act:sp_basel_stadt]
  spatial: https://ld.admin.ch/municipality/2703
```

#### list (Liste)
Wahllisten, können Teil einer Partei sein oder unabhängig.

```yaml
group_type:
  group_type_enum: list
label: Liste 1 - SP
parent_groups:
  - act:sp_basel_stadt  # Optional: Zugehörigkeit zur Partei
```

#### interest_group (Interessengruppe)
Lobbyorganisationen und Interessenverbände.

```yaml
group_type:
  group_type_enum: interest_group
label: Economiesuisse
```

#### association (Verein)
Vereine und Verbände.

```yaml
group_type:
  group_type_enum: association
label: Pro Natura
```

#### petition_carrier (Petitionsträger)
Träger von Petitionen oder Volksinitiativen.

```yaml
group_type:
  group_type_enum: petition_carrier
label: Komitee für bezahlbare Krankenkassen
```

### Andere Organe

#### control_body (Kontrollorgan)
Kontroll- und Aufsichtsorgane.

**Beispiele:**
- Eidgenössische Finanzkontrolle (EFK)
- AB-BA (Aufsichtsbehörde)

```yaml
group_type:
  group_type_enum: control_body
label: Eidgenössische Finanzkontrolle
abbreviation:
  - value: EFK
    language: de
```

#### parliamentary_services (Parlamentsdienste)
Unterstützungsdienste des Parlaments.

```yaml
group_type:
  group_type_enum: parliamentary_services
label: Parlamentsdienste der Bundesversammlung
```

#### university (Universität)
Universitäten und Hochschulen (als ausgelagerte Träger öffentlicher Aufgaben).

```yaml
group_type:
  group_type_enum: university
label: Universität Zürich
abbreviation:
  - value: UZH
    language: de
```

## Hierarchien und parent_groups

Das Attribut `parent_groups` erlaubt die Abbildung von Organisationsstrukturen:

### Parteihierarchie (Föderalismus)

```yaml
# National
- global_uri: act:fdp_schweiz
  parent_groups: []

# Kantonal
- global_uri: act:fdp_zuerich
  parent_groups: [act:fdp_schweiz]

# Kommunal
- global_uri: act:fdp_winterthur
  parent_groups: [act:fdp_zuerich]
```

### Verwaltungshierarchie

```yaml
# Departement
- global_uri: act:edi
  parent_groups: [act:bundesrat]

# Amt
- global_uri: act:bag
  parent_groups: [act:edi]

# Abteilung
- global_uri: act:bag_abteilung_gesundheitspolitik
  parent_groups: [act:bag]
```

### Kommissionshierarchie

```yaml
# Hauptkommission
- global_uri: act:sik_nr
  label: Sicherheitspolitische Kommission NR
  parent_groups: [act:nationalrat]

# Subkommission
- global_uri: act:sik_nr_sub_cyber
  label: Subkommission Cybersicherheit
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
label: Bundesversammlung
description:
  - value: Assemblée fédérale
    language: fr
  - value: Assemblea federale
    language: it
  - value: Assamblea federala
    language: rm

abbreviation:
  - value: BVers
    language: de
  - value: AsFed
    language: fr
```

## Partei-spezifische Attribute

### statutes_url
Link zu den Parteistatuten (PDF oder Webseite).

```yaml
statutes_url: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
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
  - global_uri: act:sp_basel_stadt
    group_type:
      group_type_enum: party
    label: SP Basel-Stadt

memberships:
  - global_uri: act:membership_jans_sp
    concerned_person: https://www.wikidata.org/wiki/Q813067
    concerned_group: act:sp_basel_stadt
    role_type:
      role_type_enum: member
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
global_uri: https://politics.ld.admin.ch/parliament/nationalrat
local_id: act:nationalrat
group_type:
  group_type_enum: parliament
label: Nationalrat
description:
  - value: Conseil national
    language: fr
  - value: Consiglio nazionale
    language: it
abbreviation:
  - value: NR
    language: de
  - value: CN
    language: fr
landing_page: https://www.parlament.ch/de/organe/nationalrat
spatial: https://ld.admin.ch/country/1
datetime_created: 2024-01-01T00:00:00Z
```

### Beispiel 2: Geschäftsprüfungskommission

```yaml
global_uri: act:gpk_nr
group_type:
  group_type_enum: commission
  label: Ständige Aufsichtskommission
label: Geschäftsprüfungskommission des Nationalrats
abbreviation:
  - value: GPK-N
    language: de
parent_groups:
  - act:nationalrat
landing_page: https://www.parlament.ch/de/organe/kommissionen/aufsichtskommissionen/gpk
```

### Beispiel 3: Partei mit Hierarchie

```yaml
# Bundesebene
- global_uri: act:gruene_schweiz
  group_type:
    group_type_enum: party
  label: Grüne Schweiz
  description:
    - value: Les Verts Suisses
      language: fr
  abbreviation:
    - value: GPS
      language: de
  party_color: "#84B414"
  statutes_url: https://www.gruene.ch/statuten
  spatial: https://ld.admin.ch/country/1

# Kantonsebene
- global_uri: act:gruene_bern
  group_type:
    group_type_enum: party
  label: Grüne Kanton Bern
  parent_groups:
    - act:gruene_schweiz
  spatial: https://ld.admin.ch/canton/2
  landing_page: https://www.gruenebern.ch
```

### Beispiel 4: Bundesrat

```yaml
global_uri: https://politics.ld.admin.ch/government/bundesrat
local_id: act:bundesrat
group_type:
  group_type_enum: government
label: Bundesrat
description:
  - value: Conseil fédéral
    language: fr
  - value: Consiglio federale
    language: it
spatial: https://ld.admin.ch/country/1
landing_page: https://www.admin.ch/gov/de/start/bundesrat.html
contacts:
  - contact_type: email
    value: info@gs-uvek.admin.ch
  - contact_type: contact_website
    value: https://www.admin.ch/gov/de/start/bundesrat.html
addresses:
  - address_type: businessAddress
    street_address: Bundeshaus West
    postal_code: "3003"
    postal_locality: Bern
```

### Beispiel 5: Fraktion

```yaml
global_uri: act:sp_fraktion_nr
group_type:
  group_type_enum: faction
label: SP-Fraktion im Nationalrat
abbreviation:
  - value: SP
    language: de
parent_groups:
  - act:nationalrat
  - act:sp_schweiz  # Verbindung zur Partei
landing_page: https://www.sp-ps.ch/fraktion
```

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:

{{include:ech-0294_actors/output/docs/Group.md}}
