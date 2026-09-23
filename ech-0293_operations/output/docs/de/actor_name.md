---
search:
  boost: 5.0
---

# Slot: actor_name 


_Name des politischen Organs im Klartext (z.B. Nationalrat), zusätzlich zur Referenz `actor_id`._




<div data-search-exclude markdown="1">



URI: [ops:actor_name](https://ch.paf.link/schema/operations/actor_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: actor_name
annotations:
  description_de:
    tag: description_de
    value: 'Name des politischen Organs im Klartext (z.B. Nationalrat), zusätzlich
      zur Referenz `actor_id`.

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organe politique en clair (p. ex. Conseil national), en complément
      de la référence `actor_id`.

      '
description: 'Name des politischen Organs im Klartext (z.B. Nationalrat), zusätzlich
  zur Referenz `actor_id`.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>