---
search:
  boost: 5.0
---

# Slot: interest_type 


_Art der Interessenbindung, den Kategorien der Offenlegungsregister folgend (berufliche Tätigkeit, Sitz in einem Führungsgremium, Mandat für eine Interessengruppe, Amt in der öffentlichen Hand, Mitgliedschaft)._




<div data-search-exclude markdown="1">



URI: [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [InterestTypeEnum](InterestTypeEnum.md) |
| Domäne von | [InterestLink](InterestLink.md) |
| Slot-URI | [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |









## Beispiele

| Wert |
| --- |
| governing_body |
| interest_group_mandate |
| professional_activity |





## LinkML-Quelle

<details>
```yaml
name: interest_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der Interessenbindung, den Kategorien der Offenlegungsregister folgend
      (berufliche Tätigkeit, Sitz in einem Führungsgremium, Mandat für eine Interessengruppe,
      Amt in der öffentlichen Hand, Mitgliedschaft).

      '
  description_fr:
    tag: description_fr
    value: 'Type de lien d''intérêts, suivant les catégories tenues par les registres
      de publicité (activité professionnelle, siège dans un organe de direction, mandat
      pour un groupe d''intérêts, fonction dans la sphère publique, appartenance).

      '
description: 'Art der Interessenbindung, den Kategorien der Offenlegungsregister folgend
  (berufliche Tätigkeit, Sitz in einem Führungsgremium, Mandat für eine Interessengruppe,
  Amt in der öffentlichen Hand, Mitgliedschaft).

  '
examples:
- value: governing_body
- value: interest_group_mandate
- value: professional_activity
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestType
domain_of:
- InterestLink
range: InterestTypeEnum
required: true

```
</details></div>