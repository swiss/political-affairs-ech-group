\newpage

# Person

## Einführung und Zielsetzung

Das Personenschema beschreibt natürliche Personen im politischen Kontext und zielt darauf ab, eine präzise und gleichzeitig flexible Datenstruktur bereitzustellen. Die Umsetzung soll es ermöglichen, vorhandene Informationen hochgradig strukturiert abzubilden (z.B. der Name nach Typisierung vom BFS), aber auch Informationen, die weniger klar und vollständing sind, darzustellen. Das Ziel ist es, damit die Qualität kontinuierlich verbessern zu können.

**Kernziele:**

- **Präzision**: Unterstützung von zeitlich gültigen Attributen (z.B. Namen, Adressen, Geschlecht).
- **Flexibilität**: Optionale Felder erlauben schrittweise Datenanreicherung.
- **Interoperabilität**: URIs als globale Identifikatoren wo vorhanden, inklusive der Möglichkeit auf Wikidata-Einträge zu verweisen.
- **Mehrsprachigkeit**: Unterstützung mehrsprachiger Inhalte gemäss schweizer Anforderungen.

Notiz: *Die Verknüpfung von Personen im öffentlichen Interesse (Politikerinnen und Politiker) über die federalen Ebenen hinweg wird als ein wichtiges Langzeitziel gesehen. Eine zentrale Datenbank oder Identifizierungstelle der Personen kann nicht durch die Fachgruppe realisiert werden. Es gibt Ansätze im Datenmodell, damit man kontinuierlich die Identifikatoren über die Stufen hinweg harmonisieren kann. Zum einen durch die Benutzung von global eindeutigen Identifikatoren (URIs), sowie von Vorschlägen zu empfholenen bestehenden offenen Datenbanken (Wikidata). *


{{include:ech-0294_actors/output/docs/Person.md}} 

{{include:ech-0294_actors/output/docs/Name.md}} 

{{include:ech-0294_actors/output/docs/NameTypeEnum.md}} 

{{include:ech-0294_actors/output/docs/LanguageProficiency.md}} 

{{include:ech-0294_actors/output/docs/Citizenship.md}} 

{{include:ech-0294_actors/output/docs/Gender.md}} 

{{include:ech-0294_actors/output/docs/GenderCodeEnum.md}} 

{{include:ech-0294_actors/output/docs/Occupation.md}} 

{{include:ech-0294_actors/output/docs/Training.md}} 

{{include:ech-0294_actors/output/docs/TrainingTypeEnum.md}} 

{{include:ech-0294_actors/output/docs/ElectoralDistrict.md}}
