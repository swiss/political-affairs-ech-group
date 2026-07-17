---
search:
  boost: 5.0
---

# Slot: language 


_Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »)._

__



<div data-search-exclude markdown="1">



URI: [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [LanguageProficiency](LanguageProficiency.md) | Compétences linguistiques d'une personne indiquant la langue et le fait qu'il... |  no  |
| [MultilingualValue](MultilingualValue.md) | Une chaîne de caractères multilingue avec indication de la langue |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [LanguageProficiency](LanguageProficiency.md), [MultilingualValue](MultilingualValue.md) |
| URI du slot | [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
### Contraintes de valeur

| Propriété | Valeur |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |














## Source LinkML

<details>
```yaml
name: language
annotations:
  description_de:
    tag: description_de
    value: 'Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr",
      "it", "en").

      '
  description_fr:
    tag: description_fr
    value: 'Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. «
      de », « fr », « it », « en »).

      '
description: 'Code de langue au format ISO 639-1 (deux lettres minuscules, par ex.
  « de », « fr », « it », « en »).

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