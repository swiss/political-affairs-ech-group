---
search:
  boost: 5.0
---

# Slot: number 


_Laufende Nummer, z.B. innerhalb der Legislatur, der Session oder des Jahres._




<div data-search-exclude markdown="1">



URI: [ops:number](https://ch.paf.link/schema/operations/number)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Laufende Nummer, z.B. innerhalb der Legislatur, der Session oder des
  Jahres.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>