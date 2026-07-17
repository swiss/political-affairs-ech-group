

## Classe: Group 


_Un groupe, une organisation ou une collectivité politique (p. ex. parti, commission, parlement, département)._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| group_type | 0..1 <br/> [GroupType](GroupType.md) | Type de groupe (p. ex. parti, commission, parlement ou similaire). La désignation et la description exactes du groupe sont fournies via `label`.  |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abréviation (peut être multilingue).  |
| description | * <br/> [MultilingualValue](MultilingualValue.md) | Description de l'entité.  |
| landing_page | 0..1 <br/> [Uri](Uri.md) | Site web fournissant de plus amples informations.  |
| parent_groups | * <br/> [Uriorcurie](Uriorcurie.md) | Lien vers les groupes parents. Par exemple, le parti faîtier pour les partis cantonaux, ou pour décrire la hiérarchie au sein de l'exécutif. Utilisé également pour rattacher des sous-commissions à des commissions, ou des groupes parlementaires à la fois à leur parlement et à leur parti. (parentGroup est généralement utilisé au sein d'un même group_type, mais les liens intertypes sont autorisés, p. ex. groupe parlementaire → parlement et groupe parlementaire → parti.)  |
| spatial | 0..1 <br/> [String](String.md) | Référence spatiale (numéro OFS de commune, numéro OFS de canton ou pays). Formats : commune : ld.admin.ch/municipality/1234, canton : ld.admin.ch/canton/23, pays : ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](Contact.md) | Informations de contact (e-mail, site web, réseaux sociaux). Directive : l'e-mail est quasi obligatoire et devrait toujours être fourni lorsqu'il est disponible.  |
| addresses | * <br/> [Address](Address.md) | Adresses avec type (privée, professionnelle, locale).  |
| statutes_url | 0..1 <br/> [String](String.md) | URL vers les statuts du parti (PDF ou page web ; facultatif pour les partis).  |
| party_color | 0..1 <br/> [String](String.md) | Couleur du parti sous forme de valeur hexadécimale (facultatif pour les partis, p. ex. « #FF0000 »).  |
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





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |



















</div>