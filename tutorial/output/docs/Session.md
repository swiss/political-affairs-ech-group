

# Class: Session 



URI: [tutorial:Session](https://ch.paf.link/schema/tutorial/Session)





```mermaid
 classDiagram
    class Session
    click Session href "../Session/"
      Session : agenda_items
        
          
    
        
        
        Session --> "*" AgendaItem : agenda_items
        click AgendaItem href "../AgendaItem/"
    

        
      Session : date_begin_actual
        
      Session : date_end_actual
        
      Session : id
        
      Session : name
        
          
    
        
        
        Session --> "*" MultilingualString : name
        click MultilingualString href "../MultilingualString/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [date_begin_actual](date_begin_actual.md) | 0..1 <br/> [Date](Date.md) |  | direct |
| [date_end_actual](date_end_actual.md) | 0..1 <br/> [Date](Date.md) |  | direct |
| [name](name.md) | * <br/> [MultilingualString](MultilingualString.md) |  | direct |
| [agenda_items](agenda_items.md) | * <br/> [AgendaItem](AgendaItem.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [sessions](sessions.md) | range | [Session](Session.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:Session |
| native | tutorial:Session |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Session
from_schema: https://ch.paf.link/schema/tutorial
slots:
- id
- date_begin_actual
- date_end_actual
- name
- agenda_items

```
</details>

### Induced

<details>
```yaml
name: Session
from_schema: https://ch.paf.link/schema/tutorial
attributes:
  id:
    name: id
    from_schema: https://ch.paf.link/schema/tutorial
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
  date_begin_actual:
    name: date_begin_actual
    from_schema: https://ch.paf.link/schema/tutorial
    rank: 1000
    alias: date_begin_actual
    owner: Session
    domain_of:
    - Session
    range: date
  date_end_actual:
    name: date_end_actual
    from_schema: https://ch.paf.link/schema/tutorial
    rank: 1000
    alias: date_end_actual
    owner: Session
    domain_of:
    - Session
    range: date
  name:
    name: name
    from_schema: https://ch.paf.link/schema/tutorial
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: Session
    domain_of:
    - Session
    - AgendaItem
    range: MultilingualString
    multivalued: true
    inlined_as_list: true
  agenda_items:
    name: agenda_items
    from_schema: https://ch.paf.link/schema/tutorial
    rank: 1000
    slot_uri: tutorial:agendaItem
    alias: agenda_items
    owner: Session
    domain_of:
    - Session
    - Container
    range: AgendaItem
    multivalued: true
    inlined_as_list: true

```
</details>