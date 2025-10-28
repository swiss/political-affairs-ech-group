

# Class: Training 



URI: [act:Training](https://ch.paf.link/schema/actors/Training)





```mermaid
 classDiagram
    class Training
    click Training href "../Training/"
      Training : training
        
      Training : training_isco19_code
        
      Training : type
        
          
    
        
        
        Training --> "1" TrainingTypeEnum : type
        click TrainingTypeEnum href "../TrainingTypeEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [TrainingTypeEnum](TrainingTypeEnum.md) |  | direct |
| [training_isco19_code](training_isco19_code.md) | 0..1 <br/> [String](String.md) |  | direct |
| [training](training.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [trainings](trainings.md) | range | [Training](Training.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Training |
| native | act:Training |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Training
from_schema: https://ch.paf.link/schema/actors
attributes:
  type:
    name: type
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Training
    - Contact
    range: TrainingTypeEnum
    required: true
  training_isco19_code:
    name: training_isco19_code
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Training
  training:
    name: training
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Training

```
</details>

### Induced

<details>
```yaml
name: Training
from_schema: https://ch.paf.link/schema/actors
attributes:
  type:
    name: type
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: type
    owner: Training
    domain_of:
    - Training
    - Contact
    range: TrainingTypeEnum
    required: true
  training_isco19_code:
    name: training_isco19_code
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: training_isco19_code
    owner: Training
    domain_of:
    - Training
    range: string
  training:
    name: training
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: training
    owner: Training
    domain_of:
    - Training
    range: string

```
</details>