# Actor Schema

[en] A schema describing political actors including persons, groups, memberships, and interest links.
[de] Ein Schema zur Beschreibung politischer Akteure einschließlich Personen, Gruppen, Mitgliedschaften und Interessenbindungen.


URI: https://ch.paf.link/schema/actors

Name: ActorSchema



## Classes

| Class | Description |
| --- | --- |
| [Address](Address.md) |  |
| [Contact](Contact.md) |  |
| [Container](Container.md) | [en] Root container holding all political actors, groups, and relationships |
| [ElectoralDistrict](ElectoralDistrict.md) |  |
| [Group](Group.md) | [en] A political group, organization, or body (e |
| [GroupReference](GroupReference.md) | Reference to a group acting in a specific role |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |
| [LanguageProficiency](LanguageProficiency.md) |  |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |
| [Name](Name.md) |  |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |
| [PersonReference](PersonReference.md) | Reference to a person acting in a specific role or function |
| [Training](Training.md) |  |
| [Validity](Validity.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Citizenship](Citizenship.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gender](Gender.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Occupation](Occupation.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) | [en] Abbreviation (can be multilingual) |
| [active](active.md) |  |
| [address_type](address_type.md) |  |
| [address_URI](address_URI.md) | Preferred URI of address |
| [addresses](addresses.md) | [en] Addresses (private, business, local) |
| [authorized_to_vote](authorized_to_vote.md) | [en] Indicates if the person is authorized to vote |
| [birthdate](birthdate.md) | [en] Exact date of birth |
| [birthyear](birthyear.md) | [en] Year of birth |
| [ch_citizenship](ch_citizenship.md) |  |
| [citizenships](citizenships.md) |  |
| [committee](committee.md) | [en] Committee or board (e |
| [contacts](contacts.md) | [en] Contact information (email, website, social media) |
| [correspondence](correspondence.md) | preferred language |
| [country](country.md) | ISO 3166 country code (can't be CH) |
| [datetime_created](datetime_created.md) | [en] The time this record was created |
| [datetime_updated](datetime_updated.md) | [en] The last time this record was updated |
| [description](description.md) | [en] Description of the entity |
| [district](district.md) |  |
| [electoral_district](electoral_district.md) |  |
| [enterprise](enterprise.md) |  |
| [enterprise_uid](enterprise_uid.md) |  |
| [function](function.md) | Function of the person (e |
| [function_role](function_role.md) | [en] Function or role in the organization |
| [genders](genders.md) |  |
| [group](group.md) | Group or body the function applies to |
| [group_id](group_id.md) | [en] Reference to a group ID |
| [group_type](group_type.md) | [en] Type of group (e |
| [groups](groups.md) | [en] Collection of groups |
| [id](id.md) | [en] Unique identifier (preferably Wikidata-ID or URI) |
| [interest_links](interest_links.md) | [en] Collection of interest links |
| [interest_links_person](interest_links_person.md) | [en] Interest links of the person |
| [interest_type](interest_type.md) | [en] Type of interest link (professional activity, political office, associat... |
| [is_active](is_active.md) | [en] Indicates if the membership is currently active |
| [label](label.md) | [en] Display name of the person |
| [label_long](label_long.md) | [en] Extended display name (with title, etc |
| [landing_page](landing_page.md) | [en] URL providing further information |
| [language](language.md) | [en] Language code in ISO 639-1 format |
| [languages](languages.md) |  |
| [legal_form](legal_form.md) | [en] Legal form of the organization |
| [memberships](memberships.md) | [en] Collection of memberships |
| [name](name.md) | [en] Name (can be multilingual) |
| [name_type](name_type.md) | categories of name types |
| [names](names.md) |  |
| [native](native.md) | proficient language |
| [occupation_isco19_code](occupation_isco19_code.md) |  |
| [occupations](occupations.md) |  |
| [organization_address](organization_address.md) | [en] Address of the organization |
| [organization_label](organization_label.md) | [en] Label of the organization |
| [organization_uid](organization_uid.md) | [en] UID of the organization (for analysis with NOGA codes, etc |
| [paid](paid.md) | [en] Indicates if the position is paid |
| [parent_groups](parent_groups.md) | [en] Parent group IDs (to model party hierarchy or bind parties to parliament... |
| [party_color](party_color.md) | [en] Party color (optional for parties) |
| [person_id](person_id.md) | [en] Reference to a person ID |
| [persons](persons.md) | [en] Collection of persons |
| [picture](picture.md) | [en] Link to an image (preferred: PNG, then JPG, then GIF) |
| [postal_code](postal_code.md) |  |
| [postal_locality](postal_locality.md) |  |
| [pronouns](pronouns.md) | Pronouns used by the person |
| [role](role.md) | [en] Role of the person in the membership or function |
| [spatial](spatial.md) | [en] Spatial reference (municipality number, canton number, e |
| [street_address](street_address.md) |  |
| [text](text.md) |  |
| [training_isco19_code](training_isco19_code.md) |  |
| [trainings](trainings.md) |  |
| [type](type.md) |  |
| [type_label](type_label.md) | [en] Custom type label when standard type values don't apply |
| [uri](uri.md) | [en] Globally valid identifier (e |
| [url_statutes](url_statutes.md) | [en] URL to party statutes (optional for parties) |
| [valid_from](valid_from.md) | [en] Start date of validity period |
| [valid_until](valid_until.md) | [en] End date of validity period |
| [value](value.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AddressTypeEnum](AddressTypeEnum.md) | [en] Types of addresses |
| [ContactTypeEnum](ContactTypeEnum.md) | [en] Types of contact information |
| [GroupTypeEnum](GroupTypeEnum.md) | [en] Types of political groups and organizations |
| [InterestTypeEnum](InterestTypeEnum.md) | [en] Types of interest links (conflicts of interest, political financing) |
| [NameTypeEnum](NameTypeEnum.md) | [en] Categories of name types |
| [TrainingTypeEnum](TrainingTypeEnum.md) | [en] Types of training or education |


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
