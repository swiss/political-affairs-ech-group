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

- **actor_id**: Verweis auf das Parlament als politischen Akteur (z.B. Nationalrat, Kantonsrat) gemäss eCH-0294 Actors
- **administrative_id**: Verwaltungs-ID der gesetzgebenden Körperschaft (z.B. Gemeinde, Kanton, Land)

### Zeitliche Einordnung

Eine Legislaturperiode wird über das Mixin `IsEventWithDuration` charakterisiert. Die wichtigsten Datumsfelder sind:

- **date_begin_planned** / **date_begin_actual**: Geplanter bzw. tatsächlicher Beginn der Legislaturperiode (meist nach Wahlen)
- **date_end_planned** / **date_end_actual**: Geplantes bzw. tatsächliches Ende der Legislaturperiode (vor den nächsten Wahlen)

Bei Bedarf gibt es analoge `datetime_*`-Varianten mit Uhrzeit.

Beispiel Bundesebene: Die 51. Legislaturperiode des Schweizer Parlaments dauerte vom 5. Dezember 2019 bis zum 4. Dezember 2023.

### Identifikation

Über das Mixin `HasIdentification` stehen `local_id`, `global_uri` und `wikidata_uri` zur Verfügung. Der `global_uri` ist Pflicht und dient als eindeutiger Identifikator.

### Verlinkte Dokumente

Über den Slot **documents** können relevante Dokumente (z.B. Mitgliederverzeichnisse der Legislatur, Geschäftsverzeichnisse) als FRBR-Works verknüpft werden.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (Sitzungsperiode)

### Begriff und Bedeutung

Eine Session bezeichnet eine zusammenhängende Sitzungsperiode eines Parlaments, in der mehrere Meetings (Sitzungen) stattfinden. Sie bildet die mittlere zeitliche Gliederungseinheit zwischen der Legislaturperiode und den einzelnen Sitzungen.

### Unterscheidung: Session vs. Meeting

Diese Unterscheidung ist wichtig für das Verständnis des Standards:

- **Session**: Eine Sitzungsperiode, die sich typischerweise über mehrere Tage oder Wochen erstreckt
- **Meeting**: Eine einzelne Sitzung innerhalb einer Session

#### Beispiel Bundesebene
```
Legislature (51. Legislaturperiode)
  └─ Session (Frühjahrssession 2024)
      ├─ Meeting (Nationalratssitzung 4. März 2024)
      ├─ Meeting (Ständeratssitzung 4. März 2024)
      ├─ Meeting (Nationalratssitzung 5. März 2024)
      └─ ...
```

### Zuordnung zu Organen

Eine Session bezieht sich auf das politische Organ, das die Sessionen als Reihe von Sitzungen organisiert. Beispiele:

- **Parlament**: Sessions eines Kantonsrats oder der Bundesversammlung
- **Kommissionen**: Sitzungsperioden parlamentarischer Kommissionen
- **Gemeinsame Gremien**: Z.B. Sessions der Vereinigten Bundesversammlung

Über **body_key** kann das Organ (z.B. "NR" für Nationalrat, "SR" für Ständerat) als Schlüssel hinterlegt werden. Über **parent_legislature** wird die Session der zugehörigen Legislaturperiode zugeordnet.

### Identifikation und Nummerierung

Sessions werden üblicherweise nummeriert. Folgende Slots stehen zur Verfügung — sie sind kompatibel mit der entsprechenden Modellierung bei Meeting:

- **number**: Laufende Nummer (z.B. innerhalb der Legislature oder des Jahres)
- **sequential_number**: Laufende Nummer als String (auch römische Ziffern möglich)
- **position**: Ganzzahlige Position
- **abbreviation**: Kurze Bezeichnung (z.B. "FS24" für Frühjahrssession 2024)
- **name**: Mehrsprachige vollständige Bezeichnung

Über das Mixin `HasIdentification` stehen zusätzlich `local_id`, `global_uri` und `wikidata_uri` zur Verfügung.

### Zeitliche Attribute

Sessions nutzen das Mixin `IsEventWithDuration` und bieten damit dieselben Datumsfelder wie Legislatures und Meetings:

- **date_begin_planned** / **datetime_begin_planned**: Geplanter Beginn der Session
- **date_begin_actual** / **datetime_begin_actual**: Tatsächlicher Beginn
- **date_end_planned** / **datetime_end_planned**: Geplantes Ende der Session
- **date_end_actual** / **datetime_end_actual**: Tatsächliches Ende

### Verknüpfungen

- **meetings**: Liste der Sitzungen innerhalb der Session
- **documents**: Verknüpfte FRBR-Works (z.B. Sessionsprogramm, Sessionsvorschau)
- **url**: Landing Page der Session

### Flexibilität im Standard

Der Standard ist bewusst flexibel gestaltet, um verschiedene Organisationsformen abzubilden. Föderaleinheiten ohne formale Sessions können diese Entität optional nutzen oder direkt auf Meetings referenzieren.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (Einzelne Sitzung)

### Begriff und Bedeutung

Ein Meeting bezeichnet eine einzelne Sitzung eines parlamentarischen Organs. Dies ist die konkrete Veranstaltung, bei der sich die Mitglieder eines Parlaments, einer Kommission oder eines anderen Gremiums versammeln, um Geschäfte zu beraten und Beschlüsse zu fassen.

### Arten von Meetings

Der Standard unterscheidet verschiedene Meeting-Typen über das Feld **meeting_type** (Enum `MeetingTypeEnum`):

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

Über das Mixin `IsEventWithDuration` unterscheidet das Meeting zwischen geplanten und tatsächlichen Zeitpunkten:

#### Geplante Daten
- **date_begin_planned** / **datetime_begin_planned**: Geplanter Beginn
- **date_end_planned** / **datetime_end_planned**: Geplantes Ende

#### Tatsächliche Daten
- **date_begin_actual** / **datetime_begin_actual**: Tatsächlicher Beginn
- **date_end_actual** / **datetime_end_actual**: Tatsächliches Ende

Diese Unterscheidung ist wichtig, da:
- Sitzungen sich verzögern können
- Traktanden vorgezogen oder verschoben werden
- Sitzungen früher als geplant enden können

**Anwendungsfall:** Eine für 14:00 geplante Sitzung beginnt aufgrund von Verzögerungen erst um 14:25 und endet statt um 18:00 bereits um 17:30.

### Sitzungsstatus

Das Feld **state** (Enum `StateEnum`) erfasst den aktuellen Status eines Meetings:

- **planned**: Die Sitzung ist geplant und wird wie vorgesehen stattfinden
- **canceled**: Die Sitzung wurde abgesagt
- **postponed**: Die Sitzung wurde verschoben

Über **state_name** kann eine abweichende, freitextliche Statusbeschreibung ergänzt werden.

Dieser Status ist wichtig für:
- Aktuelle Informationen an Parlamentsmitglieder und Öffentlichkeit
- Historische Nachvollziehbarkeit von Planungsänderungen
- Automatische Benachrichtigungen bei Änderungen

### Identifikation und Nummerierung

Meetings werden identifiziert durch:

- **local_id** / **global_uri** / **wikidata_uri** (via Mixin `HasIdentification`)
- **number**: Laufende Nummer (z.B. "5" für die 5. Sitzung einer Session)
- **sequential_number**: Laufende Nummer als String (auch römische Ziffern möglich)
- **position**: Ganzzahlige Position innerhalb der Session
- **abbreviation**: Kurze Bezeichnung (z.B. "NR-24-05")
- **name**: Mehrsprachige vollständige Bezeichnung

### Ort der Sitzung

Das Feld **location** erfasst den Sitzungsort:

- Physischer Ort: "Bundeshaus, Nationalratssaal"
- Virtuelle Sitzungen: "Videokonferenz via [Plattform]"
- Hybride Formate: "Bundeshaus und Videokonferenz"

### Zuordnung zu Organen

Das zuständige Organ wird über **actor_id** (gemäss eCH-0294 Actors) referenziert. Über **actor_name** kann zusätzlich der Name des Organs für schnellen Zugriff festgehalten werden, über **body_key** ein kurzer Schlüssel (z.B. "NR", "SR"). Über **administrative_id** kann die Verwaltungsebene angegeben werden, **group_name** und **group_id** ergänzen Gruppierungen wo nötig.

- Plenarsitzungen: Verweis auf das gesamte Parlament
- Kommissionssitzungen: Verweis auf die spezifische Kommission
- Gemeinsame Sitzungen: Verweis auf das gemeinsame Gremium

### Hierarchische Verknüpfungen

- **parent_meeting**: Falls ein Meeting Teil eines übergeordneten Meetings ist
- **parent_legislature**: Die Legislatur, in deren Rahmen das Meeting stattfindet

### Beziehungen zu anderen Entitäten

Ein Meeting verbindet verschiedene Elemente des parlamentarischen Betriebs:

- **Agenda Items**: Die behandelten Traktanden
- **Votings**: Abstimmungen während der Sitzung
- **Elections**: Wahlen während der Sitzung
- **Speeches**: Wortmeldungen und Voten
- **Attendance**: Anwesenheitslisten (über `Attendance.parent_meeting`)
- **documents**: Verknüpfte FRBR-Works (Protokolle, Sitzungsunterlagen, Tagblatt etc.)

{{include:ech-0293_operations/output/docs/Meeting.md}}

{{include:ech-0293_operations/output/docs/MeetingTypeEnum.md}}

{{include:ech-0293_operations/output/docs/StateEnum.md}}

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

- **parent_meeting**: Verweis auf die spezifische Sitzung, zu der die Anwesenheitsliste gehört
- **actor_id**: Verweis auf das Organ (Parlament, Kommission) gemäss eCH-0294 Actors
- **datetime_begin**: Zeitpunkt der Anwesenheitserfassung

### Aggregierte Zahlen

- **total_count**: Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen, z.B. 200 für Nationalrat, 46 für Ständerat)
- **total_present**: Anzahl anwesender Mitglieder
- **total_excused**: Anzahl entschuldigter Mitglieder
- **total_absent**: Anzahl unentschuldigt abwesender Mitglieder

**Beispiel:**
- Total: 200
- Anwesend: 185
- Entschuldigt: 12
- Abwesend: 3

### Beschlussfähigkeit

Die Beschlussfähigkeit (Quorum) ergibt sich aus dem Verhältnis von `total_present` zu `total_count` und den jeweiligen Quorum-Regeln des Gremiums. Sie wird daher nicht als eigenes Feld gespeichert, sondern bei Bedarf datenseitig berechnet.

## IndividualAttendance (Individuelle Ebene)

### Verknüpfung

- **parent_attendance**: Verweis auf das übergeordnete `Attendance`-Aggregat (das wiederum am Meeting hängt). So wird die individuelle Erfassung sauber dem Meeting zugeordnet.
- **actor_id**: Verweis auf die Person gemäss eCH-0294 Actors

### Anwesenheitstyp

Das Feld **attendance_type** (Enum `AttendanceTypeEnum`) erfasst die Art der Anwesenheit:

- **present**: Persönlich anwesend
- **remote**: Per Fernzugriff (z.B. Videokonferenz) anwesend
- **substitute**: Stellvertretung — eine andere Person hat in der Vertretung teilgenommen

> Die Modellierung der Stellvertretung (z.B. wer hat wen vertreten, mit welchem Stimmrecht) wird in [Issue #24](https://github.com/swiss/political-affairs-ech-group/issues/24) weiter ausgearbeitet.
>
> Eine zweite Status-Achse `present` / `excused` / `absent` ("ob anwesend") parallel zur bestehenden Achse "wie anwesend" ist als Erweiterung in Diskussion.

### Grund

Das Feld **reason** (mehrsprachig) kann den Grund für Abwesenheit oder Verspätung als Freitext erfassen.

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

{{include:ech-0293_operations/output/docs/AttendanceTypeEnum.md}}

