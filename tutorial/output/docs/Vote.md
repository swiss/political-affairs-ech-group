

# Class: Vote



URI: [chpaf:Vote](https://ch.paf.link/Vote)






```mermaid
 classDiagram
    class Vote
    click Vote href "../Vote"
      Vote : question
        
      Vote : result
        
          
    
    
    Vote --> "1" ResultEnum : result
    click ResultEnum href "../ResultEnum"

        
      Vote : uid
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [uid](uid.md) | 1 <br/> [String](String.md) |  | direct |
| [question](question.md) | 1 <br/> [String](String.md) |  | direct |
| [result](result.md) | 1 <br/> [ResultEnum](ResultEnum.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [vote](vote.md) | range | [Vote](Vote.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:Vote |
| native | chpaf:Vote |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vote
from_schema: https://ch.paf.link/schema/session
slots:
- uid
- question
- result
class_uri: chpaf:Vote

```
</details>

### Induced

<details>
```yaml
name: Vote
from_schema: https://ch.paf.link/schema/session
attributes:
  uid:
    name: uid
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    identifier: true
    alias: uid
    owner: Vote
    domain_of:
    - Session
    - AgendaItem
    - Vote
    range: string
    required: true
  question:
    name: question
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    slot_uri: chpaf:question
    alias: question
    owner: Vote
    domain_of:
    - Vote
    range: string
    required: true
  result:
    name: result
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    slot_uri: chpaf:result
    alias: result
    owner: Vote
    domain_of:
    - Vote
    range: result_enum
    required: true
class_uri: chpaf:Vote

```
</details>