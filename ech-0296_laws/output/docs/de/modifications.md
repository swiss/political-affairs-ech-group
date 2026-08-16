---
search:
  boost: 5.0
---

# Slot: modifications 


_Die Änderungen in der Reihenfolge ihrer Aufzeichnung (akn:textualMod, akn:forceMod)._



<div data-search-exclude markdown="1">



URI: [laws:modifications](https://ld.ech.ch/schema/0296/laws/modifications)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActiveModifications](ActiveModifications.md) | Die Änderungen, die dieser Erlass an anderen vornimmt |  no  |
| [PassiveModifications](PassiveModifications.md) | Die Änderungen, die andere Erlasse an diesem vornehmen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Modification](Modification.md) |
| Domäne von | [ActiveModifications](ActiveModifications.md), [PassiveModifications](PassiveModifications.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: modifications
annotations:
  description_de:
    tag: description_de
    value: Die Änderungen in der Reihenfolge ihrer Aufzeichnung (akn:textualMod, akn:forceMod).
description: Die Änderungen in der Reihenfolge ihrer Aufzeichnung (akn:textualMod,
  akn:forceMod).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActiveModifications
- PassiveModifications
range: Modification
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>