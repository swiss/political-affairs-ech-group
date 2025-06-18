

# Class: Vote 



URI: [chpaf:Vote](https://ch.paf.link/Vote)






```mermaid
 classDiagram
    class Vote
    click Vote href "../Vote"
      Vote : id
        
      Vote : question
        
      Vote : result
        
          
    
        
        
        Vote --> "1" ResultEnum : result
        click ResultEnum href "../ResultEnum"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [question](question.md) | 1 <br/> [String](String.md) |  | direct |
| [result](result.md) | 1 <br/> [ResultEnum](ResultEnum.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [votes](votes.md) | range | [Vote](Vote.md) |






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
- id
- question
- result

```
</details>

### Induced

<details>
```yaml
name: Vote
from_schema: https://ch.paf.link/schema/session
attributes:
  id:
    name: id
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    identifier: true
    alias: id
    owner: Vote
    domain_of:
    - Session
    - AgendaItem
    - Vote
    - Container
    range: string
    required: true
  question:
    name: question
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
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
    alias: result
    owner: Vote
    domain_of:
    - Vote
    range: result_enum
    required: true

```
</details>