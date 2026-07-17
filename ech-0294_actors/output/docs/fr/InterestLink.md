

## Classe: InterestLink 


_Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne avec une organisation située en dehors du schéma des acteurs._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Référence à une personne avec des données instantanées au moment de la mise en relation.  |
| interest_type | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | Type de lien d'intérêts (activité professionnelle, mandat politique, association).  |
| organization_name | 0..1 <br/> [String](String.md) | Nom de l'organisation ou de l'entreprise.  |
| organization_uid | 0..1 <br/> [String](String.md) | IDE de l'organisation (format eCH-0097 : CHE-XXX.XXX.XXX) issu du registre fédéral IDE (uid.admin.ch).  |
| organization_address | 0..1 <br/> [String](String.md) | Adresse de l'organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Forme juridique de l'organisation. Voir le vocabulaire contrôlé : https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Indique si le poste est rémunéré.  |
| committee | 0..1 <br/> [String](String.md) | Comité ou organe au sein de l'organisation (p. ex. conseil d'administration, conseil de fondation, comité directeur, conseil de surveillance, comité consultatif, direction).  |
| function_role | 0..1 <br/> [String](String.md) | Fonction ou rôle dans l'organisation (p. ex. président/e, vice-président/e, membre, délégué, directeur/directrice, conseiller/ère).  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [organization_uid](organization_uid.md)
- [organization_name](organization_name.md)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |














### Exemples
#### Exemple : InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Allianz Sicherheit Schweiz, Baden
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Exemple : InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Burkart Advisory GmbH, Baden
legal_form: '0107'
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Stiebel Eltron AG, Lupfig
legal_form: '0106'
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Birchmeier Holding AG, Döttingen
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Verein Landesausstellung Svizra27, Aarau
legal_form: 0109
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Exemple : InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: 0109
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: 0109
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Bovida Real Estate AG, Baar
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: ELCA Group SA, Lausanne
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FDP.Die Liberalen
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: '0110'
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```






</div>