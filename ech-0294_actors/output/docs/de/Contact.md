

## Klasse: Contact 


_Kontaktinformation einer Person mit Angabe eines Typs (z.B. E-Mail, LinkedIn) und eines Werts._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| contact_type | 0..1 <br/> [ContactTypeEnum](ContactTypeEnum.md) | Typ der Kontaktinformation.  |
| value | 0..1 <br/> [String](String.md) | The value of an information besides other attributes such as type, language, etc.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |
| [Group](Group.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |



















</div>