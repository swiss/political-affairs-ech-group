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
