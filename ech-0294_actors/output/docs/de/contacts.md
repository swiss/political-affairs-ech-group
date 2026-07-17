---
search:
  boost: 5.0
---

# Slot: contacts 


_Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden._

__



<div data-search-exclude markdown="1">



URI: [act:contact](https://ld.ech.ch/schema/0294/actors/contact)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Contact](Contact.md) |
| Domäne von | [Person](Person.md), [Group](Group.md) |
| Slot-URI | [act:contact](https://ld.ech.ch/schema/0294/actors/contact) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: contacts
annotations:
  description_de:
    tag: description_de
    value: 'Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail
      ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.

      '
description: 'Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail
  ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:contact
domain_of:
- Person
- Group
range: Contact
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>