---
search:
  boost: 10.0
---

# Class: InterestLink 


_[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation._

_[en] An interest link (conflict of interest, political financing) of a person to an organization._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [concerned_person](concerned_person.md) | 0..1 <br/> [Person](Person.md) | [de] Link zu einer Person, auf die sich die Zugehörigkeit bezieht | direct |
| [interest_type](interest_type.md) | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verei... | direct |
| [organization_label](organization_label.md) | 0..1 <br/> [String](String.md) | [en] Label of the organization | direct |
| [organization_uid](organization_uid.md) | 0..1 <br/> [String](String.md) | [en] UID of the organization (for analysis with NOGA codes, etc | direct |
| [organization_address](organization_address.md) | 0..1 <br/> [String](String.md) | [en] Address of the organization | direct |
| [legal_form](legal_form.md) | 0..1 <br/> [String](String.md) | [en] Legal form of the organization | direct |
| [is_paid](is_paid.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Position bezahlt ist | direct |
| [committee](committee.md) | 0..1 <br/> [String](String.md) | [en] Committee or board (e | direct |
| [function_role](function_role.md) | 0..1 <br/> [String](String.md) | [en] Function or role in the organization | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:InterestLink |
| native | act:InterestLink |




## Examples
### Example: InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: professional_activity
organization_label: Bovida Real Estate AG, Baar
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: professional_activity
organization_label: Birchmeier Holding AG, Döttingen
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: professional_activity
organization_label: Burkart Advisory GmbH, Baden
legal_form: Gesellschaft mit beschränkter Haftung
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: professional_activity
organization_label: ELCA Group SA, Lausanne
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: association
organization_label: Verein Landesausstellung Svizra27, Aarau
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: false

```
### Example: InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: association
organization_label: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: association
organization_label: FDP.Die Liberalen
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: professional_activity
organization_label: Stiebel Eltron AG, Lupfig
legal_form: Aktiengesellschaft
committee: Beirat
function_role: Beirat
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: association
organization_label: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: Verein
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: association
organization_label: Allianz Sicherheit Schweiz, Baden
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: false

```
### Example: InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
concerned_person: https://www.wikidata.org/wiki/Q23060472
interest_type: association
organization_label: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: Stiftung
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```




