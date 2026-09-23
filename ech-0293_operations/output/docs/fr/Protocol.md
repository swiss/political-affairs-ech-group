

## Classe: Protocol 


_Le procès-verbal d'une séance, établi après celle-ci et tenu exactement une fois par séance. Un conteneur qui regroupe les points effectivement traités (protocol_items), les votes, les élections, les interventions, les segments de texte in extenso et les documents liés. Le procès-verbal possède son propre identifiant, peut être cité de manière autonome et est en règle générale publié après la séance ; la séance ne fait donc que le référencer (Meeting.has_protocol), et le procès-verbal lui-même est livré dans Container.protocols, de sorte qu'il puisse être livré ultérieurement sans relivrer la séance. À l'intérieur du procès-verbal, les collections sont imbriquées, car elles naissent et sont livrées avec lui. Qui publie des votes ou des interventions indépendamment du procès-verbal les livre à plat dans Container.votings ou Container.speeches et les relie par parent_meeting et la référence au point de l'ordre du jour correspondante._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un vote, une élection, une intervention, une liste de présence ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né. Les points de l'ordre du jour ne le portent pas : ils sont imbriqués dans leur séance.  |
| protocol_items | * <br/> [ProtocolItem](ProtocolItem.md) | Points de l'ordre du jour tels qu'ils ont effectivement été consignés au procès-verbal.  |
| votings | * <br/> [Voting](Voting.md) | Ensemble des votes.  |
| elections | * <br/> [Election](Election.md) | Ensemble des élections.  |
| speeches | * <br/> [Speech](Speech.md) | Ensemble des interventions.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Ensemble de segments de texte (p. ex. procès-verbal in extenso).  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [protocols](protocols.md) | range | [Protocol](Protocol.md) |
| [Meeting](Meeting.md) | [has_protocol](has_protocol.md) | range | [Protocol](Protocol.md) |
| [Voting](Voting.md) | [parent_protocol](parent_protocol.md) | range | [Protocol](Protocol.md) |
| [Election](Election.md) | [parent_protocol](parent_protocol.md) | range | [Protocol](Protocol.md) |














### Exemples
#### Exemple Protocol : Protocol as an entity in its own right referenced by the meeting

```yaml
protocols:
- global_uri: ops:protokoll_sr_winter25_sitzung_6
  parent_meeting: parl:sr_winter25_sitzung_6
  protocol_items:
  - global_uri: ops:protokollpunkt_69905
    agenda_item_type: item
    agenda_item_number: '6'
    agenda_item_position: 4
    agenda_item_title:
    - text: >-
        Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
        durchführen, um die Verzögerungen zu verstehen
      language: de
    affair_id: affairs:24.4471
    datetime_begin_actual: '2025-12-19T09:20:00+01:00'
    landing_page: >-
      https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
    agenda_item_category: agenda_item
    datetime_created: '2026-01-12T00:00:00+01:00'
    datetime_modified: '2026-01-12T00:00:00+01:00'
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```






</div>