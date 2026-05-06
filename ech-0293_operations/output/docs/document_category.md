

# Slot: document_category 


_[de] Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch 'other' verwendet._

_[en] Category of the document. If not set, 'other' is automatically used._

__





URI: [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory)
Alias: document_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DocumentCategoryEnum](DocumentCategoryEnum.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `string(other)` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | meta:documentCategory |
| native | ops:document_category |




## LinkML Source

<details>
```yaml
name: document_category
description: '[de] Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch ''other''
  verwendet.

  [en] Category of the document. If not set, ''other'' is automatically used.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:documentCategory
ifabsent: string(other)
alias: document_category
domain_of:
- Work
range: DocumentCategoryEnum

```
</details>