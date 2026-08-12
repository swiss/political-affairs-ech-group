---
search:
  boost: 5.0
---

# Slot: frbr_names 


_Mehrsprachige Namenseinträge des FRBR-Works (akn:FRBRname). Ein Eintrag pro Sprache._



<div data-search-exclude markdown="1">



URI: [laws:frbr_names](https://ld.ech.ch/schema/0296/laws/frbr_names)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRWork](FRBRWork.md) | FRBR-Work-Ebene (akn:FRBRWork): der abstrakte Erlass unabhängig von Sprache u... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [FRBRName](FRBRName.md) |
| Domäne von | [FRBRWork](FRBRWork.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: frbr_names
annotations:
  description_de:
    tag: description_de
    value: Mehrsprachige Namenseinträge des FRBR-Works (akn:FRBRname). Ein Eintrag
      pro Sprache.
description: Mehrsprachige Namenseinträge des FRBR-Works (akn:FRBRname). Ein Eintrag
  pro Sprache.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRWork
range: FRBRName
multivalued: true

```
</details></div>