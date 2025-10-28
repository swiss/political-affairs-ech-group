

# Class: Occupation 



URI: [act:Occupation](https://ch.paf.link/schema/actors/Occupation)





```mermaid
 classDiagram
    class Occupation
    click Occupation href "../Occupation/"
      Validity <|-- Occupation
        click Validity href "../Validity/"
      
      Occupation : active
        
      Occupation : enterprise
        
      Occupation : enterprise_uid
        
      Occupation : occupation
        
      Occupation : occupation_isco19_code
        
      Occupation : paid
        
      Occupation : validFrom
        
      Occupation : validUntil
        
      
```





## Inheritance
* [Validity](Validity.md)
    * **Occupation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [active](active.md) | 0..1 <br/> [Boolean](Boolean.md) |  | direct |
| [paid](paid.md) | 0..1 <br/> [Boolean](Boolean.md) |  | direct |
| [occupation_isco19_code](occupation_isco19_code.md) | 0..1 <br/> [String](String.md) |  | direct |
| [occupation](occupation.md) | 0..1 <br/> [String](String.md) |  | direct |
| [enterprise_uid](enterprise_uid.md) | 0..1 <br/> [String](String.md) |  | direct |
| [enterprise](enterprise.md) | 0..1 <br/> [String](String.md) |  | direct |
| [validFrom](validFrom.md) | 0..1 <br/> [Date](Date.md) |  | [Validity](Validity.md) |
| [validUntil](validUntil.md) | 0..1 <br/> [Date](Date.md) |  | [Validity](Validity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [occupations](occupations.md) | range | [Occupation](Occupation.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Occupation |
| native | act:Occupation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Occupation
from_schema: https://ch.paf.link/schema/actors
is_a: Validity
attributes:
  active:
    name: active
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Occupation
    range: boolean
  paid:
    name: paid
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Occupation
    range: boolean
  occupation_isco19_code:
    name: occupation_isco19_code
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Occupation
  occupation:
    name: occupation
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Occupation
  enterprise_uid:
    name: enterprise_uid
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Occupation
  enterprise:
    name: enterprise
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Occupation

```
</details>

### Induced

<details>
```yaml
name: Occupation
from_schema: https://ch.paf.link/schema/actors
is_a: Validity
attributes:
  active:
    name: active
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: active
    owner: Occupation
    domain_of:
    - Occupation
    range: boolean
  paid:
    name: paid
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: paid
    owner: Occupation
    domain_of:
    - Occupation
    range: boolean
  occupation_isco19_code:
    name: occupation_isco19_code
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: occupation_isco19_code
    owner: Occupation
    domain_of:
    - Occupation
    range: string
  occupation:
    name: occupation
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: occupation
    owner: Occupation
    domain_of:
    - Occupation
    range: string
  enterprise_uid:
    name: enterprise_uid
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: enterprise_uid
    owner: Occupation
    domain_of:
    - Occupation
    range: string
  enterprise:
    name: enterprise
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: enterprise
    owner: Occupation
    domain_of:
    - Occupation
    range: string
  validFrom:
    name: validFrom
    from_schema: https://ch.paf.link/schema/actors
    alias: validFrom
    owner: Occupation
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  validUntil:
    name: validUntil
    from_schema: https://ch.paf.link/schema/actors
    alias: validUntil
    owner: Occupation
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date

```
</details>