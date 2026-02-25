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

Eine Membership verknüpft zwei Entitäten:

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `id` | URI | Ja | Eindeutiger Identifikator der Mitgliedschaft |
| `person_id` | string | Ja | Referenz zur Person |
| `group_id` | string | Ja | Referenz zur Gruppe |

**Beispiel:**
```yaml
id: act:membership_jans_sp
person_id: https://www.wikidata.org/wiki/Q813067
group_id: act:sp_basel_stadt
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `id` | string | Eindeutiger Identifikator der Mitgliedschaft |
| `person_id` | string | Referenz zur Person (lokale ID) |
| `person_uri` | string | Referenz zur Person (Wikidata-ID) |
| `group_id` | string | Referenz zur Gruppe (lokale ID) |
| `group_uri` | string | Referenz zur Gruppe (lokale ID) |


### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `role` | string | Rolle/Funktion innerhalb der Gruppe |
| `valid_from` | date | Beginn der Mitgliedschaft |
| `valid_until` | date | Ende der Mitgliedschaft |
| `is_active` | boolean | Gibt an, ob die Mitgliedschaft derzeit aktiv ist |
| `authorized_to_vote` | boolean | Stimmberechtigung (relevant für Parlamente) |
| `datetime_updated` | datetime | Letzte Aktualisierung des Datensatzes |
| `datetime_created` | datetime | Erstellung des Datensatzes |

## Rollen (role)

Das Attribut `role` beschreibt die Funktion der Person in der Gruppe.

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

### valid_from und valid_until

Mitgliedschaften haben einen klar definierten Beginn und oft auch ein Ende:

```yaml
# Parlamentsmandat mit fester Amtszeit
id: act:membership_caroni_sr
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:staenderat
role: Mitglied
valid_from: 2015-12-07  # Amtsantritt nach Wahl
valid_until: 2023-11-30  # Ende der Amtsperiode
authorized_to_vote: true
```

```yaml
# Parteimitgliedschaft ohne Enddatum
id: act:membership_riniker_fdp
person_id: https://www.wikidata.org/wiki/Q77074968
group_id: act:fdp_aargau
role: Mitglied
valid_from: 2000-01-01
# valid_until nicht gesetzt = noch aktiv
is_active: true
```

### is_active

Alternative oder Ergänzung zu `valid_from`/`valid_until`:

- `true`: Mitgliedschaft ist derzeit aktiv
- `false`: Mitgliedschaft ist inaktiv/beendet
- Nicht gesetzt: Aktivität wird aus `valid_from`/`valid_until` abgeleitet

**Verwendung:**
```yaml
# Explizite Markierung als aktiv
is_active: true
valid_from: 2019-01-01

# Explizite Markierung als beendet
is_active: false
valid_from: 2015-01-01
valid_until: 2019-12-31
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
role: Mitglied
authorized_to_vote: true

# Nicht stimmberechtigtes Ersatzmitglied
role: Ersatzmitglied
authorized_to_vote: false

# Kommissionssekretär ohne Stimmrecht
role: Sekretär
authorized_to_vote: false
```

## Mehrfachmitgliedschaften

Eine Person kann gleichzeitig mehrere Mitgliedschaften haben:

```yaml
# Container-Struktur
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni

memberships:
  # Parteimitgliedschaft
  - id: act:membership_caroni_fdp
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:fdp_appenzell
    role: Mitglied
    valid_from: 1998-01-01
    is_active: true

  # Parlamentsmandat
  - id: act:membership_caroni_sr
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:staenderat
    role: Mitglied
    valid_from: 2015-12-07
    authorized_to_vote: true
    is_active: true

  # Fraktionsmitgliedschaft
  - id: act:membership_caroni_fdp_fraktion
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:fdp_fraktion_sr
    role: Mitglied
    valid_from: 2015-12-07
    is_active: true

  # Kommissionsmitgliedschaft
  - id: act:membership_caroni_rk_sr
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:rechtskommission_sr
    role: Mitglied
    valid_from: 2016-01-01
    valid_until: 2019-12-31
    authorized_to_vote: true
    is_active: false
```

## Hierarchische Darstellung

Memberships können auch hierarchisch organisiert werden:

### Partei → Fraktion
```yaml
# Person ist Mitglied einer Partei
- id: act:membership_jans_sp
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_schweiz
  role: Mitglied
  valid_from: 1980-01-01

# Person ist Mitglied der SP-Fraktion im Nationalrat
- id: act:membership_jans_sp_fraktion
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_fraktion_nr
  role: Mitglied
  valid_from: 2010-12-06
```

Die Fraktion selbst hat eine `parent_groups`-Beziehung zur Partei (siehe Group-Schema).

## Wechsel und Nachfolge

### Parteiwechsel

```yaml
# SP-Mitgliedschaft (beendet)
- id: act:membership_mueller_sp
  person_id: act:person_mueller
  group_id: act:sp_zuerich
  role: Mitglied
  valid_from: 2010-01-01
  valid_until: 2018-06-30
  is_active: false

# Grüne-Mitgliedschaft (neu)
- id: act:membership_mueller_gruene
  person_id: act:person_mueller
  group_id: act:gruene_zuerich
  role: Mitglied
  valid_from: 2018-07-01
  is_active: true
```

### Rollenwechsel innerhalb einer Gruppe

```yaml
# Reguläres Mitglied
- id: act:membership_schmidt_kommission_1
  person_id: act:person_schmidt
  group_id: act:sik_nr
  role: Mitglied
  valid_from: 2016-01-01
  valid_until: 2019-12-31

# Präsidentin (Nachfolge-Membership)
- id: act:membership_schmidt_kommission_2
  person_id: act:person_schmidt
  group_id: act:sik_nr
  role: Präsidentin
  valid_from: 2020-01-01
  is_active: true
```

## Interoperabilität

### Verknüpfung im Container

```yaml
id: act:political_actors_dataset
persons:
  - id: https://www.wikidata.org/wiki/Q813067
    label: Beat Jans
    # ... weitere Person-Attribute

groups:
  - id: act:sp_basel_stadt
    group_type: party
    name: [{text: "SP Basel-Stadt", language: de}]
    # ... weitere Group-Attribute

memberships:
  - id: act:membership_jans_sp
    person_id: https://www.wikidata.org/wiki/Q813067
    group_id: act:sp_basel_stadt
    role: Mitglied
    valid_from: 1990-01-01
    is_active: true
```

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
id: act:membership_riniker_nr
person_id: https://www.wikidata.org/wiki/Q77074968
group_id: act:nationalrat
role: Mitglied
valid_from: 2019-12-02  # Amtsantritt nach Wahl 2019
valid_until: 2023-11-30  # Ende der Legislaturperiode
authorized_to_vote: true
is_active: false  # Legislatur ist beendet
datetime_created: 2019-12-02T00:00:00Z
datetime_updated: 2023-11-30T00:00:00Z
```

### Beispiel 2: Kommissionsmitgliedschaft mit Präsidium

```yaml
# Reguläres Mitglied
id: act:membership_caroni_rk_1
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:rechtskommission_sr
role: Mitglied
valid_from: 2016-01-01
valid_until: 2019-12-31
authorized_to_vote: true
is_active: false

# Präsident
id: act:membership_caroni_rk_2
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:rechtskommission_sr
role: Präsident
valid_from: 2020-01-01
valid_until: 2023-12-31
authorized_to_vote: true
is_active: false
```

### Beispiel 3: Parteimitgliedschaft über alle Ebenen

```yaml
# Bundesebene
- id: act:membership_jans_sp_ch
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_schweiz
  role: Mitglied
  valid_from: 1980-01-01
  is_active: true

# Kantonsebene
- id: act:membership_jans_sp_bs
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_basel_stadt
  role: Mitglied
  valid_from: 1980-01-01
  is_active: true

# Gemeinde (optional)
- id: act:membership_jans_sp_basel
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_stadt_basel
  role: Vorstandsmitglied
  valid_from: 2000-01-01
  valid_until: 2010-12-31
  is_active: false
```

### Beispiel 4: Bundesrat

```yaml
id: act:membership_luisier_vd_regierung
person_id: https://www.wikidata.org/wiki/Q24699807
group_id: act:regierungsrat_vaud
role: Conseillère d'État
valid_from: 2022-07-01
is_active: true
authorized_to_vote: true
datetime_created: 2022-07-01T00:00:00Z
```

### Beispiel 5: Fraktionsmitgliedschaft

```yaml
id: act:membership_riniker_fdp_fraktion
person_id: https://www.wikidata.org/wiki/Q77074968
group_id: act:fdp_fraktion_nr
role: Mitglied
valid_from: 2019-12-02
valid_until: 2023-11-30
is_active: false
datetime_created: 2019-12-02T00:00:00Z
```

### Beispiel 6: Ersatzmitglied

```yaml
id: act:membership_mueller_gpk_ersatz
person_id: act:person_mueller
group_id: act:gpk_nr
role: Ersatzmitglied
valid_from: 2020-01-01
valid_until: 2023-12-31
authorized_to_vote: false  # Ersatzmitglieder sind normalerweise nicht stimmberechtigt
is_active: false
```

### Beispiel 7: Delegation

```yaml
id: act:membership_caroni_delegation
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:delegation_europarat
role: Delegierter
valid_from: 2016-01-01
is_active: true
authorized_to_vote: true
```

## Auswertungsmöglichkeiten

### Aktive Mitgliedschaften

Filtern nach `is_active: true` oder `valid_until` nicht gesetzt:
```yaml
SELECT * FROM memberships
WHERE is_active = true
OR (valid_from <= CURRENT_DATE AND (valid_until IS NULL OR valid_until >= CURRENT_DATE))
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
