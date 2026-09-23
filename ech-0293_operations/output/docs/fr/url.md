---
search:
  boost: 5.0
---

# Slot: url 


_Page d'accueil ou adresse web complémentaire, multilingue._




<div data-search-exclude markdown="1">



URI: [ops:url](https://ch.paf.link/schema/operations/url)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [Media](Media.md) | Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD o... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualString](MultilingualString.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md), [Media](Media.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: url
annotations:
  description_de:
    tag: description_de
    value: 'Landing Page oder weiterführende Webadresse, mehrsprachig.

      '
  description_fr:
    tag: description_fr
    value: 'Page d''accueil ou adresse web complémentaire, multilingue.

      '
description: 'Page d''accueil ou adresse web complémentaire, multilingue.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
- IsAgendaItem
- Media
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>