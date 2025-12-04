# Enum: VotingTypeEnum 




_[en] Type of voting procedure._

_[de] Art des Abstimmungsverfahrens._

__



URI: [ops:voting_type_enum](https://ch.paf.link/schema/operations/voting_type_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| preliminary_vote | ops:enum/voting_type/preliminary_vote | [en] Preliminary vote (Zwischenabstimmung) |
| final_vote | ops:enum/voting_type/final_vote | [en] Final vote (Schlussabstimmung) |
| tie_breaker_president | ops:enum/voting_type/tie_breaker_president | [en] President's tie-breaking vote (Stichentscheid Präsidium) |
| secret_vote | ops:enum/voting_type/secret_vote | [en] Secret ballot (Geheime Wahl/Abstimmung) |
| other | ops:enum/voting_type/other | [en] Other voting type |




## Slots

| Name | Description |
| ---  | --- |
| [voting_type](voting_type.md) | [en] Type of voting procedure (preliminary, final, secret, etc |





## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: voting_type_enum
description: '[en] Type of voting procedure.

  [de] Art des Abstimmungsverfahrens.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  preliminary_vote:
    text: preliminary_vote
    description: '[en] Preliminary vote (Zwischenabstimmung)

      [de] Zwischenabstimmung

      '
    meaning: ops:enum/voting_type/preliminary_vote
  final_vote:
    text: final_vote
    description: '[en] Final vote (Schlussabstimmung)

      [de] Schlussabstimmung

      '
    meaning: ops:enum/voting_type/final_vote
  tie_breaker_president:
    text: tie_breaker_president
    description: '[en] President''s tie-breaking vote (Stichentscheid Präsidium)

      [de] Stichentscheid Präsidium

      '
    meaning: ops:enum/voting_type/tie_breaker_president
  secret_vote:
    text: secret_vote
    description: '[en] Secret ballot (Geheime Wahl/Abstimmung)

      [de] Geheime Wahl/Abstimmung

      '
    meaning: ops:enum/voting_type/secret_vote
  other:
    text: other
    description: '[en] Other voting type

      [de] Andere Abstimmungsart

      '
    meaning: ops:enum/voting_type/other

```
</details>