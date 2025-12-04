ToDo: Nicole

# Abstimmungen und Wahlen

Parlamentarische Entscheidungen erfolgen durch Abstimmungen über Sachfragen und Wahlen von Personen. Der Standard unterscheidet diese beiden Mechanismen klar und erfasst bei offenen Verfahren auch das individuelle Stimmverhalten der Parlamentsmitglieder.

## Voting (Abstimmung)

## Zweck der Entität

Voting erfasst den Abstimmungsprozess und das Ergebnis einer formalen Entscheidung im Parlament. Die Entität dokumentiert sowohl das Verfahren (wie wurde abgestimmt) als auch das Resultat (mit welchem Stimmenverhältnis).

## Arten von Abstimmungen

Der Standard unterscheidet verschiedene Abstimmungstypen über das Feld **voting_type**:

### intermediate
Zwischenabstimmungen während der Beratung

**Beispiele:**
- Abstimmung über einen Änderungsantrag
- Abstimmung über einen einzelnen Artikel eines Gesetzes
- Rückweisungsantrag an eine Kommission

### final
Schlussabstimmungen über die gesamte Vorlage

**Beispiele:**
- Schlussabstimmung über ein Gesetz
- Gesamtabstimmung über einen Beschluss
- Annahme oder Ablehnung einer Vorlage in ihrer Gesamtheit

### casting
Stichentscheid bei Stimmengleichheit

**Anwendung:**
- Präsidialsystem: Der/die Vorsitzende gibt bei Gleichstand den Stichentscheid
- In der Schweiz selten, da meist ungerade Anzahl von Mitgliedern

### secret
Geheime Abstimmungen

**Anwendung:**
- Wahlen von Personen
- Besonders sensible Entscheidungen
- Auf Antrag einer Minderheit der Mitglieder

## Struktur einer Abstimmung

Eine Abstimmung ist immer einem AgendaItem zugeordnet und kann entweder:

```
AgendaItem (Energiegesetz - Art. 15)
  └─ Voting (Zwischenabstimmung über Art. 15)
      ├─ IndividualVote (Person A: Ja)
      ├─ IndividualVote (Person B: Nein)
      └─ IndividualVote (Person C: Ja)
```

## Abstimmungsverfahren

Das Feld **procedure** beschreibt die Art der Durchführung:

### Open procedures (Offene Abstimmungen)
- **show_of_hands**: Handzeichen (traditionell)
- **standing**: Aufstehen (seltener)
- **electronic**: Elektronische Abstimmung (häufig auf Bundesebene)
- **roll_call**: Namentliche Abstimmung mit Namensaufruf

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

## Beschreibung und Dokumentation

- **description**: Beschreibung worüber abgestimmt wurde
- **url**: Mehrsprachige URLs zu Abstimmungsdetails

## Zeitstempel

- **datetime_created**: Zeitpunkt der Durchführung der Abstimmung
- **datetime_updated**: Letzte Aktualisierung (z.B. bei Korrekturen)

## Besonderheiten verschiedener Föderalebenen

### Bundesebene
- Häufig elektronische Abstimmungen
- Namentliche Abstimmungen bei wichtigen Vorlagen
- Detaillierte Dokumentation

### Kantone
- Variiert stark: Von elektronischen Systemen bis zu Handzeichen
- Unterschiedliche Praktiken bei namentlichen Abstimmungen
- Teilweise noch traditionelle Verfahren (z.B. Aufstehen)

### Gemeinden
- Gemeindeversammlungen: Meist Handzeichen oder Aufstehen
- Gemeindeparlamente: Ähnlich wie Kantone
- Bei Versammlungen oft keine Erfassung von Einzelstimmen

## Verwendungszwecke

1. Dokumentation von Abstimmungsergebnissen und -verfahren
2. Publikation für Öffentlichkeit und Medien
3. Datengrundlage für Analysen (Abstimmungsmuster, Koalitionen)
4. Langzeitarchivierung parlamentarischer Entscheidungen

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

## Arten von Stimmen

Das Feld **vote** erfasst die Art der Stimmabgabe:

### yes
Ja-Stimme (Zustimmung)

**Bedeutung:** Die Person stimmt der Vorlage/dem Antrag zu

### no
Nein-Stimme (Ablehnung)

**Bedeutung:** Die Person lehnt die Vorlage/den Antrag ab

### abstention
Enthaltung

**Bedeutung:** Die Person nimmt an der Abstimmung teil, enthält sich aber der Stimme

### absent
Abwesend

**Bedeutung:** Die Person war zum Zeitpunkt der Abstimmung nicht anwesend

**Gründe für Abwesenheit:**
- Krankheit oder Unfall
- Anderweitige Verpflichtungen
- Ausstand (bei Interessenkonflikt)

### excused
Entschuldigt abwesend

**Bedeutung:** Die Person war abwesend, aber ordnungsgemäss entschuldigt

**Unterschied zu absent:**
- **excused**: Vorherige Meldung und Genehmigung
- **absent**: Unentschuldigte Abwesenheit

### did_not_vote
Hat nicht abgestimmt

**Bedeutung:** Die Person war anwesend, hat aber nicht abgestimmt

**Unterschied zu abstention:**
- **abstention**: Bewusste Enthaltung (wird als aktive Handlung erfasst)
- **did_not_vote**: Passive Nicht-Teilnahme

### president
Präsident/in (stimmt nicht ab)

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

2. **Ständerat**: Bei der Vereinigten Bundesversammlung (z.B. Bundesratswahl) haben Ständeräte das gleiche Stimmgewicht wie Nationalräte (weight: 1.0), obwohl die Kantone unterschiedlich gross sind

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
- "Stimmte trotz Fraktionslinie mit Nein"
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

## Datenqualität und Korrekturen

Bei elektronischen Abstimmungssystemen:
- Automatische Erfassung minimiert Fehler
- Nachträgliche Korrekturen sind möglich (datetime_updated)
- Transparente Dokumentation von Änderungen

Bei manuellen Systemen:
- Höheres Fehlerrisiko
- Sorgfältige Protokollierung erforderlich

## Verwendungszwecke

1. Nachvollziehbarkeit des individuellen Stimmverhaltens für Öffentlichkeit
2. Analysen: Parteidisziplin, Koalitionsbildung, Abstimmungsmuster
3. Datengrundlage für Parlamentsforschung und Medien
4. Monitoring durch Interessengruppen

## Besonderheiten verschiedener Föderalebenen

### Bundesebene
- Umfassende Erfassung bei allen wichtigen Abstimmungen
- Elektronisches System für hohe Datenqualität
- Öffentliche APIs für Datenzugriff

### Kantone
- Unterschiedlich: Einige Kantone erfassen alle Abstimmungen namentlich, andere nur auf Antrag
- Technische Systeme variieren stark
- Nicht alle Kantone publizieren Einzelstimmen online

### Gemeinden
- Gemeindeparlamente: Ähnlich wie Kantone
- Gemeindeversammlungen: Erfassung von Einzelstimmen meist nicht möglich (zu viele Teilnehmende)

## Datenschutz und Öffentlichkeitsprinzip

Spannungsfeld zwischen:
- **Transparenz**: Öffentlichkeit hat Recht zu wissen, wie ihre Vertreter abstimmen
- **Datenschutz**: Persönliche Daten müssen geschützt werden

In der Schweiz gilt:
- Abstimmungsverhalten von Parlamentsmitgliedern ist grundsätzlich öffentlich
- Namen und Mandate sind öffentliche Informationen
- Detaillierte persönliche Daten (Adressen, etc.) sind geschützt

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

## Verwendungszwecke

Die Election-Entität ermöglicht:

1. **Dokumentation**: Vollständige Erfassung von Wahlvorgängen
2. **Transparenz**: Nachvollziehbare Ergebnisse (soweit nicht geheim)
3. **Archivierung**: Langfristige Bewahrung von Wahlentscheiden
4. **Analyse**: Auswertung von Wahlverhalten, Erfolgschancen, Mustern
5. **Legitimation**: Nachweis der korrekten Durchführung

{{include:ech-0293_operations/output/docs/Election.md}}
