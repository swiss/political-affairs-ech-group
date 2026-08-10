\newpage

# Geteilte Elemente

## Reference Classes

`PersonReference` und `GroupReference` werden verwendet, um Personen bzw. Gruppen **lokal** innerhalb einer anderen Entität zu referenzieren. Neben dem eigentlichen Link zur vollständigen Entität werden dabei nur die relevanten Informationen zum **Zeitpunkt der Verknüpfung** gespeichert – es müssen also nicht alle Informationen einer Person oder Gruppe bei jeder Erwähnung wiederholt werden.

Ein Beispiel: Eine Motion verweist auf die Person, die sie eingereicht hat. Zusätzlich zum Link auf die vollständige Personen-Entität speichert die Motion lokal Informationen wie die politische Partei oder die Rolle der Person **zum Zeitpunkt der Einreichung**. Wechselt die Person später die Partei oder die Rolle, bleibt die Information in der Motion dennoch korrekt und unveränderlich.

Dies dient drei Zwecken:

- **Nützliche lokale Daten** ohne aufwändige Abfragen der vollständigen Entität
- **Keine Redundanz**, da nicht alle Informationen bei jeder Erwähnung wiederholt werden müssen
- **Implizite Versionierung**, da die lokale Referenz unverändert bleibt, auch wenn sich die verknüpfte Entität später ändert

Anders als eine Entität ist eine Referenz nicht aus sich heraus identifiziert – sie benennt bloss eine identifizierte Entität. Deshalb ist die `global_uri` hier nicht obligatorisch: Verlangt wird nur, dass mindestens eine der beiden Angaben `local_id` oder `global_uri` gesetzt ist. Ein System, das von der referenzierten Entität nur die lokale Id kennt, gibt diese an; sie wird innerhalb derselben Lieferung aufgelöst. Über die Lieferung hinaus verweist die `global_uri`.

{{include:ech-0294_actors/output/docs/PersonReference.md}}

{{include:ech-0294_actors/output/docs/GroupReference.md}}

## Mehrfach benutzte Klassen

Eine Adresse wird in `street_address`, `postal_code`, `postal_locality` und `country` geschrieben und kann über `address_uri` ins Amtliche Gebäudeadressverzeichnis von swisstopo verweisen. Die letzte Zahl dieser URI ist die EGAID, der eidgenössische Gebäudeadressidentifikator; `https://geo.ld.admin.ch/location/address/101009806` bezeichnet damit „Rue de Genève 17, 1003 Lausanne" als amtlich geführte Gebäudeadresse.

`address_uri` ist optional. Die geschriebene Adresse allein ist zulässig, vorzuziehen ist aber der Verweis über die EGAID: Sie ist ein eindeutiger Identifikator und über die Zeit stabil, während Strassennamen geändert, Gemeinden fusioniert und Postleitzahlen neu zugeschnitten werden.

Um zur EGAID zu gelangen, kann man die [Such-API von geo.admin.ch](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Rue+de+Gen%C3%A8ve+17+1003+Lausanne&type=locations&origins=address) benutzen oder mit dem [Amtlichen Verzeichnis der Gebäudeadressen](https://www.swisstopo.admin.ch/de/amtliches-verzeichnis-der-gebaeudeadressen) abgleichen. Erfasst wird das Ergebnis in `address_uri`.

{{include:ech-0294_actors/output/docs/Address.md}}

{{include:ech-0294_actors/output/docs/AddressTypeEnum.md}}

{{include:ech-0294_actors/output/docs/Contact.md}}


## Mixin-Klassen

Vier Klassen tragen keine eigenen Daten, sondern bündeln Slots, die in vielen Klassen gleich aussehen: die Identifikation einer Entität, die Identifikation einer Referenz, die zeitliche Gültigkeit und die Erstellungs- und Änderungsdaten. Sie stammen aus dem gemeinsamen Schema der Fachgruppe (eCH-0292) und werden von den Standards der Fachgruppe eingebunden, damit dieselben Angaben überall gleich heissen und gleich funktionieren.

Ein Mixin ist keine Oberklasse: Es entsteht keine Instanz einer Mixin-Klasse, und in den Daten ist von ihr nichts zu sehen. Die Attributtabellen der Klassen führen die geerbten Slots deshalb einzeln auf und vermerken mit „Vererbung" die Herkunft — die vier folgenden Abschnitte erklären, was hinter dieser Angabe steht.

{{include:ech-0294_actors/output/docs/HasIdentification.md}}

{{include:ech-0294_actors/output/docs/HasReferenceIdentification.md}}

{{include:ech-0294_actors/output/docs/HasTemporalValidity.md}}

{{include:ech-0294_actors/output/docs/HasCreationModificationDates.md}}
