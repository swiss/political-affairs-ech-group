

# Class: PersonReference 


_Reference to a person acting in a specific role or function_





URI: [act:PersonReference](https://ch.paf.link/schema/actors/PersonReference)





```mermaid
 classDiagram
    class PersonReference
    click PersonReference href "../PersonReference/"
      PersonReference : function
        
      PersonReference : group
        
      PersonReference : id
        
      PersonReference : name
        
      PersonReference : role
        
      PersonReference : uri
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | Internal system identifier | direct |
| [uri](uri.md) | 0..1 <br/> [String](String.md) | Globally valid identifier (eCH-0285 compatible) | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Full name of the person | direct |
| [role](role.md) | 1 <br/> [String](String.md) | Role of the person (e | direct |
| [function](function.md) | 0..1 <br/> [String](String.md) | Function of the person (e | direct |
| [group](group.md) | 0..1 <br/> [String](String.md) | Group or body the function applies to | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:PersonReference |
| native | act:PersonReference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonReference
description: Reference to a person acting in a specific role or function
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    description: Internal system identifier
    from_schema: https://ch.paf.link/schema/actors
    identifier: true
    domain_of:
    - Person
    - PersonReference
    - GroupReference
    required: true
  uri:
    name: uri
    description: Globally valid identifier (eCH-0285 compatible)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - PersonReference
    - GroupReference
  name:
    name: name
    description: Full name of the person
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - PersonReference
    - GroupReference
    required: true
  role:
    name: role
    description: Role of the person (e.g. speaker, author, holder, leading)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - PersonReference
    - GroupReference
    required: true
  function:
    name: function
    description: Function of the person (e.g. president, member)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - PersonReference
  group:
    name: group
    description: Group or body the function applies to
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - PersonReference

```
</details>

### Induced

<details>
```yaml
name: PersonReference
description: Reference to a person acting in a specific role or function
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    description: Internal system identifier
    from_schema: https://ch.paf.link/schema/actors
    identifier: true
    alias: id
    owner: PersonReference
    domain_of:
    - Person
    - PersonReference
    - GroupReference
    range: string
    required: true
  uri:
    name: uri
    description: Globally valid identifier (eCH-0285 compatible)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: uri
    owner: PersonReference
    domain_of:
    - PersonReference
    - GroupReference
    range: string
  name:
    name: name
    description: Full name of the person
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: name
    owner: PersonReference
    domain_of:
    - PersonReference
    - GroupReference
    range: string
    required: true
  role:
    name: role
    description: Role of the person (e.g. speaker, author, holder, leading)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: role
    owner: PersonReference
    domain_of:
    - PersonReference
    - GroupReference
    range: string
    required: true
  function:
    name: function
    description: Function of the person (e.g. president, member)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: function
    owner: PersonReference
    domain_of:
    - PersonReference
    range: string
  group:
    name: group
    description: Group or body the function applies to
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: group
    owner: PersonReference
    domain_of:
    - PersonReference
    range: string

```
</details>