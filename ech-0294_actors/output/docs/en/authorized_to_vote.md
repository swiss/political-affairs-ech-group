---
search:
  boost: 5.0
---

# Slot: authorized_to_vote 


_Indicates if the person is authorized to vote in the group. Typically false for substitute members (when not deputizing), observers, secretaries, and guests._

__



<div data-search-exclude markdown="1">



URI: [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Membership](Membership.md) |
| Slot URI | [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

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
description: 'Indicates if the person is authorized to vote in the group. Typically
  false for substitute members (when not deputizing), observers, secretaries, and
  guests.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:authorizedToVote
domain_of:
- Membership
range: boolean

```
</details></div>