---
search:
  boost: 5.0
---

# Slot: title 

<div data-search-exclude markdown="1">



URI: [ops:title](https://ch.paf.link/schema/operations/title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Election](Election.md), [Motion](Motion.md), [Media](Media.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: title
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Election
- Motion
- Media
range: string

```
</details></div>