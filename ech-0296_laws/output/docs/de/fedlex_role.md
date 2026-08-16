---
search:
  boost: 5.0
---

# Slot: fedlex_role 


_Fedlex-Erweiterungsattribut fedlex:role. FLX-XF-003 lässt 'marginal' (nur an akn:level, FLX-XF-004) und 'reference' (nur an akn:subheading, FLX-XF-005) zu; die publizierte Bundesverfassung führt zusätzlich 'heading' an einem Präambel-Absatz._




<div data-search-exclude markdown="1">



URI: [laws:fedlex_role](https://ld.ech.ch/schema/0296/laws/fedlex_role)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  yes  |
| [BlockParagraph](BlockParagraph.md) | Ein Fliesstext-Absatz in Content (akn:p) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [FedlexRoleEnum](FedlexRoleEnum.md) |
| Domäne von | [Level](Level.md), [BlockParagraph](BlockParagraph.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: fedlex_role
annotations:
  description_de:
    tag: description_de
    value: 'Fedlex-Erweiterungsattribut fedlex:role. FLX-XF-003 lässt ''marginal''
      (nur an akn:level, FLX-XF-004) und ''reference'' (nur an akn:subheading, FLX-XF-005)
      zu; die publizierte Bundesverfassung führt zusätzlich ''heading'' an einem Präambel-Absatz.

      '
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: fedlex:role
  xml_namespace:
    tag: xml_namespace
    value: http://fedlex.admin.ch/
  schematron_rules:
    tag: schematron_rules
    value: FLX-XF-003, FLX-XF-004, FLX-XF-005
description: 'Fedlex-Erweiterungsattribut fedlex:role. FLX-XF-003 lässt ''marginal''
  (nur an akn:level, FLX-XF-004) und ''reference'' (nur an akn:subheading, FLX-XF-005)
  zu; die publizierte Bundesverfassung führt zusätzlich ''heading'' an einem Präambel-Absatz.

  '
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Level
- BlockParagraph
range: FedlexRoleEnum

```
</details></div>