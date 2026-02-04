

# Class: Citizenship 



URI: [act:Citizenship](https://ch.paf.link/schema/actors/Citizenship)





```mermaid
 classDiagram
    class Citizenship
    click Citizenship href "../Citizenship/"
      Validity <|-- Citizenship
        click Validity href "../Validity/"
      
      Citizenship : country
        
      Citizenship : valid_until
        
      Citizenship : valid_from
        
      
```





## Inheritance
* [Validity](Validity.md)
    * **Citizenship**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [country](country.md) | 1 <br/> [String](String.md) | ISO 3166 country code (can't be CH) | direct |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) |  | [Validity](Validity.md) |
| [valid_until](valid_until.md) | 0..1 <br/> [Date](Date.md) |  | [Validity](Validity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [citizenships](citizenships.md) | range | [Citizenship](Citizenship.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Citizenship |
| native | act:Citizenship |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Citizenship
from_schema: https://ch.paf.link/schema/actors
is_a: Validity
attributes:
  country:
    name: country
    description: ISO 3166 country code (can't be CH)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Citizenship
    required: true

```
</details>

### Induced

<details>
```yaml
name: Citizenship
from_schema: https://ch.paf.link/schema/actors
is_a: Validity
attributes:
  country:
    name: country
    description: ISO 3166 country code (can't be CH)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: country
    owner: Citizenship
    domain_of:
    - Citizenship
    range: string
    required: true
  valid_from:
    name: valid_from
    from_schema: https://ch.paf.link/schema/actors
    slot_uri: act:validFrom
    alias: valid_from
    owner: Citizenship
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
    owner: Citizenship
    domain_of:
    - Validity
    - ElectoralDistrict
    range: date

```
</details>