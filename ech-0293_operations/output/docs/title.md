

# Slot: title 



URI: [ops:title](https://ch.paf.link/schema/operations/title)
Alias: title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:title |
| native | ops:title |




## LinkML Source

<details>
```yaml
name: title
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: title
domain_of:
- Election
- Motion
- Media
range: string

```
</details>