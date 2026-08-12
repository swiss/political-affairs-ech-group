---
search:
  boost: 5.0
---

# Slot: books 


_Buch-Kindelemente (akn:book)._



<div data-search-exclude markdown="1">



URI: [laws:books](https://ld.ech.ch/schema/0296/laws/books)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Book](Book.md) |
| Domäne von | [ActBody](ActBody.md), [Title](Title.md), [Level](Level.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: books
annotations:
  description_de:
    tag: description_de
    value: Buch-Kindelemente (akn:book).
description: Buch-Kindelemente (akn:book).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- ActBody
- Title
- Level
range: Book
multivalued: true

```
</details></div>