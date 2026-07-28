

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
#### Exemple : Group-groups__it

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
group_type:
  group_type_enum: interest_group
  label: Interessengruppe
spatial: https://ld.admin.ch/country/CHE
valid_from: 2012-01-01

```
#### Exemple : Group-groups__de

```yaml
local_id: 50
global_uri: https://api.openparldata.ch/v1/groups/50
label:
- value: Büro des Grossen Rates
  language: de
group_type:
  group_type_enum: parliamentary_bureau
  label: Ratsbüro
spatial: https://ld.admin.ch/canton/12

```
#### Exemple : Group-groups__fr

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
    Genf, Jura, Neuenburg, Waadt und Wallis. Sie ist für die parlamentarische Aufsicht
    über den Vollzug der beiden lateinischen Konkordate über den strafrechtlichen
    Freiheitsentzug zuständig.
  language: de
- value: 'La Commission interparlementaire de contrôle détention pénale est composée
    de 18 députés issus des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel,
    Vaud et Valais. Elle est chargée de la surveillance parlementaire de l''exécution
    des deux concordats latins sur la détention pénale.'
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