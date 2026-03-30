

# Slot: organization_label 


_[en] Label of the organization._

_[de] Bezeichnung der Organisation._

__





URI: [act:organizationLabel](https://ld.ech.ch/schema/0294/actors/organizationLabel)
Alias: organization_label

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
| Slot URI | [act:organizationLabel](https://ld.ech.ch/schema/0294/actors/organizationLabel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:organizationLabel |
| native | act:organization_label |




## LinkML Source

<details>
```yaml
name: organization_label
description: '[en] Label of the organization.

  [de] Bezeichnung der Organisation.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationLabel
alias: organization_label
domain_of:
- InterestLink
range: string

```
</details>