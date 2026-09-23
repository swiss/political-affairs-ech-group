---
search:
  boost: 5.0
---

# Slot: vote_procedures 


_Verfahren, in denen abgestimmt wurde. Offene Verfahren: Handzeichen, Aufstehen, elektronische Abstimmung, Namensaufruf, in Krisenlagen zudem externe Stimmabgabe (vorgängig dem Präsidium mitgeteilte Stimmen, die zusammen mit der Abstimmung im Rat erfasst werden), Zirkulationsverfahren oder Stimmabgabe an virtuellen Sitzungen. Geheime Verfahren: Stimmzettel, elektronische geheime Abstimmung. Das Verfahren bestimmt, ob Einzelstimmen erfasst werden können._




<div data-search-exclude markdown="1">



URI: [ops:vote_procedures](https://ch.paf.link/schema/operations/vote_procedures)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | Der formale Beschluss zu einem Traktandum, einschliesslich der angewandten Ab... |  no  |






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
    value: 'Verfahren, in denen abgestimmt wurde. Offene Verfahren: Handzeichen, Aufstehen,
      elektronische Abstimmung, Namensaufruf, in Krisenlagen zudem externe Stimmabgabe
      (vorgängig dem Präsidium mitgeteilte Stimmen, die zusammen mit der Abstimmung
      im Rat erfasst werden), Zirkulationsverfahren oder Stimmabgabe an virtuellen
      Sitzungen. Geheime Verfahren: Stimmzettel, elektronische geheime Abstimmung.
      Das Verfahren bestimmt, ob Einzelstimmen erfasst werden können.

      '
  description_fr:
    tag: description_fr
    value: 'Procédures selon lesquelles le vote a eu lieu. Procédures ouvertes : main
      levée, assis-debout, vote électronique, appel nominal et, en situation de crise,
      vote à distance (voix communiquées à l''avance à la présidence et saisies en
      même temps que le vote au conseil), procédure par voie de circulation ou vote
      lors de séances virtuelles. Procédures secrètes : bulletin de vote, vote électronique
      secret. La procédure détermine si les voix individuelles peuvent être saisies.

      '
description: 'Verfahren, in denen abgestimmt wurde. Offene Verfahren: Handzeichen,
  Aufstehen, elektronische Abstimmung, Namensaufruf, in Krisenlagen zudem externe
  Stimmabgabe (vorgängig dem Präsidium mitgeteilte Stimmen, die zusammen mit der Abstimmung
  im Rat erfasst werden), Zirkulationsverfahren oder Stimmabgabe an virtuellen Sitzungen.
  Geheime Verfahren: Stimmzettel, elektronische geheime Abstimmung. Das Verfahren
  bestimmt, ob Einzelstimmen erfasst werden können.

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