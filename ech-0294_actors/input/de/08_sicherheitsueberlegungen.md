\newpage

# Sicherheitsüberlegungen

<!-- ENTWURF — durch die Fachgruppe fachlich und juristisch zu prüfen.
     Grundlage: Feedback M. Stingelin vom 13.08.2026 (fehlende Kapitel gemäss
     eCH-0003-Vorlage) sowie die Notizen in 07_privacy_reflections.md_ -->

Der vorliegende Standard beschreibt Daten über natürliche Personen. Sie sind Personendaten im Sinne von Art. 5 lit. a des Bundesgesetzes über den Datenschutz (DSG, in Kraft seit 1. September 2023). Angaben zu Parteizugehörigkeit, Mandaten und Interessenbindungen lassen auf politische Ansichten schliessen und gelten als besonders schützenswerte Personendaten (Art. 5 lit. c DSG).

Der Standard schafft keine Rechtsgrundlage für eine Veröffentlichung. Er strukturiert Daten, deren Publikation sich aus dem Öffentlichkeitsprinzip, aus Offenlegungspflichten der Parlamente oder aus einer Einwilligung ergibt. Ob ein Datenelement publiziert werden darf, entscheidet die publizierende Stelle, nicht das Schema.

Bei der Anwendung sind insbesondere folgende Punkte zu beachten:

- **Rechtsgrundlage je Element.** Nicht jedes Element des Schemas ist in jedem Kontext publizierbar. Die publizierende Stelle prüft für jedes befüllte Element, ob eine gesetzliche Grundlage oder eine Einwilligung vorliegt.
- **Datensparsamkeit.** Optionale Elemente — insbesondere Geburtsdatum, Adresse und Kontaktangaben — sind nur zu befüllen, wenn sie für den Zweck der Publikation erforderlich sind.
- **Private Wohnadressen.** Deren Veröffentlichung ist Gegenstand parlamentarischer Vorstösse (vgl. Anhang A). Wo eine Adresse erforderlich ist, ist wenn möglich eine Geschäfts- oder Zustelladresse zu verwenden.
- **Aggregation.** Das Zusammenführen mehrerer Quellen kann Persönlichkeitsprofile ergeben, die über den Zweck der einzelnen Publikation hinausgehen. Wer Daten nach diesem Standard zusammenführt, prüft die Zweckbindung erneut.
- **Historische Angaben in Referenzen.** `PersonReference` und `GroupReference` halten lokale Merkmale zum Zeitpunkt der Verknüpfung fest. Diese dürfen nicht als aktueller Stand interpretiert werden.
- **Übertragung und Zugriff.** Werden Daten nach diesem Standard ausgetauscht, bevor sie öffentlich sind, sind die üblichen Vorkehrungen zu treffen: verschlüsselter Transport, Zugriff nur für autorisierte Personen, Schutz vor Veränderung während der Übertragung.
- **Verarbeitung fremder Daten.** Vor der Weiterverarbeitung eingelesener Lieferungen ist eine Schema-Validierung vorzunehmen. In Freitextfeldern übermittelte Inhalte sind vor der Anzeige zu escapen.
