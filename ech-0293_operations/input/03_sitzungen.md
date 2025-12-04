ToDo: Christian

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

### Beziehungen zu anderen Entitäten

Ein Meeting verbindet verschiedene Elemente des parlamentarischen Betriebs:

- **Agenda Items**: Die behandelten Traktanden
- **Votings**: Abstimmungen während der Sitzung
- **Elections**: Wahlen während der Sitzung
- **Speeches**: Wortmeldungen und Voten
- **Attendance**: Anwesenheitslisten

{{include:ech-0293_operations/output/docs/Meeting.md}}

# Anwesenheit und Wortmeldungen

Neben den formalen Entscheidungen dokumentiert der Standard auch die Teilnahme an Sitzungen und die geführten Debatten. Anwesenheitslisten erfassen wer an einer Sitzung teilgenommen hat, während Wortmeldungen die parlamentarische Debatte mit Text- und Medienaufzeichnungen festhalten.

## Attendance (Anwesenheit)

## Begriff und Bedeutung

Die Attendance (Anwesenheit) erfasst, welche Mitglieder eines parlamentarischen Organs bei einer Sitzung anwesend, abwesend oder entschuldigt waren. Sie dient der Dokumentation der Teilnahme und ist Voraussetzung für die Beschlussfähigkeit (Quorum).

## Zweiebenen-Struktur

Der Standard unterscheidet zwischen zwei Ebenen der Anwesenheitserfassung:

### 1. Attendance (Aggregierte Ebene)
Zusammenfassung der Anwesenheit für ein Meeting:
- Gesamtzahl Anwesende
- Gesamtzahl Abwesende (entschuldigt/unentschuldigt)
- Beschlussfähigkeit

### 2. IndividualAttendance (Individuelle Ebene)
Detaillierte Erfassung für jede einzelne Person:
- Wer war anwesend?
- Wer war abwesend?
- War die Abwesenheit entschuldigt?

```
Meeting (Nationalratssitzung 4. März 2024)
  └─ Attendance (Aggregierte Anwesenheit)
      ├─ IndividualAttendance (Person A: anwesend)
      ├─ IndividualAttendance (Person B: entschuldigt)
      ├─ IndividualAttendance (Person C: abwesend)
      └─ ...
```

## Attendance (Aggregierte Ebene)

### Zuordnung zu Meeting und Organ

- **meeting_id**: Verweis auf die spezifische Sitzung
- **group_id**: Verweis auf das Organ (Parlament, Kommission)

### Arten der Anwesenheitserfassung

Das Feld **attendance_type** unterscheidet:

#### start
Anwesenheit zu Beginn der Sitzung

**Anwendung:**
- Feststellung der Beschlussfähigkeit
- Offizielle Eröffnung der Sitzung
- Basis für Präsenzlisten

#### continuous
Kontinuierliche Anwesenheitserfassung

**Anwendung:**
- Elektronische Systeme mit permanenter Erfassung
- Erkennung von Zu- und Weggängen während der Sitzung

#### end
Anwesenheit am Ende der Sitzung

**Anwendung:**
- Abschliessende Kontrolle
- Seltener verwendet

### Aggregierte Zahlen

- **present_count**: Anzahl anwesender Mitglieder
- **absent_count**: Anzahl abwesender Mitglieder (unentschuldigt)
- **excused_count**: Anzahl entschuldigter Mitglieder
- **total_count**: Gesamtzahl der Mitglieder

**Beispiel:**
- Anwesend: 185
- Entschuldigt: 12
- Abwesend: 3
- Total: 200

### Beschlussfähigkeit

Das Feld **quorum_reached** zeigt an, ob das erforderliche Quorum erreicht wurde:

- **true**: Sitzung ist beschlussfähig
- **false**: Sitzung ist nicht beschlussfähig

**Konsequenz bei nicht erreichtem Quorum:**
- Sitzung kann nicht stattfinden oder muss unterbrochen werden
- Keine gültigen Beschlüsse möglich
- Vertag auf spätere Sitzung

## IndividualAttendance (Individuelle Ebene)

### Identifikation der Person

- **person_id**: Verweis auf die Person gemäss eCH-0294 Actors
- **person_name**: Name für schnellen Zugriff

### Status der Anwesenheit

Das Feld **status** erfasst den Anwesenheitsstatus:

#### present
Anwesend

**Bedeutung:** Die Person war während der (gesamten) Sitzung anwesend

#### absent
Abwesend (unentschuldigt)

**Bedeutung:** Die Person war nicht anwesend und hatte keine Entschuldigung

**Mögliche Gründe:**
- Vergessen
- Private Gründe ohne Entschuldigung
- Politisches Signal (Fernbleiben als Protest)

#### excused
Entschuldigt abwesend

**Bedeutung:** Die Person war nicht anwesend, aber ordnungsgemäss entschuldigt

**Gründe:**
- Krankheit
- Anderweitige offizielle Verpflichtungen
- Persönliche Gründe (mit Genehmigung)

#### late
Verspätet eingetroffen

**Bedeutung:** Die Person kam nach Sitzungsbeginn

#### left_early
Vorzeitig gegangen

**Bedeutung:** Die Person verliess die Sitzung vor deren Ende

### Zeiterfassung

- **arrival_time**: Zeitpunkt der Ankunft (bei Verspätung)
- **departure_time**: Zeitpunkt des Verlassens (bei vorzeitigem Weggang)

### Grund der Abwesenheit

Das Feld **reason** kann den Grund für Abwesenheit oder Verspätung erfassen:

**Beispiele:**
- "Krankheit"
- "Offizieller Auslandbesuch"
- "Sitzung Kommission XY (Überschneidung)"
- "Familiärer Notfall"

### Stellvertretung

Das Feld **substitute_person_id** erfasst, ob eine Stellvertretung anwesend war:

**Anwendung:**
- In Systemen, die Stellvertretung erlauben
- Kantone mit Ersatzmitgliedern
- Vertretungsregelungen in Kommissionen

## Unterschied: Attendance vs. IndividualVote

Wichtige Abgrenzung:

| Aspekt | Attendance | IndividualVote |
|--------|------------|----------------|
| Erfasst | Anwesenheit bei Sitzung | Stimmabgabe bei Abstimmung |
| Zeitpunkt | Beginn/während Sitzung | Zeitpunkt der Abstimmung |
| Granularität | Pro Meeting | Pro Voting |

**Beispiel:** Eine Person kann bei der Sitzung anwesend sein (Attendance: present), aber bei einer spezifischen Abstimmung als absent erfasst werden (IndividualVote: absent), weil sie in diesem Moment kurz den Raum verlassen hat.

## Verwendungszwecke

Die Attendance-Entitäten ermöglichen:

1. **Dokumentation**: Nachvollziehbare Erfassung der Teilnahme
2. **Quorum-Prüfung**: Sicherstellung der Beschlussfähigkeit
3. **Transparenz**: Öffentliche Information über Anwesenheit
4. **Rechenschaft**: Kontrolle der Pflichtenerfüllung
5. **Statistik**: Auswertung von Anwesenheitsquoten
6. **Administration**: Berechnung von Entschädigungen und Spesen

{{include:ech-0293_operations/output/docs/Attendance.md}}

{{include:ech-0293_operations/output/docs/IndividualAttendance.md}}

