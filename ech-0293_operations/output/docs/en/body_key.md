---
search:
  boost: 5.0
---

# Slot: body_key 


_Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland)._




<div data-search-exclude markdown="1">



URI: [ops:body_key](https://ch.paf.link/schema/operations/body_key)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: body_key
annotations:
  description_de:
    tag: description_de
    value: 'Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit
      (z.B. BE für Bern, CHE für Schweiz).

      '
  description_fr:
    tag: description_fr
    value: 'Clé identifiant l''organe politique ou la collectivité (p. ex. BE pour
      Berne, CHE pour la Suisse).

      '
description: 'Key identifying the political body or jurisdiction (e.g., BE for Bern,
  CHE for Switzerland).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>