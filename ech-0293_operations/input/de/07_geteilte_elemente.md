\newpage

# Geteilte Elemente

## Referenzklassen

`PersonReference` und `GroupReference` benennen eine Person beziehungsweise eine Gruppe, ohne sie hier zu beschreiben: Wer eine Person oder ein Organ ist, definiert eCH-0294; der Ratsbetrieb verweist nur darauf. Neben dem Verweis hält die Referenz die wichtigsten Merkmale zum **Zeitpunkt der Verknüpfung** fest — bei einer Wortmeldung etwa die Fraktion, der die sprechende Person damals angehörte.

Das dient drei Zwecken:

- **Nützliche lokale Daten** ohne aufwändige Abfragen der vollständigen Entität
- **Keine Redundanz**, da nicht alle Angaben bei jeder Erwähnung wiederholt werden müssen
- **Implizite Versionierung**, da die Referenz unverändert bleibt, auch wenn sich die verknüpfte Person oder Gruppe später ändert

Anders als eine Entität ist eine Referenz nicht aus sich heraus identifiziert — sie benennt bloss eine identifizierte Entität. Deshalb ist die `global_uri` hier nicht obligatorisch: Verlangt wird nur, dass mindestens eine der beiden Angaben `local_id` oder `global_uri` gesetzt ist. Ein System, das von der referenzierten Entität nur die lokale Id kennt, gibt diese an; sie wird innerhalb derselben Lieferung aufgelöst. Über die Lieferung hinaus verweist die `global_uri`.

{{include:ech-0293_operations/output/docs/PersonReference.md}}

{{include:ech-0293_operations/output/docs/GroupReference.md}}

## Mixin-Klassen

Drei Klassen tragen keine eigenen Daten, sondern bündeln Slots, die in vielen Klassen gleich aussehen: die Identifikation einer Entität, ihre Erstellungs- und Änderungsdaten sowie der zeitliche Verlauf eines Ereignisses mit geplantem und tatsächlichem Beginn und Ende. Sie stammen aus dem gemeinsamen Schema der Fachgruppe (eCH-0292) und werden von deren Standards eingebunden, damit dieselben Angaben überall gleich heissen und gleich funktionieren.

Ein Mixin ist keine Oberklasse: Es entsteht keine Instanz einer Mixin-Klasse, und in den Daten ist von ihr nichts zu sehen. Die Attributtabellen der Klassen führen die geerbten Slots deshalb einzeln auf und vermerken mit „Vererbung" die Herkunft — die drei folgenden Abschnitte erklären, was hinter dieser Angabe steht.

{{include:ech-0293_operations/output/docs/HasIdentification.md}}

{{include:ech-0293_operations/output/docs/HasCreationModificationDates.md}}

{{include:ech-0293_operations/output/docs/IsEventWithDuration.md}}
