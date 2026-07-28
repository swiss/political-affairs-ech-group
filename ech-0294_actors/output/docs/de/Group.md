

## Klasse: Group 


_Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](GroupType.md) | Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Benennung und Beschreibung der Gruppierung wird über `label` gemacht.  |
| label | 1..* <br/> [MultilingualValue](MultilingualValue.md) | Bezeichnung der Gruppe mit der Sprache, in der sie publiziert wird. Ist eine Gruppe amtlich in mehreren Sprachen benannt, wird pro Sprache ein Eintrag erfasst.  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abkürzung (kann mehrsprachig sein).  |
| description | * <br/> [MultilingualValue](MultilingualValue.md) | Kurze Beschreibung der Gruppierung.  |
| landing_page | * <br/> [MultilingualUri](MultilingualUri.md) | Website mit weiteren Informationen. Wird die Website je Sprache unter einer eigenen Adresse publiziert, wird pro Sprache ein Eintrag erfasst.  |
| parent_groups | * <br/> [Uriorcurie](Uriorcurie.md) | Übergeordnete Gruppe. Zum Beispiel die Mutterpartei zu Kantonalparteien, oder zur Beschreibung der Hierarchie in der Exekutive. Auch zur Verknüpfung von Subkommissionen mit Kommissionen oder Fraktionen mit Parlament und Partei. (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament und Fraktion → Partei.)  |
| spatial | 0..1 <br/> [String](String.md) | Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land). Formate: Gemeinde: ld.admin.ch/municipality/1234, Kanton: ld.admin.ch/canton/23, Bund: ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](Contact.md) | Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.  |
| addresses | * <br/> [Address](Address.md) | Adressen mit Typ (privat, geschäftlich, lokal).  |
| statutes_url | 0..1 <br/> [String](String.md) | URL zu Parteistatuten (PDF oder Webseite; optional für Parteien).  |
| party_color | 0..1 <br/> [String](String.md) | Parteifarbe als Hexadezimalwert (optional für Parteien, z.B. "#FF0000").  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |














### Beispiele
#### Beispiel: Group-groups__it

```yaml
local_id: 6627
global_uri: https://api.openparldata.ch/v1/groups/6627
label:
- value: Konsumenteninformation und -schutz
  language: de
- value: Information et défense des consommateurs
  language: fr
- value: Informazione e tutela dei consumatori
  language: it
description:
- value: L'intergroupe parlementaire « Information et défense des consommateurs »
    réunit toutes les sensibilités politiques. Cet intergroupe a pour mission d'informer
    et de sensibiliser les élu·e·s aux questions relatives à la défense des consommateur·rice·s
    en Suisse.
  language: fr
landing_page:
- value: https://www.parlament.ch/centers/documents/de/gruppen-der-bundesversammlung.pdf
  language: de
group_type:
  group_type_enum: interest_group
  label: Interessengruppe
spatial: https://ld.admin.ch/country/CHE
valid_from: 2012-01-01

```
#### Beispiel: Group-groups__de

```yaml
local_id: 50
global_uri: https://grosserrat.bs.ch/gremien/praesidium-und-buero
label:
- value: Büro des Grossen Rates
  language: de
group_type:
  group_type_enum: parliamentary_bureau
  label: Ratsbüro
spatial: https://ld.admin.ch/canton/12

```
#### Beispiel: Group-groups__fr

```yaml
local_id: 5000
global_uri: https://api.openparldata.ch/v1/groups/5000
label:
- value: Freiburger Delegation IPK strafrechtliche Einschliessung
  language: de
- value: Délégation FR à la CIP détention pénale
  language: fr
abbreviation:
- value: Del-StRFE
  language: de
- value: Del-DetPen
  language: fr
description:
- value: Die Interparlamentarische Aufsichtskommission strafrechtliche Einschliessung
    besteht aus 18 Grossrätinnen und Grossräten aus den sechs Vertragskantonen Freiburg,
    Genf, Jura, Neuenburg, Waadt und Wallis.
  language: de
- value: 'La Commission interparlementaire de contrôle détention pénale est composée
    de 18 députés issus des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel,
    Vaud et Valais.'
  language: fr
landing_page:
- value: https://www.fr.ch/de/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: de
- value: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: fr
group_type:
  group_type_enum: delegation
  label: Delegation
spatial: https://ld.admin.ch/canton/10
valid_from: 2007-12-12

```






</div>