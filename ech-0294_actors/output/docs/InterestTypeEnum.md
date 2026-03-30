# Enum: InterestTypeEnum 




_[en] Types of interest links (conflicts of interest, political financing)._

_[de] Typen von Interessenbindungen (Interessenkonflikte, Politikfinanzierung)._

__



URI: [act:InterestTypeEnum](https://ld.ech.ch/schema/0294/actors/InterestTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| professional_activity | act:enum/interest_type/professional_activity | [en] Professional activity |
| political_office | act:enum/interest_type/political_office | [en] Political office |
| association | act:enum/interest_type/association | [en] Association membership |




## Slots

| Name | Description |
| ---  | --- |
| [interest_type](interest_type.md) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verei... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors






## LinkML Source

<details>
```yaml
name: InterestTypeEnum
description: '[en] Types of interest links (conflicts of interest, political financing).

  [de] Typen von Interessenbindungen (Interessenkonflikte, Politikfinanzierung).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
permissible_values:
  professional_activity:
    text: professional_activity
    description: '[en] Professional activity.

      [de] Berufliche Tätigkeit.

      '
    meaning: act:enum/interest_type/professional_activity
  political_office:
    text: political_office
    description: '[en] Political office.

      [de] Politische Ämter.

      '
    meaning: act:enum/interest_type/political_office
  association:
    text: association
    description: '[en] Association membership.

      [de] Vereinsmitgliedschaft.

      '
    meaning: act:enum/interest_type/association

```
</details>