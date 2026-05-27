---
search:
  boost: 2.0
---


# Enum: IndividualVoteTypeEnum 




_[en] Type of individual vote cast by a member._

_[de] Art der Einzelstimme eines Mitglieds._

__



<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| yes | ops:enum/individual_vote_type/yes | [en] Vote in favor (yes) |
| no | ops:enum/individual_vote_type/no | [en] Vote against (no) |
| abstention | ops:enum/individual_vote_type/abstention | [en] Abstention |
| not_voted | ops:enum/individual_vote_type/not_voted | [en] Not Voted |
| tie_breaker | ops:enum/individual_vote_type/tie_breaker | [en] Tie-breaking vote, TODO english |
| other | ops:enum/individual_vote_type/other | [en] Other vote type |




## Slots

| Name | Description |
| ---  | --- |
| [individual_vote_type](individual_vote_type.md) | [en] Type of vote cast (yes, no, abstention, no vote, etc |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: IndividualVoteTypeEnum
description: '[en] Type of individual vote cast by a member.

  [de] Art der Einzelstimme eines Mitglieds.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  'yes':
    text: 'yes'
    description: '[en] Vote in favor (yes)

      [de] Ja-Stimme

      '
    meaning: ops:enum/individual_vote_type/yes
  'no':
    text: 'no'
    description: '[en] Vote against (no)

      [de] Nein-Stimme

      '
    meaning: ops:enum/individual_vote_type/no
  abstention:
    text: abstention
    description: '[en] Abstention

      [de] Enthaltung

      '
    meaning: ops:enum/individual_vote_type/abstention
  not_voted:
    text: not_voted
    description: '[en] Not Voted

      [de] Nicht abgestimmt

      '
    meaning: ops:enum/individual_vote_type/not_voted
  tie_breaker:
    text: tie_breaker
    description: '[en] Tie-breaking vote, TODO english

      [de] Stichentscheid, meist durch Präsidium

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

</div>