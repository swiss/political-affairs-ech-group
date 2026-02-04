

# Class: Contact 



URI: [act:Contact](https://ch.paf.link/schema/actors/Contact)





```mermaid
 classDiagram
    class Contact
    click Contact href "../Contact/"
      Contact : type
        
          
    
        
        
        Contact --> "1" ContactTypeEnum : type
        click ContactTypeEnum href "../ContactTypeEnum/"
    

        
      Contact : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [ContactTypeEnum](ContactTypeEnum.md) |  | direct |
| [value](value.md) | 1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |
| [Group](Group.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Contact |
| native | act:Contact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Contact
from_schema: https://ch.paf.link/schema/actors
attributes:
  type:
    name: type
    from_schema: https://ch.paf.link/schema/actors
    domain_of:
    - Training
    - Contact
    range: ContactTypeEnum
    required: true
  value:
    name: value
    from_schema: https://ch.paf.link/schema/actors
    domain_of:
    - Name
    - Gender
    - Occupation
    - Training
    - Contact
    required: true

```
</details>

### Induced

<details>
```yaml
name: Contact
from_schema: https://ch.paf.link/schema/actors
attributes:
  type:
    name: type
    from_schema: https://ch.paf.link/schema/actors
    alias: type
    owner: Contact
    domain_of:
    - Training
    - Contact
    range: ContactTypeEnum
    required: true
  value:
    name: value
    from_schema: https://ch.paf.link/schema/actors
    alias: value
    owner: Contact
    domain_of:
    - Name
    - Gender
    - Occupation
    - Training
    - Contact
    range: string
    required: true

```
</details>