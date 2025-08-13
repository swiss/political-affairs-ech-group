

# Class: Actor 



URI: [act:Actor](https://ch.paf.link/schema/actors/Actor)





```mermaid
 classDiagram
    class Actor
    click Actor href "../Actor/"
      Actor : id
        
      Actor : name
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [name](name.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [actors](actors.md) | range | [Actor](Actor.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Actor |
| native | act:Actor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Actor
from_schema: https://ch.paf.link/schema/actors
slots:
- id
- name

```
</details>

### Induced

<details>
```yaml
name: Actor
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: dcterm:identifier
    identifier: true
    alias: id
    owner: Actor
    domain_of:
    - Container
    - Actor
    range: string
    required: true
  name:
    name: name
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: name
    owner: Actor
    domain_of:
    - Actor
    range: string

```
</details>