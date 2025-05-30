

# Class: Session 



URI: [chpaf:Session](https://ch.paf.link/Session)






```mermaid
 classDiagram
    class Session
    click Session href "../Session"
      Session : agendaItems
        
          
    
        
        
        Session --> "*" AgendaItem : agendaItems
        click AgendaItem href "../AgendaItem"
    

        
      Session : id
        
      Session : name
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [name](name.md) | 1 <br/> [String](String.md) |  | direct |
| [agendaItems](agendaItems.md) | * <br/> [AgendaItem](AgendaItem.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [sessions](sessions.md) | range | [Session](Session.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:Session |
| native | chpaf:Session |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Session
from_schema: https://ch.paf.link/schema/session
slots:
- id
- name
- agendaItems

```
</details>

### Induced

<details>
```yaml
name: Session
from_schema: https://ch.paf.link/schema/session
attributes:
  id:
    name: id
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    identifier: true
    alias: id
    owner: Session
    domain_of:
    - Session
    - AgendaItem
    - Vote
    - Container
    range: string
    required: true
  name:
    name: name
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    slot_uri: dcterm:title
    alias: name
    owner: Session
    domain_of:
    - Session
    - AgendaItem
    range: string
    required: true
  agendaItems:
    name: agendaItems
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    slot_uri: chpaf:agendaItem
    alias: agendaItems
    owner: Session
    domain_of:
    - Session
    range: AgendaItem
    multivalued: true
    inlined_as_list: true

```
</details>