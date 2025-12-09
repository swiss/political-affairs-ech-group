

# Class: MultilingualString 



URI: [tutorial:MultilingualString](https://ch.paf.link/schema/tutorial/MultilingualString)





```mermaid
 classDiagram
    class MultilingualString
    click MultilingualString href "../MultilingualString/"
      MultilingualString : language
        
      MultilingualString : text
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [text](text.md) | 1 <br/> [String](String.md) |  | direct |
| [language](language.md) | 1 <br/> [String](String.md) | [en] Language code in ISO 639-1 format | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Session](Session.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [AgendaItem](AgendaItem.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:MultilingualString |
| native | tutorial:MultilingualString |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MultilingualString
from_schema: https://ch.paf.link/schema/tutorial
slots:
- text
- language

```
</details>

### Induced

<details>
```yaml
name: MultilingualString
from_schema: https://ch.paf.link/schema/tutorial
attributes:
  text:
    name: text
    from_schema: https://ch.paf.link/schema/tutorial
    rank: 1000
    alias: text
    owner: MultilingualString
    domain_of:
    - MultilingualString
    range: string
    required: true
  language:
    name: language
    description: '[en] Language code in ISO 639-1 format.

      [de] Sprachcode im ISO 639-1-Format.

      '
    from_schema: https://ch.paf.link/schema/tutorial
    rank: 1000
    slot_uri: dcterm:language
    alias: language
    owner: MultilingualString
    domain_of:
    - MultilingualString
    range: string
    required: true
    pattern: ^[a-z]{2}$

```
</details>