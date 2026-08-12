\newpage

<!-- ToDo: Christian -->

# Zeitliche Organisation des Ratsbetriebs

Der Ratsbetrieb ist zeitlich in vier Klassen gegliedert:

```
Legislature (Legislaturperiode)
  └─ Session (z.B. Frühjahrssession)
      └─ Meeting (einzelne Sitzung)
          └─ AgendaItem (Traktandum)
```

Die Legislaturperiode bildet den langfristigen Rahmen, die Session strukturiert die Arbeit innerhalb einer Legislaturperiode, das Meeting ist die konkrete Sitzung, in der Geschäfte beraten werden, und das Traktandum gliedert die einzelne Sitzung. Die Ebenen greifen auf zwei Arten ineinander: Die Session nimmt ihre Sitzungen als Liste auf (`meetings`), während Sitzung und Traktandum über Referenzen nach oben zeigen (`parent_legislature`, `parent_meeting`, `parent_agenda_item`). Wer keine Sessionen führt, liefert seine Sitzungen einzeln und hängt sie über `parent_legislature` an die Legislaturperiode.

Die ersten drei Klassen sind nachfolgend beschrieben, das Traktandum im nächsten Kapitel.

## Gemeinsame Elemente

Die drei Klassen sind bewusst gleich gebaut. Die folgenden Felder haben auf allen Ebenen dieselbe Bedeutung.

**Identifikation.** `global_uri` ist der Identifikator und obligatorisch. `local_id` nimmt die Id des liefernden Systems auf, `wikidata_uri` verweist auf den Wikidata-Eintrag, sofern es einen gibt.

**Beginn und Ende.** Die Zeitangaben werden doppelt geführt: `date_begin_planned` und `date_end_planned` halten fest, was angesetzt war, `date_begin_actual` und `date_end_actual`, was tatsächlich geschah. Wo die Uhrzeit relevant ist, stehen die Varianten `datetime_*` zur Verfügung.

**Raum und Organ.** `spatial` verweist auf die Raumeinheit gemäss LINDAS — Land, Kanton, Bezirk oder Gemeinde, also `https://ld.admin.ch/canton/2` statt „BE". Es ist dasselbe Feld, mit dem eCH-0294 seine Gruppen verortet, sodass ein Ratsbetrieb und die Akteure, die ihn tragen, auf dieselbe Ressource zeigen. Wer innerhalb dieser Raumeinheit tagt, sagt `actor_id` als Kurzreferenz auf das Organ gemäss eCH-0294.

**Verlinkte Dokumente.** `documents` verknüpft Dokumente als FRBR-Works gemäss eCH-0292 — bei der Legislaturperiode etwa Mitglieder- und Geschäftsverzeichnisse, bei der Session das Sessionsprogramm, beim Meeting das Protokoll.

## Legislature (Legislaturperiode)

Eine Legislaturperiode bezeichnet den Zeitraum, für den ein Parlament gewählt wird und in seiner aktuellen Zusammensetzung tätig ist.

### Dauer und Verlauf

Die Dauer ist nicht vorgegeben — die Beispiele zeigen eine vier- und eine fünfjährige Amtsdauer. Anders als bei der Sitzung fallen Planung und Verlauf hier kaum auseinander; wo eine Legislaturperiode gesetzlich auf den Tag festgelegt ist, tragen `*_planned` und `*_actual` dieselben Daten.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (Sitzungsperiode)

Eine Session ist eine zusammenhängende Sitzungsperiode, in der mehrere Meetings stattfinden.

### Optionale Ebene

Die Session ist die einzige der drei Ebenen, auf die verzichtet werden kann: Föderaleinheiten ohne formale Sessionen lassen sie weg und führen ihre Sitzungen direkt. Session und Meeting können auch zusammenfallen — eine eintägige Sitzung des Landrats oder eine Landsgemeinde wird als Sitzungsperiode mit einer einzigen Sitzung geführt.

### Nummerierung

Nummeriert wird sehr unterschiedlich, weshalb vier Felder zur Verfügung stehen: `number` hält die laufende Nummer als Zahl fest, `sequential_number` dieselbe Angabe als Zeichenkette (und damit auch römische Ziffern), `position` die Position innerhalb der Legislaturperiode und `meeting_abbreviation` eine Kurzbezeichnung wie „FS24“. Das Meeting kennt dieselben vier Felder.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (Einzelne Sitzung)

Ein Meeting ist die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Beschlüsse gefasst und Wortmeldungen festgehalten werden.

### Sitzungstypen

`meeting_type` unterscheidet vier Typen: `session` für Plenarsitzungen eines Parlaments oder einer Kammer, `committee` für Kommissionssitzungen, `sitting` für Versammlungen wie Landsgemeinden, Gemeinde- und Bürgergemeindeversammlungen und `various` als Auffangwert. Der Wert `sitting` ist eine bewusste Setzung: Landsgemeinden und Gemeindeversammlungen sind Versammlungen der Stimmberechtigten selbst, entscheiden aber als tagendes Organ mit Traktandenliste und werden deshalb wie eine Ratssitzung abgebildet.

### Planung und Verlauf

Auf dieser Ebene fallen die geplanten und die tatsächlichen Zeiten regelmässig auseinander: Eine für 14:00 angesetzte Sitzung beginnt wegen Verzögerungen erst um 14:25 und endet statt um 18:00 bereits um 17:30. Ob eine Sitzung überhaupt wie vorgesehen stattfindet, hält `state` fest (`planned`, `canceled`, `postponed`); `state_name` nimmt eine abweichende, freitextliche Statusbezeichnung auf. `location` erfasst den Sitzungsort — den physischen Raum („Bundeshaus, Nationalratssaal“), eine Videokonferenz oder ein hybrides Format.

### Anknüpfungspunkte

Das Meeting ist der Knoten, an dem die übrigen Klassen dieses Standards hängen: Traktanden (`AgendaItem`), Abstimmungen und Wahlen (`Voting`, `Election`), Wortmeldungen (`Speech`) sowie die Anwesenheitsliste (`Attendance.parent_meeting`). `documents` verknüpft Sitzungsunterlagen wie Tagblatt oder Beilagen, `protocol_ref` das Protokoll. `parent_meeting` bildet Sitzungen ab, die Teil einer übergeordneten Sitzung sind; `actor_name`, `group_name` und `group_id` halten Organ und Gruppierung zusätzlich im Klartext fest.

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

