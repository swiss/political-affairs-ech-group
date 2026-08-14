---
search:
  boost: 5.0
---

# Slot: act_ref 


_Der Erlass (akn:act). Muss das einzige Kind von akn:akomaNtoso sein (FLX-RT-001)._



<div data-search-exclude markdown="1">



URI: [laws:act_ref](https://ld.ech.ch/schema/0296/laws/act_ref)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FedlexDocument](FedlexDocument.md) | Wurzelelement eines Fedlex AkomaNtoso-Dokuments (akn:akomaNtoso) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Act](Act.md) |
| Domäne von | [FedlexDocument](FedlexDocument.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |












## LinkML-Quelle

<details>
```yaml
name: act_ref
annotations:
  description_de:
    tag: description_de
    value: Der Erlass (akn:act). Muss das einzige Kind von akn:akomaNtoso sein (FLX-RT-001).
  xml_element:
    tag: xml_element
    value: akn:act
description: Der Erlass (akn:act). Muss das einzige Kind von akn:akomaNtoso sein (FLX-RT-001).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FedlexDocument
range: Act
required: true

```
</details></div>