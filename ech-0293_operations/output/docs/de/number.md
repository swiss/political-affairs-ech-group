---
search:
  boost: 5.0
---

# Slot: number 


_Nummer der Session oder Sitzung, wie sie das Organ vergibt, z.B. innerhalb der Legislatur, der Session oder des Jahres. Als Zeichenkette erlaubt sie auch römische Ziffern. Nummeriert wird sehr unterschiedlich, weshalb number, sequential_number, position und meeting_abbreviation nebeneinander zur Verfügung stehen._




<div data-search-exclude markdown="1">



URI: [ops:number](https://ch.paf.link/schema/operations/number)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislatu... |  no  |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






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
description: 'Nummer der Session oder Sitzung, wie sie das Organ vergibt, z.B. innerhalb
  der Legislatur, der Session oder des Jahres. Als Zeichenkette erlaubt sie auch römische
  Ziffern. Nummeriert wird sehr unterschiedlich, weshalb number, sequential_number,
  position und meeting_abbreviation nebeneinander zur Verfügung stehen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>