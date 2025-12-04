# Zeitliche Organisation des Ratsbetriebs

Der parlamentarische Betrieb ist zeitlich auf drei Ebenen organisiert: Legislaturperioden bilden den langfristigen Rahmen, Sessions strukturieren die Arbeit innerhalb einer Legislature, und Meetings sind die konkreten Sitzungen, in denen Geschäfte beraten werden. Diese Hierarchie ermöglicht sowohl langfristige Planung als auch flexible Anpassung an aktuelle Erfordernisse.

## Legislature (Legislaturperiode)

### Begriff und Bedeutung

Eine Legislaturperiode bezeichnet den Zeitraum, für den ein Parlament gewählt wird und in seiner aktuellen Zusammensetzung tätig ist. Sie bildet die oberste zeitliche Gliederungseinheit des parlamentarischen Betriebs und markiert den Rahmen für die legislative Arbeit eines Parlaments.

In der Schweiz variiert die Dauer von Legislaturperioden je nach Föderalebene:

- **Bundesebene**: 4 Jahre (Nationalrat und Ständerat)
- **Kantone**: Meist 4 Jahre, in einigen Kantonen auch 5 Jahre
- **Gemeinden**: Unterschiedlich, häufig 4 Jahre

### Struktur und Hierarchie

Die Legislaturperiode steht hierarchisch über den Sessions (Sessionen) und Meetings (Sitzungen):

```
Legislature (Legislaturperiode)
  └─ Sessions (z.B. Frühjahrssession, Herbstsession)
      └─ Meetings (einzelne Sitzungen)
          └─ Agenda Items (Traktanden)
```

### Parlamentarischer Kontext

Jede Legislature ist einem spezifischen parlamentarischen Organ zugeordnet, identifiziert durch:

- **group_id**: Verweis auf das Parlament (z.B. Nationalrat, Kantonsrat)
- **group_name**: Name des Organs für schnelle Referenz
- **body_key**: Optionaler Schlüssel zur Unterscheidung (z.B. "NR" für Nationalrat, "SR" für Ständerat)

Diese Verweise verwenden Identifikatoren aus dem eCH-0294 Actors Standard, der die politischen Akteure und Organe definiert.

### Zeitliche Einordnung

Eine Legislaturperiode wird charakterisiert durch:

- **begin_date**: Beginn der Legislaturperiode (meist nach Wahlen)
- **end_date**: Ende der Legislaturperiode (vor den nächsten Wahlen)

Beispiel Bundesebene: Die 51. Legislaturperiode des Schweizer Parlaments dauerte vom 5. Dezember 2019 bis zum 4. Dezember 2023.

### Mehrsprachigkeit

Da die Schweiz ein mehrsprachiges Land ist, werden Namen und Beschreibungen mehrsprachig erfasst:

- **name**: Array von MultilingualString-Objekten (z.B. "51. Legislatur", "51e législature", "51a legislatura")
- **url**: Mehrsprachige URLs zu weiterführenden Informationen

### Anwendungsbeispiele

#### Bundesebene
Die Bundesversammlung arbeitet in 4-jährigen Legislaturperioden. Innerhalb einer Legislature finden jährlich vier ordentliche Sessions statt (Frühlings-, Sommer-, Herbst- und Wintersession).

#### Kantone
Kantone mit Milizparlamenten haben oft kürzere, aber häufigere Sessions innerhalb einer Legislaturperiode. Kantonsparlamente mit vollamtlichen Mitgliedern ähneln strukturell dem Bundesparlament.

#### Gemeinden
In Gemeinden mit Parlamenten (üblicherweise grössere Städte) entspricht die Structure weitgehend derjenigen auf Kantonsebene. Gemeinden mit Gemeindeversammlungen kennen keine klassischen Legislaturperioden im engeren Sinne.

### Verwendung im Standard

Die Legislature-Entität dient primär dazu:

1. Zeitliche Kontextualisierung aller parlamentarischen Aktivitäten
2. Filterung und Abfrage von Daten nach Wahlperioden
3. Historische Analysen über mehrere Legislaturperioden hinweg
4. Zuordnung von Mitgliedschaften und Mandaten zu bestimmten Perioden

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (Sitzungsperiode)

### Begriff und Bedeutung

Eine Session bezeichnet eine zusammenhängende Sitzungsperiode eines Parlaments, in der mehrere Meetings (Sitzungen) stattfinden. Sie bildet die mittlere zeitliche Gliederungseinheit zwischen der Legislaturperiode und den einzelnen Sitzungen.

### Unterscheidung: Session vs. Meeting

Diese Unterscheidung ist wichtig für das Verständnis des Standards:

- **Session**: Eine Sitzungsperiode, die sich typischerweise über mehrere Tage oder Wochen erstreckt
- **Meeting**: Eine einzelne Sitzung innerhalb einer Session

#### Beispiel Bundesebene

Die Bundesversammlung kennt vier ordentliche Sessions pro Jahr:

- **Frühjahrssession**: Typischerweise 3 Wochen im Februar/März
- **Sommersession**: Typischerweise 3 Wochen im Mai/Juni
- **Herbstsession**: Typischerweise 3 Wochen im September
- **Wintersession**: Typischerweise 2-3 Wochen im November/Dezember

Innerhalb der Frühjahrssession 2024 fanden beispielsweise separate Meetings des Nationalrats und des Ständerats an verschiedenen Tagen statt.

### Hierarchische Einordnung

```
Legislature (51. Legislaturperiode)
  └─ Session (Frühjahrssession 2024)
      ├─ Meeting (Nationalratssitzung 4. März 2024)
      ├─ Meeting (Ständeratssitzung 4. März 2024)
      ├─ Meeting (Nationalratssitzung 5. März 2024)
      └─ ...
```

### Zuordnung zu Organen

Eine Session kann sich auf verschiedene parlamentarische Organe beziehen:

- **Vollparlament**: Sessions des National- oder Kantonsrats
- **Kommissionen**: Sitzungsperioden parlamentarischer Kommissionen
- **Gemeinsame Gremien**: Z.B. Sessions der Vereinigten Bundesversammlung

Über **group_id** und **group_name** wird das betreffende Organ referenziert (gemäss eCH-0294 Actors).

### Identifikation und Nummerierung

Sessions werden üblicherweise nummeriert:

- **number**: Laufende Nummer innerhalb der Legislature oder des Jahres
- **abbreviation**: Kurze Bezeichnung (z.B. "FS24" für Frühjahrssession 2024)
- **name**: Mehrsprachige vollständige Bezeichnung

### Zeitliche Attribute

- **begin_date**: Geplanter Beginn der Session
- **end_date**: Geplantes Ende der Session

Im Gegensatz zu Meetings gibt es auf Session-Ebene keine "actual" Daten, da die übergeordnete Planung meist eingehalten wird.

### Verwendungszwecke

Die Session-Entität ermöglicht:

1. **Gruppierung**: Zusammenfassung mehrerer thematisch oder zeitlich verbundener Sitzungen
2. **Planung**: Vorausschauende Organisation des parlamentarischen Kalenders
3. **Kommunikation**: Bündelung von Informationen für Öffentlichkeit und Medien
4. **Analyse**: Auswertung parlamentarischer Aktivitäten nach Sitzungsperioden

### Flexibilität im Standard

Der Standard ist bewusst flexibel gestaltet, um verschiedene Organisationsformen abzubilden:

- Föderaleinheiten ohne formale Sessions können diese Entität optional nutzen oder direkt auf Meetings referenzieren
- Die Verwendung von **type**-Feldern erlaubt die Differenzierung verschiedener Session-Arten

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (Einzelne Sitzung)

### Begriff und Bedeutung

Ein Meeting bezeichnet eine einzelne Sitzung eines parlamentarischen Organs. Dies ist die konkrete Veranstaltung, bei der sich die Mitglieder eines Parlaments, einer Kommission oder eines anderen Gremiums versammeln, um Geschäfte zu beraten und Beschlüsse zu fassen.

### Arten von Meetings

Der Standard unterscheidet verschiedene Meeting-Typen über das Feld **type**:

#### session
Plenarsitzungen des gesamten Parlaments oder einer Kammer

**Beispiele:**
- Nationalratssitzung während der Herbstsession
- Sitzung des Kantonsrats
- Sitzung der Vereinigten Bundesversammlung

#### committee
Sitzungen parlamentarischer Kommissionen

**Beispiele:**
- Sitzung der Kommission für Wirtschaft und Abgaben (WAK)
- Geschäftsprüfungskommission (GPK)
- Aussenpolitische Kommission (APK)

#### sitting
Spezielle Sitzungsformen

**Beispiele:**
- Landsgemeinden (in den Kantonen Glarus und Appenzell Innerrhoden)
- Bürgergemeindeversammlungen
- Gemeindeversammlungen

#### various
Andere Sitzungsformen, die nicht in die obigen Kategorien fallen

### Hierarchie und Struktur

Ein Meeting ist Teil einer Session (wenn verwendet) und enthält mehrere Agenda Items (Traktanden):

```
Session (Frühjahrssession 2024)
  └─ Meeting (Nationalratssitzung, 4. März 2024, 08:00)
      ├─ AgendaItem (Traktandum 1: Begrüssung)
      ├─ AgendaItem (Traktandum 2: Gesetzesberatung)
      └─ AgendaItem (Traktandum 3: Abstimmungen)
```

### Zeitliche Planung vs. Realität

Ein besonderes Merkmal der Meeting-Entität ist die Unterscheidung zwischen geplanten und tatsächlichen Zeitpunkten:

#### Geplante Daten
- **begin_date**: Geplanter Beginn
- **end_date**: Geplantes Ende

#### Tatsächliche Daten
- **begin_date_actual**: Tatsächlicher Beginn
- **end_date_actual**: Tatsächliches Ende

Diese Unterscheidung ist wichtig, da:
- Sitzungen sich verzögern können
- Traktanden vorgezogen oder verschoben werden
- Sitzungen früher als geplant enden können

**Anwendungsfall:** Eine für 14:00 geplante Sitzung beginnt aufgrund von Verzögerungen erst um 14:25 und endet statt um 18:00 bereits um 17:30.

### Sitzungsstatus

Das Feld **state** erfasst den aktuellen Status eines Meetings:

- **planned**: Die Sitzung ist geplant und wird wie vorgesehen stattfinden
- **canceled**: Die Sitzung wurde abgesagt
- **postponed**: Die Sitzung wurde verschoben

Dieser Status ist wichtig für:
- Aktuelle Informationen an Parlamentsmitglieder und Öffentlichkeit
- Historische Nachvollziehbarkeit von Planungsänderungen
- Automatische Benachrichtigungen bei Änderungen

### Identifikation und Nummerierung

Meetings werden identifiziert durch:

- **id**: Eindeutiger Identifikator
- **number**: Laufende Nummer (z.B. "5" für die 5. Sitzung einer Session)
- **abbreviation**: Kurze Bezeichnung (z.B. "NR-24-05")
- **name**: Mehrsprachige vollständige Bezeichnung

### Ort der Sitzung

Das Feld **location** erfasst den Sitzungsort:

- Physischer Ort: "Bundeshaus, Nationalratssaal"
- Virtuelle Sitzungen: "Videokonferenz via [Plattform]"
- Hybride Formate: "Bundeshaus und Videokonferenz"

### Zuordnung zu Organen

Wie bei Legislature und Session wird über **group_id**, **group_name** und **body_key** das zuständige Organ referenziert:

- Plenarsitzungen: Verweis auf das gesamte Parlament
- Kommissionssitzungen: Verweis auf die spezifische Kommission
- Gemeinsame Sitzungen: Verweis auf das gemeinsame Gremium

### Mehrsprachigkeit und URLs

- **name**: Array von MultilingualString für Namen in allen Landessprachen
- **url**: Mehrsprachige URLs zu Sitzungsunterlagen, Livestreams, Protokollen

### Beziehungen zu anderen Entitäten

Ein Meeting verbindet verschiedene Elemente des parlamentarischen Betriebs:

- **Agenda Items**: Die behandelten Traktanden
- **Votings**: Abstimmungen während der Sitzung
- **Elections**: Wahlen während der Sitzung
- **Speeches**: Wortmeldungen und Voten
- **Attendance**: Anwesenheitslisten

{{include:ech-0293_operations/output/docs/Meeting.md}}
