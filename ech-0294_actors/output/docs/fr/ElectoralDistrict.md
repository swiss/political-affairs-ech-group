

## Classe: ElectoralDistrict 


_Circonscription ou région électorale associée à une affiliation. La validité temporelle est héritée de l'affiliation englobante._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Pour les références IRI, les ressources LINDAS doivent être utilisées. Les IRI des différents niveaux administratifs des unités spatiales suisses sont disponibles à l'adresse : https://ld.admin.ch/country/CHE. Sous les liens de la section schema:containsPlace, le niveau souhaité peut être sélectionné. Exemples pour chaque niveau administratif : - Pays - Suisse : https://ld.admin.ch/country/CHE - Canton - Argovie : https://ld.admin.ch/canton/19 - District - Brigue : https://ld.admin.ch/district/2301 - Commune - Versoix : https://ld.admin.ch/municipality/6644 <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |



















</div>