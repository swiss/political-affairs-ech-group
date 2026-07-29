---
search:
  boost: 5.0
---

# Slot: administrative_id 


_Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land._




<div data-search-exclude markdown="1">



URI: [ops:administrative_id](https://ch.paf.link/schema/operations/administrative_id)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Legislature](Legislature.md), [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: administrative_id
annotations:
  description_de:
    tag: description_de
    value: 'Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder
      Land.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant administratif du corps législatif, p. ex. commune, canton
      ou pays.

      '
description: 'Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton
  oder Land.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
range: string

```
</details></div>