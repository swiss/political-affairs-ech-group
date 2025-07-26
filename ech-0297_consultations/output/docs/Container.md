

# Class: Container



URI: [chpaf:Container](https://ch.paf.link/Container)






```mermaid
 classDiagram
    class Container
    click Container href "../Container"
      Container : consultations
        
          
    
    
    Container --> "*" Consultation : consultations
    click Consultation href "../Consultation"

        
      Container : id
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [consultations](consultations.md) | * <br/> [Consultation](Consultation.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/consultation




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:Container |
| native | chpaf:Container |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Container
from_schema: https://ch.paf.link/schema/consultation
slots:
- id
- consultations
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Container
from_schema: https://ch.paf.link/schema/consultation
attributes:
  id:
    name: id
    from_schema: https://ch.paf.link/schema/consultation
    rank: 1000
    identifier: true
    alias: id
    owner: Container
    domain_of:
    - Consultation
    - Container
    range: string
    required: true
  consultations:
    name: consultations
    from_schema: https://ch.paf.link/schema/consultation
    rank: 1000
    slot_uri: chpaf:consultation
    alias: consultations
    owner: Container
    domain_of:
    - Container
    range: Consultation
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>