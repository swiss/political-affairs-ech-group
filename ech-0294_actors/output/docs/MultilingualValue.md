

# Class: MultilingualValue 


_[de] Ein mehrsprachiger String mit Angabe der Sprache._

_[en] A multilingual string with language specification._

__





URI: [act:MultilingualValue](https://ld.ech.ch/schema/0294/actors/MultilingualValue)





```mermaid
 classDiagram
    class MultilingualValue
    click MultilingualValue href "../MultilingualValue/"
      MultilingualValue : language
        
      MultilingualValue : value
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ... | direct |
| [language](language.md) | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |
| [Group](Group.md) | [description](description.md) | range | [MultilingualValue](MultilingualValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:MultilingualValue |
| native | act:MultilingualValue |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MultilingualValue
description: '[de] Ein mehrsprachiger String mit Angabe der Sprache.

  [en] A multilingual string with language specification.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
slots:
- value
- language

```
</details>

### Induced

<details>
```yaml
name: MultilingualValue
description: '[de] Ein mehrsprachiger String mit Angabe der Sprache.

  [en] A multilingual string with language specification.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
attributes:
  value:
    name: value
    description: '[de] Der eigentliche Wert einer Information neben weiteren attributen
      wie Typ, Sprache, etc.

      [en] The value of an information besides other attributes such as type, language,
      etc.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:value
    alias: value
    owner: MultilingualValue
    domain_of:
    - Name
    - Contact
    - MultilingualValue
    range: string
  language:
    name: language
    description: '[de] Sprachcode im ISO 639-1 Format.

      [en] Language code in ISO 639-1 format.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:language
    alias: language
    owner: MultilingualValue
    domain_of:
    - LanguageProficiency
    - MultilingualValue
    range: string
    pattern: ^[a-z]{2}$

```
</details>