---
search:
  boost: 5.0
---

# Slot: source 


_Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'._



<div data-search-exclude markdown="1">



URI: [laws:source](https://ld.ech.ch/schema/0296/laws/source)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Identification](Identification.md) | FRBR-Identifikationsblock (akn:identification) mit Work-, Expression- und Man... |  no  |
| [References](References.md) | Benannte Referenz-Definitionen für das gesamte Dokument (akn:references) |  no  |
| [Notes](Notes.md) | Anmerkungsblock der Metadaten mit den Anmerkungen, auf die ein Erlass verweis... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [AnchorRef](AnchorRef.md) |
| Domäne von | [Identification](Identification.md), [References](References.md), [Notes](Notes.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: source
annotations:
  description_de:
    tag: description_de
    value: Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
description: Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Identification
- References
- Notes
range: AnchorRef

```
</details></div>