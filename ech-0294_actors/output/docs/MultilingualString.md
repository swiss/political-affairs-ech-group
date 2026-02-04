

# Class: MultilingualString 


_[en] A string that can contain text in multiple languages._

_[de] Ein String, der Text in mehreren Sprachen enthalten kann._

__





URI: [act:MultilingualString](https://ch.paf.link/schema/actors/MultilingualString)





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
| [Group](Group.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [Group](Group.md) | [abbreviation](abbreviation.md) | range | [MultilingualString](MultilingualString.md) |
| [Group](Group.md) | [description](description.md) | range | [MultilingualString](MultilingualString.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:MultilingualString |
| native | act:MultilingualString |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MultilingualString
description: '[en] A string that can contain text in multiple languages.

  [de] Ein String, der Text in mehreren Sprachen enthalten kann.

  '
from_schema: https://ch.paf.link/schema/actors
slots:
- text
- language

```
</details>

### Induced

<details>
```yaml
name: MultilingualString
description: '[en] A string that can contain text in multiple languages.

  [de] Ein String, der Text in mehreren Sprachen enthalten kann.

  '
from_schema: https://ch.paf.link/schema/actors
attributes:
  text:
    name: text
    from_schema: https://ch.paf.link/schema/actors
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

      [de] Sprachcode im ISO 639-1 Format.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: language
    owner: MultilingualString
    domain_of:
    - LanguageProficiency
    - MultilingualString
    range: string
    required: true
    pattern: ^[a-z]{2}$

```
</details>