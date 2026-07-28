\newpage

# Person

Das Personenschema beschreibt natürliche Personen im politischen Kontext.

- **Stabile Person, zeitlich gültige Merkmale:** Die `Person` selbst trägt keine zeitliche Gültigkeit, ihre Merkmale hingegen schon – Name, Staatsangehörigkeit, Geschlecht, Beruf und Ausbildung tragen je eigene `valid_from`/`valid_through`. So bleibt die Identität der Person stabil, während sich einzelne Angaben über die Zeit ändern und die Historie erhalten bleibt (z. B. Namensänderung bei Heirat). Der Wahlkreis ist demgegenüber kein Personenmerkmal: Er hängt an der `Membership` (`electoral_district`) und erbt deren zeitliche Gültigkeit – ein Wechsel des Wahlkreises bildet sich damit über die jeweilige Mitgliedschaft ab.
- **Anzeigename (`label`) obligatorisch, Namensstruktur (`names`) optional:** Jede Person hat einen kurzen Anzeigenamen. So ist auch bei unvollständigen Angaben immer ein Name vorhanden. Empfohlen wird die Kombination aus amtlichem Namen (`PersonOfficialName`) und Rufname (`PersonCallFirstName`). Über `label_long` können auch akademische Titel abgebildet werden.
- **Namenstypen nach amtlicher Systematik:** Die Namenstypen (`NameTypeEnum`) übernehmen die Systematik der Registerharmonisierung (u. a. amtlicher Name, angestammter Name, Allianzname, Rufname sowie Varianten für ausländische Ausweise). Massgebend ist der [Amtliche Katalog der Merkmale](https://www.bfs.admin.ch/bfs/de/home/register/personenregister/registerharmonisierung/nomenklaturen.assetdetail.24565576.html), den das Bundesamt für Statistik gestützt auf Art. 4 des Registerharmonisierungsgesetzes (RHG, SR 431.02) herausgibt; die Nummern in den Wertbeschreibungen (211–224) sind die Merkmalsnummern dieses Katalogs. Das zugehörige Austauschformat definiert der eCH-Standard [eCH-0011 Datenstandard Personendaten](https://www.ech.ch/de/ech/ech-0011/9.0.0), auf den dieser Standard damit aufsetzt. Die Namen sind so mit den amtlichen Personenregistern kompatibel und ihre Semantik ist klar.
- **Geburtsdatum in zwei Genauigkeitsstufen (`birth_year` / `birth_date`):** Ist das genaue Geburtsdatum nicht verfügbar oder nicht zur Veröffentlichung bestimmt, kann nur das Geburtsjahr angegeben werden. Liegt ein `birth_date` vor, hat es Vorrang.
- **Mehrfachwerte statt Einzelwerte:** Namen, Staatsangehörigkeiten und Geschlechtsangaben sind als Listen mit zeitlicher Gültigkeit modelliert – etwa für Doppelbürgerschaften, Namensänderungen oder eine sich ändernde Geschlechtsangabe.
- **Geschlecht: amtliche Codes plus offene Kategorie (`GenderCodeEnum`):** `male` und `female` entsprechen den Werten der Registerharmonisierung und verweisen über `meaning` auf die I14Y-Konzepte `sex/1` und `sex/2`. Für `non_binary` gibt es dort bewusst keine Entsprechung: Die amtliche Codeliste kennt als dritten Wert nur „unbestimmt", was etwas anderes bedeutet als eine positive Angabe jenseits von männlich und weiblich. Ist das Geschlecht nicht bekannt, wird deshalb gar kein Eintrag gesetzt — ein fehlender Eintrag und `non_binary` sind klar zu unterscheiden.
- **Harmonisierung über föderale Ebenen (Langzeitziel):** Die Verknüpfung derselben Person über die föderalen Ebenen hinweg ist ein wichtiges Langzeitziel. Der Aufbau einer zentralen Personendatenbank liegt ausserhalb der Möglichkeiten der eCH-Fachgruppe. Da für diesen Zweck bereits eine offene, etablierte Infrastruktur besteht, wird **Wikidata als übergreifender Identifikator empfohlen** (`wikidata_uri`); zusammen mit global eindeutigen Identifikatoren (URIs) lässt sich die Zuordnung so schrittweise über die Systeme hinweg harmonisieren.


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
