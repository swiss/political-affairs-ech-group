

## Class: Contact 


_Contact information of a person indicating a type (e.g., email, LinkedIn) and a value._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| contact_type | 1 <br/> [ContactTypeEnum](ContactTypeEnum.md) | Type of contact information.  |
| value | 1 <br/> [String](String.md) | The value of an information besides other attributes such as type, language, etc.  |
| label | 0..1 <br/> [String](String.md) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Person](Person.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |
| [Group](Group.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |



















</div>