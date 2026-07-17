---
search:
  boost: 5.0
---

# Slot: language 


_Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en")._

__



<div data-search-exclude markdown="1">



URI: [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [LanguageProficiency](LanguageProficiency.md) | Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die be... |  no  |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [LanguageProficiency](LanguageProficiency.md), [MultilingualValue](MultilingualValue.md) |
| Slot-URI | [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
### Wertebeschränkungen

| Eigenschaft | Wert |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |














## LinkML-Quelle

<details>
```yaml
name: language
annotations:
  description_de:
    tag: description_de
    value: 'Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr",
      "it", "en").

      '
description: 'Language code in ISO 639-1 format (two lowercase letters, e.g. "de",
  "fr", "it", "en").

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:language
domain_of:
- LanguageProficiency
- MultilingualValue
range: string
pattern: ^[a-z]{2}$

```
</details></div>