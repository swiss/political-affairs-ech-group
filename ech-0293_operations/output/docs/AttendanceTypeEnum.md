---
search:
  boost: 2.0
---


# Enum: AttendanceTypeEnum 




_[en] Type of individual attendance._

_[de] Art der individuellen Anwesenheit._

__



<div data-search-exclude markdown="1">

URI: [ops:AttendanceTypeEnum](https://ch.paf.link/schema/operations/AttendanceTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| remote | ops:enum/attendance_type/remote | [en] Remote participation |
| substitute | ops:enum/attendance_type/substitute | [en] Substitute (Stellvertretung) |
| present | ops:enum/attendance_type/present | [en] Present in person |




## Slots

| Name | Description |
| ---  | --- |
| [attendance_type](attendance_type.md) | Type of individual attendance |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: AttendanceTypeEnum
description: '[en] Type of individual attendance.

  [de] Art der individuellen Anwesenheit.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  remote:
    text: remote
    description: '[en] Remote participation

      [de] Teilnahme per Fernzugriff

      '
    meaning: ops:enum/attendance_type/remote
  substitute:
    text: substitute
    description: '[en] Substitute (Stellvertretung)

      [de] Stellvertretung

      '
    meaning: ops:enum/attendance_type/substitute
  present:
    text: present
    description: '[en] Present in person

      [de] Persönlich anwesend

      '
    meaning: ops:enum/attendance_type/present

```
</details>

</div>