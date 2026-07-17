# Actors Schema

Ein Schema zur Beschreibung politischer Akteure einschliesslich Personen, Gruppen, Mitgliedschaften und Interessenbindungen.


URI: https://ld.ech.ch/schema/0294/actors

Name: actors-schema



## Klassen

| Klasse | Beschreibung |
| --- | --- |
| [Address](Address.md) | Eine Adresse mit einem Typ (z |
| [Citizenship](Citizenship.md) | Staatsangehörigkeit (wird auch für Nationalität verwendet) einer Person unter... |
| [Contact](Contact.md) | Kontaktinformation einer Person mit Angabe eines Typs (z |
| [Container](Container.md) | Container für politische Akteure, Gruppen und Beziehungen |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitli... |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |
| [GroupType](GroupType.md) | Art der Gruppe (z |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |
| [HasTemporalValidity](HasTemporalValidity.md) | A mixin class that provides slots for modeling a temporal validity of informa... |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | A mixin class that provides slots for modeling instantaneous events or occurr... |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |
| [LanguageProficiency](LanguageProficiency.md) | Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die be... |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |
| [Name](Name.md) | Ein Name mit einem Typ (z |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [RoleType](RoleType.md) | Rolle einer Person in einer Mitgliedschaft oder Funktion (z |
| [Training](Training.md) | Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |



## Slots

| Slot | Beschreibung |
| --- | --- |
| [abbreviation](abbreviation.md) | Abbreviation (can be multilingual) |
| [address_type](address_type.md) | Typ der Adresse |
| [address_uri](address_uri.md) | URI der Adresse aus dem eidgenössischen Gebäudeadressverzeichnis |
| [addresses](addresses.md) | Adressen mit Typ (privat, geschäftlich, lokal) |
| [authorized_to_vote](authorized_to_vote.md) | Gibt an, ob die Person in der Gruppe stimmberechtigt ist |
| [birth_date](birth_date.md) | Genaues Geburtsdatum, sofern verfügbar und öffentlich |
| [birth_year](birth_year.md) | Geburtsjahr |
| [citizenships](citizenships.md) | Staatsbürgerschaften der Person |
| [committee](committee.md) | Gremium innerhalb der Organisation (z |
| [contact_type](contact_type.md) | Typ der Kontaktinformation |
| [contacts](contacts.md) | Kontaktinformationen (E-Mail, Website, Social Media) |
| [country](country.md) | ISO 3166-1 alpha-2 Ländercode |
| [date_actual](date_actual.md) | The actual date of an instantaneous event or occurrence (without time duratio... |
| [date_begin_actual](date_begin_actual.md) | The actual start date of an event or occurrence with time duration |
| [date_begin_planned](date_begin_planned.md) | The planned start date of an event or occurrence with time duration |
| [date_created](date_created.md) | The date when an entity was created |
| [date_end_actual](date_end_actual.md) | The actual end date of an event or occurrence with time duration |
| [date_end_planned](date_end_planned.md) | The planned end date of an event or occurrence with time duration |
| [date_modified](date_modified.md) | The date when an entity was last modified |
| [date_planned](date_planned.md) | The planned date of an instantaneous event or occurrence (without time durati... |
| [datetime_actual](datetime_actual.md) | The actual date and time of an instantaneous event or occurrence (without tim... |
| [datetime_begin_actual](datetime_begin_actual.md) | The actual start date and time of an event or occurrence with time duration |
| [datetime_begin_planned](datetime_begin_planned.md) | The planned start date and time of an event or occurrence with time duration |
| [datetime_created](datetime_created.md) | The date and time when an entity was created |
| [datetime_end_actual](datetime_end_actual.md) | The actual end date and time of an event or occurrence with time duration |
| [datetime_end_planned](datetime_end_planned.md) | The planned end date and time of an event or occurrence with time duration |
| [datetime_modified](datetime_modified.md) | The date and time when an entity was last modified |
| [datetime_planned](datetime_planned.md) | The planned date and time of an instantaneous event or occurrence (without ti... |
| [death_date](death_date.md) | Genaues Todesdatum |
| [description](description.md) | Kurze Beschreibung der Gruppierung |
| [district](district.md) | Wahlkreis oder Wahlregion |
| [electoral_district](electoral_district.md) | Link zum Wahlbezirk |
| [function_role](function_role.md) | Funktion oder Rolle in der Organisation (z |
| [gender_code](gender_code.md) | Geschlechtscode |
| [genders](genders.md) | Geschlecht der Person |
| [global_uri](global_uri.md) | A unique, globally valid URI for the entity |
| [group_label](group_label.md) | Name of the body/group at time of linking |
| [group_reference](group_reference.md) | Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung |
| [group_type](group_type.md) | Klasse der Gruppierung, wie z |
| [group_type_enum](group_type_enum.md) | Link zum kontrollierten Vokabular für Gruppentypen |
| [groups](groups.md) | Sammlung von Gruppen |
| [interest_links](interest_links.md) | Sammlung von Interessenbindungen |
| [interest_type](interest_type.md) | Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein) |
| [is_active](is_active.md) | Indicates whether the information is currently valid |
| [is_correspondence](is_correspondence.md) | Gibt an, ob es sich um die bevorzugte Sprache handelt |
| [is_native](is_native.md) | Gibt an, ob es sich um die Muttersprache handelt |
| [is_paid](is_paid.md) | Gibt an, ob die Position bezahlt ist |
| [label](label.md) | Assign a label to a structured piece of information (e |
| [label_long](label_long.md) | Assign an extended label to a structured piece of information (e |
| [landing_page](landing_page.md) | Website mit weiteren Informationen |
| [language](language.md) | Language code in ISO 639-1 format (two lowercase letters, e |
| [language_proficiencies](language_proficiencies.md) | Sprachkompetenzen der Person |
| [legal_form](legal_form.md) | Rechtsform der Organisation |
| [local_id](local_id.md) | Local identifier |
| [memberships](memberships.md) | Sammlung von Mitgliedschaften |
| [multilingual_value](multilingual_value.md) | A multilingual value with language specification |
| [name_type](name_type.md) | Typ des Namens gemäss eCH-0011 (personNameData) |
| [names](names.md) | Namen der Person mit Typ und Wert |
| [occupation_code](occupation_code.md) | ISCO-19 Code der Tätigkeit |
| [occupations](occupations.md) | Berufe oder Tätigkeiten der Person |
| [organization_address](organization_address.md) | Adresse der Organisation |
| [organization_name](organization_name.md) | Name der Organisation oder des Unternehmens |
| [organization_uid](organization_uid.md) | UID der Organisation (Format eCH-0097: CHE-XXX |
| [parent_groups](parent_groups.md) | Übergeordnete Gruppe |
| [party_color](party_color.md) | Parteifarbe als Hexadezimalwert (optional für Parteien, z |
| [person_reference](person_reference.md) | Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung |
| [persons](persons.md) | Sammlung von Personen |
| [picture](picture.md) | Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF) |
| [postal_code](postal_code.md) | Postleitzahl |
| [postal_locality](postal_locality.md) | Ort |
| [pronouns](pronouns.md) | Von der Person verwendete Pronomen |
| [remark](remark.md) | Free-text remark or note for edge cases or additional context on a process st... |
| [role_label](role_label.md) | Beschreibende Bezeichnung für die Rolle, wenn 'other' im RoleEnum ausgewählt ... |
| [role_type](role_type.md) | Rolle der Person in der Mitgliedschaft oder Funktion |
| [role_type_enum](role_type_enum.md) | Rolle der Person in der Mitgliedschaft oder Funktion |
| [spatial](spatial.md) | Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land) |
| [statutes_url](statutes_url.md) | URL zu Parteistatuten (PDF oder Webseite; optional für Parteien) |
| [street_address](street_address.md) | Strassenadresse |
| [training_code](training_code.md) | ISCO-19 Code der Ausbildung oder Bildung |
| [training_type](training_type.md) | Typ der Ausbildung oder Bildung |
| [trainings](trainings.md) | Ausbildungen oder Bildungen der Person |
| [valid_from](valid_from.md) | The date from which the information is valid |
| [valid_through](valid_through.md) | The date until which the information is valid, inclusive |
| [value](value.md) | The value of an information besides other attributes such as type, language, ... |
| [wikidata_uri](wikidata_uri.md) | A URI that refers to a Wikidata entity, e |


## Enums

| Aufzählung | Beschreibung |
| --- | --- |
| [AddressTypeEnum](AddressTypeEnum.md) | Adresstypen |
| [ContactTypeEnum](ContactTypeEnum.md) | Kontaktinformationstypen |
| [GenderCodeEnum](GenderCodeEnum.md) | Geschlechtscodes für Personen |
| [GroupTypeEnum](GroupTypeEnum.md) | Typen politischer Gruppen und Organisationen |
| [InterestTypeEnum](InterestTypeEnum.md) | Typen von Interessenbindungen (Interessenkonflikte, Politikfinanzierung) |
| [LegalFormEnum](LegalFormEnum.md) | Rechtsformen basierend auf der Codeliste des eidgenössischen UID-Registers (e... |
| [NameTypeEnum](NameTypeEnum.md) | Kategorien von Namenstypen gemäss eCH-0011 (personNameData) und https://dam-a... |
| [RoleEnum](RoleEnum.md) | Rollen, die eine Person im Rahmen einer Mitgliedschaft haben kann |
| [TrainingTypeEnum](TrainingTypeEnum.md) | Ausbildungs- oder Bildungstypen basierend auf der BFS LEVEL_EDUC Codeliste |


## Typen

| Typ | Beschreibung |
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

| Subset | Beschreibung |
| --- | --- |
