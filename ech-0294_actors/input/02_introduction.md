
# Einführung

Der Inhalt dieses Substandards sind die politischen Akteure, seien es Personen (Rats- oder Verwaltungsmitglieder) oder Gruppen (Parteien, Fraktionen, Gremien, Kommissionen und Verbände).

Zum einen wird eine Struktur definiert, die es erlaubt, Informationen in Ratsinformationssystemen oder ähnlichen Systemen der Öffentlichkeit strukturiert zur Verfügung zu stellen. Zum anderen werden den politischen Akteuren eindeutige Identifikatoren zugeteilt, mit dem Ziel, aus anderen Standards dieser Fachgruppe darauf referenzieren zu können.

Es wurde bei der Definition darauf geachtet, dass es den publizierenden Organisationen ermöglicht wird, alle Informationen möglichst strukturiert zu veröffentlichen. Dies erlaubt es, für die Konsumenten einen maximalen Nutzen zu erzielen. Es ist aber jeweils auch möglich auszudrücken, wenn Informationen nicht in der maximalen Detailstufe vorhanden sind. (Es kann zum Beispiel bei einem Vornamen angegeben werden, ob es sich um den Rufnamen oder den amtlichen Namen handelt. Falls diese Information aber nicht vorhanden ist, kann der Name auch ohne diese Zusatzinformation publiziert werden.)

## Ziele des Standards und erhoffte Wirkung

Das Ziel des Standards ist es, Organisationen, welche Informationen zu politischen Geschäften veröffentlichen, ein Datenmodell zur Verfügung zu stellen. Die Wirkung, die dabei erhofft wird, ist eine einheitliche Informationsgrundlage zu den politischen Geschäften in der Schweiz über alle föderalen Ebenen hinweg. Damit können die Informationen im politischen Diskurs besser gelesen, verarbeitet und verstanden werden. Die Transparenz und Nachvollziehbarkeit der Entscheidungen im politischen System der Schweiz soll weiter erhöht werden.

Besondere Ziele des Substandards sind, die Akteure im politischen Prozess identifizierbar zu machen und mit den rechtlich nötigen Informationen auszugestalten. Als weiteres Ziel wird ein langfristiger Abgleich der Akteure über die föderalen Stufen angestrebt. Der Substandard bietet eine Struktur an, welche von den jeweiligen Organisationen (Städte, Kantone und Bund) nach deren Anforderungen und rechtlichem Kontext umgesetzt werden kann.

## Identifizierte Zielgruppen

Die Arbeitsgruppe hat folgende Zielgruppen für den Standard identifiziert, welche direkt oder indirekt angesprochen werden. Diese Zielgruppen wurden als Leitfaden bei Entscheidungen zum Standard als Bedarfsträger identifiziert.

* Städte/Gemeinden, Kantone und Eidgenossenschaft (Publikation im Auftrag)
* Politikerinnen und Politiker (Entstehung und Konsum)
* Journalismus, Forschung: Politikwissenschaft, Historiker, Open-Data-Portale, Politmonitor/OParlData (Konsum, Monitoring und Veredelung von Informationen)
* Öffentliche Verwaltung: Statistikämter und Archive (Auswertung, Monitoring, Archivierung)
* Öffentlichkeit (Konsum)

## Arbeitsvorgang

Folgende Themen wurden in der aufgeführten Reihenfolge seit 2025 in der Subgruppe angegangen:

1. Personen: Ratsmitglieder, Verwaltungsmitglieder
2. Gruppen / Organe / Interessengruppen: Parteien, Fraktionen, Gremien, Kommissionen, Verbände
3. Interessenbindungen, Konflikte, Politikfinanzierung
4. Verknüpfungen gleicher Personen über föderale Stufen hinweg

## Allgemeine Technische Informationen

### Übersicht

Das Schema basiert auf vier Hauptklassen, die zusammen das politische Akteurssystem der Schweiz abbilden:

- **Person** – Natürliche Personen im politischen Kontext
- **Group** – Politische Gruppen, Organe und Organisationen
- **Membership** – Verbindung zwischen Personen und Gruppen
- **InterestLink** – Interessenbindungen von Personen an Organisationen

`Membership` ist das zentrale Bindeglied zwischen `Person` und `Group` und ermöglicht die Zuordnung zu Parteien, Fraktionen, Kommissionen und Parlamenten. `InterestLink` ergänzt das Schema um Transparenzanforderungen gemäss den Vorgaben der Bundesversammlung.

### Identifikatoren

Das vorliegende Daten-Modell erlaubt es folgende Typen von Identifikatoren zu verwenden:

1. **Lokaler Identifikator (`local_id`)**: Ein systeminterner Identifikator welcher vom publizierenden System genutzt wird, wenn nicht schon ausschliesslich eine `global_uri` benutzt wird. (Optional)

2. **Globaler Identifikator (`global_uri`)**: Ein globaler Identifikator welcher über verschiedene Systeme hinweg gültig ist. Dieser besteht meist aus einem Namespace (Domainnamen) der publizierenden Organisation zusammen mit einem lokalen Identifikator. (z.B. https://ld.bs.ch/personen_id/3456) (Zwingend)

3. **Wikidata Identifikator (`wikidata_uri`)**: Eine Wikidata Identifikator, um Personen und Gruppen Systemübergreifend zu identifizieren (z.B. http://www.wikidata.org/entity/Q115531 für Adolf Ogi) (Optional)


### Temporale Validität

Viele Attribute unterstützen zeitliche Gültigkeit durch `valid_from` und `valid_until`, wie z.B. Name, Adresse, Geschlecht, Staatsbürgerschaft, Beruf und Wahlkreis.

**Beispiel:**
```yaml
names:
  - name_type: officialLastName
    value: Müller
    valid_from: 1980-01-01
    valid_until: 2010-06-15
  - name_type: officialLastName
    value: Meier-Müller
    valid_from: 2010-06-16
```