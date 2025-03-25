

# Class: Traktandum



URI: [chpaf:Traktandum](https://ch.paf.link/Traktandum)






```mermaid
 classDiagram
    class Traktandum
    click Traktandum href "../Traktandum"
      Traktandum : abstimmungen
        
          
    
    
    Traktandum --> "*" Abstimmung : abstimmungen
    click Abstimmung href "../Abstimmung"

        
      Traktandum : name
        
      Traktandum : uid
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [uid](uid.md) | 1 <br/> [String](String.md) |  | direct |
| [name](name.md) | 1 <br/> [String](String.md) |  | direct |
| [abstimmungen](abstimmungen.md) | * <br/> [Abstimmung](Abstimmung.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Session](Session.md) | [traktanden](traktanden.md) | range | [Traktandum](Traktandum.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:Traktandum |
| native | chpaf:Traktandum |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Traktandum
from_schema: https://ch.paf.link/schema/session
slots:
- uid
- name
- abstimmungen
class_uri: chpaf:Traktandum

```
</details>

### Induced

<details>
```yaml
name: Traktandum
from_schema: https://ch.paf.link/schema/session
attributes:
  uid:
    name: uid
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    identifier: true
    alias: uid
    owner: Traktandum
    domain_of:
    - Session
    - Traktandum
    - Abstimmung
    range: string
    required: true
  name:
    name: name
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    slot_uri: dcterm:title
    alias: name
    owner: Traktandum
    domain_of:
    - Session
    - Traktandum
    range: string
    required: true
  abstimmungen:
    name: abstimmungen
    from_schema: https://ch.paf.link/schema/session
    rank: 1000
    slot_uri: chpaf:abstimmung
    alias: abstimmungen
    owner: Traktandum
    domain_of:
    - Traktandum
    range: Abstimmung
    multivalued: true
    inlined: true
    inlined_as_list: true
class_uri: chpaf:Traktandum

```
</details>