

# Slot: text 



URI: [ops:text](https://ch.paf.link/schema/operations/text)
Alias: text

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |  no  |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:text |
| native | ops:text |




## LinkML Source

<details>
```yaml
name: text
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: text
domain_of:
- Speech
- TextSegment
- MultilingualString
range: string
required: true

```
</details>