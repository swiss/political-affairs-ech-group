

# Slot: media_type 


_Type of media (audio, video, document)_





URI: [ops:media_type](https://ch.paf.link/schema/operations/media_type)
Alias: media_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:media_type |
| native | ops:media_type |




## LinkML Source

<details>
```yaml
name: media_type
description: Type of media (audio, video, document)
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: media_type
domain_of:
- Speech
- Media
range: string

```
</details>