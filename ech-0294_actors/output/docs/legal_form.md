

# Slot: legal_form 


_[en] Legal form of the organization._

_[de] Rechtsform der Organisation._

__





URI: [act:legalForm](https://ld.ech.ch/schema/0294/actors/legalForm)
Alias: legal_form

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:legalForm](https://ld.ech.ch/schema/0294/actors/legalForm) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:legalForm |
| native | act:legal_form |




## LinkML Source

<details>
```yaml
name: legal_form
description: '[en] Legal form of the organization.

  [de] Rechtsform der Organisation.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:legalForm
alias: legal_form
domain_of:
- InterestLink
range: string

```
</details>