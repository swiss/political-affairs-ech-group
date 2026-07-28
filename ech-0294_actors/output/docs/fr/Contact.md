

## Classe: Contact 


_Informations de contact d'une personne indiquant un type (p. ex. e-mail, LinkedIn) et une valeur._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| contact_type | 1 <br/> [ContactTypeEnum](ContactTypeEnum.md) | Type d'informations de contact.  |
| value | 1 <br/> [String](String.md) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |
| [Group](Group.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |



















</div>