---
search:
  boost: 5.0
---

# Slot: birth_date 


_Genaues Geburtsdatum, sofern verfügbar und öffentlich. Dieses Feld hat Vorrang vor dem Feld `birthYear`._

__



<div data-search-exclude markdown="1">



URI: [schema:birthDate](http://schema.org/birthDate)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [Person](Person.md) |
| Slot-URI | [schema:birthDate](http://schema.org/birthDate) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| 1964-07-12 |





## LinkML-Quelle

<details>
```yaml
name: birth_date
annotations:
  description_de:
    tag: description_de
    value: 'Genaues Geburtsdatum, sofern verfügbar und öffentlich. Dieses Feld hat
      Vorrang vor dem Feld `birthYear`.

      '
description: 'Genaues Geburtsdatum, sofern verfügbar und öffentlich. Dieses Feld hat
  Vorrang vor dem Feld `birthYear`.

  '
examples:
- value: '1964-07-12'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:birthDate
domain_of:
- Person
range: date

```
</details></div>