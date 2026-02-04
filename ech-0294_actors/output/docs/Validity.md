

# Class: Validity 



URI: [act:Validity](https://ch.paf.link/schema/actors/Validity)





```mermaid
 classDiagram
    class Validity
    click Validity href "../Validity/"
      Validity <|-- Citizenship
        click Citizenship href "../Citizenship/"
      Validity <|-- Gender
        click Gender href "../Gender/"
      Validity <|-- Occupation
        click Occupation href "../Occupation/"
      
      Validity : valid_until
        
      Validity : valid_from
        
      
```





## Inheritance
* **Validity**
    * [Citizenship](Citizenship.md)
    * [Gender](Gender.md)
    * [Occupation](Occupation.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) |  | direct |
| [valid_until](valid_until.md) | 0..1 <br/> [Date](Date.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [ch_citizenship](ch_citizenship.md) | range | [Validity](Validity.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Validity |
| native | act:Validity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Validity
from_schema: https://ch.paf.link/schema/actors
attributes:
  valid_from:
    name: valid_from
    from_schema: https://ch.paf.link/schema/actors
    slot_uri: act:validFrom
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  valid-until:
    name: valid-until
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:validUntil
    domain_of:
    - Validity
    - ElectoralDistrict
    range: date

```
</details>

### Induced

<details>
```yaml
name: Validity
from_schema: https://ch.paf.link/schema/actors
attributes:
  valid_from:
    name: valid_from
    from_schema: https://ch.paf.link/schema/actors
    slot_uri: act:validFrom
    alias: valid_from
    owner: Validity
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  valid-until:
    name: valid-until
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:validUntil
    alias: valid_until
    owner: Validity
    domain_of:
    - Validity
    - ElectoralDistrict
    range: date

```
</details>