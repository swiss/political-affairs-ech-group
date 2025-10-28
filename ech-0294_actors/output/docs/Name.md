

# Class: Name 



URI: [act:Name](https://ch.paf.link/schema/actors/Name)





```mermaid
 classDiagram
    class Name
    click Name href "../Name/"
      Name : nameType
        
          
    
        
        
        Name --> "1" NameTypeEnum : nameType
        click NameTypeEnum href "../NameTypeEnum/"
    

        
      Name : validFrom
        
      Name : validUntil
        
      Name : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [nameType](nameType.md) | 1 <br/> [NameTypeEnum](NameTypeEnum.md) | categories of name types | direct |
| [value](value.md) | 1 <br/> [String](String.md) |  | direct |
| [validFrom](validFrom.md) | 0..1 <br/> [Date](Date.md) |  | direct |
| [validUntil](validUntil.md) | 0..1 <br/> [Date](Date.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [names](names.md) | range | [Name](Name.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Name |
| native | act:Name |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Name
from_schema: https://ch.paf.link/schema/actors
attributes:
  nameType:
    name: nameType
    description: categories of name types
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Name
    range: NameTypeEnum
    required: true
  value:
    name: value
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Name
    required: true
  validFrom:
    name: validFrom
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  validUntil:
    name: validUntil
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date

```
</details>

### Induced

<details>
```yaml
name: Name
from_schema: https://ch.paf.link/schema/actors
attributes:
  nameType:
    name: nameType
    description: categories of name types
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: nameType
    owner: Name
    domain_of:
    - Name
    range: NameTypeEnum
    required: true
  value:
    name: value
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: value
    owner: Name
    domain_of:
    - Name
    range: string
    required: true
  validFrom:
    name: validFrom
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: validFrom
    owner: Name
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  validUntil:
    name: validUntil
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: validUntil
    owner: Name
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date

```
</details>