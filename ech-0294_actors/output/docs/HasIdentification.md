

# Class: HasIdentification 


_[de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügung stellt._

_[en] A mixin class that provides slots for the identification of an entity._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'local_id',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.\n'
     '[en] Local identifier. For example, a UUID from the council information '
     'system.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:localId',
  'owner': 'HasIdentification',
  'domain_of': ['HasIdentification'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.
[en] Local identifier. For example, a UUID from the council information system.
 | direct |
| SlotDefinition({
  'name': 'global_uri',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Eine eindeutige, global gültige URI für die Entität.\n'
     '[en] A unique, globally valid URI for the entity.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:globalURI',
  'identifier': True,
  'owner': 'HasIdentification',
  'domain_of': ['HasIdentification'],
  'range': 'uriorcurie',
  'required': True
}) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität.
[en] A unique, globally valid URI for the entity.
 | direct |
| SlotDefinition({
  'name': 'wikidata_uri',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. '
     'https://www.wikidata.org/wiki/Q39 für die Schweiz.\n'
     '[en] A URI that refers to a Wikidata entity, e.g. '
     'https://www.wikidata.org/wiki/Q39 for Switzerland.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:wikidataUri',
  'owner': 'HasIdentification',
  'domain_of': ['HasIdentification'],
  'range': 'uriorcurie'
}) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz.
[en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland.
 | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |
| [PersonReference](PersonReference.md) | [de] Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifika... |
| [GroupReference](GroupReference.md) | [de] Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifika... |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:HasIdentification |
| native | act:HasIdentification |







