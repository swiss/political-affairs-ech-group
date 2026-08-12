---
search:
  boost: 5.0
---

# Slot: as_role 


_Rolle des Autors (akn:FRBRauthor/@as), als Anker-Referenz, z.B. '#publisher', '#rightsHolder'._




<div data-search-exclude markdown="1">



URI: [laws:as_role](https://ld.ech.ch/schema/0296/laws/as_role)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRAuthor](FRBRAuthor.md) | Ein Autoren- oder Rechteinhaber-Eintrag einer FRBR-Entität (akn:FRBRauthor) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [AnchorRef](AnchorRef.md) |
| Domäne von | [FRBRAuthor](FRBRAuthor.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: as_role
annotations:
  description_de:
    tag: description_de
    value: 'Rolle des Autors (akn:FRBRauthor/@as), als Anker-Referenz, z.B. ''#publisher'',
      ''#rightsHolder''.

      '
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: as
description: 'Rolle des Autors (akn:FRBRauthor/@as), als Anker-Referenz, z.B. ''#publisher'',
  ''#rightsHolder''.

  '
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRAuthor
range: AnchorRef

```
</details></div>