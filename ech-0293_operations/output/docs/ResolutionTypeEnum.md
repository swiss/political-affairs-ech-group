# Enum: ResolutionTypeEnum 




_[en] Type of resolutiontaken on an agenda item._

_[de] Art der Resolution zu einem Traktandum._

__



URI: [ops:resolution_type_enum](https://ch.paf.link/schema/operations/resolution_type_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| accepted | ops:enum/resolution_type/accepted | [en] Accepted (Annahme) |
| rejected | ops:enum/resolution_type/rejected | [en] Rejected (Ablehnung) |
| noted | ops:enum/resolution_type/noted | [en] Noted (Kenntnisnahme) |
| accepted_point_by_point | ops:enum/resolution_type/accepted_point_by_point | [en] Accepted point by point (Punktweise Annahme) |
| accepted_with_postulate | ops:enum/resolution_type/accepted_with_postulate | [en] Accepted with postulate (Annahme mit Postulat) |
| orally_settled | ops:enum/resolution_type/orally_settled | [en] Orally settled (Mündlich erledigt) |
| nearly_unanimous | ops:enum/resolution_type/nearly_unanimous | [en] Nearly unanimous (Beinahe einstimmig) |
| other | ops:enum/resolution_type/other | [en] Other resolutiontype not covered by standard categories |




## Slots

| Name | Description |
| ---  | --- |
| [resolution_type](resolution_type.md) | [en] Type of resolutiontaken on the agenda item |





## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: resolution_type_enum
description: '[en] Type of resolutiontaken on an agenda item.

  [de] Art der Resolution zu einem Traktandum.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  accepted:
    text: accepted
    description: '[en] Accepted (Annahme)

      [de] Annahme

      '
    meaning: ops:enum/resolution_type/accepted
  rejected:
    text: rejected
    description: '[en] Rejected (Ablehnung)

      [de] Ablehnung

      '
    meaning: ops:enum/resolution_type/rejected
  noted:
    text: noted
    description: '[en] Noted (Kenntnisnahme)

      [de] Kenntnisnahme

      '
    meaning: ops:enum/resolution_type/noted
  accepted_point_by_point:
    text: accepted_point_by_point
    description: '[en] Accepted point by point (Punktweise Annahme)

      [de] Punktweise Annahme

      '
    meaning: ops:enum/resolution_type/accepted_point_by_point
  accepted_with_postulate:
    text: accepted_with_postulate
    description: '[en] Accepted with postulate (Annahme mit Postulat)

      [de] Annahme mit Postulat

      '
    meaning: ops:enum/resolution_type/accepted_with_postulate
  orally_settled:
    text: orally_settled
    description: '[en] Orally settled (Mündlich erledigt)

      [de] Mündlich erledigt

      '
    meaning: ops:enum/resolution_type/orally_settled
  nearly_unanimous:
    text: nearly_unanimous
    description: '[en] Nearly unanimous (Beinahe einstimmig)

      [de] Beinahe einstimmig

      '
    meaning: ops:enum/resolution_type/nearly_unanimous
  other:
    text: other
    description: '[en] Other resolutiontype not covered by standard categories

      [de] Andere Resolution, nicht durch Standardkategorien abgedeckt

      '
    meaning: ops:enum/resolution_type/other

```
</details>