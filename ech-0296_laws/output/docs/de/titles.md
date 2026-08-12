---
search:
  boost: 5.0
---

# Slot: titles 


_Titel-Kindelemente (akn:title)._



<div data-search-exclude markdown="1">



URI: [laws:titles](https://ld.ech.ch/schema/0296/laws/titles)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Title](Title.md) |
| Domäne von | [ActBody](ActBody.md), [Book](Book.md), [Level](Level.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: titles
annotations:
  description_de:
    tag: description_de
    value: Titel-Kindelemente (akn:title).
description: Titel-Kindelemente (akn:title).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
- Book
- Level
range: Title
multivalued: true

```
</details></div>