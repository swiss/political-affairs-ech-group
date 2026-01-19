# Design Principles Modell Politische Geschäfte

* Grundsätzlich keine Versionierung ausser es ist im Datenmodell vorgesehen (also nicht im Hintergrund ist alles versioniert)
* Es gibt keine volle Normalisierung
  - primär weil es keine einzelne Autorität gibt
  - gewisse Dinge werden wiederholt, als Vorteil davon hat man auch eine gewisse Geschichtsschreibung
  - Bsp: Eine Motion wird eingereicht, diese wird nicht nur mit einer ID zu einer Person verlinkt, sondern es werden auch "lokal" Infos hinzugefügt, bspw. Partei (obwohl die irgendwoanders auch zur Person hinterlegt ist)
* Wir machen unsere Schema für Daten Austausch, nicht so sehr dafür, dass die Systeme intern so arbeiten können
* Daten zu Personen, die aktualisiert werden, wenn die Person aber etwas macht, dann wird "snapshot" mässig ein paar Informationen festgehalten, die im Nachhinein nicht geändert werden (Name für dieses Prinzip muss noch irgendwie bezeichnet werden, evt. Actors-Reference)
* Wir haben jeweils URI (RDF; global) und ID (meist intern im Ratssystem)
* Wann machen wir eine eigene Klasse, wann ein Attribut type oder ähnlich um verschiedene "Klassen" zu machen?
