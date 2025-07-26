

# Class: MultilingualString 



URI: [ops:MultilingualString](https://ch.paf.link/schema/operations/MultilingualString)






```mermaid
 classDiagram
    class MultilingualString
    click MultilingualString href "../MultilingualString"
      MultilingualString : language
        
      MultilingualString : text
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [text](text.md) | 1 <br/> [String](String.md) |  | direct |
| [language](language.md) | 1 <br/> [String](String.md) | Language code in ISO 639-1 format | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Legislature](Legislature.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [Legislature](Legislature.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |
| [Session](Session.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [Session](Session.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |
| [Meeting](Meeting.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [Meeting](Meeting.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |
| [MeetingItem](MeetingItem.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:MultilingualString |
| native | ops:MultilingualString |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MultilingualString
from_schema: https://ch.paf.link/schema/operations
slots:
- text
- language

```
</details>

### Induced

<details>
```yaml
name: MultilingualString
from_schema: https://ch.paf.link/schema/operations
attributes:
  text:
    name: text
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: text
    owner: MultilingualString
    domain_of:
    - MultilingualString
    range: string
    required: true
  language:
    name: language
    description: Language code in ISO 639-1 format
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: language
    owner: MultilingualString
    domain_of:
    - MultilingualString
    range: string
    required: true
    pattern: ^[a-z]{2}$

```
</details>