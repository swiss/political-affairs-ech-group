---
search:
  boost: 5.0
---

# Slot: contacts 


_Informations de contact (e-mail, site web, réseaux sociaux). Directive : l'e-mail est quasi obligatoire et devrait toujours être fourni lorsqu'il est disponible._

__



<div data-search-exclude markdown="1">



URI: [act:contact](https://ld.ech.ch/schema/0294/actors/contact)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Contact](Contact.md) |
| Domaine de | [Person](Person.md), [Group](Group.md) |
| URI du slot | [act:contact](https://ld.ech.ch/schema/0294/actors/contact) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: contacts
annotations:
  description_de:
    tag: description_de
    value: 'Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail
      ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.

      '
  description_fr:
    tag: description_fr
    value: 'Informations de contact (e-mail, site web, réseaux sociaux). Directive
      : l''e-mail est quasi obligatoire et devrait toujours être fourni lorsqu''il
      est disponible.

      '
description: 'Informations de contact (e-mail, site web, réseaux sociaux). Directive
  : l''e-mail est quasi obligatoire et devrait toujours être fourni lorsqu''il est
  disponible.

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