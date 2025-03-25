

# Class: Person



URI: [personinfo:Person](https://w3id.org/linkml/examples/personinfo/Person)






```mermaid
 classDiagram
    class Person
    click Person href "../Person"
      Person : age
        
      Person : aliases
        
      Person : full_name
        
      Person : id
        
      Person : phone
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [full_name](full_name.md) | 1 <br/> [String](String.md) | name of the person | direct |
| [aliases](aliases.md) | * <br/> [String](String.md) | other names for the person | direct |
| [phone](phone.md) | 0..1 <br/> [String](String.md) |  | direct |
| [age](age.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [persons](persons.md) | range | [Person](Person.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/examples/personinfo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | personinfo:Person |
| native | personinfo:Person |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Person
from_schema: https://w3id.org/linkml/examples/personinfo
attributes:
  id:
    name: id
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    identifier: true
    domain_of:
    - Person
    required: true
  full_name:
    name: full_name
    description: name of the person
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    domain_of:
    - Person
    required: true
  aliases:
    name: aliases
    description: other names for the person
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    domain_of:
    - Person
    multivalued: true
  phone:
    name: phone
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    domain_of:
    - Person
    pattern: ^[\d\(\)\-]+$
  age:
    name: age
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    domain_of:
    - Person
    range: integer
    minimum_value: 0
    maximum_value: 200

```
</details>

### Induced

<details>
```yaml
name: Person
from_schema: https://w3id.org/linkml/examples/personinfo
attributes:
  id:
    name: id
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    identifier: true
    alias: id
    owner: Person
    domain_of:
    - Person
    range: string
  full_name:
    name: full_name
    description: name of the person
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    alias: full_name
    owner: Person
    domain_of:
    - Person
    range: string
    required: true
  aliases:
    name: aliases
    description: other names for the person
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    alias: aliases
    owner: Person
    domain_of:
    - Person
    range: string
    multivalued: true
  phone:
    name: phone
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    alias: phone
    owner: Person
    domain_of:
    - Person
    range: string
    pattern: ^[\d\(\)\-]+$
  age:
    name: age
    from_schema: https://w3id.org/linkml/examples/personinfo
    rank: 1000
    alias: age
    owner: Person
    domain_of:
    - Person
    range: integer
    minimum_value: 0
    maximum_value: 200

```
</details>