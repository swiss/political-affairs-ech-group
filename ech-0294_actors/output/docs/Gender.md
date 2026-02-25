

# Class: Gender 



URI: [act:Gender](https://ch.paf.link/schema/actors/Gender)





```mermaid
 classDiagram
    class Gender
    click Gender href "../Gender/"
      Validity <|-- Gender
        click Validity href "../Validity/"
      
      Gender : pronouns
        
      Gender : valid_from
        
      Gender : valid_until
        
      Gender : value
        
      
```





## Inheritance
* [Validity](Validity.md)
    * **Gender**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | Gender code | direct |
| [pronouns](pronouns.md) | * <br/> [String](String.md) | Pronouns used by the person | direct |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) |  | [Validity](Validity.md) |
| [valid_until](valid_until.md) | 0..1 <br/> [Date](Date.md) |  | [Validity](Validity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [genders](genders.md) | range | [Gender](Gender.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Gender |
| native | act:Gender |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gender
from_schema: https://ch.paf.link/schema/actors
is_a: Validity
attributes:
  value:
    name: value
    description: Gender code
    from_schema: https://ch.paf.link/schema/actors
    domain_of:
    - Name
    - Gender
    - Occupation
    - Training
    - Contact
    required: true
  pronouns:
    name: pronouns
    description: Pronouns used by the person
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Gender
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: Gender
from_schema: https://ch.paf.link/schema/actors
is_a: Validity
attributes:
  value:
    name: value
    description: Gender code
    from_schema: https://ch.paf.link/schema/actors
    alias: value
    owner: Gender
    domain_of:
    - Name
    - Gender
    - Occupation
    - Training
    - Contact
    range: string
    required: true
  pronouns:
    name: pronouns
    description: Pronouns used by the person
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: pronouns
    owner: Gender
    domain_of:
    - Gender
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  valid_from:
    name: valid_from
    from_schema: https://ch.paf.link/schema/actors
    slot_uri: act:validFrom
    alias: valid_from
    owner: Gender
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  valid_until:
    name: valid_until
    from_schema: https://ch.paf.link/schema/actors
    slot_uri: act:validUntil
    alias: valid_until
    owner: Gender
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    - Validity
    - ElectoralDistrict
    range: date

```
</details>