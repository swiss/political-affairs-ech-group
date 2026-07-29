---
search:
  boost: 5.0
---

# Slot: number 


_Numéro courant, p. ex. au sein de la législature, de la session ou de l'année._




<div data-search-exclude markdown="1">



URI: [ops:number](https://ch.paf.link/schema/operations/number)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






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
    value: 'Laufende Nummer, z.B. innerhalb der Legislatur, der Session oder des Jahres.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro courant, p. ex. au sein de la législature, de la session ou de
      l''année.

      '
description: 'Numéro courant, p. ex. au sein de la législature, de la session ou de
  l''année.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>