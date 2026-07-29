---
search:
  boost: 5.0
---

# Slot: count 


_Die Anzahl der Stimmen für die Kategorie „Andere“._




<div data-search-exclude markdown="1">



URI: [ops:count](https://ch.paf.link/schema/operations/count)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TotalOther](TotalOther.md) | Zusätzliche Stimmzahlen, wenn mehrere Optionen zur Abstimmung gestellt werden... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [TotalOther](TotalOther.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: count
annotations:
  description_de:
    tag: description_de
    value: 'Die Anzahl der Stimmen für die Kategorie „Andere“.

      '
  description_fr:
    tag: description_fr
    value: 'Le nombre de voix pour la catégorie « autres ».

      '
description: 'Die Anzahl der Stimmen für die Kategorie „Andere“.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- TotalOther
range: integer

```
</details></div>