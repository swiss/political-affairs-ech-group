---
search:
  boost: 5.0
---

# Slot: description 


_Beschreibender Text zum Element._




<div data-search-exclude markdown="1">



URI: [ops:description](https://ch.paf.link/schema/operations/description)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [Motion](Motion.md) | Ein formeller Antrag, der während der Verhandlungen eingereicht wird |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Legislature](Legislature.md), [Meeting](Meeting.md), [Motion](Motion.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: description
annotations:
  description_de:
    tag: description_de
    value: 'Beschreibender Text zum Element.

      '
  description_fr:
    tag: description_fr
    value: 'Texte descriptif de l''élément.

      '
description: 'Beschreibender Text zum Element.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
- Motion
range: string

```
</details></div>