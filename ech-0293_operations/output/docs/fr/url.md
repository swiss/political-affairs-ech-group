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
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [Media](Media.md) | Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD o... |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualString](MultilingualString.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Media](Media.md) |

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
- AgendaItem
- Media
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>