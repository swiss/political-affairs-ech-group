---
search:
  boost: 5.0
---

# Slot: contact_type 


_Type of contact information._

__



<div data-search-exclude markdown="1">



URI: [act:contactType](https://ld.ech.ch/schema/0294/actors/contactType)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Contact](Contact.md) | Contact information of a person indicating a type (e |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [ContactTypeEnum](ContactTypeEnum.md) |
| Domaine de | [Contact](Contact.md) |
| URI du slot | [act:contactType](https://ld.ech.ch/schema/0294/actors/contactType) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| contact_website |
| email |





## Source LinkML

<details>
```yaml
name: contact_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ der Kontaktinformation.

      '
description: 'Type of contact information.

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