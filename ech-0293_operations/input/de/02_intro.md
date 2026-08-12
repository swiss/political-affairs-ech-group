\newpage

# Einleitung

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
