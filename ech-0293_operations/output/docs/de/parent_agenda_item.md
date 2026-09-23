---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem Traktandum bildet er eine Hierarchie von Traktanden — z.B. eine Traktandengruppe „Gesetzesberatungen“ mit den Untertraktanden „Energiegesetz (Detailberatung)“ und „Energiegesetz (Schlussabstimmung)“; bei einer Wortmeldung bezeichnet er das Traktandum, unter dem sie erfolgte._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [IsAgendaItem](IsAgendaItem.md), [Speech](Speech.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: parent_agenda_item
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem
      Traktandum bildet er eine Hierarchie von Traktanden — z.B. eine Traktandengruppe
      „Gesetzesberatungen“ mit den Untertraktanden „Energiegesetz (Detailberatung)“
      und „Energiegesetz (Schlussabstimmung)“; bei einer Wortmeldung bezeichnet er
      das Traktandum, unter dem sie erfolgte.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant du point de l''ordre du jour auquel cet enregistrement se
      rattache. Pour un point de l''ordre du jour, il forme une hiérarchie de points
      — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi
      sur l''énergie (discussion par article) » et « Loi sur l''énergie (vote final)
      » ; pour une intervention, il désigne le point sous lequel elle a été faite.

      '
description: 'Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem
  Traktandum bildet er eine Hierarchie von Traktanden — z.B. eine Traktandengruppe
  „Gesetzesberatungen“ mit den Untertraktanden „Energiegesetz (Detailberatung)“ und
  „Energiegesetz (Schlussabstimmung)“; bei einer Wortmeldung bezeichnet er das Traktandum,
  unter dem sie erfolgte.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
- Speech
range: string

```
</details></div>