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

## Speech (Wortmeldung, Votum)

## Begriff und Bedeutung

Eine Speech (Wortmeldung, Votum) bezeichnet einen mündlichen Beitrag einer Person während einer parlamentarischen Sitzung. Sie ist das zentrale Instrument der politischen Debatte und Meinungsäusserung im Parlament.

## Arten von Speeches

Parlamentarische Wortmeldungen haben verschiedene Formen:

### Hauptvoten
- Ausführliche Stellungnahmen zu einem Geschäft
- Begründung von Anträgen
- Darlegung der Fraktionsmeinung

### Kurzinterventionen
- Kurze Wortmeldungen
- Zwischenfragen
- Richtigstellungen

### Fraktionserklärungen
- Offizielle Stellungnahme einer Fraktion
- Vorgetragen durch Fraktionssprecher/in

### Regierungsvoten
- Stellungnahmen von Regierungsmitgliedern
- Beantwortung von Fragen
- Verteidigung von Vorlagen

## Struktur und Zuordnung

Eine Speech ist immer einem bestimmten Kontext zugeordnet:

```
Meeting (Sitzung)
  └─ AgendaItem (Traktandum)
      └─ Speech (Wortmeldung Person A)
          ├─ TextSegment (Transkription)
          ├─ Media (Audio-Aufzeichnung)
          └─ Media (Video-Aufzeichnung)
```

### Zuordnungsfelder

- **meeting_id**: Die Sitzung, in der die Wortmeldung erfolgte
- **agenda_item_id**: Das Traktandum, zu dem gesprochen wurde
- **person_id**: Die sprechende Person (gemäss eCH-0294 Actors)

## Identifikation der Sprechenden

- **person_id**: Eindeutige Identifikation der Person
- **person_name**: Name für schnellen Zugriff
- **role**: Rolle der Person (z.B. "Fraktionspräsident/in", "Berichterstatter/in", "Bundesrat/Bundesrätin")

## Zeitliche Erfassung

- **start_time**: Beginn der Wortmeldung
- **end_time**: Ende der Wortmeldung
- **duration**: Dauer in Sekunden (berechnet oder erfasst)

Diese Zeitangaben ermöglichen:
- Genaue Referenzierung in Audio-/Video-Aufzeichnungen
- Analyse der Redezeit pro Person/Fraktion
- Kontrolle der Einhaltung von Zeitlimiten

## Sprache der Wortmeldung

Das Feld **language** erfasst die Sprache, in der gesprochen wurde:

- **de**: Deutsch
- **fr**: Französisch
- **it**: Italienisch
- **rm**: Rätoromanisch
- **en**: Englisch

## Textdokumente

Das Feld **text_segments** verweist auf TextSegment-Entitäten, die den gesprochenen Text enthalten.

### Verschiedene Textversionen

#### Rohtranskript
- Wörtliche Niederschrift
- Unbearbeitet, mit Füllwörtern
- Direkt nach der Sitzung verfügbar

#### Bearbeitetes Transkript
- Redaktionell überarbeitet
- Grammatikalisch korrigiert
- Offizielle Protokollversion

#### Übersetzungen
- In andere Landessprachen
- Für internationale Publikationen

### TextSegment-Struktur

Jedes TextSegment kann enthalten:
- **text**: Der eigentliche Text
- **language**: Sprache des Texts
- **version**: Art der Version (raw, edited, translated)
- **format**: Format (plain, markdown, HTML)

## Multimedia-Aufzeichnungen

Das Feld **media** verweist auf Media-Entitäten mit Audio- und Video-Aufzeichnungen.

### Audio-Aufzeichnungen
- Originalton der Wortmeldung
- Format: MP3, WAV, etc.
- Technische Metadaten (Qualität, Bitrate)

### Video-Aufzeichnungen
- Visuelle Aufzeichnung (bei Plenarsitzungen)
- Format: MP4, WebM, etc.
- Verschiedene Auflösungen

### Livestreaming
- Echtzeit-Übertragung
- URL zum Stream
- Archivierung nach der Sitzung

## Titel und Beschreibung

- **title**: Kurzer Titel (z.B. "Votum zur Energiepolitik")
- **description**: Zusammenfassung oder Kontext der Wortmeldung

## Typ der Wortmeldung

Das Feld **speech_type** kann verschiedene Arten unterscheiden:

- **statement**: Stellungnahme
- **question**: Frage
- **response**: Antwort (z.B. Regierung auf Frage)
- **procedural**: Verfahrensantrag
- **declaration**: Erklärung

{{include:ech-0293_operations/output/docs/Speech.md}}
