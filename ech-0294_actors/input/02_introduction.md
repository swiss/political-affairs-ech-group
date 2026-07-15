\newpage

# Einführung

## Die Standardfamilie „Politische Geschäfte"

Das politische Geschehen der Schweiz findet auf Bundes-, Kantons- und Gemeindeebene statt – in Parlamenten und Gemeindeversammlungen, in Exekutiven und Verwaltungen, in Vernehmlassungen und Konsultationen sowie über die direktdemokratische Mitwirkung der Stimmberechtigten. Die Fachgruppe „Politische Geschäfte" des Vereins eCH entwickelt dafür eine Familie aufeinander abgestimmter Standards, welche diese Daten föderal übergreifend strukturieren. Die Standards nutzen gemeinsame Datenelemente (eCH-0292) und referenzieren sich gegenseitig über eindeutige Identifikatoren.

Die Familie umfasst:

- **eCH-0292 – Gemeinsame Datenelemente (Meta):** Definiert die übergreifend genutzten Datenelemente und Metaprozesse, auf denen die übrigen Standards aufbauen.
- **eCH-0293 – Öffentlicher Ratsbetrieb (Operations):** Beschreibt den öffentlichen Ratsbetrieb – Sitzungen, Traktanden, Wortmeldungen sowie Abstimmungen und Wahlen.
- **eCH-0294 – Politische Akteure (Actors) – dieser Standard:** Definiert Personen, Gruppen und Organe im politischen Kontext sowie deren Mitgliedschaften und Interessenbindungen. Die übrigen Standards referenzieren diese Akteure über ihre Identifikatoren.
- **eCH-0295 – Parlamentarische Geschäfte (Affairs):** Beschreibt den Lebenszyklus politischer Geschäfte.
- **eCH-0296 – Erlasse und Gesetzestexte (Laws):** Erfasst die Resultate des parlamentarischen Prozesses – die verabschiedeten Gesetze und Erlasse.
- **eCH-0297 – Öffentliche Konsultationen (Consultations):** Strukturiert Vernehmlassungsverfahren, die oft Ausgangspunkt für parlamentarische Geschäfte sind.

Ziel dieser Standardfamilie ist es, eine gemeinsam nutzbare Struktur für politische Daten zu schaffen und Organisationen, die Informationen zu politischen Geschäften veröffentlichen, ein tragfähiges Datenmodell an die Hand zu geben.

## Abgrenzung zur Fachgruppe „Politische Rechte"

Neben der Fachgruppe „Politische Geschäfte" besteht beim Verein eCH die Fachgruppe „Politische Rechte". Beide betreffen den politischen Bereich, decken aber unterschiedliche Domänen ab:

- **Politische Geschäfte** (diese Standardfamilie) beschreibt den parlamentarischen und behördlichen Willensbildungs- und Entscheidungsprozess: die Akteure (eCH-0294), den Ratsbetrieb (eCH-0293), die parlamentarischen Geschäfte (eCH-0295), die daraus hervorgehenden Erlasse (eCH-0296) sowie die vorgelagerten Vernehmlassungen (eCH-0297).
- **Politische Rechte** befasst sich mit der Ausübung der politischen Rechte durch die Stimmberechtigten: Stimm- und Wahlregister, die Durchführung von Volksabstimmungen und Wahlen, die elektronische Stimmabgabe (eVoting), Stimmrechtsausweise sowie Abstimmungs- und Wahlergebnisse (u.a. eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

Berührungspunkte bestehen an zwei Stellen:

- **Abstimmungen und Wahlen:** eCH-0293 erfasst Abstimmungen und Wahlen **innerhalb des Ratsbetriebs** (z.B. namentliche Abstimmungen im Parlament oder die Wahl von Behördenmitgliedern durch den Rat), während Volksabstimmungen und Volkswahlen samt der zugehörigen Register, Durchführung und Ergebnisse von der Fachgruppe „Politische Rechte" abgedeckt werden.
- **Gewählte Personen:** In den Wahlergebnissen der Fachgruppe „Politische Rechte" erscheinen Kandidierende und Gewählte. Sobald Personen ein Mandat innehaben, werden sie in eCH-0294 als politische Akteurinnen und Akteure mit ihren Rollen und Mitgliedschaften geführt.

## Der Standard eCH-0294 – Politische Akteure

Dieser Standard definiert vier Hauptklassen:

- **Person** – Natürliche Personen im politischen Kontext
- **Group** – Gremien, Parteien, Fraktionen, Räte, Kommissionen, Organisationen etc.
- **Membership** – Verbindung zwischen Personen und Gruppen
- **InterestLink** – Interessenbindungen von Personen

`Membership` ist das zentrale Bindeglied zwischen `Person` und `Group` und hält fest, in welchem Parlament, in welcher Kommission etc. eine Person aktiv ist oder war. `InterestLink` ermöglicht die Beschreibung von Interessenbindungen.