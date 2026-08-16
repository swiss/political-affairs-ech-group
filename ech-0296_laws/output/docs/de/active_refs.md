---
search:
  boost: 5.0
---

# Slot: active_refs 


_Verweise auf die Erlasse, die dieses Dokument ändert (akn:activeRef)._



<div data-search-exclude markdown="1">



URI: [laws:active_refs](https://ld.ech.ch/schema/0296/laws/active_refs)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [References](References.md) | Benannte Referenz-Definitionen für das gesamte Dokument (akn:references) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ActiveRef](ActiveRef.md) |
| Domäne von | [References](References.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: active_refs
annotations:
  description_de:
    tag: description_de
    value: Verweise auf die Erlasse, die dieses Dokument ändert (akn:activeRef).
  xml_element:
    tag: xml_element
    value: akn:activeRef
description: Verweise auf die Erlasse, die dieses Dokument ändert (akn:activeRef).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:activeRef
rank: 1000
domain_of:
- References
range: ActiveRef
multivalued: true

```
</details></div>