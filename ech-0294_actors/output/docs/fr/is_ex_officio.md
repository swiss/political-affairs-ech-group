---
search:
  boost: 5.0
---

# Slot: is_ex_officio 


_Indique si la personne exerce le mandat pour le compte de la collectivité à laquelle elle appartient — donc en tant que représentante de celle-ci et non à titre privé. L'indication est indépendante du type de lien d'intérêts et se combine avec chacun d'eux : un même siège au conseil d'administration n'a pas la même portée selon que la commune y délègue une personne ou que celle-ci l'occupe à titre privé. Sont concernées avant tout les fonctions exécutives, car la représentation dans les organes des organisations concernées y va généralement de pair avec le dicastère._




<div data-search-exclude markdown="1">



URI: [act:isExOfficio](https://ld.ech.ch/schema/0294/actors/isExOfficio)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Boolean](Boolean.md) |
| Domaine de | [InterestLink](InterestLink.md) |
| URI du slot | [act:isExOfficio](https://ld.ech.ch/schema/0294/actors/isExOfficio) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: is_ex_officio
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Person das Mandat im Auftrag des Gemeinwesens wahrnimmt,
      dem sie angehört — also als dessen Vertretung und nicht privat. Die Angabe ist
      unabhängig vom Typ der Interessenbindung und lässt sich mit jedem Wert kombinieren:
      Derselbe Verwaltungsratssitz ist etwas anderes, wenn die Gemeinde jemanden dorthin
      delegiert, als wenn er privat gehalten wird. Betroffen sind vor allem Exekutivämter,
      weil die Vertretung in den Organen beteiligter Organisationen dort in der Regel
      mit dem Ressort einhergeht.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si la personne exerce le mandat pour le compte de la collectivité
      à laquelle elle appartient — donc en tant que représentante de celle-ci et non
      à titre privé. L''indication est indépendante du type de lien d''intérêts et
      se combine avec chacun d''eux : un même siège au conseil d''administration n''a
      pas la même portée selon que la commune y délègue une personne ou que celle-ci
      l''occupe à titre privé. Sont concernées avant tout les fonctions exécutives,
      car la représentation dans les organes des organisations concernées y va généralement
      de pair avec le dicastère.

      '
description: 'Indique si la personne exerce le mandat pour le compte de la collectivité
  à laquelle elle appartient — donc en tant que représentante de celle-ci et non à
  titre privé. L''indication est indépendante du type de lien d''intérêts et se combine
  avec chacun d''eux : un même siège au conseil d''administration n''a pas la même
  portée selon que la commune y délègue une personne ou que celle-ci l''occupe à titre
  privé. Sont concernées avant tout les fonctions exécutives, car la représentation
  dans les organes des organisations concernées y va généralement de pair avec le
  dicastère.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isExOfficio
domain_of:
- InterestLink
range: boolean

```
</details></div>