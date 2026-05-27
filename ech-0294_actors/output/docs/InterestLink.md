

# Class: InterestLink 


_[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation._

_[en] An interest link (conflict of interest, political financing) of a person to an organization._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](PersonReference.md) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung. [en] Reference to a person with snapshot data at time of linking.  |
| interest_type | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein). [en] Type of interest link (professional activity, political office, association).  |
| organization_label | 0..1 <br/> [String](String.md) | [en] Label of the organization. [de] Bezeichnung der Organisation.  |
| organization_uid | 0..1 <br/> [String](String.md) | [en] UID of the organization (for analysis with NOGA codes, etc.). [de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).  |
| organization_address | 0..1 <br/> [String](String.md) | [en] Address of the organization. [de] Adresse der Organisation.  |
| legal_form | 0..1 <br/> [String](String.md) | [en] Legal form of the organization. [de] Rechtsform der Organisation.  |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Position bezahlt ist. [en] Indicates if the position is paid.  |
| committee | 0..1 <br/> [String](String.md) | [en] Committee or board (e.g., foundation board, board of directors). [de] Gremium (z.B. Stiftungsrat, Verwaltungsrat).  |
| function_role | 0..1 <br/> [String](String.md) | [en] Function or role in the organization. [de] Funktion oder Rolle in der Organisation.  |
| local_id | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |














### Examples
#### Example: InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Bovida Real Estate AG, Baar
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Birchmeier Holding AG, Döttingen
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Burkart Advisory GmbH, Baden
legal_form: Gesellschaft mit beschränkter Haftung
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: ELCA Group SA, Lausanne
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Verein Landesausstellung Svizra27, Aarau
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FDP.Die Liberalen
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Stiebel Eltron AG, Lupfig
legal_form: Aktiengesellschaft
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: Verein
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Allianz Sicherheit Schweiz, Baden
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: Stiftung
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```






</div>