

# Class: Container 



URI: [act:Container](https://ch.paf.link/schema/actors/Container)






```mermaid
 classDiagram
    class Container
    click Container href "../Container"
      Container : actors
        
          
    
        
        
        Container --> "*" Actor : actors
        click Actor href "../Actor"
    

        
      Container : id
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [actors](actors.md) | * <br/> [Actor](Actor.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Container |
| native | act:Container |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Container
from_schema: https://ch.paf.link/schema/actors
slots:
- id
- actors
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Container
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: dcterm:identifier
    identifier: true
    alias: id
    owner: Container
    domain_of:
    - Container
    - Actor
    range: string
    required: true
  actors:
    name: actors
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:actor
    alias: actors
    owner: Container
    domain_of:
    - Container
    range: Actor
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>