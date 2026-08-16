---
search:
  boost: 5.0
---

# Slot: citation_list 


_Die Erwägungen selbst (akn:citation)._



<div data-search-exclude markdown="1">



URI: [laws:citation_list](https://ld.ech.ch/schema/0296/laws/citation_list)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Citations](Citations.md) | Die Erwägungen des Vorspruchs — worauf sich der Erlass beruft |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Citation](Citation.md) |
| Domäne von | [Citations](Citations.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: citation_list
annotations:
  description_de:
    tag: description_de
    value: Die Erwägungen selbst (akn:citation).
  xml_element:
    tag: xml_element
    value: akn:citation
description: Die Erwägungen selbst (akn:citation).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:citation
rank: 1000
domain_of:
- Citations
range: Citation
multivalued: true

```
</details></div>