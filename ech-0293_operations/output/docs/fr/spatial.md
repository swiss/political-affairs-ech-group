---
search:
  boost: 5.0
---

# Slot: spatial 


_Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234, district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23, pays : https://ld.admin.ch/country/CHE._




<div data-search-exclude markdown="1">



URI: [ops:spatial](https://ch.paf.link/schema/operations/spatial)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
### Contraintes de valeur

| Propriété | Valeur |
| --- | --- |
| Regex Pattern | `^https://ld\.admin\.ch/(country/[A-Z]{3}|canton/[0-9]+|district/[0-9]+|municipality/[0-9]+)$` |














## Source LinkML

<details>
```yaml
name: spatial
annotations:
  description_de:
    tag: description_de
    value: 'Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer,
      Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234,
      Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23,
      Bund: https://ld.admin.ch/country/CHE.

      '
  description_fr:
    tag: description_fr
    value: 'Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro
      OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234,
      district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23,
      pays : https://ld.admin.ch/country/CHE.

      '
description: 'Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro
  OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234,
  district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23,
  pays : https://ld.admin.ch/country/CHE.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Session
- Meeting
range: string
pattern: ^https://ld\.admin\.ch/(country/[A-Z]{3}|canton/[0-9]+|district/[0-9]+|municipality/[0-9]+)$

```
</details></div>