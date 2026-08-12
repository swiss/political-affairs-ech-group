---
search:
  boost: 5.0
---

# Slot: parts 


_Teil-Kindelemente (akn:part)._



<div data-search-exclude markdown="1">



URI: [laws:parts](https://ld.ech.ch/schema/0296/laws/parts)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |  no  |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Part](Part.md) |
| Domäne von | [ActBody](ActBody.md), [Book](Book.md), [Title](Title.md), [Level](Level.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: parts
annotations:
  description_de:
    tag: description_de
    value: Teil-Kindelemente (akn:part).
description: Teil-Kindelemente (akn:part).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
- Book
- Title
- Level
range: Part
multivalued: true

```
</details></div>