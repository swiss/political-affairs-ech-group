

# Class: ElectoralDistrict 



URI: [act:ElectoralDistrict](https://ch.paf.link/schema/actors/ElectoralDistrict)





```mermaid
 classDiagram
    class ElectoralDistrict
    click ElectoralDistrict href "../ElectoralDistrict/"
      ElectoralDistrict : district
        
      ElectoralDistrict : validFrom
        
      ElectoralDistrict : validUntil
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [district](district.md) | 1 <br/> [String](String.md) |  | direct |
| [validFrom](validFrom.md) | 0..1 <br/> [Date](Date.md) |  | direct |
| [validUntil](validUntil.md) | 0..1 <br/> [Date](Date.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:ElectoralDistrict |
| native | act:ElectoralDistrict |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ElectoralDistrict
from_schema: https://ch.paf.link/schema/actors
attributes:
  district:
    name: district
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - ElectoralDistrict
    required: true
  validFrom:
    name: validFrom
    from_schema: https://ch.paf.link/schema/actors
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  validUntil:
    name: validUntil
    from_schema: https://ch.paf.link/schema/actors
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date

```
</details>

### Induced

<details>
```yaml
name: ElectoralDistrict
from_schema: https://ch.paf.link/schema/actors
attributes:
  district:
    name: district
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: district
    owner: ElectoralDistrict
    domain_of:
    - ElectoralDistrict
    range: string
    required: true
  validFrom:
    name: validFrom
    from_schema: https://ch.paf.link/schema/actors
    alias: validFrom
    owner: ElectoralDistrict
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  validUntil:
    name: validUntil
    from_schema: https://ch.paf.link/schema/actors
    alias: validUntil
    owner: ElectoralDistrict
    domain_of:
    - Name
    - Validity
    - ElectoralDistrict
    range: date

```
</details>