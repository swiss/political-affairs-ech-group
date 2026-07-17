---
search:
  boost: 5.0
---

# Slot: value 


_The value of an information besides other attributes such as type, language, etc._

__



<div data-search-exclude markdown="1">



URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Name](Name.md) | Ein Name mit einem Typ (z |  no  |
| [Training](Training.md) | Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |  no  |
| [Contact](Contact.md) | Kontaktinformation einer Person mit Angabe eines Typs (z |  no  |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Name](Name.md), [Training](Training.md), [Contact](Contact.md), [MultilingualValue](MultilingualValue.md) |
| Slot-URI | [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: value
annotations:
  description_de:
    tag: description_de
    value: 'Der eigentliche Wert einer Information neben weiteren attributen wie Typ,
      Sprache, etc.

      '
description: 'The value of an information besides other attributes such as type, language,
  etc.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:value
domain_of:
- Name
- Training
- Contact
- MultilingualValue
range: string

```
</details></div>