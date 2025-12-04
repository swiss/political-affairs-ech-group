# Enum: IndividualVoteTypeEnum 




_[en] Type of individual vote cast by a member._

_[de] Art der Einzelstimme eines Mitglieds._

__



URI: [ops:individual_vote_type_enum](https://ch.paf.link/schema/operations/individual_vote_type_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| yes | ops:enum/individual_vote_type/yes | [en] Yes vote |
| no | ops:enum/individual_vote_type/no | [en] No vote |
| abstention | ops:enum/individual_vote_type/abstention | [en] Abstention |
| absent | ops:enum/individual_vote_type/absent | [en] Absent (not excused) |
| absent_excused | ops:enum/individual_vote_type/absent_excused | [en] Absent (excused) |
| abstention_president | ops:enum/individual_vote_type/abstention_president | [en] President abstains from voting |
| tie_breaker | ops:enum/individual_vote_type/tie_breaker | [en] Tie-breaking vote |
| other | ops:enum/individual_vote_type/other | [en] Other vote type |




## Slots

| Name | Description |
| ---  | --- |
| [individual_vote_type](individual_vote_type.md) | [en] Type of vote cast (yes, no, abstention, absent, etc |





## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: individual_vote_type_enum
description: '[en] Type of individual vote cast by a member.

  [de] Art der Einzelstimme eines Mitglieds.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  'yes':
    text: 'yes'
    description: '[en] Yes vote

      [de] Ja-Stimme

      '
    meaning: ops:enum/individual_vote_type/yes
  'no':
    text: 'no'
    description: '[en] No vote

      [de] Nein-Stimme

      '
    meaning: ops:enum/individual_vote_type/no
  abstention:
    text: abstention
    description: '[en] Abstention

      [de] Enthaltung

      '
    meaning: ops:enum/individual_vote_type/abstention
  absent:
    text: absent
    description: '[en] Absent (not excused)

      [de] Abwesend (nicht entschuldigt)

      '
    meaning: ops:enum/individual_vote_type/absent
  absent_excused:
    text: absent_excused
    description: '[en] Absent (excused)

      [de] Abwesend (entschuldigt)

      '
    meaning: ops:enum/individual_vote_type/absent_excused
  abstention_president:
    text: abstention_president
    description: '[en] President abstains from voting

      [de] Präsident enthält sich der Stimme

      '
    meaning: ops:enum/individual_vote_type/abstention_president
  tie_breaker:
    text: tie_breaker
    description: '[en] Tie-breaking vote

      [de] Stichentscheid

      '
    meaning: ops:enum/individual_vote_type/tie_breaker
  other:
    text: other
    description: '[en] Other vote type

      [de] Andere Stimmabgabe

      '
    meaning: ops:enum/individual_vote_type/other

```
</details>