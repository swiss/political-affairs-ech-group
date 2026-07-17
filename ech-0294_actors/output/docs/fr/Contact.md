

## Classe: Contact 


_Contact information of a person indicating a type (e.g., email, LinkedIn) and a value._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| contact_type | 0..1 <br/> [ContactTypeEnum](ContactTypeEnum.md) | Type of contact information.  |
| value | 0..1 <br/> [String](String.md) | The value of an information besides other attributes such as type, language, etc.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |
| [Group](Group.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |



















</div>