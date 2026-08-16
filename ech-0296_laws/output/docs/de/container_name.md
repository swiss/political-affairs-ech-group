---
search:
  boost: 5.0
---

# Slot: container_name 


_Zweck des Behälters (akn:container/@name)._



<div data-search-exclude markdown="1">



URI: [laws:container_name](https://ld.ech.ch/schema/0296/laws/container_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Ein generischer Behälter (akn:container), dessen @name den Zweck nennt |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ContainerNameEnum](ContainerNameEnum.md) |
| Domäne von | [Container](Container.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| headerOfAnnex |





## LinkML-Quelle

<details>
```yaml
name: container_name
annotations:
  description_de:
    tag: description_de
    value: Zweck des Behälters (akn:container/@name).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: name
description: Zweck des Behälters (akn:container/@name).
examples:
- value: headerOfAnnex
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Container
range: ContainerNameEnum

```
</details></div>