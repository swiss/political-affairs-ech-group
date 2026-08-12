

## Classe: Legislature 


_Durée du mandat d'un parlement en tant qu'assemblée législative. Elle est en règle générale de quatre ans._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| spatial | 0..1 <br/> [String](String.md) | Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234, district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23, pays : https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> [String](String.md) | Identifiant administratif du corps législatif, p. ex. commune, canton ou pays.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Désignation complète multilingue.  |
| description | 0..1 <br/> [String](String.md) | Texte descriptif de l'élément.  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [legislatures](legislatures.md) | range | [Legislature](Legislature.md) |














### Exemples
#### Exemple Legislature : Ongoing cantonal legislature with a five-year term

```yaml
legislatures:
- global_uri: ops:legislature_vd_2022_2027
  wikidata_uri: http://www.wikidata.org/entity/Q131627357
  spatial: https://ld.admin.ch/canton/22
  name:
  - text: Législature 2022-2027
    language: fr
  description: Le Grand Conseil vaudois est élu pour cinq ans.
  landing_page: https://www.vd.ch/gc
  actor_id:
    global_uri: actors:gc_vd
    label: Grand Conseil du canton de Vaud
    abbreviation:
    - value: GC
      language: fr
  date_begin_actual: '2022-07-01'
  date_end_planned: '2027-06-30'
  datetime_created: '2022-05-10T14:00:00+02:00'
  datetime_modified: '2025-01-08T11:20:00+01:00'

```
#### Exemple Legislature : Cantonal legislature with a four-year term

```yaml
legislatures:
- global_uri: ops:legislature_be_2022_2026
  local_id: GR-BE-2022-2026
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Legislatur 2022–2026
    language: de
  - text: Législature 2022-2026
    language: fr
  landing_page: https://www.gr.be.ch/de/start/grosser-rat.html
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/253
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  date_begin_planned: '2022-06-01'
  date_end_planned: '2026-05-31'
  date_begin_actual: '2022-06-01'
  date_end_actual: '2026-05-31'
  datetime_created: '2022-04-01T10:15:00+02:00'
  datetime_modified: '2026-06-01T07:00:00+02:00'

```
#### Exemple Legislature : Completed federal legislature

```yaml
legislatures:
- global_uri: ops:legislature_51
  wikidata_uri: http://www.wikidata.org/entity/Q71712404
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: 51. Legislaturperiode
    language: de
  - text: 51e législature
    language: fr
  - text: 51ª legislatura
    language: it
  description: >-
    Amtsdauer der am 20. Oktober 2019 gewählten Bundesversammlung; sie endete am Vortag
    der konstituierenden Sitzung der 52. Legislaturperiode vom 4. Dezember 2023.
  landing_page: https://www.parlament.ch/de/ratsbetrieb/sessionen
  actor_id:
    global_uri: actors:bundesversammlung
    label: Bundesversammlung
    abbreviation:
    - value: BV
      language: de
  date_begin_actual: '2019-12-02'
  date_end_actual: '2023-12-03'
  datetime_created: '2019-12-02T09:00:00+01:00'
  datetime_modified: '2023-12-04T08:30:00+01:00'

```






</div>