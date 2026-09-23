

## Klasse: ElectoralDistrict 


_Wahlkreis oder Wahlregion, die einer Mitgliedschaft zugeordnet ist. Die zeitliche Gültigkeit wird von der umschliessenden Mitgliedschaft übernommen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Für IRI-Referenzen sollen die LINDAS-Ressourcen verwendet werden. Die IRI für die verschiedenen Verwaltungsebenen der Schweizer Raumeinheiten sind bei LINDAS zu finden: https://ld.admin.ch/country/CHE. Unter den Links im Abschnitt schema:containsPlace kann die gewünschte Ebene gefunden werden. Beispiele für die einzelnen Verwaltungsebenen: - Land - Schweiz: https://ld.admin.ch/country/CHE - Kanton - Aargau: https://ld.admin.ch/canton/19 - Bezirk - Brig: https://ld.admin.ch/district/2301 - Gemeinde - Versoix: https://ld.admin.ch/municipality/6644 Wahlkreise, die keiner amtlichen Raumeinheit entsprechen, etwa Wahlkreise, die Wohnviertel einer Gemeinde zusammenfassen, erhalten stattdessen einen Identifikator im Namensraum der publizierenden Stelle. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| label | * <br/> [MultilingualValue](MultilingualValue.md) | Bezeichnung des Wahlkreises, wie sie von der für die Wahl zuständigen Stelle publiziert wird, mit der Sprache, in der sie publiziert wird. Ist ein Wahlkreis amtlich in mehreren Sprachen benannt, wird pro Sprache ein Eintrag erfasst.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |














### Beispiele
#### Beispiel ElectoralDistrict: Canton as electoral district identified via its LINDAS resource

```yaml
electoral_district:
  global_uri: https://ld.admin.ch/canton/12
  label:
  - value: Basel-Stadt
    language: de

```
#### Beispiel ElectoralDistrict: Electoral district without an official spatial unit

```yaml
electoral_district:
  global_uri: https://grosserrat.bs.ch/wahlkreise/kleinbasel
  label:
  - value: Kleinbasel
    language: de

```






</div>