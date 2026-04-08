---
search:
  boost: 5.0
---

# Slot: is_correspondence 


_[de] Gibt an, ob es sich um die bevorzugte Sprache handelt._

_[en] Indicates if this is the preferred language._

__



<div data-search-exclude markdown="1">



URI: [act:isCorrespondence](https://ld.ech.ch/schema/0294/actors/isCorrespondence)
Alias: is_correspondence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LanguageProficiency](LanguageProficiency.md) | [de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um d... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [LanguageProficiency](LanguageProficiency.md) |
| Slot URI | [act:isCorrespondence](https://ld.ech.ch/schema/0294/actors/isCorrespondence) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:isCorrespondence |
| native | act:is_correspondence |




## LinkML Source

<details>
```yaml
name: is_correspondence
description: '[de] Gibt an, ob es sich um die bevorzugte Sprache handelt.

  [en] Indicates if this is the preferred language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isCorrespondence
alias: is_correspondence
domain_of:
- LanguageProficiency
range: boolean

```
</details></div>