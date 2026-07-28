---
search:
  boost: 5.0
---

# Slot: contact_type 


_Typ der Kontaktinformation._

__



<div data-search-exclude markdown="1">



URI: [act:contactType](https://ld.ech.ch/schema/0294/actors/contactType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Contact](Contact.md) | Kontaktinformation einer Person mit Angabe eines Typs (z |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ContactTypeEnum](ContactTypeEnum.md) |
| Domäne von | [Contact](Contact.md) |
| Slot-URI | [act:contactType](https://ld.ech.ch/schema/0294/actors/contactType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| contact_website |
| email |





## LinkML-Quelle

<details>
```yaml
name: contact_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ der Kontaktinformation.

      '
  description_fr:
    tag: description_fr
    value: 'Type d''informations de contact.

      '
description: 'Typ der Kontaktinformation.

  '
examples:
- value: contact_website
- value: email
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:contactType
domain_of:
- Contact
range: ContactTypeEnum

```
</details></div>