---
search:
  boost: 5.0
---

# Slot: authorized_to_vote 


_Indique si la personne dispose du droit de vote au sein du groupe. Généralement false pour les membres suppléants (lorsqu'ils ne remplacent personne), les observateurs, les secrétaires et les invités._

__



<div data-search-exclude markdown="1">



URI: [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Boolean](Boolean.md) |
| Domaine de | [Membership](Membership.md) |
| URI du slot | [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: authorized_to_vote
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Person in der Gruppe stimmberechtigt ist. Typischerweise
      false für Ersatzmitglieder (wenn nicht im Einsatz), Beobachter/innen, Sekretär/innen
      und Gäste.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si la personne dispose du droit de vote au sein du groupe. Généralement
      false pour les membres suppléants (lorsqu''ils ne remplacent personne), les
      observateurs, les secrétaires et les invités.

      '
description: 'Indique si la personne dispose du droit de vote au sein du groupe. Généralement
  false pour les membres suppléants (lorsqu''ils ne remplacent personne), les observateurs,
  les secrétaires et les invités.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:authorizedToVote
domain_of:
- Membership
range: boolean

```
</details></div>