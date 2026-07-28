

## Classe: Group 


_Un groupe, une organisation ou une collectivité politique (p. ex. parti, commission, parlement, département)._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](GroupType.md) | Type de groupe (p. ex. parti, commission, parlement ou similaire). La désignation et la description exactes du groupe sont fournies via `label`.  |
| label | 1..* <br/> [MultilingualValue](MultilingualValue.md) | Désignation du groupe avec la langue dans laquelle elle est publiée. Lorsqu'un groupe porte officiellement un nom dans plusieurs langues, une entrée est saisie par langue.  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abréviation (peut être multilingue).  |
| description | * <br/> [MultilingualValue](MultilingualValue.md) | Description de l'entité.  |
| organization_uid | 0..1 <br/> [String](String.md) | IDE de l'organisation (format eCH-0097 : CHE-XXX.XXX.XXX) issu du registre fédéral IDE (uid.admin.ch).  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Forme juridique de l'organisation. Voir le vocabulaire contrôlé : https://register.ld.admin.ch/i14y/concept/legalForm  |
| landing_page | * <br/> [MultilingualUri](MultilingualUri.md) | Site web fournissant de plus amples informations. Lorsque le site est publié à une adresse propre par langue, une entrée est saisie par langue.  |
| parent_groups | * <br/> [Uriorcurie](Uriorcurie.md) | Lien vers les groupes parents. Par exemple, le parti faîtier pour les partis cantonaux, ou pour décrire la hiérarchie au sein de l'exécutif. Utilisé également pour rattacher des sous-commissions à des commissions, ou des groupes parlementaires à la fois à leur parlement et à leur parti. (parentGroup est généralement utilisé au sein d'un même group_type, mais les liens intertypes sont autorisés, p. ex. groupe parlementaire → parlement et groupe parlementaire → parti.)  |
| spatial | 0..1 <br/> [String](String.md) | Référence spatiale (numéro OFS de commune, numéro OFS de canton ou pays). Formats : commune : ld.admin.ch/municipality/1234, canton : ld.admin.ch/canton/23, pays : ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](Contact.md) | Informations de contact (e-mail, site web, réseaux sociaux). Directive : l'e-mail est quasi obligatoire et devrait toujours être fourni lorsqu'il est disponible.  |
| addresses | * <br/> [Address](Address.md) | Adresses avec type (privée, professionnelle, locale).  |
| statutes_url | 0..1 <br/> [String](String.md) | URL vers les statuts du parti (PDF ou page web ; facultatif pour les partis).  |
| party_color | 0..1 <br/> [String](String.md) | Couleur du parti sous forme de valeur hexadécimale (facultatif pour les partis, p. ex. « #FF0000 »).  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |














### Exemples
#### Exemple : Cantonal parliament as a superordinate group

```yaml
local_id: 33
global_uri: https://www.grosserrat.bs.ch/
label:
- value: Grosser Rat Basel-Stadt
  language: de
group_type:
  group_type_enum: council_legislative
  label: Parlament (Legislativrat)
spatial: https://ld.admin.ch/canton/12

```
#### Exemple : Council bureau

```yaml
local_id: 50
global_uri: https://grosserrat.bs.ch/gremien/praesidium-und-buero
label:
- value: Büro des Grossen Rates
  language: de
parent_groups:
- https://www.grosserrat.bs.ch/
group_type:
  group_type_enum: council_bureau
  label: Ratsbüro
spatial: https://ld.admin.ch/canton/12

```
#### Exemple : Bilingual delegation to an intercantonal body

```yaml
local_id: 5000
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
- value: Die Interparlamentarische Aufsichtskommission strafrechtliche Einschliessung besteht aus 18 Grossrätinnen
    und Grossräten aus den sechs Vertragskantonen Freiburg, Genf, Jura, Neuenburg, Waadt und Wallis.
  language: de
- value: 'La Commission interparlementaire de contrôle détention pénale est composée de 18 députés issus
    des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel, Vaud et Valais.'
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
#### Exemple : Parliamentary group referencing its parliament and supporting parties

```yaml
local_id: 1266
global_uri: https://grosserrat.bs.ch/gremien/parteien-und-fraktionen/mitte-evp
label:
- value: Die Mitte / Evangelische Volkspartei
  language: de
parent_groups:
- https://www.grosserrat.bs.ch/
- https://bs.die-mitte.ch/
- https://www.evp-bs.ch/
group_type:
  group_type_enum: parliamentary_group
  label: Fraktion
spatial: https://ld.admin.ch/canton/12

```
#### Exemple : State chancellery as the staff unit of the executive

```yaml
local_id: 7172
global_uri: https://www.bs.ch/regierungsrat/staatskanzlei
label:
- value: Staatskanzlei Basel-Stadt
  language: de
parent_groups:
- https://www.regierungsrat.bs.ch/
group_type:
  group_type_enum: council_secretariat
  label: Staatskanzlei
spatial: https://ld.admin.ch/canton/12

```
#### Exemple : Executive council of a canton

```yaml
local_id: 1300
global_uri: https://www.regierungsrat.bs.ch/
label:
- value: Regierungsrat Basel-Stadt
  language: de
group_type:
  group_type_enum: council_executive
  label: Regierung (Exekutivrat)
spatial: https://ld.admin.ch/canton/12

```
#### Exemple : Municipal parliament with spatial reference

```yaml
local_id: 700
global_uri: https://www.stadt.sg.ch/home/verwaltung-politik/demokratie-politik/stadtparlament.html
label:
- value: Stadtparlament St. Gallen
  language: de
group_type:
  group_type_enum: council_legislative
  label: Parlament (Legislativrat)
spatial: https://ld.admin.ch/municipality/3203

```
#### Exemple : Committee with a common abbreviation

```yaml
local_id: 3
global_uri: https://api.openparldata.ch/v1/groups/3
label:
- value: Geschäftsprüfungskommission
  language: de
abbreviation:
- value: GPK
  language: de
landing_page:
- value: https://ar.ch/kantonsrat/kommissionen/staendige-kommissionen-des-kantonsrates/
  language: de
group_type:
  group_type_enum: committee
  label: Kommission
spatial: https://ld.admin.ch/canton/15

```
#### Exemple : Association with UID and legal form from the commercial register

```yaml
global_uri: https://www.frc.ch/
organization_uid: CHE-106.063.525
legal_form: 0109
label:
- value: Fédération romande des consommateurs
  language: fr
abbreviation:
- value: FRC
  language: fr
group_type:
  group_type_enum: association
  label: Verein
spatial: https://ld.admin.ch/canton/22

```
#### Exemple : Interest group with a trilingual name and contact

```yaml
local_id: 6627
global_uri: https://www.parlament.ch/de/organe/gruppen/konsumenteninformation-und-schutz
label:
- value: Konsumenteninformation und -schutz
  language: de
- value: Information et défense des consommateurs
  language: fr
- value: Informazione e tutela dei consumatori
  language: it
description:
- value: L'intergroupe parlementaire « Information et défense des consommateurs » réunit toutes les sensibilités
    politiques. Cet intergroupe a pour mission d'informer et de sensibiliser les élu·e·s aux questions
    relatives à la défense des consommateur·rice·s en Suisse.
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
  street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale 585
  postal_code: '1001'
  postal_locality: Lausanne
  country: CH
group_type:
  group_type_enum: interest_group
  label: Interessengruppe
spatial: https://ld.admin.ch/country/CHE
valid_from: 2012-01-01

```






</div>