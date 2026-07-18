

## Classe: Membership 


_Une relation d'affiliation entre une personne et un groupe, représentant une appartenance formelle (p. ex. membre d'un parti, membre d'une commission, parlementaire). À distinguer de InterestLink, qui recouvre les liens d'intérêts externes et les conflits d'intérêts avec des organisations situées en dehors du schéma des acteurs._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Référence à une personne avec des données instantanées au moment de la mise en relation.  |
| group_reference | 1 <br/> [GroupReference](GroupReference.md) | Référence à un groupe avec des données instantanées au moment de la mise en relation.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | Lien vers la circonscription électorale.  |
| role_type | 0..1 <br/> [RoleType](RoleType.md) | Rôle de la personne dans l'affiliation ou la fonction.  |
| authorized_to_vote | 0..1 <br/> [Boolean](Boolean.md) | Indique si la personne dispose du droit de vote au sein du groupe. Généralement false pour les membres suppléants (lorsqu'ils ne remplacent personne), les observateurs, les secrétaires et les invités.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'affiliation est actuellement active. Peut compléter ou remplacer `valid_from`/`valid_through`. Si cette valeur n'est pas renseignée, l'activité est déduite des champs de validité temporelle.  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |



















</div>