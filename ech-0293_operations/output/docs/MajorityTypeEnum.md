# Enum: MajorityTypeEnum 




_Type of majority required for the vote_



URI: [ops:majority_type_enum](https://ch.paf.link/schema/operations/majority_type_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| absolute | ops:enum/majority_type/absolute |  |
| two-third | ops:enum/majority_type/two-third |  |
| other | ops:enum/majority_type/other |  |




## Slots

| Name | Description |
| ---  | --- |
| [majority_type](majority_type.md) | [en] Type of majority required for the vote (absolute, two-thirds, etc |





## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: majority_type_enum
description: Type of majority required for the vote
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  absolute:
    text: absolute
    meaning: ops:enum/majority_type/absolute
  two-third:
    text: two-third
    meaning: ops:enum/majority_type/two-third
  other:
    text: other
    meaning: ops:enum/majority_type/other

```
</details>