---
search:
  boost: 5.0
---

# Slot: number 


_Numéro de la session ou de la séance tel qu'attribué par l'organe, p. ex. au sein de la législature, de la session ou de l'année. En tant que chaîne de caractères, il admet aussi les chiffres romains. Les pratiques de numérotation variant fortement, number, sequential_number, position et meeting_abbreviation sont disponibles côte à côte._




<div data-search-exclude markdown="1">



URI: [ops:number](https://ch.paf.link/schema/operations/number)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session : une période de séances continue au sein d'une législature |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: number
annotations:
  description_de:
    tag: description_de
    value: 'Nummer der Session oder Sitzung, wie sie das Organ vergibt, z.B. innerhalb
      der Legislatur, der Session oder des Jahres. Als Zeichenkette erlaubt sie auch
      römische Ziffern. Nummeriert wird sehr unterschiedlich, weshalb number, sequential_number,
      position und meeting_abbreviation nebeneinander zur Verfügung stehen.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro de la session ou de la séance tel qu''attribué par l''organe, p.
      ex. au sein de la législature, de la session ou de l''année. En tant que chaîne
      de caractères, il admet aussi les chiffres romains. Les pratiques de numérotation
      variant fortement, number, sequential_number, position et meeting_abbreviation
      sont disponibles côte à côte.

      '
description: 'Numéro de la session ou de la séance tel qu''attribué par l''organe,
  p. ex. au sein de la législature, de la session ou de l''année. En tant que chaîne
  de caractères, il admet aussi les chiffres romains. Les pratiques de numérotation
  variant fortement, number, sequential_number, position et meeting_abbreviation sont
  disponibles côte à côte.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>