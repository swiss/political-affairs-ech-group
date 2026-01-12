

# Class: Person 


_A person with identifiers, names, addresses, citizenships, and occupations._





URI: [act:Person](https://ch.paf.link/schema/actors/Person)





```mermaid
 classDiagram
    class Person
    click Person href "../Person/"
      Person : addresses
        
          
    
        
        
        Person --> "*" Address : addresses
        click Address href "../Address/"
    

        
      Person : birthdate
        
      Person : birthyear
        
      Person : ch_citizenship
        
          
    
        
        
        Person --> "0..1" Validity : ch_citizenship
        click Validity href "../Validity/"
    

        
      Person : citizenships
        
          
    
        
        
        Person --> "*" Citizenship : citizenships
        click Citizenship href "../Citizenship/"
    

        
      Person : contacts
        
          
    
        
        
        Person --> "*" Contact : contacts
        click Contact href "../Contact/"
    

        
      Person : electoral_district
        
          
    
        
        
        Person --> "0..1" ElectoralDistrict : electoral_district
        click ElectoralDistrict href "../ElectoralDistrict/"
    

        
      Person : genders
        
          
    
        
        
        Person --> "*" Gender : genders
        click Gender href "../Gender/"
    

        
      Person : id
        
      Person : label
        
      Person : label_long
        
      Person : languages
        
          
    
        
        
        Person --> "*" LanguageProficiency : languages
        click LanguageProficiency href "../LanguageProficiency/"
    

        
      Person : names
        
          
    
        
        
        Person --> "*" Name : names
        click Name href "../Name/"
    

        
      Person : occupations
        
          
    
        
        
        Person --> "*" Occupation : occupations
        click Occupation href "../Occupation/"
    

        
      Person : picture
        
      Person : trainings
        
          
    
        
        
        Person --> "*" Training : trainings
        click Training href "../Training/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | Wikidata-ID preferred | direct |
| [label](label.md) | 1 <br/> [String](String.md) | Display name of the person | direct |
| [label_long](label_long.md) | 0..1 <br/> [String](String.md) | Extended display name (with title, etc | direct |
| [birthyear](birthyear.md) | 0..1 <br/> [Integer](Integer.md) | Year of birth | direct |
| [birthdate](birthdate.md) | 0..1 <br/> [Date](Date.md) | Exact date of birth | direct |
| [picture](picture.md) | 0..1 <br/> [String](String.md) | Link to an image (preferred: PNG, then JPG, then GIF) | direct |
| [names](names.md) | * <br/> [Name](Name.md) |  | direct |
| [addresses](addresses.md) | * <br/> [Address](Address.md) | place of residence and work | direct |
| [languages](languages.md) | * <br/> [LanguageProficiency](LanguageProficiency.md) |  | direct |
| [ch_citizenship](ch_citizenship.md) | 0..1 <br/> [Validity](Validity.md) |  | direct |
| [citizenships](citizenships.md) | * <br/> [Citizenship](Citizenship.md) |  | direct |
| [genders](genders.md) | * <br/> [Gender](Gender.md) |  | direct |
| [occupations](occupations.md) | * <br/> [Occupation](Occupation.md) |  | direct |
| [trainings](trainings.md) | * <br/> [Training](Training.md) |  | direct |
| [contacts](contacts.md) | * <br/> [Contact](Contact.md) |  | direct |
| [electoral_district](electoral_district.md) | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) |  | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Person |
| native | act:Person |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Person
description: A person with identifiers, names, addresses, citizenships, and occupations.
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    description: Wikidata-ID preferred
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    identifier: true
    domain_of:
    - Person
    - PersonReference
    - GroupReference
    required: true
  label:
    name: label
    description: Display name of the person
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Person
    required: true
  label_long:
    name: label_long
    description: Extended display name (with title, etc.)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Person
  birthyear:
    name: birthyear
    description: Year of birth
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Person
    range: integer
  birthdate:
    name: birthdate
    description: Exact date of birth
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Person
    range: date
  picture:
    name: picture
    description: 'Link to an image (preferred: PNG, then JPG, then GIF)'
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Person
  names:
    name: names
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:name
    domain_of:
    - Person
    range: Name
    multivalued: true
    inlined: true
    inlined_as_list: true
  addresses:
    name: addresses
    description: place of residence and work
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:address
    domain_of:
    - Person
    range: Address
    multivalued: true
    inlined: true
    inlined_as_list: true
  languages:
    name: languages
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:language
    domain_of:
    - Person
    range: LanguageProficiency
    multivalued: true
    inlined: true
    inlined_as_list: true
  ch_citizenship:
    name: ch_citizenship
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:chCitizenship
    domain_of:
    - Person
    range: Validity
  citizenships:
    name: citizenships
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:citizenship
    domain_of:
    - Person
    range: Citizenship
    multivalued: true
    inlined: true
    inlined_as_list: true
  genders:
    name: genders
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:gender
    domain_of:
    - Person
    range: Gender
    multivalued: true
    inlined: true
    inlined_as_list: true
  occupations:
    name: occupations
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:occupation
    domain_of:
    - Person
    range: Occupation
    multivalued: true
    inlined: true
    inlined_as_list: true
  trainings:
    name: trainings
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:training
    domain_of:
    - Person
    range: Training
    multivalued: true
    inlined: true
    inlined_as_list: true
  contacts:
    name: contacts
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:contact
    domain_of:
    - Person
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  electoral_district:
    name: electoral_district
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:electoralDistrict
    domain_of:
    - Person
    range: ElectoralDistrict
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Person
description: A person with identifiers, names, addresses, citizenships, and occupations.
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    description: Wikidata-ID preferred
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    identifier: true
    alias: id
    owner: Person
    domain_of:
    - Person
    - PersonReference
    - GroupReference
    range: string
    required: true
  label:
    name: label
    description: Display name of the person
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: label
    owner: Person
    domain_of:
    - Person
    range: string
    required: true
  label_long:
    name: label_long
    description: Extended display name (with title, etc.)
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: label_long
    owner: Person
    domain_of:
    - Person
    range: string
  birthyear:
    name: birthyear
    description: Year of birth
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: birthyear
    owner: Person
    domain_of:
    - Person
    range: integer
  birthdate:
    name: birthdate
    description: Exact date of birth
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: birthdate
    owner: Person
    domain_of:
    - Person
    range: date
  picture:
    name: picture
    description: 'Link to an image (preferred: PNG, then JPG, then GIF)'
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: picture
    owner: Person
    domain_of:
    - Person
    range: string
  names:
    name: names
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:name
    alias: names
    owner: Person
    domain_of:
    - Person
    range: Name
    multivalued: true
    inlined_as_list: true
  addresses:
    name: addresses
    description: place of residence and work
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:address
    alias: addresses
    owner: Person
    domain_of:
    - Person
    range: Address
    multivalued: true
    inlined_as_list: true
  languages:
    name: languages
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:language
    alias: languages
    owner: Person
    domain_of:
    - Person
    range: LanguageProficiency
    multivalued: true
    inlined_as_list: true
  ch_citizenship:
    name: ch_citizenship
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:chCitizenship
    alias: ch_citizenship
    owner: Person
    domain_of:
    - Person
    range: Validity
  citizenships:
    name: citizenships
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:citizenship
    alias: citizenships
    owner: Person
    domain_of:
    - Person
    range: Citizenship
    multivalued: true
    inlined_as_list: true
  genders:
    name: genders
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:gender
    alias: genders
    owner: Person
    domain_of:
    - Person
    range: Gender
    multivalued: true
    inlined_as_list: true
  occupations:
    name: occupations
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:occupation
    alias: occupations
    owner: Person
    domain_of:
    - Person
    range: Occupation
    multivalued: true
    inlined_as_list: true
  trainings:
    name: trainings
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:training
    alias: trainings
    owner: Person
    domain_of:
    - Person
    range: Training
    multivalued: true
    inlined_as_list: true
  contacts:
    name: contacts
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:contact
    alias: contacts
    owner: Person
    domain_of:
    - Person
    range: Contact
    multivalued: true
    inlined_as_list: true
  electoral_district:
    name: electoral_district
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:electoralDistrict
    alias: electoral_district
    owner: Person
    domain_of:
    - Person
    range: ElectoralDistrict
tree_root: true

```
</details>