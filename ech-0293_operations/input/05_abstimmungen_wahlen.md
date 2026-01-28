ToDo: Nicole

# Abstimmungen und Wahlen

Parlamentarische Beschlussfassungen erfolgen entweder durch Abstimmungen über Sachfragen oder durch Wahlen von Personen. Der Standard unterscheidet diese beiden Mechanismen klar und erfasst bei offenen Verfahren zudem das individuelle Stimm- und Wahlverhalten jedes Parlamentsmitglieds. Parlamentspräsidentinnen oder Parlamentspräsidenten nehmen an Abstimmungen grundsätzlich nicht teil; sie stimmen nur bei Wahlen mit. Bei Abstimmungen mit Stimmengleichstand fällen sie den Stichentscheid. 

## Voting (Abstimmung)

## Zweck der Entität

"Voting" erfasst den Abstimmungsprozess und das Ergebnis einer formalen Entscheidung im Parlament. Die Entität dokumentiert sowohl den Abstimmungsgegenstand (Frage), als auch das Verfahren (wie wurde abgestimmt) und das Resultat (mit welchem Stimmenverhältnis).

## Arten von Abstimmungen

Der Standard unterscheidet verschiedene Abstimmungstypen über das Feld **voting_type**:

### intermediate
Zwischenabstimmungen während der Beratung.

**Beispiele:**
- Abstimmung über Eintreten auf ein Geschäft
- Abstimmung über einen Antrag
- Gegenüberstellung von zwei Anträgen, die sich gegenseitig ausschliessen oder sich auf denselben Textabschnitt beziehen
- Eventualabstimmung wenn zu einem Abstimmungsgegenstand mehr als zwei Anträge vorliegen
- Punktweise Abstimmung über einen Vorstoss (Nicole: eine punktweise Abstimmung ist keine Zwischenabstimmung, denn es gibt dabei keine Schlussabstimmung oder ein Endresultat über alle Punkte).
- Abstimmung über einen einzelnen Artikel eines Gesetzes
- Gesamtabstimmung nach der ersten Lesung eines Erlasses, der in zwei Lesungen beraten wird

### final
Schlussabstimmung über die gesamte Vorlage

**Beispiele:**
- Schlussabstimmung nach der letzten Lesung eines Erlasses 
- Gesamtabstimmung über einen Beschluss
- Annahme oder Ablehnung einer Vorlage in ihrer Gesamtheit

### casting
Stichentscheid des/der Vorsitzenden bei Stimmengleichheit. Vorsitzende nehmen an Abstimmungen nicht teil, haben bei Stimmengleichheit jedoch den Stichentscheid. Bei geheimer Abstimmung gilt bei Stimmengleichheit der Antrag des vorberatenden Ratsorgans als angenommen. 

### secret
Geheime Stimmabgabe bei Abstimmungen und Wahlen

**Anwendung:**
- Wahl von Personen
- Abstimmung über besonders heikles Sachgeschäft wie Gnadengesuch oder Aufhebung der Immunität
- Abstimmung nach geheimer Beratung
- Geheime Abstimmung auf Antrag 

## Struktur einer Abstimmung

Eine Abstimmung ist immer einer Sitzungsphase, einer Sitzung, einem Traktandum (Agenda-Item) und einem Geschäft mit Geschäftsnummer zugeordnet. Sie umfasst den Abstimmungstyp, den Abstimmungsgegenstand (Frage), das Ergebnis und – bei nicht geheimer Abstimmung – die Einzelstimmen der Mitglieder. 
Sie kann entweder:

```
AgendaItem (Energiegesetz - Art. 15)
  └─ Voting (Zwischenabstimmung über Art. 15)
      ├─ IndividualVote (Person A: Ja)
      ├─ IndividualVote (Person B: Nein)
      └─ IndividualVote (Person C: Ja)
```


Beispiel Auswahl:
3 Optionen: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
5 Optionen: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=23f01ba9b3f3410cb9cfb85f32f3dfe0

## Abstimmungsverfahren

Das Feld **procedure** beschreibt die Art der Durchführung:

### Open procedures (Offene Abstimmungen)
- **show_of_hands**: Handzeichen (traditionell)
- **standing**: Aufstehen (seltener)
- **electronic**: Elektronische Abstimmung (häufig auf Bundesebene und Kantonsebene)
- **roll_call**: Namentliche Abstimmung mit Namensaufruf
  
***[Nicole: Die folgenden Abstimmungstypen haben wir vergessen]***
- **remote_voting**: Externe Stimmabgabe bei Krisen (Ratsmitglieder geben ihre Stimme dem Parlamentspräsidium im Vorfeld des Sitzungstags bekannt. Die extern abgegebenen Stimmen werden gleichzeitig mit der im Rat laufenden Abstimmung erfasst.
- **circulation_voting**: Zirkulationsverfahren bei Krisen (Das Parlamentspräsidium führt die Abstimmung im Zirkulationsverfahren durch und informiert über das Ergebnis)
- **virtual_voting**: Stimmabgabe an virtuellen Sitzungen in Krisenfällen.

### Secret procedures (Geheime Abstimmungen)
- **secret_ballot**: Geheime Wahl mit Stimmzetteln
- **electronic_secret**: Elektronische geheime Abstimmung

Die Wahl des Verfahrens beeinflusst, ob Einzelstimmen erfasst werden können:
- Offene Verfahren: Einzelstimmen dokumentierbar
- Geheime Verfahren: Nur Gesamtergebnis verfügbar


## Abstimmungsergebnis

Das Ergebnis wird auf zwei Arten erfasst:

### Gesamtergebnis (result)
- **passed**: Angenommen
- **failed**: Abgelehnt
- **tied**: Stimmengleichheit

### Detaillierte Zahlen
- **yes_count**: Anzahl Ja-Stimmen
- **no_count**: Anzahl Nein-Stimmen
- **abstention_count**: Anzahl Enthaltungen
- **absent_count**: Anzahl Abwesende (die nicht abstimmen konnten)
- **total_count**: Gesamtzahl der abstimmenden Mitglieder

**Beispiel:**
- Ja: 120
- Nein: 75
- Enthaltungen: 5
- Abwesend: 0
- Total: 200
- Ergebnis: passed

## Mehrheitstypen

Das Feld **majority_type** definiert die erforderliche Mehrheit:

### simple
Einfache Mehrheit (mehr Ja als Nein)

**Anwendung:**
- Standardfall für die meisten Beschlüsse
- Enthaltungen zählen nicht mit

**Beispiel:** 100 Ja, 80 Nein, 20 Enthaltungen → Angenommen

### absolute
Absolute Mehrheit (mehr als die Hälfte aller Mitglieder)

**Anwendung:**
- Wahlen
- Verfassungsänderungen in einigen Kantonen
- Besonders wichtige Beschlüsse

**Beispiel:** Bei 200 Mitgliedern sind mindestens 101 Ja-Stimmen erforderlich

### two_thirds
Zweidrittelmehrheit

**Anwendung:**
- Dringlichkeitsklauseln auf Bundesebene
- Verfassungsänderungen in einigen Kantonen
- Aufhebung der Immunität

**Beispiel:** Bei 200 Mitgliedern sind mindestens 134 Ja-Stimmen erforderlich

### qualified
Qualifizierte Mehrheit (andere Schwellenwerte)

**Anwendung:**
- Spezielle Anforderungen in einzelnen Kantonen oder Gemeinden
- Das konkrete Quorum wird in **majority_threshold** angegeben

## Schwellenwert

Das Feld **majority_threshold** gibt bei qualifizierten Mehrheiten den genauen Schwellenwert an (z.B. 0.6 für 60%).

## Quorum

Das Feld **quorum** definiert die Mindestanzahl anwesender Mitglieder für die Beschlussfähigkeit:

**Beispiel:** Ein Parlament mit 200 Mitgliedern ist beschlussfähig, wenn mindestens 100 Mitglieder anwesend sind (quorum: 100).

## Namentliche Abstimmungen
***[Nicole: "nominal" ist in diesem Zusammenhang unüblich - besser "named_vote" oder "is_named"]***
Das Feld **is_nominal** zeigt an, ob es sich um eine namentliche Abstimmung handelt: 

- **true**: Die Einzelstimmen werden erfasst und publiziert
- **false**: Nur das Gesamtergebnis wird erfasst

Namentliche Abstimmungen sind wichtig für:
- Transparenz des Abstimmungsverhaltens
- Analyse von Abstimmungsmustern
- Rechenschaftspflicht gegenüber Wählerinnen

## Beziehung zu Einzelstimmen

Bei namentlichen Abstimmungen verweist die Voting-Entität auf die einzelnen IndividualVote-Entitäten:

```
Voting
  ├─ IndividualVote (Person A)
  ├─ IndividualVote (Person B)
  └─ ...
```

**Beispiel:** Namensliste in Akkordeon https://www.tagblatt.gr.be.ch/shareparl?agendaItemUid=e65d81c90d1d43deb19ef078f7e363f3&segmentType=vote&unitName=default&scroll=true&autoplay=false 


## Beschreibung und Dokumentation

- **description**: Beschreibung worüber abgestimmt wurde
- **url**: Mehrsprachige URLs zu Abstimmungsdetails

## Zeitstempel

- **datetime_created**: Zeitpunkt der Durchführung der Abstimmung
- **datetime_updated**: Letzte Aktualisierung (z.B. bei Korrekturen)


{{include:ech-0293_operations/output/docs/Voting.md}}

## Individual Vote (Einzelstimme)

## Zweck der Entität

IndividualVote erfasst das Stimmverhalten einzelner Parlamentsmitglieder bei namentlichen Abstimmungen. Die Entität wird nur erstellt, wenn eine Abstimmung namentlich durchgeführt wird (Voting.is_nominal = true).

## Beziehung zur Abstimmung

Jede Individual Vote ist Teil einer übergeordneten Voting (Abstimmung):

```
Voting (Schlussabstimmung Energiegesetz)
  ├─ IndividualVote (Nationalrätin Anna Müller: Ja)
  ├─ IndividualVote (Nationalrat Beat Schweizer: Nein)
  ├─ IndividualVote (Nationalrätin Carla Rossi: Enthaltung)
  └─ ...
```

## Identifikation der Person

Die stimmende Person wird über das Feld **person_id** referenziert. Diese ID entspricht einer Person gemäss eCH-0294 Actors Standard.

Zusätzlich können weitere Identifikationsdaten erfasst werden:
- **person_name**: Name der Person (für schnellen Zugriff)
- **person_number**: Interne Nummer (z.B. Mandatsnummer)
- **person_political_group**: Fraktionszugehörigkeit
- **person_party**: Parteizugehörigkeit

## Arten von Stimmen

Das Feld **vote** erfasst die Art der Stimmabgabe:

### yes
Ja-Stimme (Zustimmung)

**Bedeutung:** Die Person stimmt der Vorlage/dem Antrag zu.

### no
Nein-Stimme (Ablehnung)

**Bedeutung:** Die Person lehnt die Vorlage/den Antrag ab.

### abstention
Enthaltung

**Bedeutung:** Die Person nimmt an der Abstimmung teil, enthält sich aber der Stimme.

### absent
Nicht entschuldigt abwesend.

**Bedeutung:** Die Person war zum Zeitpunkt der Abstimmung nicht anwesend.

**Gründe für Abwesenheit:**
- Krankheit oder Unfall
- Anderweitige Verpflichtungen
- Ausstand (bei Interessenkonflikt)

### excused
Entschuldigt abwesend.

**Bedeutung:** Die Person war abwesend, aber ordnungsgemäss entschuldigt.

**Unterschied zu absent:**
- **excused**: Vorherige Meldung und Genehmigung.
- **absent**: Unentschuldigte Abwesenheit.

### did_not_vote
Hat nicht abgestimmt.

**Bedeutung:** Die Person war anwesend, hat aber nicht abgestimmt ***Nicole: Dieses Feld scheint mir überflüssig. Wie wollte man die Anwesenden denn zählen, wenn sie nicht abstimmen – wer sollte sie zählen? Mit "absent" ist dieser Fall meiner Meinung nach abgedeckt.***

**Unterschied zu abstention:**
- **abstention**: Bewusste Enthaltung (wird als aktive Handlung erfasst)
- **did_not_vote**: Passive Nicht-Teilnahme

### president
Präsident/in (stimmt nicht ab, aber fällt bei Stimmengleichheit den Stichentscheid)

**Bedeutung:** Die Person führt den Vorsitz und stimmt daher nicht ab

**Anwendung:**
- In vielen Parlamenten stimmt der/die Vorsitzende nur bei Stimmengleichheit (casting vote)
- Im Normalfall wird die Stimme als "president" erfasst

## Stimmgewicht

Das Feld **weight** erfasst das Stimmgewicht:

- **Standardfall**: 1.0 (eine Stimme)
- **Spezialfälle**: Andere Werte möglich

### Anwendungsfälle für abweichendes Stimmgewicht

1. **Stellvertretung**: In einigen Systemen kann eine Person für eine abwesende Person mitstimmen (weight: 2.0)
3. **Gemeindeversammlungen**: In speziellen Fällen können juristische Personen mehrere Stimmen haben
4. **Historische Systeme**: Früher hatten in einigen Kantonen verschiedene Personengruppen unterschiedliches Stimmgewicht

## Gruppenzugehörigkeit

Das Feld **group_id** erfasst die Fraktionszugehörigkeit zum Zeitpunkt der Abstimmung:

**Nutzen:**
- Analyse des Abstimmungsverhaltens nach Fraktionen
- Ermittlung der Parteidisziplin
- Identifikation von Koalitionen

**Beispiel:** Bei einer Abstimmung über das Energiegesetz stimmen 90% der SP-Fraktion mit Ja, 80% der SVP-Fraktion mit Nein.

## Position und Reihenfolge

Das Feld **position** definiert die Sortierreihenfolge bei der Darstellung:

**Anwendung:**
- Alphabetische Sortierung nach Nachname
- Sortierung nach Fraktion
- Sortierung nach Stimmabgabe (erst Ja, dann Nein, dann Enthaltungen)

## Beschreibung und Kontext

Das Feld **description** kann zusätzliche Informationen erfassen:

**Beispiele:**
- "Enthaltung wegen Interessenkonflikt (Verwaltungsrat Energieunternehmen)"
- "Abwesend wegen Krankheit"

## Zeitstempel

- **datetime_created**: Zeitpunkt der Stimmabgabe
- **datetime_updated**: Letzte Aktualisierung (z.B. bei Korrekturen)

## Anwesenheit vs. Stimmabgabe

Wichtiger Unterschied:

- **Attendance** (andere Entität): Erfasst die generelle Anwesenheit bei einer Sitzung
- **IndividualVote**: Erfasst die spezifische Stimmabgabe bei einer Abstimmung

Eine Person kann bei einer Sitzung anwesend sein (Attendance), aber bei einzelnen Abstimmungen mit "absent" oder "did_not_vote" erfasst werden (z.B. wenn sie kurz den Raum verlässt).

## Namentliche vs. geheime Abstimmungen

IndividualVote-Entitäten werden nur bei namentlichen (offenen) Abstimmungen erfasst:

- **Namentliche Abstimmung**: Jede Stimme wird erfasst und ist öffentlich
- **Geheime Abstimmung**: Nur das Gesamtergebnis wird erfasst, keine IndividualVotes

{{include:ech-0293_operations/output/docs/IndividualVote.md}}

## Election (Wahl)

## Begriff und Bedeutung

Eine Election (Wahl) bezeichnet die Bestimmung einer oder mehrerer Personen für ein Amt oder eine Funktion durch ein parlamentarisches Organ. Im Gegensatz zu Abstimmungen (Votings), bei denen über Sachfragen entschieden wird, geht es bei Wahlen um Personenentscheidungen.

## Unterschied: Wahl vs. Abstimmung

| Kriterium | Election (Wahl) | Voting (Abstimmung) |
|-----------|-----------------|---------------------|
| Gegenstand | Personen | Sachfragen, Vorlagen |
| Ergebnis | Gewählte Person(en) | Angenommen/Abgelehnt |
| Verfahren | Oft geheim | Oft offen |
| Mehrheit | Meist absolut | Meist einfach |

## Arten von Wahlen

Der Standard unterscheidet verschiedene Wahltypen über das Feld **election_type**:

### open
Offene Wahl

**Charakteristik:**
- Stimmabgabe ist öffentlich sichtbar
- Jedes Mitglied gibt seine Stimme offen ab
- Nachvollziehbar, wer wen gewählt hat

**Anwendung:**
- Wenn Transparenz gewünscht ist
- Bei unumstrittenen Wahlen
- In kleineren Gremien

### secret
Geheime Wahl

**Charakteristik:**
- Stimmabgabe ist anonym
- Wahlzettel oder elektronisches Geheimwahlsystem
- Nicht nachvollziehbar, wer wen gewählt hat

**Anwendung:**
- Personenwahlen (Standard)
- Wenn freie, unbeeinflusste Entscheidung gewährleistet werden soll
- Gesetzlich oft vorgeschrieben

**Beispiele auf Bundesebene:**
- Wahl des Bundesrats
- Wahl der Bundesrichter
- Wahl der Kommissionspräsidien

**Beispiele auf Kantonsebene:**
- Wahl der Parlamentspräsidentin oder des Parlamentspräsidenten
- Wahl der Regierungspräsidentin oder des Regierungspräsidenten
- Wahl der Präsidentinnen und Präsidenten der obersten kantonalen Gerichte
- Wahl der Richterinnen und Richter
- Wahl er Staatsschreiberin oder des Staatsschreibers
- Wahl der Kommissionspräsidentinnen oder der Kommissionspräsidenten
- Wahl idien
- Wahl der Kommissions

### tacit
Stille Wahl

**Charakteristik:**
- Keine formale Abstimmung erforderlich
- Wahl erfolgt durch Akklamation oder Konsens
- Nur wenn keine Gegenstimmen erhoben werden

**Anwendung:**
- Bei Einstimmigkeit
- Unumstrittene Wahlen
- Wiederwahlen ohne Gegenkandidaten

**Beispiel:** Wiederwahl eines Kommissionspräsidenten ohne Gegenkandidatur

## Zuordnung zu Traktanden

Jede Wahl ist einem AgendaItem zugeordnet:

```
AgendaItem (Wahl des Bundesrats)
  └─ Election (Wahl für Departement XY)
      ├─ Kandidat A: 120 Stimmen
      ├─ Kandidat B: 75 Stimmen
      └─ Leere Stimmzettel: 5
```

## Beschreibung und Titel

- **title**: Titel der Wahl (z.B. "Wahl Kommissionspräsidium WAK")
- **description**: Ausführliche Beschreibung, Kontext, besondere Umstände

## Wahlergebnis

Das Feld **result** erfasst das Ergebnis:

- **elected**: Person(en) gewählt
- **not_elected**: Keine Person gewählt (z.B. bei absoluter Mehrheit nicht erreicht)
- **deferred**: Wahl verschoben
- **withdrawn**: Wahl zurückgezogen

## Gewählte Person(en)

Das Feld **elected_person_id** enthält die ID(s) der gewählten Person(en) gemäss eCH-0294 Actors.

Bei Mehrfachwahlen (z.B. Wahl mehrerer Kommissionsmitglieder gleichzeitig) können mehrere IDs erfasst werden.

## Stimmenverteilung

Bei offenen Wahlen oder nach Publikation der Ergebnisse:

- **total_votes**: Gesamtzahl abgegebener Stimmen
- **valid_votes**: Gültige Stimmen
- **invalid_votes**: Ungültige Stimmen
- **blank_votes**: Leere Stimmzettel

Zusätzlich Details pro Kandidat (über separate Entitäten oder als strukturierte Daten).

## Wahlverfahren

Das Feld **procedure** beschreibt das konkrete Verfahren:

- **written_ballot**: Schriftliche Wahl mit Stimmzetteln
- **electronic**: Elektronische Wahl
- **show_of_hands**: Handzeichen (bei offenen Wahlen)
- **acclamation**: Akklamation (bei stillen Wahlen)

## Mehrheitsverhältnisse

Das Feld **majority_type** definiert die erforderliche Mehrheit:

### absolute
Absolute Mehrheit (mehr als die Hälfte der Stimmenden)

**Anwendung:**
- Bundesratswahl
- Wahl von Kommissionspräsidien
- Standardfall bei Personenwahlen

**Beispiel:** Bei 200 abgegebenen Stimmen sind mindestens 101 Stimmen erforderlich

**Besonderheit:** Wenn im ersten Wahlgang niemand die absolute Mehrheit erreicht, folgt meist ein zweiter Wahlgang, in dem die einfache Mehrheit genügt.

### simple
Einfache Mehrheit (mehr Stimmen als andere Kandidaten)

**Anwendung:**
- Zweiter Wahlgang nach erfolglosem ersten Wahlgang
- Einige Kommissionswahlen

### qualified
Qualifizierte Mehrheit

**Anwendung:**
- Seltener bei Wahlen
- Spezielle Funktionen mit erhöhten Anforderungen

## Wahlgänge

Bei Wahlen mit absoluter Mehrheit im ersten Wahlgang:

```
1. Wahlgang (absolute Mehrheit erforderlich)
   └─ Kein Kandidat erreicht absolute Mehrheit

2. Wahlgang (einfache Mehrheit genügt)
   └─ Kandidat A gewählt
```

Jeder Wahlgang wird als separate Election-Entität erfasst, verbunden über das gemeinsame AgendaItem.

## Zeitstempel

- **datetime_created**: Zeitpunkt der Durchführung
- **datetime_updated**: Letzte Aktualisierung

## URL und Dokumentation

- **url**: Mehrsprachige URLs zu Wahlunterlagen:
  - Kandidatenprofile
  - Wahlresultate
  - Protokolle

## Besonderheiten verschiedener Wahlen

### Bundesratswahl
- Geheime Wahl
- Absolute Mehrheit erforderlich (im 1. Wahlgang)
- Durch die Vereinigte Bundesversammlung

### Bundesrichterwahl
- Geheime Wahl
- Proporzprinzip (Berücksichtigung von Parteien, Landesteilen, Geschlechtern)

### Kommissionspräsidien
- Wahl durch das jeweilige Parlament
- Oft weniger öffentlich

### Kantons- und Gemeindeebene
- Grosse Vielfalt an Wahlverfahren
- Teilweise Volkswahl statt parlamentarische Wahl
- Unterschiedliche Mehrheitserfordernisse

## Transparenz und Geheimhaltung

Spannungsfeld:
- **Wahlgeheimnis**: Schutz der individuellen Wahlentscheidung
- **Transparenz**: Öffentliches Interesse am Wahlergebnis

Bei geheimen Wahlen:
- Nur Gesamtergebnis wird publiziert
- Keine IndividualVote-Entitäten
- Schutz der Wahlfreiheit

Bei offenen Wahlen:
- Individuelle Stimmabgaben können erfasst werden
- Höhere Transparenz
- Potenzielle soziale Druckeffekte

{{include:ech-0293_operations/output/docs/Election.md}}
