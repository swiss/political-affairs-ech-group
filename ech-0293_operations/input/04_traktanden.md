ToDo: Michel

# Traktanden und Beschlüsse

Die Tagesordnung einer Sitzung wird durch Traktanden strukturiert. Zu jedem Traktandum können Anträge gestellt und Beschlüsse gefasst werden.

## AgendaItem (Traktandum)

### Zweck der Entität

AgendaItem strukturiert die Tagesordnung einer Sitzung und verbindet die zeitliche Organisation (Meeting) mit den inhaltlichen Geschäften (Affairs aus eCH-0295). Es ist die zentrale Entität zur Abbildung des Sitzungsablaufs.

### Hierarchie und Struktur

Agenda Items können hierarchisch organisiert sein, um die Struktur komplexer Tagesordnungen abzubilden:

```
Meeting (Sitzung vom 4. März 2024)
  ├─ AgendaItem 1: Mitteilungen und Begrüssung
  ├─ AgendaItem 2: Gesetzesberatungen
  │   ├─ AgendaItem 2.1: Energiegesetz (Detailberatung)
  │   ├─ AgendaItem 2.2: Energiegesetz (Schlussabstimmung)
  │   └─ AgendaItem 2.3: Gesundheitsgesetz (Eintretensdebatte)
  └─ AgendaItem 3: Verschiedenes
```

Die Hierarchie wird über das Feld **parent_agenda_item** abgebildet, das auf das übergeordnete Traktandum verweist.

### Identifikation und Nummerierung

- **id**: Eindeutiger Identifikator
- **number**: Traktandennummer auf der Tagesordnung (z.B. "2.1", "3")
- **position**: Sortierreihenfolge (für die Darstellung)
- **title**: Titel des Traktandums

### Typen von Agenda Items

Das Feld **agenda_item_type** unterscheidet verschiedene Arten:

- **item**: Ein reguläres Traktandum mit Beratung und ggf. Abstimmung
- **item_group**: Eine Gruppe von Traktanden (z.B. "Gesetzesberatungen")
- **note**: Informative Einträge ohne Abstimmung (z.B. "Mitteilungen")

### Beziehung zu parlamentarischen Geschäften

Das Feld **affairs** verweist auf die zugehörigen parlamentarischen Geschäfte gemäss eCH-0295. Ein Traktandum kann sich auf mehrere Geschäfte beziehen:

- **Einzelnes Geschäft**: Ein Traktandum behandelt eine spezifische Vorlage
- **Mehrere Geschäfte**: Ein Traktandum fasst zusammenhängende Geschäfte zusammen
- **Kein Geschäft**: Administrative Traktanden (z.B. "Genehmigung des Protokolls")

**Beispiel:** Das Traktandum "Energiegesetz - Schlussabstimmung" verweist auf das Geschäft "23.XXX Energiegesetz" in eCH-0295.

### Zeitliche Planung

- **date_time**: Geplanter Zeitpunkt der Behandlung
- **date_time_actual**: Tatsächlicher Zeitpunkt der Behandlung

Diese Unterscheidung ist wichtig, da:
- Die Tagesordnung im Voraus festgelegt wird
- Der tatsächliche Ablauf davon abweichen kann
- Traktanden vorgezogen, verschoben oder vertagt werden können

### Status und Ergebnis

#### Status
Das Feld **status** zeigt den Bearbeitungsstand:
- "pending": Noch nicht behandelt
- "in_progress": Aktuell in Beratung
- "completed": Behandlung abgeschlossen
- "postponed": Vertagt auf eine spätere Sitzung
- "withdrawn": Zurückgezogen

#### Ergebnis
Das Feld **result** erfasst das Ergebnis der Behandlung:
- "accepted": Angenommen
- "rejected": Abgelehnt
- "referred": Zurückgewiesen (z.B. an Kommission)
- "noted": Zur Kenntnis genommen
- "no_decision": Keine Beschlussfassung

### Kategorisierung

Das Feld **category** erlaubt die Gruppierung nach inhaltlichen Kriterien:
- "Gesetzgebung"
- "Budget und Finanzen"
- "Interpellationen und Anfragen"
- "Wahlen"
- "Diverses"

Diese Kategorisierung ist nicht standardisiert und kann je nach Föderaleinheit variieren.

### Resolutionen zu Traktanden

Das Feld **resolution** verweist auf die Resolution(en), die zu diesem Traktandum gefasst wurde(n). Eine Resolution dokumentiert den formalen Beschluss:

```
AgendaItem: "Energiegesetz - Schlussabstimmung"
  └─ Resolution: "Annahme des Energiegesetzes mit 120 zu 75 Stimmen bei 5 Enthaltungen"
      └─ Voting: Details der Abstimmung
```

### Beschreibung und URL

- **description**: Ausführliche Beschreibung des Traktandums
- **url**: Array von mehrsprachigen URLs zu Sitzungsunterlagen:
  - Botschaften und Berichte
  - Anträge
  - Änderungsanträge
  - Abstimmungsergebnisse

### Besonderheiten verschiedener Verfahren

#### Gesetzgebungsverfahren
Ein Geschäft durchläuft mehrere Traktanden:
1. Eintretensdebatte
2. Detailberatung
3. Schlussabstimmung
4. Ggf. Differenzbereinigung zwischen den Räten

#### Interpellationen und Anfragen
- Einreichung als Traktandum
- Antwort der Regierung
- Ggf. Diskussion

#### Wahlen
- Wahlvorschlag als Traktandum
- Durchführung der Wahl
- Verkündung des Ergebnisses

### Verknüpfung mit anderen Entitäten

Ein AgendaItem ist das zentrale Bindeglied zwischen:

- **Meeting**: Die Sitzung, in der es behandelt wird
- **Affairs** (eCH-0295): Die inhaltlichen Geschäfte
- **Resolution**: Der formale Beschluss
- **Voting**: Die Abstimmung(en) zum Traktandum
- **Speech**: Voten und Wortmeldungen zum Traktandum

### Anwendungsbeispiele

...

### Verwendungszwecke

1. Strukturierung des Sitzungsablaufs und Tagesordnung
2. Verknüpfung zwischen Meetings und Affairs (eCH-0295)
3. Dokumentation von Status und Ergebnis pro Traktandum
4. Grundlage für Sitzungsprotokolle und Publikationen

{{include:ech-0293_operations/output/docs/AgendaItem.md}}

## Resolution (Beschluss)

### Zweck der Entität

Die Resolution-Entität erfasst den formalen Beschluss zu einem Traktandum. Sie dokumentiert **was** entschieden wurde, während Voting dokumentiert **wie** (mit welchem Verfahren und Stimmenverhältnis) entschieden wurde.

### Beziehung zu AgendaItem und Voting

```
AgendaItem (Energiegesetz - Schlussabstimmung)
  ├─ Resolution (Annahme des Energiegesetzes)
  └─ Voting (120 Ja, 75 Nein, 5 Enthaltungen)
```

Ein AgendaItem kann mehrere Resolutions haben (z.B. bei mehreren Abstimmungen zum selben Traktandum). Jede Resolution referenziert typischerweise ein Voting, das die Abstimmungsdetails enthält.

### Typen von Resolutionen

Das **resolution_type**-Feld verwendet ein kontrolliertes Vokabular:

#### accepted
Das Traktandum wurde angenommen

**Anwendung:**
- Gesetzesvorlagen wurden angenommen
- Anträge wurden gutgeheissen
- Beschlüsse wurden gefasst

#### rejected
Das Traktandum wurde abgelehnt

**Anwendung:**
- Gesetzesvorlagen wurden abgelehnt
- Anträge wurden abgewiesen
- Ablehnungsbeschlüsse

#### referred_back
Rückweisung an ein anderes Gremium

**Anwendung:**
- Rückweisung an Kommission zur Überarbeitung
- Rückweisung an Regierung
- Zurück an andere Kammer (in Zweikammersystemen)

#### noted
Zur Kenntnis genommen

**Anwendung:**
- Berichte ohne Abstimmung
- Mitteilungen
- Informative Traktanden

#### postponed
Vertagt auf später

**Anwendung:**
- Aufschub der Behandlung
- Noch nicht entscheidungsreif
- Weitere Abklärungen nötig

#### withdrawn
Zurückgezogen

**Anwendung:**
- Antragsteller zieht Vorlage zurück
- Geschäft wird nicht weiterverfolgt

#### amended
Mit Änderungen angenommen

**Anwendung:**
- Gesetz mit Amendments angenommen
- Modifizierte Fassung beschlossen
- Kompromisslösung

#### no_decision
Kein Beschluss gefasst

**Anwendung:**
- Keine Mehrheit für irgendeinen Antrag
- Patt-Situation ohne Stichentscheid
- Nicht beschlussfähig

### Designentscheid: Warum separate Resolution-Entität?

**Alternative wäre gewesen:** Resolution-Typ direkt im AgendaItem speichern.

**Gründe für separate Entität:**

1. **Mehrere Beschlüsse pro Traktandum**: Ein Traktandum kann mehrere Beschlüsse haben (z.B. erst Änderungsantrag, dann Gesamtabstimmung)

2. **Strukturierte Verknüpfung zu Votings**: Klare 1:1-Beziehung zwischen Resolution und Voting

3. **Mehrsprachige Beschlusstexte**: Resolution kann ausführliche Beschlusstexte in mehreren Sprachen enthalten

4. **Zeitliche Flexibilität**: Resolution kann zeitlich vom AgendaItem getrennt erfasst werden

### Beschlusstext

- **title**: Kurze Zusammenfassung des Beschlusses
- **description**: Ausführlicher Beschlusstext

**Beispiel:**
- title: "Annahme Energiegesetz"
- description: "Der Nationalrat nimmt das Bundesgesetz über die Energiewende in der Fassung der Kommission mit 120 zu 75 Stimmen bei 5 Enthaltungen an."

### Verknüpfung zur Abstimmung

Das Feld **voting_id** verweist auf das zugehörige Voting, das die Abstimmungsdetails enthält:

- Stimmenverhältnis
- Abstimmungsverfahren
- Einzelstimmen (bei namentlichen Abstimmungen)

**Nicht alle Resolutions haben ein Voting:**
- "Zur Kenntnis genommen" erfolgt oft ohne formale Abstimmung
- Stille Annahmen
- Administrativbeschlüsse

### Zeitstempel

- **datetime_created**: Zeitpunkt des Beschlusses
- **datetime_updated**: Letzte Änderung (z.B. bei Korrekturen)

### URLs und Dokumentation

Das Feld **url** kann auf weiterführende Dokumente verweisen:
- Detaillierte Beschlusstexte
- Begründungen
- Rechtliche Grundlagen

### Anwendungsfälle in verschiedenen Kontexten

#### Gesetzgebungsverfahren
Mehrere Resolutions zu verschiedenen Phasen:
1. Resolution "Eintreten" (accepted/rejected)
2. Resolution zu Artikel 1 (accepted/amended)
3. Resolution zu Artikel 2 (accepted)
4. Resolution Gesamtabstimmung (accepted/rejected)

#### Differenzbereinigung (Zweikammersystem)
- Resolution "Zustimmung zur Fassung des Erstrats"
- Resolution "Festhalten an eigener Fassung"
- Resolution "Annahme Kompromissvorschlag"

#### Kommissionsarbeit
- Resolution "Rückweisung an Kommission mit Zusatzauftrag"
- Resolution "Annahme Kommissionsbericht"

### Technische Überlegungen

#### Granularität
Die Granularität der Resolution-Erfassung variiert:
- **Detailliert**: Jede Einzelabstimmung erhält eigene Resolution
- **Aggregiert**: Nur finaler Beschluss wird erfasst

Der Standard erlaubt beide Ansätze.

#### Mehrsprachigkeit
Bei mehrsprachigen Parlamenten (CH, BE, etc.) müssen Beschlusstexte in allen Amtssprachen erfasst werden. Dies erfolgt über MultilingualString-Arrays in title und description.

### Verwendungszwecke

1. **Offizielle Dokumentation**: Was wurde entschieden?
2. **Rechtliche Verbindlichkeit**: Formaler Beschlussnachweis
3. **Öffentliche Information**: Verständliche Zusammenfassung komplexer Abstimmungen
4. **Geschäftsführung**: Nachverfolgung von Beschlüssen und deren Umsetzung
5. **Statistische Auswertung**: Annahme-/Ablehnungsquoten

{{include:ech-0293_operations/output/docs/Resolution.md}}

## Motion (Anträge)

### Zweck

Erfasst Anträge, die während der Sitzung gestellt werden (Änderungsanträge, Verfahrensanträge, etc.).

### Struktur

- **motion_type**: Art des Antrags
  - **amendment**: Änderungsantrag zu Gesetzestext
  - **procedural**: Verfahrensantrag (z.B. Schluss der Debatte)
  - **referral**: Rückweisungsantrag
  - **other**: Sonstige Anträge
- **title**: Kurztitel des Antrags
- **description**: Vollständiger Antragstext
- **proposer_person_id**: Antragsteller/in
- **seconder_person_id**: Mitstimmende (falls erforderlich)
- **result**: Ergebnis (accepted, rejected, withdrawn)

### Designentscheid

**Warum eigene Entität statt nur in AgendaItem?**
- Ein Traktandum kann mehrere Anträge enthalten
- Anträge haben eigene Lifecycle (gestellt, unterstützt, abgestimmt)
- Strukturierte Erfassung von Antragsteller und Unterstützern
- Separate Abstimmungen pro Antrag möglich

### Anwendung

Verknüpft mit AgendaItem und optional mit Voting:

```
AgendaItem (Energiegesetz - Art. 15)
  ├─ Motion (Änderungsantrag Person A)
  │   └─ Voting (Abstimmung über Änderungsantrag)
  ├─ Motion (Änderungsantrag Person B)
  │   └─ Voting (Abstimmung über Änderungsantrag)
  └─ Voting (Abstimmung über Artikel in Gesamtheit)
```

{{include:ech-0293_operations/output/docs/Motion.md}}
