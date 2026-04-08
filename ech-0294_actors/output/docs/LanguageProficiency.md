---
search:
  boost: 10.0
---

# Class: LanguageProficiency 


_[de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die bevorzugte Sprache oder die Muttersprache handelt._

_[en] Language proficiency of a person indicating the language and whether it is the preferred language or native language._

__



<div data-search-exclude markdown="1">



URI: [act:LanguageProficiency](https://ld.ech.ch/schema/0294/actors/LanguageProficiency)




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [language](language.md) | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format | direct |
| [is_correspondence](is_correspondence.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob es sich um die bevorzugte Sprache handelt | direct |
| [is_native](is_native.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob es sich um die Muttersprache handelt | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [language_proficiencies](language_proficiencies.md) | range | [LanguageProficiency](LanguageProficiency.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:LanguageProficiency |
| native | act:LanguageProficiency |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LanguageProficiency
description: '[de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es
  sich um die bevorzugte Sprache oder die Muttersprache handelt.

  [en] Language proficiency of a person indicating the language and whether it is
  the preferred language or native language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
slots:
- language
- is_correspondence
- is_native

```
</details>

### Induced

<details>
```yaml
name: LanguageProficiency
description: '[de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es
  sich um die bevorzugte Sprache oder die Muttersprache handelt.

  [en] Language proficiency of a person indicating the language and whether it is
  the preferred language or native language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
attributes:
  language:
    name: language
    description: '[de] Sprachcode im ISO 639-1 Format.

      [en] Language code in ISO 639-1 format.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:language
    alias: language
    owner: LanguageProficiency
    domain_of:
    - LanguageProficiency
    - MultilingualValue
    range: string
    pattern: ^[a-z]{2}$
  is_correspondence:
    name: is_correspondence
    description: '[de] Gibt an, ob es sich um die bevorzugte Sprache handelt.

      [en] Indicates if this is the preferred language.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:isCorrespondence
    alias: is_correspondence
    owner: LanguageProficiency
    domain_of:
    - LanguageProficiency
    range: boolean
  is_native:
    name: is_native
    description: '[de] Gibt an, ob es sich um die Muttersprache handelt.

      [en] Indicates if this is the native language.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:isNative
    alias: is_native
    owner: LanguageProficiency
    domain_of:
    - LanguageProficiency
    range: boolean

```
</details></div>