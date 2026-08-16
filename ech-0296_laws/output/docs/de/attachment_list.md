---
search:
  boost: 5.0
---

# Slot: attachment_list 


_Die beigefügten Dokumente (akn:attachment)._



<div data-search-exclude markdown="1">



URI: [laws:attachment_list](https://ld.ech.ch/schema/0296/laws/attachment_list)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Attachments](Attachments.md) | Dem Erlass beigefügte Dokumente |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Attachment](Attachment.md) |
| Domäne von | [Attachments](Attachments.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: attachment_list
annotations:
  description_de:
    tag: description_de
    value: Die beigefügten Dokumente (akn:attachment).
  xml_element:
    tag: xml_element
    value: akn:attachment
description: Die beigefügten Dokumente (akn:attachment).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:attachment
rank: 1000
domain_of:
- Attachments
range: Attachment
multivalued: true

```
</details></div>