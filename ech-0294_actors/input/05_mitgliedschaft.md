# Mitgliedschaften (Memberships)

## Einführung und Zielsetzung

Das Membership-Schema bildet die Beziehung zwischen Personen und Gruppen ab. Es ist das zentrale Bindeglied im Actor-Schema und ermöglicht die Zuordnung von Personen zu Parteien, Fraktionen, Kommissionen, Parlamenten und anderen politischen Organen.

**Kernziele:**
- **Verknüpfung**: Strukturierte Verbindung zwischen Person und Group
- **Rollen**: Erfassung der Funktion innerhalb der Gruppe
- **Zeitliche Dimension**: Dokumentation von Beginn und Ende der Mitgliedschaft
- **Status**: Unterscheidung zwischen aktiven und inaktiven Mitgliedschaften
- **Stimmberechtigung**: Erfassung der Stimmberechtigung (relevant für Parlamente)

## Anwendungsszenarien

Memberships werden für verschiedene Zuordnungen verwendet:

1. **Parteimitgliedschaften**: Zugehörigkeit zu politischen Parteien
2. **Fraktionsmitgliedschaften**: Zuordnung zu parlamentarischen Fraktionen
3. **Kommissionsmitgliedschaften**: Mitarbeit in parlamentarischen Kommissionen
4. **Parlamentsmitgliedschaften**: Mandate in Parlamenten (Bund, Kantone, Gemeinden)
5. **Regierungsmitgliedschaften**: Mitgliedschaft in Exekutivorganen
6. **Delegationen**: Teilnahme an Delegationen
7. **Gremien**: Mitwirkung in Gremien und Arbeitsgruppen

## Technische Struktur

### Identifikatoren und Referenzen

Eine Membership verknüpft Person und Gruppe über deren `global_uri`:

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `global_uri` | URI | Ja | Identifikator der Mitgliedschaft |
| `concerned_person` | URI | Nein | `global_uri` der Person (z.B. Wikidata) |
| `concerned_group` | URI | Nein | `global_uri` der Gruppe |

**Beispiel:**
```yaml
global_uri: act:membership_jans_sp
concerned_person: https://www.wikidata.org/wiki/Q813067
concerned_group: act:sp_basel_stadt
```

### Datenmodell (LinkML-Auszug)

```yaml
global_uri: act:membership_jans_sp
concerned_person: https://www.wikidata.org/wiki/Q813067
concerned_group: act:sp_basel_stadt
role_type:
  role_type_enum: member
valid_from: 1990-01-01
is_active: true
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `global_uri` | URI | Eindeutiger Identifikator der Mitgliedschaft |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `concerned_person` | URI | Referenz zur Person (`global_uri`) |
| `concerned_group` | URI | Referenz zur Gruppe (`global_uri`) |
| `role_type` | RoleType | Rolle (`role_type_enum`, optional `label`) |
| `valid_from` | date | Beginn der Mitgliedschaft |
| `valid_through` | date | Ende der Mitgliedschaft |
| `is_active` | boolean | Gibt an, ob die Mitgliedschaft derzeit aktiv ist |
| `authorized_to_vote` | boolean | Stimmberechtigung (relevant für Parlamente) |
| `datetime_modified` | datetime | Letzte Aktualisierung des Datensatzes |
| `datetime_created` | datetime | Erstellung des Datensatzes |

## Rollen (`role_type`)

Das Attribut `role_type` beschreibt die Funktion der Person in der Gruppe. Standardisierte Werte über `RoleEnum` (`member`, `president`, `stellvertreter`, `other`); bei `other` zusätzlich `label` (z.B. «Sekretär», «Ersatzmitglied»).

Unterstützende Personen einer Gruppierung (Regierung/Rat) sind Mitglieder des Gremiums; die konkrete Funktion wird über `role_type` ausgedrückt (z.B. Sekretär/Sekretärin).

### RoleEnum im Schema

| `role_type_enum` | Verwendung |
|------------------|------------|
| `member` | Reguläres Mitglied (Standard) |
| `president` | Präsident/in, Vorsitz |
| `stellvertreter` | Stellvertretung |
| `other` | Weitere Rollen; `label` setzen (siehe Listen unten) |

### Typische Rollen in Parlamenten

- **Mitglied**: Reguläres Parlamentsmitglied
- **Präsident/Präsidentin**: Parlamentspräsident/in
- **Vizepräsident/Vizepräsidentin**: Stellvertretung
- **Ersatzmitglied**: Stellvertretende Person
- **Beobachter/Beobachterin**: Beobachterstatus ohne Stimmrecht

### Typische Rollen in Kommissionen

- **Mitglied**: Reguläres Kommissionsmitglied
- **Präsident/Präsidentin**: Kommissionspräsident/in
- **Vizepräsident/Vizepräsidentin**: Stellvertretung
- **Ersatzmitglied**: Stellvertretende Person
- **Sekretär/Sekretärin**: Kommissionssekretär/in (oft nicht stimmberechtigtes Mitglied)

### Typische Rollen in Parteien

- **Mitglied**: Parteimitglied
- **Präsident/Präsidentin**: Parteipräsident/in
- **Vorstandsmitglied**: Mitglied des Parteivorstands
- **Geschäftsführer/Geschäftsführerin**: Geschäftsführung
- **Ehrenmitglied**: Ehrenmitgliedschaft

### Typische Rollen in Regierungen

- **Regierungsrat/Regierungsrätin**: Mitglied der Kantonsregierung
- **Bundesrat/Bundesrätin**: Mitglied des Bundesrats
- **Bundespräsident/Bundespräsidentin**: Rotierendes Amt
- **Vizepräsident/Vizepräsidentin**: Stellvertretung

## Zeitliche Validität

### valid_from und valid_through

Mitgliedschaften haben einen klar definierten Beginn und oft auch ein Ende:

```yaml
# Parlamentsmandat mit fester Amtszeit
global_uri: act:membership_caroni_sr
concerned_person: https://www.wikidata.org/wiki/Q493598
concerned_group: act:staenderat
role_type:
  role_type_enum: member
valid_from: 2015-12-07  # Amtsantritt nach Wahl
valid_through: 2023-11-30  # Ende der Amtsperiode
authorized_to_vote: true
```

```yaml
# Parteimitgliedschaft ohne Enddatum
global_uri: act:membership_riniker_fdp
concerned_person: https://www.wikidata.org/wiki/Q77074968
concerned_group: act:fdp_aargau
role_type:
  role_type_enum: member
valid_from: 2000-01-01
# valid_through nicht gesetzt = noch aktiv
is_active: true
```

### is_active

Alternative oder Ergänzung zu `valid_from`/`valid_through`:

- `true`: Mitgliedschaft ist derzeit aktiv
- `false`: Mitgliedschaft ist inaktiv/beendet
- Nicht gesetzt: Aktivität wird aus `valid_from`/`valid_through` abgeleitet

**Verwendung:**
```yaml
# Explizite Markierung als aktiv
is_active: true
valid_from: 2019-01-01

# Explizite Markierung als beendet
is_active: false
valid_from: 2015-01-01
valid_through: 2019-12-31
```

## Stimmberechtigung (authorized_to_vote)

Das Attribut `authorized_to_vote` gibt an, ob die Person in der Gruppe stimmberechtigt ist.

**Relevant für:**
- Parlamentsmitgliedschaften
- Kommissionsmitgliedschaften
- Gremien mit Beschlussfassungen

**Nicht stimmberechtigt können sein:**
- Ersatzmitglieder (wenn nicht im Einsatz)
- Beobachter/Beobachterinnen
- Sekretärinnen/Sekretäre
- Gäste

**Beispiele:**
```yaml
# Stimmberechtigtes Mitglied
role_type:
  role_type_enum: member
authorized_to_vote: true

# Nicht stimmberechtigtes Ersatzmitglied
role_type:
  role_type_enum: other
  label: Ersatzmitglied
authorized_to_vote: false

# Kommissionssekretär ohne Stimmrecht
role_type:
  role_type_enum: other
  label: Sekretär
authorized_to_vote: false
```

## Mehrfachmitgliedschaften

Eine Person kann gleichzeitig mehrere Mitgliedschaften haben:

```yaml
# Container-Struktur
persons:
  - global_uri: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni

memberships:
  # Parteimitgliedschaft
  - global_uri: act:membership_caroni_fdp
    concerned_person: https://www.wikidata.org/wiki/Q493598
    concerned_group: act:fdp_appenzell
    role_type:
      role_type_enum: member
    valid_from: 1998-01-01
    is_active: true

  # Parlamentsmandat
  - global_uri: act:membership_caroni_sr
    concerned_person: https://www.wikidata.org/wiki/Q493598
    concerned_group: act:staenderat
    role_type:
      role_type_enum: member
    valid_from: 2015-12-07
    authorized_to_vote: true
    is_active: true

  # Fraktionsmitgliedschaft
  - global_uri: act:membership_caroni_fdp_fraktion
    concerned_person: https://www.wikidata.org/wiki/Q493598
    concerned_group: act:fdp_fraktion_sr
    role_type:
      role_type_enum: member
    valid_from: 2015-12-07
    is_active: true

  # Kommissionsmitgliedschaft
  - global_uri: act:membership_caroni_rk_sr
    concerned_person: https://www.wikidata.org/wiki/Q493598
    concerned_group: act:rechtskommission_sr
    role_type:
      role_type_enum: member
    valid_from: 2016-01-01
    valid_through: 2019-12-31
    authorized_to_vote: true
    is_active: false
```

## Hierarchische Darstellung

Memberships können auch hierarchisch organisiert werden:

### Partei → Fraktion
```yaml
# Person ist Mitglied einer Partei
- global_uri: act:membership_jans_sp
  concerned_person: https://www.wikidata.org/wiki/Q813067
  concerned_group: act:sp_schweiz
  role_type:
    role_type_enum: member
  valid_from: 1980-01-01

# Person ist Mitglied der SP-Fraktion im Nationalrat
- global_uri: act:membership_jans_sp_fraktion
  concerned_person: https://www.wikidata.org/wiki/Q813067
  concerned_group: act:sp_fraktion_nr
  role_type:
    role_type_enum: member
  valid_from: 2010-12-06
```

Die Fraktion selbst hat eine `parent_groups`-Beziehung zur Partei (siehe Group-Schema).

## Wechsel und Nachfolge

### Parteiwechsel

```yaml
# SP-Mitgliedschaft (beendet)
- global_uri: act:membership_mueller_sp
  concerned_person: act:person_mueller
  concerned_group: act:sp_zuerich
  role_type:
    role_type_enum: member
  valid_from: 2010-01-01
  valid_through: 2018-06-30
  is_active: false

# Grüne-Mitgliedschaft (neu)
- global_uri: act:membership_mueller_gruene
  concerned_person: act:person_mueller
  concerned_group: act:gruene_zuerich
  role_type:
    role_type_enum: member
  valid_from: 2018-07-01
  is_active: true
```

### Rollenwechsel innerhalb einer Gruppe

```yaml
# Reguläres Mitglied
- global_uri: act:membership_schmidt_kommission_1
  concerned_person: act:person_schmidt
  concerned_group: act:sik_nr
  role_type:
    role_type_enum: member
  valid_from: 2016-01-01
  valid_through: 2019-12-31

# Präsidentin (Nachfolge-Membership)
- global_uri: act:membership_schmidt_kommission_2
  concerned_person: act:person_schmidt
  concerned_group: act:sik_nr
  role_type:
    role_type_enum: president
  valid_from: 2020-01-01
  is_active: true
```

## Interoperabilität

### Verknüpfung im Container

```yaml
global_uri: act:political_actors_dataset
persons:
  - global_uri: https://www.wikidata.org/wiki/Q813067
    label: Beat Jans
    # ... weitere Person-Attribute

groups:
  - global_uri: act:sp_basel_stadt
    group_type:
      group_type_enum: party
    label: SP Basel-Stadt
    # ... weitere Group-Attribute

memberships:
  - global_uri: act:membership_jans_sp
    concerned_person: https://www.wikidata.org/wiki/Q813067
    concerned_group: act:sp_basel_stadt
    role_type:
      role_type_enum: member
    valid_from: 1990-01-01
    is_active: true
```

### Auswertungen
### Auswertungen

**Nach Gruppe:**
```sparql
# Alle Mitglieder der SP Basel-Stadt
SELECT ?person ?role WHERE {
  ?membership a act:Membership ;
    act:group_id act:sp_basel_stadt ;
    act:person_id ?person ;
    act:role ?role ;
    act:isActive true .
}
```

**Nach Person:**
```sparql
# Alle Gruppen von Beat Jans
SELECT ?group ?role WHERE {
  ?membership a act:Membership ;
    act:person_id <https://www.wikidata.org/wiki/Q813067> ;
    act:group_id ?group ;
    act:role ?role ;
    act:isActive true .
}
```

## Anwendungsbeispiele

### Beispiel 1: Nationalratsmandat

```yaml
global_uri: act:membership_riniker_nr
concerned_person: https://www.wikidata.org/wiki/Q77074968
concerned_group: act:nationalrat
role_type:
  role_type_enum: member
valid_from: 2019-12-02  # Amtsantritt nach Wahl 2019
valid_through: 2023-11-30  # Ende der Legislaturperiode
authorized_to_vote: true
is_active: false  # Legislatur ist beendet
datetime_created: 2019-12-02T00:00:00Z
datetime_modified: 2023-11-30T00:00:00Z
```

### Beispiel 2: Kommissionsmitgliedschaft mit Präsidium

```yaml
# Reguläres Mitglied
global_uri: act:membership_caroni_rk_1
concerned_person: https://www.wikidata.org/wiki/Q493598
concerned_group: act:rechtskommission_sr
role_type:
  role_type_enum: member
valid_from: 2016-01-01
valid_through: 2019-12-31
authorized_to_vote: true
is_active: false

# Präsident
global_uri: act:membership_caroni_rk_2
concerned_person: https://www.wikidata.org/wiki/Q493598
concerned_group: act:rechtskommission_sr
role_type:
  role_type_enum: president
valid_from: 2020-01-01
valid_through: 2023-12-31
authorized_to_vote: true
is_active: false
```

### Beispiel 3: Parteimitgliedschaft über alle Ebenen

```yaml
# Bundesebene
- global_uri: act:membership_jans_sp_ch
  concerned_person: https://www.wikidata.org/wiki/Q813067
  concerned_group: act:sp_schweiz
  role_type:
    role_type_enum: member
  valid_from: 1980-01-01
  is_active: true

# Kantonsebene
- global_uri: act:membership_jans_sp_bs
  concerned_person: https://www.wikidata.org/wiki/Q813067
  concerned_group: act:sp_basel_stadt
  role_type:
    role_type_enum: member
  valid_from: 1980-01-01
  is_active: true

# Gemeinde (optional)
- global_uri: act:membership_jans_sp_basel
  concerned_person: https://www.wikidata.org/wiki/Q813067
  concerned_group: act:sp_stadt_basel
  role_type:
    role_type_enum: other
    label: Vorstandsmitglied
  valid_from: 2000-01-01
  valid_through: 2010-12-31
  is_active: false
```

### Beispiel 4: Bundesrat

```yaml
global_uri: act:membership_luisier_vd_regierung
concerned_person: https://www.wikidata.org/wiki/Q24699807
concerned_group: act:regierungsrat_vaud
role_type:
  role_type_enum: other
  label: Conseillère d'État
valid_from: 2022-07-01
is_active: true
authorized_to_vote: true
datetime_created: 2022-07-01T00:00:00Z
```

### Beispiel 5: Fraktionsmitgliedschaft

```yaml
global_uri: act:membership_riniker_fdp_fraktion
concerned_person: https://www.wikidata.org/wiki/Q77074968
concerned_group: act:fdp_fraktion_nr
role_type:
  role_type_enum: member
valid_from: 2019-12-02
valid_through: 2023-11-30
is_active: false
datetime_created: 2019-12-02T00:00:00Z
```

### Beispiel 6: Ersatzmitglied

```yaml
global_uri: act:membership_mueller_gpk_ersatz
concerned_person: act:person_mueller
concerned_group: act:gpk_nr
role_type:
  role_type_enum: other
  label: Ersatzmitglied
valid_from: 2020-01-01
valid_through: 2023-12-31
authorized_to_vote: false  # Ersatzmitglieder sind normalerweise nicht stimmberechtigt
is_active: false
```

### Beispiel 7: Delegation

```yaml
global_uri: act:membership_caroni_delegation
concerned_person: https://www.wikidata.org/wiki/Q493598
concerned_group: act:delegation_europarat
role_type:
  role_type_enum: other
  label: Delegierter
valid_from: 2016-01-01
is_active: true
authorized_to_vote: true
```

## Auswertungsmöglichkeiten

### Aktive Mitgliedschaften

Filtern nach `is_active: true` oder `valid_through` nicht gesetzt:
```yaml
SELECT * FROM memberships
WHERE is_active = true
OR (valid_from <= CURRENT_DATE AND (valid_through IS NULL OR valid_through >= CURRENT_DATE))
```

### Historische Analysen

- Parteiwechsel über Zeit
- Durchschnittliche Dauer von Mandaten
- Fluktuation in Kommissionen
- Karrierewege (Gemeinde → Kanton → Bund)

### Netzwerkanalysen

- Welche Personen sind in denselben Gruppen?
- Ko-Mitgliedschaften in Kommissionen
- Parteizugehörigkeit vs. Fraktionszugehörigkeit

### Stimmberechtigungen

- Anzahl stimmberechtigter Mitglieder pro Gruppe
- Anteil von Ersatzmitgliedern
- Quorum-Berechnungen

## Unterschied zu InterestLink

**Membership** vs. **InterestLink**:

| Aspekt | Membership | InterestLink |
|--------|-----------|--------------|
| **Zweck** | Formale Zugehörigkeit zu politischen Gruppen | Interessenbindungen und Konflikte |
| **Zielgruppe** | Gruppen im Actor-Schema | Externe Organisationen |
| **Beispiele** | Parteimitglied, Kommissionsmitglied | Verwaltungsratsmandat, Vereinsvorstand |
| **Transparenzpflicht** | Standard-Zuordnung | Offenlegungspflicht wegen Interessenkonflikten |
| **Stimmberechtigung** | Ja (authorized_to_vote) | Nein |

**Überschneidung:**
Eine Person kann sowohl Membership (z.B. Nationalrat) als auch InterestLink (z.B. Verwaltungsrat bei Swisscom) haben.

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:

{{include:ech-0294_actors/output/docs/Membership.md}} 
