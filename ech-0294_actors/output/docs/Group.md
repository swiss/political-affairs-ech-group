---
search:
  boost: 10.0
---

# Class: Group 


_[de] Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

_[en] A political group, organization, or body (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [group_type](group_type.md) | 0..1 <br/> [GroupType](GroupType.md) | [de] Klasse der Gruppierung, wie z | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |
| [abbreviation](abbreviation.md) | * <br/> [MultilingualValue](MultilingualValue.md) | [de] Abkürzung (kann mehrsprachig sein) | direct |
| [description](description.md) | * <br/> [MultilingualValue](MultilingualValue.md) | [de] Kurze Beschreibung der Gruppierung | direct |
| [landing_page](landing_page.md) | 0..1 <br/> [Uri](Uri.md) | [de] Website mit weiteren Informationen | direct |
| [parent_groups](parent_groups.md) | * <br/> [Uriorcurie](Uriorcurie.md) | [de] Übergeordneten Gruppe | direct |
| [spatial](spatial.md) | 0..1 <br/> [String](String.md) | [de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z | direct |
| [contacts](contacts.md) | * <br/> [Contact](Contact.md) | [en] Contact information (email, website, social media) | direct |
| [addresses](addresses.md) | * <br/> [Address](Address.md) | [de] Adressen mit Typ (privat, geschäftlich, lokal) | direct |
| [statutes_url](statutes_url.md) | 0..1 <br/> [String](String.md) | [de] URL zu Parteistatuten (optional für Parteien) | direct |
| [party_color](party_color.md) | 0..1 <br/> [String](String.md) | [de] Parteifarbe (optional für Parteien) | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |
| [Membership](Membership.md) | [concerned_group](concerned_group.md) | range | [Group](Group.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Group |
| native | act:Group |







