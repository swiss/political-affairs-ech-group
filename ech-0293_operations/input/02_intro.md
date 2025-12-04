# Einleitung

## Kontext: Öffentlicher Ratsbetrieb

Auf Bundes-, Kantons- und Gemeindeebene tagen Räte und Versammlungen, beraten über politische Geschäfte, fassen Beschlüsse und kontrollieren die Exekutive.

## Zusammenhang mit anderen eCH-Standards

eCH-0293 ist Teil eines Ökosystems von Standards für politische Daten:

### eCH-0294: Politische Akteure (Actors)
Definiert Personen, Organe und Gruppen im politischen Kontext. eCH-0293 referenziert diese Akteure über `actor_id` (z.B. welches Parlament, welche Person hat abgestimmt).

### eCH-0295: Parlamentarische Geschäfte (Affairs)
Beschreibt den Lebenszyklus politischer Geschäfte. AgendaItems in eCH-0293 verweisen über `affair_id` auf die zugehörigen Geschäfte.

### eCH-0296: Erlasse und Gesetzestexte (Laws)
Erfasst die Resultate des parlamentarischen Prozesses - die verabschiedeten Gesetze und Erlasse.

### eCH-0297: Öffentliche Konsultationen (Consultations)
Strukturiert Vernehmlassungsverfahren, die oft Ausgangspunkt für parlamentarische Geschäfte sind.
