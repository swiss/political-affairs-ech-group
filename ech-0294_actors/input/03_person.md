\newpage

# Person

Das Personenschema beschreibt natürliche Personen im politischen Kontext.

- **Stabile Person, zeitlich gültige Merkmale:** Die `Person` selbst trägt keine zeitliche Gültigkeit, ihre Merkmale hingegen schon – Name, Staatsangehörigkeit, Geschlecht, Beruf, Ausbildung und Wahlkreis tragen je eigene `valid_from`/`valid_through`. So bleibt die Identität der Person stabil, während sich einzelne Angaben über die Zeit ändern und die Historie erhalten bleibt (z. B. Namensänderung bei Heirat oder Wechsel des Wahlkreises).
- **Obligatorischer Anzeigename (`label`) neben strukturierten Namen (`names`):** Jede Person hat einen zwingenden Kurznamen, damit auch bei unvollständigen Angaben immer ein Anzeigename vorhanden ist. Empfohlen wird die Kombination aus amtlichem Namen (`PersonOfficialName`) und Rufname (`PersonCallFirstName`), bei Namensgleichheit ergänzt um das Geburtsjahr. `label_long` nimmt zusätzlich akademische Titel auf; die feingliedrige, typisierte Namensstruktur (`names`) ist optional.
- **Namenstypen nach amtlicher Systematik:** Die Namenstypen (`NameTypeEnum`) folgen der Registerharmonisierung des BFS bzw. eCH-0011 (u. a. amtlicher Name, angestammter Name, Allianzname, Rufname sowie Varianten für ausländische Ausweise). Damit sind die Namen mit den amtlichen Personenregistern kompatibel, statt eine eigene Systematik einzuführen.
- **`birth_year` als datensparsame Alternative zu `birth_date`:** Ist das genaue Geburtsdatum nicht verfügbar oder nicht zur Veröffentlichung bestimmt, kann nur das Geburtsjahr angegeben werden. Liegt ein `birth_date` vor, hat es Vorrang.
- **Mehrfachwerte statt Einzelwerte:** Namen, Staatsangehörigkeiten und Geschlechtsangaben sind als Listen mit zeitlicher Gültigkeit modelliert – etwa für Doppelbürgerschaften, Namensänderungen oder eine sich ändernde Geschlechtsangabe.
- **Harmonisierung über föderale Ebenen (Langzeitziel):** Die Verknüpfung derselben Person über die föderalen Ebenen hinweg ist ein wichtiges Langzeitziel. Der Aufbau einer zentralen Personendatenbank läge ausserhalb des Auftrags der eCH-Fachgruppe. Da für diesen Zweck bereits eine offene, etablierte Infrastruktur besteht, wird **Wikidata als übergreifender Identifikator empfohlen** (`wikidata_uri`); zusammen mit global eindeutigen Identifikatoren (URIs) lässt sich die Zuordnung so schrittweise über die Systeme hinweg harmonisieren.


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
