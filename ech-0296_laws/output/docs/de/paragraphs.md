---
search:
  boost: 5.0
---

# Slot: paragraphs 


_Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts._



<div data-search-exclude markdown="1">



URI: [laws:paragraphs](https://ld.ech.ch/schema/0296/laws/paragraphs)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Article](Article.md) | Ein Artikel, die primäre legislative Einheit (akn:article) |  no  |
| [Subdivision](Subdivision.md) | Ein Unterabschnitt in einem Artikel, der zusammengehörige Absätze gruppiert (... |  no  |
| [Transitional](Transitional.md) | Eine Übergangsbestimmung im Hauptteil eines Erlasses (akn:transitional) |  no  |
| [Proviso](Proviso.md) | Ein Vorbehalt im Hauptteil eines Erlasses (akn:proviso) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Paragraph](Paragraph.md) |
| Domäne von | [Article](Article.md), [Subdivision](Subdivision.md), [Transitional](Transitional.md), [Proviso](Proviso.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: paragraphs
annotations:
  description_de:
    tag: description_de
    value: Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts.
description: Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Article
- Subdivision
- Transitional
- Proviso
range: Paragraph
multivalued: true

```
</details></div>