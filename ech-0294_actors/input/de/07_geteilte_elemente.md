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

Eine Adresse wird zweifach geführt: als Verweis ins Amtliche Gebäudeadressverzeichnis von swisstopo (`address_uri`) und als geschriebene Adresse in `street_address`, `postal_code`, `postal_locality` und `country`. Die letzte Zahl der URI ist die EGAID, der eidgenössische Gebäudeadressidentifikator – `https://geo.ld.admin.ch/location/address/101009806` bezeichnet damit „Rue de Genève 17, 1003 Lausanne" als amtlich geführte Gebäudeadresse.

Der Verweis ist die stabilere Angabe: Strassennamen werden geändert, Gemeinden fusionieren, Postleitzahlen werden neu zugeschnitten, doch die EGAID bleibt und lässt sich mit dem Gebäude- und Wohnungsregister sowie mit Geodaten verbinden. Die geschriebene Adresse ersetzt sie nicht, weil sie oft mehr enthält als das Verzeichnis kennt – einen Organisationsnamen, ein Postfach, einen Zusatz „c/o". Im Beispiel der Fédération romande des consommateurs zeigt sich das deutlich: Die EGAID bezeichnet die physische Adresse an der Rue de Genève 17 in 1003 Lausanne, während die geschriebene Adresse das Postfach 585 und dessen eigene Postleitzahl 1001 führt. Beide Angaben sind richtig, und keine ist aus der anderen herzuleiten.

Wer nur die geschriebene Adresse hat, kommt auf zwei Wegen zur EGAID. Für einzelne Adressen liefert die Such-API von geo.admin.ch sie mit:

```
https://api3.geo.admin.ch/rest/services/api/SearchServer
  ?searchText=Rue+de+Genève+17+1003+Lausanne&type=locations&origins=address
```

Im Treffer steht sie im `links`-Eintrag zum Layer `ch.swisstopo.amtliches-gebaeudeadressverzeichnis` als letzter Abschnitt der Adresse — hier `101009806`. Für viele Adressen lohnt der zweite Weg: Das Amtliche Verzeichnis der Gebäudeadressen ist als Ganzes beziehbar (CSV, GDB, XTF) und lässt sich einmalig gegen den eigenen Bestand abgleichen.

Zu unterscheiden sind dabei vier Identifikatoren, die im selben Datensatz nebeneinander stehen: die **EGAID** (`adr_egaid`) bezeichnet die Adresse, der **EGID** (`bdg_egid`) das Gebäude, der **EDID** (`adr_edid`) den Eingang und der **ESID** (`str_esid`) die Strasse. In `address_uri` gehört die EGAID.

Nicht jede Adresse ist im Verzeichnis auffindbar, etwa eine Adresse im Ausland. `address_uri` ist deshalb optional; wo sie bekannt ist, soll sie gesetzt werden.

{{include:ech-0294_actors/output/docs/Address.md}}

{{include:ech-0294_actors/output/docs/AddressTypeEnum.md}}

{{include:ech-0294_actors/output/docs/Contact.md}}