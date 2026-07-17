---
search:
  boost: 5.0
---

# Slot: authorized_to_vote 


_Gibt an, ob die Person in der Gruppe stimmberechtigt ist. Typischerweise false für Ersatzmitglieder (wenn nicht im Einsatz), Beobachter/innen, Sekretär/innen und Gäste._

__



<div data-search-exclude markdown="1">



URI: [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Boolean](Boolean.md) |
| Domäne von | [Membership](Membership.md) |
| Slot-URI | [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Gibt an, ob die Person in der Gruppe stimmberechtigt ist. Typischerweise
  false für Ersatzmitglieder (wenn nicht im Einsatz), Beobachter/innen, Sekretär/innen
  und Gäste.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:authorizedToVote
domain_of:
- Membership
range: boolean

```
</details></div>