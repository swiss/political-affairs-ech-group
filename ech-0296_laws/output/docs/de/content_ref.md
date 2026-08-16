---
search:
  boost: 5.0
---

# Slot: content_ref 


_Inhaltselement innerhalb eines Absatzes (akn:content)._



<div data-search-exclude markdown="1">



URI: [laws:content_ref](https://ld.ech.ch/schema/0296/laws/content_ref)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |
| [Paragraph](Paragraph.md) | Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph) |  no  |
| [MainBody](MainBody.md) | Hauptteil eines beiliegenden Dokuments (akn:mainBody) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Content](Content.md) |
| Domäne von | [Level](Level.md), [Paragraph](Paragraph.md), [MainBody](MainBody.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: content_ref
annotations:
  description_de:
    tag: description_de
    value: Inhaltselement innerhalb eines Absatzes (akn:content).
  xml_element:
    tag: xml_element
    value: akn:content
description: Inhaltselement innerhalb eines Absatzes (akn:content).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Level
- Paragraph
- MainBody
range: Content

```
</details></div>