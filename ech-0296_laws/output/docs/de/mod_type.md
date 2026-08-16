---
search:
  boost: 5.0
---

# Slot: mod_type 


_Art der Änderung (@type); die zulässigen Werte sind die von Akoma Ntoso._



<div data-search-exclude markdown="1">



URI: [laws:mod_type](https://ld.ech.ch/schema/0296/laws/mod_type)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TextualMod](TextualMod.md) | Eine Textänderung: der Wortlaut eines anderen Erlasses wird eingefügt, ersetz... |  no  |
| [ForceMod](ForceMod.md) | Eine Änderung der Rechtskraft: ein Erlass oder ein Teil davon tritt in Kraft,... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md)&nbsp;or&nbsp;<br />[ModTypeEnum](ModTypeEnum.md) |
| Domäne von | [TextualMod](TextualMod.md), [ForceMod](ForceMod.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'ModTypeEnum'})
- AnonymousSlotExpression({'range': 'string'})

</details>










## Beispiele

| Wert |
| --- |
| entryIntoForce |
| insertion |
| substitution |





## LinkML-Quelle

<details>
```yaml
name: mod_type
annotations:
  description_de:
    tag: description_de
    value: Art der Änderung (@type); die zulässigen Werte sind die von Akoma Ntoso.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: type
description: Art der Änderung (@type); die zulässigen Werte sind die von Akoma Ntoso.
examples:
- value: entryIntoForce
- value: insertion
- value: substitution
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- TextualMod
- ForceMod
range: string
any_of:
- range: ModTypeEnum
- range: string

```
</details></div>