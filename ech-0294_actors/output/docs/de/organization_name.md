---
search:
  boost: 5.0
---

# Slot: organization_name 


_Name der Organisation oder des Unternehmens mit der Sprache, in der er publiziert wird. Zweisprachige Register führen den Namen in beiden Sprachen; erfasst wird pro Sprache ein Eintrag._




<div data-search-exclude markdown="1">



URI: [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualValue](MultilingualValue.md) |
| Domäne von | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot-URI | [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: organization_name
annotations:
  description_de:
    tag: description_de
    value: 'Name der Organisation oder des Unternehmens mit der Sprache, in der er
      publiziert wird. Zweisprachige Register führen den Namen in beiden Sprachen;
      erfasst wird pro Sprache ein Eintrag.

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organisation ou de l''entreprise, avec la langue dans laquelle
      il est publié. Les registres bilingues indiquent le nom dans les deux langues
      ; une entrée est saisie par langue.

      '
description: 'Name der Organisation oder des Unternehmens mit der Sprache, in der
  er publiziert wird. Zweisprachige Register führen den Namen in beiden Sprachen;
  erfasst wird pro Sprache ein Eintrag.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationName
domain_of:
- InterestLink
- Occupation
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>