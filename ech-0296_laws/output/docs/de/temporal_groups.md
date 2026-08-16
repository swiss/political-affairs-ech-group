---
search:
  boost: 5.0
---

# Slot: temporal_groups 


_Die Zeitgruppen (akn:temporalGroup)._



<div data-search-exclude markdown="1">



URI: [laws:temporal_groups](https://ld.ech.ch/schema/0296/laws/temporal_groups)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TemporalData](TemporalData.md) | Die Zeitgruppen, auf die sich eine Änderung bezieht |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [TemporalGroup](TemporalGroup.md) |
| Domäne von | [TemporalData](TemporalData.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: temporal_groups
annotations:
  description_de:
    tag: description_de
    value: Die Zeitgruppen (akn:temporalGroup).
  xml_element:
    tag: xml_element
    value: akn:temporalGroup
description: Die Zeitgruppen (akn:temporalGroup).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:temporalGroup
rank: 1000
domain_of:
- TemporalData
range: TemporalGroup
multivalued: true

```
</details></div>