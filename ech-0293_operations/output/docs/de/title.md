---
search:
  boost: 5.0
---

# Slot: title 


_Titel des Elements._




<div data-search-exclude markdown="1">



URI: [ops:title](https://ch.paf.link/schema/operations/title)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Motion](Motion.md) | Ein formeller Antrag, der während der Verhandlungen eingereicht wird |  no  |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Election](Election.md), [Motion](Motion.md), [Media](Media.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: title
annotations:
  description_de:
    tag: description_de
    value: 'Titel des Elements.

      '
  description_fr:
    tag: description_fr
    value: 'Titre de l''élément.

      '
description: 'Titel des Elements.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Election
- Motion
- Media
range: string

```
</details></div>