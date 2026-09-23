---
search:
  boost: 5.0
---

# Slot: agenda_item_category 


_Catégorisation libre du point selon son contenu ou son regroupement, p. ex. « Législation », « Budget et finances », « Interpellations et questions », « Élections », par département, ou points introductifs et techniques. La catégorisation n'est pas standardisée et peut varier selon l'unité fédérale._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_category](https://ch.paf.link/schema/operations/agenda_item_category)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| ANNONCES ET INTERPELLATIONS |
| Budget und Finanzen |
| Gesetzgebung |





## Source LinkML

<details>
```yaml
name: agenda_item_category
annotations:
  description_de:
    tag: description_de
    value: 'Freie Kategorisierung des Traktandums nach Inhalt oder Gruppierung, z.B.
      „Gesetzgebung“, „Budget und Finanzen“, „Interpellationen und Anfragen“, „Wahlen“,
      nach Departement oder einleitende und technische Traktanden. Die Kategorisierung
      ist nicht standardisiert und kann je nach Föderaleinheit variieren.

      '
  description_fr:
    tag: description_fr
    value: 'Catégorisation libre du point selon son contenu ou son regroupement, p.
      ex. « Législation », « Budget et finances », « Interpellations et questions
      », « Élections », par département, ou points introductifs et techniques. La
      catégorisation n''est pas standardisée et peut varier selon l''unité fédérale.

      '
description: 'Catégorisation libre du point selon son contenu ou son regroupement,
  p. ex. « Législation », « Budget et finances », « Interpellations et questions »,
  « Élections », par département, ou points introductifs et techniques. La catégorisation
  n''est pas standardisée et peut varier selon l''unité fédérale.

  '
examples:
- value: ANNONCES ET INTERPELLATIONS
- value: Budget und Finanzen
- value: Gesetzgebung
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>