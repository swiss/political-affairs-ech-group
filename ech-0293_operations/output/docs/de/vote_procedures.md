---
search:
  boost: 5.0
---

# Slot: vote_procedures 


_Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung._




<div data-search-exclude markdown="1">



URI: [ops:vote_procedures](https://ch.paf.link/schema/operations/vote_procedures)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | Eine Resolution oder Entscheidung zu einem Traktandum, einschliesslich Abstim... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Resolution](Resolution.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: vote_procedures
annotations:
  description_de:
    tag: description_de
    value: 'Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.

      '
  description_fr:
    tag: description_fr
    value: 'Modalités du vote, p. ex. vote secret ou vote ouvert.

      '
description: 'Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>