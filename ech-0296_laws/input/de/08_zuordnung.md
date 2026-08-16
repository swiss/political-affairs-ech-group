\newpage

# Anhang B – Zuordnung zu Akoma Ntoso

Jede Klasse und jeder Slot dieses Standards trägt die Entsprechung im Akoma-Ntoso-Vokabular am Element selbst — als `exact_mappings`, `close_mappings` und die weiteren Mapping-Angaben, die LinkML dafür vorsieht. Die folgende Tabelle ist daraus erzeugt und nicht von Hand geführt; wer eine Klasse an ein anderes Element bindet, ändert das Schema.

Aus derselben Quelle entsteht ein Mapping-Set nach SSSOM (Simple Standard for Sharing Ontology Mappings) als `output/mappings/ech-0296_laws.sssom.tsv`. Es hält zu jeder Zeile fest, wie eng die Entsprechung ist (`exactMatch`, `closeMatch`, `narrowMatch`, `broadMatch`) und worauf sie beruht, und lässt sich mit den Werkzeugen der Mapping Commons prüfen und weiterverarbeiten. Dieselben Angaben stehen als `skos:exactMatch`-Tripel im RDF-Export des Schemas (`output/schema.ttl`).

Die Zuordnung zum European Legislation Identifier ist für den Identifikationsblock gesetzt, und zwar auf zwei Arten. Wo die Entsprechung eins zu eins ist, trägt das Element den ELI-Begriff als eigene Identität (`class_uri`, `slot_uri`): Die FRBR-Ebenen *sind* `eli:LegalResource`, `eli:LegalExpression` und `eli:Format`, und der RDF-Export schreibt sie unmittelbar so. Wo die Entsprechung nur nahe liegt, bleibt es bei `closeMatch` — `frbr_country` etwa nennt einen Ländercode, wo ELI eine Verwaltungseinheit erwartet, und `frbr_authoritative` ist ein Wahrheitswert, wo ELI eine Werteliste führt.

Eine dritte Art von Zuordnung hängt weder an der Klasse noch am Slot, sondern am **Wert**: Welche ELI-Eigenschaft ein Datum meint, entscheidet sein `@name`. Die zulässigen Werte tragen ihre Entsprechung deshalb selbst, und die Zuordnung stellt zwei fremde Vokabulare gegenüber — `jolux:dateEntryInForce` gegen `eli:first_date_entry_in_force`. Kantonale Publikationsstellen führen eigene Bezeichnungen wie `Beschlussdatum`; der Slot lässt sie zu, ohne Zuordnung.

{{include:ech-0296_laws/output/mappings/ech-0296_laws_de.md}}
