---
search:
  boost: 5.0
---

# Slot: committee 


_Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung) mit der Sprache, in der es publiziert wird; erfasst wird pro Sprache ein Eintrag._




<div data-search-exclude markdown="1">



URI: [act:committee](https://ld.ech.ch/schema/0294/actors/committee)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualValue](MultilingualValue.md) |
| Domäne von | [InterestLink](InterestLink.md) |
| Slot-URI | [act:committee](https://ld.ech.ch/schema/0294/actors/committee) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: committee
annotations:
  description_de:
    tag: description_de
    value: 'Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat,
      Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung) mit der Sprache, in der es
      publiziert wird; erfasst wird pro Sprache ein Eintrag.

      '
  description_fr:
    tag: description_fr
    value: 'Comité ou organe au sein de l''organisation (p. ex. conseil d''administration,
      conseil de fondation, comité directeur, conseil de surveillance, comité consultatif,
      direction), avec la langue dans laquelle il est publié ; une entrée est saisie
      par langue.

      '
description: 'Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat,
  Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung) mit der Sprache, in der es publiziert
  wird; erfasst wird pro Sprache ein Eintrag.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:committee
domain_of:
- InterestLink
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>