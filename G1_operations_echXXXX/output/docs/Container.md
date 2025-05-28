

# Class: Container 



URI: [ops:Container](https://ch.paf.link/schema/operations/Container)






```mermaid
 classDiagram
    class Container
    click Container href "../Container"
      Container : id
        
      Container : legislatures
        
          
    
        
        
        Container --> "*" Legislature : legislatures
        click Legislature href "../Legislature"
    

        
      Container : meeting_items
        
          
    
        
        
        Container --> "*" MeetingItem : meeting_items
        click MeetingItem href "../MeetingItem"
    

        
      Container : meetings
        
          
    
        
        
        Container --> "*" Meeting : meetings
        click Meeting href "../Meeting"
    

        
      Container : sessions
        
          
    
        
        
        Container --> "*" Session : sessions
        click Session href "../Session"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [legislatures](legislatures.md) | * <br/> [Legislature](Legislature.md) |  | direct |
| [sessions](sessions.md) | * <br/> [Session](Session.md) |  | direct |
| [meetings](meetings.md) | * <br/> [Meeting](Meeting.md) |  | direct |
| [meeting_items](meeting_items.md) | * <br/> [MeetingItem](MeetingItem.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:Container |
| native | ops:Container |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Container
from_schema: https://ch.paf.link/schema/operations
slots:
- id
- legislatures
- sessions
- meetings
- meeting_items
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Container
from_schema: https://ch.paf.link/schema/operations
attributes:
  id:
    name: id
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: dcterm:identifier
    identifier: true
    alias: id
    owner: Container
    domain_of:
    - Container
    - Legislature
    - Session
    - Meeting
    - MeetingItem
    range: string
    required: true
  legislatures:
    name: legislatures
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:legislature
    alias: legislatures
    owner: Container
    domain_of:
    - Container
    range: Legislature
    multivalued: true
    inlined_as_list: true
  sessions:
    name: sessions
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:session
    alias: sessions
    owner: Container
    domain_of:
    - Container
    range: Session
    multivalued: true
    inlined_as_list: true
  meetings:
    name: meetings
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:meeting
    alias: meetings
    owner: Container
    domain_of:
    - Container
    range: Meeting
    multivalued: true
    inlined_as_list: true
  meeting_items:
    name: meeting_items
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:meetingItem
    alias: meeting_items
    owner: Container
    domain_of:
    - Container
    range: MeetingItem
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>