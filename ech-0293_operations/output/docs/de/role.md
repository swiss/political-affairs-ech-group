---
search:
  boost: 5.0
---

# Slot: role 


_Rolle der Person (z.B. Kommissionssprecherin oder Kommissionssprecher)._




<div data-search-exclude markdown="1">



URI: [ops:role](https://ch.paf.link/schema/operations/role)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Speech](Speech.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| speaker |





## LinkML-Quelle

<details>
```yaml
name: role
annotations:
  description_de:
    tag: description_de
    value: 'Rolle der Person (z.B. Kommissionssprecherin oder Kommissionssprecher).

      '
  description_fr:
    tag: description_fr
    value: 'Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission).

      '
description: 'Rolle der Person (z.B. Kommissionssprecherin oder Kommissionssprecher).

  '
examples:
- value: speaker
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>