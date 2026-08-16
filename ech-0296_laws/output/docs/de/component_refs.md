---
search:
  boost: 5.0
---

# Slot: component_refs 


_Verweise auf anderswo gehaltene Bestandteile (akn:componentRef)._



<div data-search-exclude markdown="1">



URI: [laws:component_refs](https://ld.ech.ch/schema/0296/laws/component_refs)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ComponentRef](ComponentRef.md) |
| Domäne von | [ActBody](ActBody.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: component_refs
annotations:
  description_de:
    tag: description_de
    value: Verweise auf anderswo gehaltene Bestandteile (akn:componentRef).
  xml_element:
    tag: xml_element
    value: akn:componentRef
description: Verweise auf anderswo gehaltene Bestandteile (akn:componentRef).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:componentRef
rank: 1000
domain_of:
- ActBody
range: ComponentRef
multivalued: true

```
</details></div>