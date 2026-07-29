\newpage

# Einleitung

## Kontext: Öffentlicher Ratsbetrieb

Auf Bundes-, Kantons- und Gemeindeebene tagen Räte und Versammlungen, beraten über politische Geschäfte, fassen Beschlüsse und kontrollieren die Exekutive.

## Die Standardfamilie „Politische Geschäfte"

Das politische Geschehen der Schweiz findet auf Bundes-, Kantons- und Gemeindeebene statt – in Parlamenten und Gemeindeversammlungen, in Exekutiven und Verwaltungen, in Vernehmlassungen und Konsultationen sowie über die direktdemokratische Mitwirkung der Stimmberechtigten. Die Fachgruppe „Politische Geschäfte" des Vereins eCH entwickelt dafür eine Familie aufeinander abgestimmter Standards, welche diese Daten föderal übergreifend strukturieren. Die Standards nutzen gemeinsame Datenelemente (eCH-0292) und referenzieren sich gegenseitig über eindeutige Identifikatoren.

Die Familie umfasst:

- **eCH-0292 – Gemeinsame Datenelemente (Meta):** Definiert die übergreifend genutzten Datenelemente und Metaprozesse, auf denen die übrigen Standards aufbauen. eCH-0293 übernimmt daraus unter anderem die Identifikations- und Datumselemente sowie die FRBR-Struktur für verknüpfte Dokumente.
- **eCH-0293 – Öffentlicher Ratsbetrieb (Operations) – dieser Standard:** Beschreibt den öffentlichen Ratsbetrieb – Legislaturperioden und Sessionen, Sitzungen und Traktanden, Protokolle und Beschlüsse, Abstimmungen und Wahlen, Anwesenheiten sowie Wortmeldungen.
- **eCH-0294 – Politische Akteure (Actors):** Definiert Personen, Gruppen und Organe im politischen Kontext sowie deren Mitgliedschaften und Interessenbindungen. eCH-0293 referenziert diese Akteure über `actor_id` – etwa welches Parlament getagt und welche Person abgestimmt hat.
- **eCH-0295 – Parlamentarische Geschäfte (Affairs):** Beschreibt den Lebenszyklus politischer Geschäfte. Traktanden in eCH-0293 verweisen über `affair_id` auf das zugehörige Geschäft.
- **eCH-0296 – Erlasse und Gesetzestexte (Laws):** Erfasst die Resultate des parlamentarischen Prozesses – die verabschiedeten Gesetze und Erlasse.
- **eCH-0297 – Öffentliche Konsultationen (Consultations):** Strukturiert Vernehmlassungsverfahren, die oft Ausgangspunkt für parlamentarische Geschäfte sind.

Ziel dieser Standardfamilie ist es, eine gemeinsam nutzbare Struktur für politische Daten zu schaffen und Organisationen, die Informationen zu politischen Geschäften veröffentlichen, ein tragfähiges Datenmodell an die Hand zu geben.

## Abgrenzung zur Fachgruppe „Politische Rechte"

Neben der Fachgruppe „Politische Geschäfte" besteht beim Verein eCH die Fachgruppe „Politische Rechte". Beide betreffen den politischen Bereich, decken aber unterschiedliche Domänen ab:

- **Politische Geschäfte** (diese Standardfamilie) beschreibt den parlamentarischen und behördlichen Willensbildungs- und Entscheidungsprozess: die Akteure (eCH-0294), den Ratsbetrieb (eCH-0293), die parlamentarischen Geschäfte (eCH-0295), die daraus hervorgehenden Erlasse (eCH-0296) sowie die vorgelagerten Vernehmlassungen (eCH-0297).
- **Politische Rechte** befasst sich mit der Ausübung der politischen Rechte durch die Stimmberechtigten: Stimm- und Wahlregister, die Durchführung von Volksabstimmungen und Volkswahlen, die elektronische Stimmabgabe (eVoting), Stimmrechtsausweise sowie Abstimmungs- und Wahlergebnisse (u.a. eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

Für eCH-0293 ist diese Abgrenzung besonders relevant, weil der Standard Abstimmungen und Wahlen modelliert. Massgebend ist nicht, wer stimmberechtigt ist, sondern **wo entschieden wird** – in der tagenden Versammlung oder an der Urne:

- **In der Versammlung** – dieser Standard: Abstimmungen und Wahlen, die ein tagendes Organ im Rahmen einer Sitzung mit Traktandenliste vornimmt. Dazu gehören namentliche Abstimmungen und Schlussabstimmungen im Parlament ebenso wie die Wahl von Behördenmitgliedern, Gerichten oder Kommissionspräsidien durch den Rat. Erfasst wird dies über `Voting`, `IndividualVote` und `Election`.
- **An der Urne** – Fachgruppe „Politische Rechte": Volksabstimmungen und Volkswahlen samt Stimmregistern, Durchführung, Stimmrechtsausweisen und Ergebnissen. Diese werden hier nicht modelliert.

Bewusst auf der Seite dieses Standards liegen **Landsgemeinden und Gemeindeversammlungen** (`meeting_type: sitting`). Sie sind zwar Versammlungen der Stimmberechtigten selbst, entscheiden aber als tagendes Organ mit Traktandenliste, Wortmeldungen und Beschlüssen – und werden deshalb wie eine Ratssitzung abgebildet.

Ein zweiter Berührungspunkt sind die gewählten Personen: In den Wahlergebnissen der Fachgruppe „Politische Rechte" erscheinen Kandidierende und Gewählte. Sobald Personen ein Mandat innehaben, werden sie in eCH-0294 als politische Akteurinnen und Akteure mit ihren Rollen und Mitgliedschaften geführt – eCH-0293 referenziert sie von dort über `actor_id`.
