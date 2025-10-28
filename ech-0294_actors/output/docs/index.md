# Person Schema

A schema describing a person with addresses, names, languages, citizenships, occupations, training, and contact details.

URI: https://ch.paf.link/schema/actors

Name: PersonSchema



## Classes

| Class | Description |
| --- | --- |
| [Address](Address.md) |  |
| [Contact](Contact.md) |  |
| [ElectoralDistrict](ElectoralDistrict.md) |  |
| [LanguageProficiency](LanguageProficiency.md) |  |
| [Name](Name.md) |  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |
| [Training](Training.md) |  |
| [Validity](Validity.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Citizenship](Citizenship.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gender](Gender.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Occupation](Occupation.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [active](active.md) |  |
| [address_type](address_type.md) |  |
| [address_URI](address_URI.md) | Preferred URI of address |
| [addresses](addresses.md) | place of residence and work |
| [birthdate](birthdate.md) | Exact date of birth |
| [birthyear](birthyear.md) | Year of birth |
| [ch_citizenship](ch_citizenship.md) |  |
| [citizenships](citizenships.md) |  |
| [contacts](contacts.md) |  |
| [correspondence](correspondence.md) | preferred language |
| [country](country.md) | ISO 3166 country code (can't be CH) |
| [district](district.md) |  |
| [electoral_district](electoral_district.md) |  |
| [enterprise](enterprise.md) |  |
| [enterprise_uid](enterprise_uid.md) |  |
| [genders](genders.md) |  |
| [id](id.md) | Wikidata-ID preferred |
| [label](label.md) | Display name of the person |
| [label_long](label_long.md) | Extended display name (with title, etc |
| [language](language.md) | ISO language code |
| [languages](languages.md) |  |
| [name_type](name_type.md) | categories of name types |
| [names](names.md) |  |
| [native](native.md) | proficient language |
| [occupation_isco19_code](occupation_isco19_code.md) |  |
| [occupations](occupations.md) |  |
| [paid](paid.md) |  |
| [picture](picture.md) | Link to an image (preferred: PNG, then JPG, then GIF) |
| [postal_code](postal_code.md) |  |
| [postal_locality](postal_locality.md) |  |
| [pronouns](pronouns.md) | Pronouns used by the person |
| [street_address](street_address.md) |  |
| [training_isco19_code](training_isco19_code.md) |  |
| [trainings](trainings.md) |  |
| [type](type.md) |  |
| [valid_until](valid_until.md) |  |
| [valid_from](valid_from.md) |  |
| [valid_until](valid_until.md) |  |
| [value](value.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AddressTypeEnum](AddressTypeEnum.md) |  |
| [ContactTypeEnum](ContactTypeEnum.md) |  |
| [NameTypeEnum](NameTypeEnum.md) |  |
| [TrainingTypeEnum](TrainingTypeEnum.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
