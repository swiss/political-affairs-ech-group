---
search:
  boost: 5.0
---

# Slot: organization_uid 


_UID of the organization (eCH-0097 format: CHE-XXX.XXX.XXX) from the federal UID register (uid.admin.ch)._

__



<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| URI du slot | [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
### Contraintes de valeur

| Propriété | Valeur |
| --- | --- |
| Regex Pattern | `^CHE-\d{3}\.\d{3}\.\d{3}$` |














## Source LinkML

<details>
```yaml
name: organization_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen
      UID-Register (uid.admin.ch).

      '
description: 'UID of the organization (eCH-0097 format: CHE-XXX.XXX.XXX) from the
  federal UID register (uid.admin.ch).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
domain_of:
- InterestLink
- Occupation
range: string
pattern: ^CHE-\d{3}\.\d{3}\.\d{3}$

```
</details></div>