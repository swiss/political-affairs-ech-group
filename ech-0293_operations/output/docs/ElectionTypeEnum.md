# Enum: ElectionTypeEnum 




_[en] Type of election procedure._

_[de] Art des Wahlverfahrens._

__



URI: [ops:election_type_enum](https://ch.paf.link/schema/operations/election_type_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| secret | ops:enum/election_type/secret | [en] Secret election (Geheime Wahl) |
| open | ops:enum/election_type/open | [en] Open election (Offene Wahl) |
| silent | ops:enum/election_type/silent | [en] Silent election without opponent (Stille Wahl ohne Gegenkandidat) |




## Slots

| Name | Description |
| ---  | --- |
| [election_type](election_type.md) | Type of election procedure |





## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: election_type_enum
description: '[en] Type of election procedure.

  [de] Art des Wahlverfahrens.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  secret:
    text: secret
    description: '[en] Secret election (Geheime Wahl)

      [de] Geheime Wahl

      '
    meaning: ops:enum/election_type/secret
  open:
    text: open
    description: '[en] Open election (Offene Wahl)

      [de] Offene Wahl

      '
    meaning: ops:enum/election_type/open
  silent:
    text: silent
    description: '[en] Silent election without opponent (Stille Wahl ohne Gegenkandidat)

      [de] Stille Wahl ohne Gegenkandidat

      '
    meaning: ops:enum/election_type/silent

```
</details>