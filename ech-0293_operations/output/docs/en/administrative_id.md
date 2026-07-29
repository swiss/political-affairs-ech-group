---
search:
  boost: 5.0
---

# Slot: administrative_id 


_Administrative ID of the legislative body, such as a municipality, canton, or country._




<div data-search-exclude markdown="1">



URI: [ops:administrative_id](https://ch.paf.link/schema/operations/administrative_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Legislature](Legislature.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: administrative_id
annotations:
  description_de:
    tag: description_de
    value: 'Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder
      Land.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant administratif du corps législatif, p. ex. commune, canton
      ou pays.

      '
description: 'Administrative ID of the legislative body, such as a municipality, canton,
  or country.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
range: string

```
</details></div>