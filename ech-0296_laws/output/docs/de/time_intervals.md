---
search:
  boost: 5.0
---

# Slot: time_intervals 


_Die Intervalle dieser Gruppe (akn:timeInterval)._



<div data-search-exclude markdown="1">



URI: [laws:time_intervals](https://ld.ech.ch/schema/0296/laws/time_intervals)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TemporalGroup](TemporalGroup.md) | Ein benannter Zeitraum, auf den sich eine Änderung über @period bezieht |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [TimeInterval](TimeInterval.md) |
| Domäne von | [TemporalGroup](TemporalGroup.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: time_intervals
annotations:
  description_de:
    tag: description_de
    value: Die Intervalle dieser Gruppe (akn:timeInterval).
  xml_element:
    tag: xml_element
    value: akn:timeInterval
description: Die Intervalle dieser Gruppe (akn:timeInterval).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:timeInterval
rank: 1000
domain_of:
- TemporalGroup
range: TimeInterval
multivalued: true

```
</details></div>