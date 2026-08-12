\newpage

# Identifikation

## ELI-URI-Vorlage

Der Standard folgt ELI und identifiziert Rechtstexte über HTTP-URIs. Die URIs werden formell über maschinenlesbare URI-Vorlagen nach RFC 6570 beschrieben. Die Umsetzung von ELI-URIs ist nur einer von vier Pfeilern des ELI-Standards; die Pfeiler 2 bis 4 setzen eine Beschreibung der Rechtsdaten mit Metadaten voraus — siehe das Kapitel Metadaten.

ELI-URIs bestehen aus hierarchisch aufgebauten Komponenten, die nach nationalen Anforderungen ausgewählt werden. Die Komponenten werden durch „/" getrennt und bilden zusammen einen Pfad, der aus Sicht der Endnutzenden wie aus rechtlicher Sicht eine semantische Bedeutung tragen kann. Mit Ausnahme der ersten Komponente `eli` sind alle optional. Das folgende Muster nutzt sämtliche vorgeschlagenen Referenzkomponenten in der vorgeschlagenen Reihenfolge:

```
/eli/{jurisdiction}/{agent}/{subagent}/{year}/{month}/{day}/{type}/{subtype}/{domain}/{natural identifier}/{level 1…}/{point in time}/{version}/{language}
```

Die Referenzkomponenten lassen sich in vier Gruppen aufteilen: Jurisdiction, Reference, Subdivision und Point in time. Zusätzlich wird zwischen der massgebenden und der konsolidierten Fassung (Version) sowie zwischen den sprachlichen Fassungen (Language) unterschieden. Gliederungsebenen innerhalb eines Dokuments (Subdivision) und der Umgang mit Korrigenda (Subtype) bleiben hier ausgeblendet, weil die Dokumentenperspektive im Vordergrund steht.

Zwei Komponentengruppen sind für die schweizerische URI-Vorlage massgebend:

- **Jurisdiction im weiteren Sinn** — bei mehreren publizierenden Stellen ist zunächst zu klären, welchem Gemeinwesen ein Rechtstext zugeordnet wird und, wo nötig, welcher Akteur ihn erlassen hat (Agent beziehungsweise Subagent).
- **Reference** — zur eindeutigen Identifikation muss ein Rechtstext referenzierbar sein. Wie das geschieht, ist von Land zu Land verschieden und hängt stark von der Publikationspraxis ab; denkbar sind Zeitangaben, Dokumententyp, Themen-Codes (Domain) und weitere Unterscheidungsmerkmale (Natural identifier).

## Referenzkomponenten für die Schweiz

| Komponente | Beschreibung | Beispielwert |
|---|---|---|
| `jurisdiction` | Zuständiger Staat oder Kanton | `ch`, `ch-zh`, `ch-ge` |
| `type` | Typ des Rechtsdokuments | `cc` (konsolidiert), `oc` (Amtsblatt), `fga`, `dl` |
| `year` | Erlassjahr | `1999`, `2024` |
| `natural_id` | Natürliche Identifikationsnummer | `404`, `123` |
| `language` | Sprachcode (ISO 639-1) | `de`, `fr`, `it`, `rm` |

## Identifikation im Dokument

Der FRBR-Block `akn:identification` trägt die drei Ebenen Work, Expression und Manifestation. Jede Ebene führt ihre eigene URI, ihre Daten und ihre Autoren; die Ebene Expression ergänzt die Sprache, die Ebene Manifestation das Format.

{{include:ech-0296_laws/output/docs/Identification.md}}

{{include:ech-0296_laws/output/docs/FRBRWork.md}}

{{include:ech-0296_laws/output/docs/FRBRExpression.md}}

{{include:ech-0296_laws/output/docs/FRBRManifestation.md}}

{{include:ech-0296_laws/output/docs/FRBRDate.md}}

{{include:ech-0296_laws/output/docs/FRBRAuthor.md}}

{{include:ech-0296_laws/output/docs/FRBRName.md}}

## Element-Identifikatoren

Innerhalb eines Dokuments trägt jedes Hierarchieelement, jeder Artikel, jeder Unterabschnitt und jeder Absatz ein `@eId`. Es folgt der AKN-Namenskonvention und bildet den Pfad im Dokument ab (`ti_1`, `ch_1`, `art_1`, `art_1-para_1`) — es ist also bewusst kein zufälliger Identifikator. Die Fedlex-Schematron-Regeln verlangen seine Anwesenheit, nicht aber seine Eindeutigkeit: Reale Dokumente der Systematischen Rechtssammlung enthalten mehrfach vergebene `@eId`.

{{include:ech-0296_laws/output/docs/ELIURI.md}}

{{include:ech-0296_laws/output/docs/EIdType.md}}

{{include:ech-0296_laws/output/docs/AnchorRef.md}}
