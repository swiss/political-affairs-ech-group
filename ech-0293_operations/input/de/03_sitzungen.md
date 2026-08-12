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

Legislaturperioden bilden den langfristigen Rahmen, Sessions strukturieren die Arbeit innerhalb einer Legislaturperiode, Meetings sind die konkreten Sitzungen, in denen Geschäfte beraten werden, und Traktanden gliedern die einzelne Sitzung. Die ersten drei Klassen sind nachfolgend beschrieben, das Traktandum im nächsten Kapitel.

Die drei Klassen sind bewusst gleich gebaut: Identifikation, Zeitangaben, Organbezug und verknüpfte Dokumente sind auf allen Ebenen dieselben. `actor_id` zeigt dabei auf die politischen Akteure gemäss eCH-0294, `documents` auf FRBR-Works gemäss eCH-0292. Beginn und Ende werden doppelt geführt: Auf Stufe Legislaturperiode fallen Planung (`*_planned`) und Verlauf (`*_actual`) kaum auseinander, auf Stufe Sitzung regelmässig.

## Legislature (Legislaturperiode)

Eine Legislaturperiode bezeichnet den Zeitraum, für den ein Parlament gewählt wird und in seiner aktuellen Zusammensetzung tätig ist. Ihre Dauer ist nicht vorgegeben — die Beispiele zeigen eine vier- und eine fünfjährige Amtsdauer.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (Sitzungsperiode)

Eine Session ist eine zusammenhängende Sitzungsperiode, in der mehrere Meetings stattfinden. Sie ist die mittlere Ebene — und optional: Föderaleinheiten ohne formale Sessions lassen sie weg und führen ihre Meetings direkt. Session und Meeting können auch zusammenfallen: Eine eintägige Sitzung des Landrats oder eine Landsgemeinde wird als Sitzungsperiode mit einer einzigen Sitzung geführt.

Nummeriert wird sehr unterschiedlich, weshalb vier Felder zur Verfügung stehen: `number` hält die laufende Nummer als Zahl fest, `sequential_number` dieselbe Angabe als Zeichenkette (und damit auch römische Ziffern), `position` die Position innerhalb der Legislaturperiode und `meeting_abbreviation` eine Kurzbezeichnung wie „FS24“. Das Meeting kennt dieselben vier Felder. `body_key` hält das Organ als Kurzschlüssel fest (z.B. „NR“, „SR“), `parent_legislature` ordnet die Session ihrer Legislaturperiode zu.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (Einzelne Sitzung)

Ein Meeting ist die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Beschlüsse gefasst und Wortmeldungen festgehalten werden. `meeting_type` unterscheidet vier Typen: `session` für Plenarsitzungen eines Parlaments oder einer Kammer, `committee` für Kommissionssitzungen, `sitting` für Versammlungen wie Landsgemeinden, Gemeinde- und Bürgergemeindeversammlungen und `various` als Auffangwert. Der Wert `sitting` ist eine bewusste Setzung: Landsgemeinden und Gemeindeversammlungen sind Versammlungen der Stimmberechtigten selbst, entscheiden aber als tagendes Organ mit Traktandenliste und werden deshalb wie eine Ratssitzung abgebildet.

Auf dieser Ebene fallen Planung und Verlauf regelmässig auseinander: Eine für 14:00 angesetzte Sitzung beginnt wegen Verzögerungen erst um 14:25 und endet statt um 18:00 bereits um 17:30. Genau dafür sind die `*_planned`- und `*_actual`-Felder da; für Uhrzeiten sind die `datetime_*`-Varianten zu verwenden. Ob eine Sitzung überhaupt wie vorgesehen stattfindet, hält `state` fest (`planned`, `canceled`, `postponed`); `state_name` nimmt eine abweichende, freitextliche Statusbezeichnung auf. `location` erfasst den Sitzungsort — den physischen Raum („Bundeshaus, Nationalratssaal“), eine Videokonferenz oder ein hybrides Format.

Zusätzlich zu `actor_id` und `administrative_id` hält `actor_name` den Namen des Organs für den schnellen Zugriff fest und `body_key` einen kurzen Schlüssel; `group_name` und `group_id` ergänzen Gruppierungen, wo nötig. `parent_meeting` bildet Sitzungen ab, die Teil einer übergeordneten Sitzung sind, `parent_legislature` ordnet die Sitzung der Legislaturperiode zu. Nummeriert wird wie bei der Session.

Das Meeting ist der Knoten, an dem die übrigen Klassen dieses Standards hängen: Traktanden (`AgendaItem`), Abstimmungen und Wahlen (`Voting`, `Election`), Wortmeldungen (`Speech`) sowie die Anwesenheitsliste (`Attendance.parent_meeting`). `documents` verknüpft Sitzungsunterlagen wie Tagblatt oder Beilagen, `protocol_ref` das Protokoll.

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

