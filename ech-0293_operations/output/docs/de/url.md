---
search:
  boost: 5.0
---

# Slot: url 


_Landing Page oder weiterführende Webadresse, mehrsprachig._




<div data-search-exclude markdown="1">



URI: [ops:url](https://ch.paf.link/schema/operations/url)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualString](MultilingualString.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Media](Media.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

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
description: 'Landing Page oder weiterführende Webadresse, mehrsprachig.

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