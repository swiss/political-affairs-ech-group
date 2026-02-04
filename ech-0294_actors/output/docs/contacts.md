

# Slot: contacts 


_[en] Contact information (email, website, social media)._

_[de] Kontaktinformationen (E-Mail, Website, Social Media)._

__





URI: [act:contact](https://ch.paf.link/schema/actors/contact)
Alias: contacts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [Contact](Contact.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:contact |
| native | act:contacts |




## LinkML Source

<details>
```yaml
name: contacts
description: '[en] Contact information (email, website, social media).

  [de] Kontaktinformationen (E-Mail, Website, Social Media).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:contact
alias: contacts
domain_of:
- Person
- Group
range: Contact
multivalued: true
inlined: true
inlined_as_list: true

```
</details>