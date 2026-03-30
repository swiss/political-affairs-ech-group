

# Slot: label_long 


_[de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.)._

_[en] Option to assign an extended label to a structured piece of information (e.g., display name with title, position, etc.)._

__





URI: [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong)
Alias: label_long

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:labelLong |
| native | act:label_long |




## LinkML Source

<details>
```yaml
name: label_long
description: '[de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel
  zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).

  [en] Option to assign an extended label to a structured piece of information (e.g.,
  display name with title, position, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:labelLong
alias: label_long
domain_of:
- Person
range: string

```
</details>