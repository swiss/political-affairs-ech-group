---
search:
  boost: 5.0
---

# Slot: function_role 


_Function or role in the organization (e.g., Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in)._

__



<div data-search-exclude markdown="1">



URI: [act:functionRole](https://ld.ech.ch/schema/0294/actors/functionRole)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:functionRole](https://ld.ech.ch/schema/0294/actors/functionRole) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: function_role
annotations:
  description_de:
    tag: description_de
    value: 'Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in,
      Mitglied, Delegierter, Geschäftsführer/in, Berater/in).

      '
  description_fr:
    tag: description_fr
    value: 'Fonction ou rôle dans l''organisation (p. ex. président/e, vice-président/e,
      membre, délégué, directeur/directrice, conseiller/ère).

      '
description: 'Function or role in the organization (e.g., Präsident/in, Vizepräsident/in,
  Mitglied, Delegierter, Geschäftsführer/in, Berater/in).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:functionRole
domain_of:
- InterestLink
range: string

```
</details></div>