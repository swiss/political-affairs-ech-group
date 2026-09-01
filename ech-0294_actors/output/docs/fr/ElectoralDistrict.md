

## Classe: ElectoralDistrict 


_Circonscription ou région électorale associée à une affiliation. La validité temporelle est héritée de l'affiliation englobante._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Pour les références IRI, les ressources LINDAS doivent être utilisées. Les IRI des différents niveaux administratifs des unités spatiales suisses sont disponibles à l'adresse : https://ld.admin.ch/country/CHE. Sous les liens de la section schema:containsPlace, le niveau souhaité peut être sélectionné. Exemples pour chaque niveau administratif : - Pays - Suisse : https://ld.admin.ch/country/CHE - Canton - Argovie : https://ld.admin.ch/canton/19 - District - Brigue : https://ld.admin.ch/district/2301 - Commune - Versoix : https://ld.admin.ch/municipality/6644 Les circonscriptions qui ne correspondent à aucune unité spatiale officielle, par exemple celles qui regroupent des quartiers d'une commune, reçoivent à la place un identifiant dans l'espace de noms de l'organe qui les publie. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| label | * <br/> [MultilingualValue](MultilingualValue.md) | Désignation de la circonscription électorale telle qu'elle est publiée par l'organe compétent pour l'élection, avec la langue dans laquelle elle est publiée. Lorsqu'une circonscription porte officiellement un nom dans plusieurs langues, une entrée est saisie par langue.  |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |














### Exemples
#### Exemple ElectoralDistrict : Canton as electoral district identified via its LINDAS resource

```yaml
electoral_district:
  global_uri: https://ld.admin.ch/canton/12
  label:
  - value: Basel-Stadt
    language: de

```
#### Exemple ElectoralDistrict : Electoral district without an official spatial unit

```yaml
electoral_district:
  global_uri: https://grosserrat.bs.ch/wahlkreise/kleinbasel
  label:
  - value: Kleinbasel
    language: de

```






</div>