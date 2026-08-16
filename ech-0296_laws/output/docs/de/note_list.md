---
search:
  boost: 5.0
---

# Slot: note_list 


_Die Anmerkungen selbst (akn:note)._



<div data-search-exclude markdown="1">



URI: [laws:note_list](https://ld.ech.ch/schema/0296/laws/note_list)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Notes](Notes.md) | Anmerkungsblock der Metadaten mit den Anmerkungen, auf die ein Erlass verweis... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Note](Note.md) |
| Domäne von | [Notes](Notes.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: note_list
annotations:
  description_de:
    tag: description_de
    value: Die Anmerkungen selbst (akn:note).
  xml_element:
    tag: xml_element
    value: akn:note
description: Die Anmerkungen selbst (akn:note).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:note
rank: 1000
domain_of:
- Notes
range: Note
multivalued: true

```
</details></div>