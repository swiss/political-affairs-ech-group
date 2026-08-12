---
search:
  boost: 5.0
---

# Slot: fedlex_role 


_Fedlex-Erweiterungsattribut fedlex:role. Nur zwei Werte erlaubt (FLX-XF-003): 'marginal' (nur bei akn:level, FLX-XF-004) und 'reference' (nur bei akn:subheading, FLX-XF-005)._




<div data-search-exclude markdown="1">



URI: [laws:fedlex_role](https://ld.ech.ch/schema/0296/laws/fedlex_role)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [FedlexRoleEnum](FedlexRoleEnum.md) |
| Domäne von | [Level](Level.md) |

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
    value: 'Fedlex-Erweiterungsattribut fedlex:role. Nur zwei Werte erlaubt (FLX-XF-003):
      ''marginal'' (nur bei akn:level, FLX-XF-004) und ''reference'' (nur bei akn:subheading,
      FLX-XF-005).

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
description: 'Fedlex-Erweiterungsattribut fedlex:role. Nur zwei Werte erlaubt (FLX-XF-003):
  ''marginal'' (nur bei akn:level, FLX-XF-004) und ''reference'' (nur bei akn:subheading,
  FLX-XF-005).

  '
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Level
range: FedlexRoleEnum

```
</details></div>