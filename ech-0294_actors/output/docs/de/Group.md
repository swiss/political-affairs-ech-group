

## Klasse: Group 


_Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| group_type | 1 <br/> [GroupType](GroupType.md) | Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Benennung und Beschreibung der Gruppierung wird über `label` gemacht.  |
| label | 1..* <br/> [MultilingualValue](MultilingualValue.md) | Bezeichnung der Gruppe mit der Sprache, in der sie publiziert wird. Ist eine Gruppe amtlich in mehreren Sprachen benannt, wird pro Sprache ein Eintrag erfasst.  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abkürzung (kann mehrsprachig sein).  |
| description | * <br/> [MultilingualValue](MultilingualValue.md) | Kurze Beschreibung der Gruppierung.  |
| organization_uid | 0..1 <br/> [String](String.md) | UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm  |
| landing_page | * <br/> [MultilingualUri](MultilingualUri.md) | Website mit weiteren Informationen. Wird die Website je Sprache unter einer eigenen Adresse publiziert, wird pro Sprache ein Eintrag erfasst.  |
| parent_groups | * <br/> [GroupReference](GroupReference.md) | Verweis auf die übergeordneten Gruppen als GroupReference, also angegeben über deren local_id oder deren global_uri. Hierher gehört nur eine echte Über-/Unterordnung: die Mutterpartei einer Kantonalpartei, die Hierarchie in der Exekutive, eine Subkommission unter ihrer Kommission oder eine Fraktion unter ihrem Parlament. (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament.) Die eine Fraktion tragenden Parteien sind ihr nicht übergeordnet und werden hier deshalb nicht angegeben.  |
| spatial | 0..1 <br/> [String](String.md) | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](Contact.md) | Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.  |
| addresses | * <br/> [Address](Address.md) | Adressen mit Typ (privat, geschäftlich, lokal).  |
| statutes_url | 0..1 <br/> [String](String.md) | URL zu Parteistatuten (PDF oder Webseite; optional für Parteien).  |
| party_color | 0..1 <br/> [String](String.md) | Parteifarbe als Hexadezimalwert (optional für Parteien, z.B. "#FF0000").  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |














### Beispiele
#### Beispiel Group: Cantonal party referencing its national party

```yaml
groups:
- global_uri: https://www.evp-bs.ch/
  label:
  - value: Evangelische Volkspartei Basel-Stadt
    language: de
  abbreviation:
  - value: EVP BS
    language: de
  group_type:
    group_type_enum: party
    label:
    - value: Partei
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - global_uri: https://www.evppev.ch/
    label: Evangelische Volkspartei der Schweiz
    abbreviation:
    - value: EVP
      language: de

```
#### Beispiel Group: Council bureau referencing its parliament

```yaml
groups:
- local_id: 50
  global_uri: https://grosserrat.bs.ch/gremien/praesidium-und-buero
  label:
  - value: Büro des Grossen Rates
    language: de
  group_type:
    group_type_enum: council_bureau
    label:
    - value: Ratsbüro
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 33
    global_uri: https://www.grosserrat.bs.ch/
    label: Grosser Rat Basel-Stadt

- local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label:
  - value: Grosser Rat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Beispiel Group: Municipal parliament with spatial reference

```yaml
groups:
- local_id: 700
  global_uri: >-
    https://www.stadt.sg.ch/home/verwaltung-politik/demokratie-politik/stadtparlament.html
  label:
  - value: Stadtparlament St. Gallen
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/municipality/3203

```
#### Beispiel Group: State chancellery referencing its government

```yaml
groups:
- local_id: 7172
  global_uri: https://www.bs.ch/regierungsrat/staatskanzlei
  label:
  - value: Staatskanzlei Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_secretariat
    label:
    - value: Staatskanzlei
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 1300
    global_uri: https://www.regierungsrat.bs.ch/
    label: Regierungsrat Basel-Stadt

- local_id: 1300
  global_uri: https://www.regierungsrat.bs.ch/
  label:
  - value: Regierungsrat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_executive
    label:
    - value: Regierung (Exekutivrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Beispiel Group: Parliamentary group referencing the parliament it belongs to

```yaml
groups:
- local_id: 1266
  global_uri: https://grosserrat.bs.ch/gremien/parteien-und-fraktionen/mitte-evp
  label:
  - value: Die Mitte / Evangelische Volkspartei
    language: de
  group_type:
    group_type_enum: parliamentary_group
    label:
    - value: Fraktion
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 33
    global_uri: https://www.grosserrat.bs.ch/
    label: Grosser Rat Basel-Stadt

```
#### Beispiel Group: Committee referencing its cantonal council

```yaml
groups:
- local_id: 3
  global_uri: >-
    https://ar.ch/kantonsrat/kommissionen/staendige-kommissionen-des-kantonsrates/geschaeftspruefungskommission/
  label:
  - value: Geschäftsprüfungskommission
    language: de
  abbreviation:
  - value: GPK
    language: de
  group_type:
    group_type_enum: committee
    label:
    - value: Kommission
      language: de
  spatial: https://ld.admin.ch/canton/15
  parent_groups:
  - local_id: 34
    global_uri: https://www.ar.ch/kantonsrat/
    label: Kantonsrat Appenzell Ausserrhoden

- local_id: 34
  global_uri: https://www.ar.ch/kantonsrat/
  label:
  - value: Kantonsrat Appenzell Ausserrhoden
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/15

```
#### Beispiel Group: Interest group with a trilingual name and contact

```yaml
groups:
- local_id: 6627
  global_uri: https://www.parlament.ch/de/organe/gruppen/konsumenteninformation-und-schutz
  label:
  - value: Konsumenteninformation und -schutz
    language: de
  - value: Information et défense des consommateurs
    language: fr
  - value: Informazione e tutela dei consumatori
    language: it
  description:
  - value: >-
      L'intergroupe parlementaire « Information et défense des consommateurs » réunit
      toutes les sensibilités politiques. Cet intergroupe a pour mission d'informer
      et de sensibiliser les élu·e·s aux questions relatives à la défense des consommateur·rice·s
      en Suisse.
    language: fr
  landing_page:
  - value: https://www.parlament.ch/centers/documents/de/gruppen-der-bundesversammlung.pdf
    language: de
  contacts:
  - contact_type: email
    value: l.altwegg@frc.ch
    label: Sekretariat
  - contact_type: phone
    value: +41 21 331 00 95
    label: Sekretariat
  addresses:
  - address_type: businessAddress
    address_uri: https://geo.ld.admin.ch/location/address/101009806
    street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
      585
    postal_code: '1001'
    postal_locality: Lausanne
    country: CH
  group_type:
    group_type_enum: interest_group
    label:
    - value: Interessengruppe
      language: de
    - value: Groupe d'intérêt
      language: fr
    - value: Gruppo d'interesse
      language: it
  spatial: https://ld.admin.ch/country/CHE
  valid_from: 2012-01-01

```
#### Beispiel Group: Extra-parliamentary commission with decision-making powers

```yaml
groups:
- global_uri: https://www.weko.admin.ch/
  label:
  - value: Wettbewerbskommission
    language: de
  - value: Commission de la concurrence
    language: fr
  - value: Commissione della concorrenza
    language: it
  abbreviation:
  - value: WEKO
    language: de
  - value: COMCO
    language: fr
  - value: COMCO
    language: it
  landing_page:
  - value: https://www.weko.admin.ch/de
    language: de
  - value: https://www.weko.admin.ch/fr
    language: fr
  - value: https://www.weko.admin.ch/it
    language: it
  group_type:
    group_type_enum: committee_extraparliamentary
    label:
    - value: Ausserparlamentarische Kommission
      language: de
  spatial: https://ld.admin.ch/country/CHE

```
#### Beispiel Group: Bilingual delegation to an intercantonal body

```yaml
groups:
- local_id: 5000
  global_uri: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
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
  - value: >-
      Die Interparlamentarische Aufsichtskommission strafrechtliche Einschliessung
      besteht aus 18 Grossrätinnen und Grossräten aus den sechs Vertragskantonen Freiburg,
      Genf, Jura, Neuenburg, Waadt und Wallis.
    language: de
  - value: >-
      La Commission interparlementaire de contrôle détention pénale est composée de
      18 députés issus des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel,
      Vaud et Valais.
    language: fr
  landing_page:
  - value: https://www.fr.ch/de/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
    language: de
  - value: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
    language: fr
  group_type:
    group_type_enum: delegation
    label:
    - value: Delegation
      language: de
    - value: Délégation
      language: fr
  spatial: https://ld.admin.ch/canton/10
  valid_from: 2007-12-12

```
#### Beispiel Group: Association with UID and legal form from the commercial register

```yaml
groups:
- global_uri: https://www.frc.ch/
  organization_uid: CHE106063525
  legal_form: '0109'
  label:
  - value: Fédération romande des consommateurs
    language: fr
  abbreviation:
  - value: FRC
    language: fr
  group_type:
    group_type_enum: association
    label:
    - value: Verein
      language: de
  spatial: https://ld.admin.ch/canton/22

```






</div>