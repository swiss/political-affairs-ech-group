

## Klasse: GroupReference 


_Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Die referenzierte Gruppe wird über `local_id` oder `global_uri` bezeichnet; mindestens eines von beiden ist erforderlich. Eine `local_id` wird innerhalb derselben Lieferung aufgelöst, eine `global_uri` auch darüber hinaus._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator der referenzierten Entität. Er wird innerhalb derselben Lieferung aufgelöst. <br/><br/>Vererbung: [HasReferenceIdentification](HasReferenceIdentification.md) |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Die eindeutige, global gültige URI der referenzierten Entität. Im Unterschied zu einer local_id ist sie auch über die Lieferung hinaus auflösbar. <br/><br/>Vererbung: [HasReferenceIdentification](HasReferenceIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasReferenceIdentification](HasReferenceIdentification.md) |
| label | 0..1 <br/> [String](String.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abkürzung (kann mehrsprachig sein).  |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [local_id](local_id.md)
- [global_uri](global_uri.md)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [parent_groups](parent_groups.md) | range | [GroupReference](GroupReference.md) |
| [Membership](Membership.md) | [group_reference](group_reference.md) | range | [GroupReference](GroupReference.md) |



















</div>