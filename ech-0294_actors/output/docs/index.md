# Actors Schema

[de] Ein Schema zur Beschreibung politischer Akteure einschliesslich Personen, Gruppen, Mitgliedschaften und Interessenbindungen.
[en] A schema describing political actors including persons, groups, memberships, and interest links.


URI: https://ld.ech.ch/schema/0294/actors

Name: actors-schema



## Classes

| Class | Description |
| --- | --- |
| [Address](Address.md) | [de] Eine Adresse mit einem Typ (z |
| [Citizenship](Citizenship.md) | [de] Staatsangehörigkeit einer Person unter Angabe des Landes und der zeitlic... |
| [Contact](Contact.md) | [de] Kontaktinformation einer Person mit Angabe eines Typs (z |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |
| [ElectoralDistrict](ElectoralDistrict.md) | [de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit z... |
| [Gender](Gender.md) | [de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitli... |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |
| [GroupType](GroupType.md) | [de] Art der Gruppe (z |
| [HasCreationModificationDates](HasCreationModificationDates.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Ä... |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |
| [HasTemporalValidity](HasTemporalValidity.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gülti... |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereign... |
| [LanguageProficiency](LanguageProficiency.md) | [de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um d... |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |
| [MultilingualValue](MultilingualValue.md) | [de] Ein mehrsprachiger String mit Angabe der Sprache |
| [Name](Name.md) | [de] Ein Name mit einem Typ (z |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |
| [RoleType](RoleType.md) | [de] Rolle einer Person in einer Mitgliedschaft oder Funktion (z |
| [Training](Training.md) | [de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) | [de] Abkürzung (kann mehrsprachig sein) |
| [address_type](address_type.md) | [de] Typ der Adresse |
| [address_uri](address_uri.md) | [de] URI der Adresse |
| [addresses](addresses.md) | [de] Adressen mit Typ (privat, geschäftlich, lokal) |
| [authorized_to_vote](authorized_to_vote.md) | [de] Gibt an, ob die Person stimmberechtigt ist |
| [birth_date](birth_date.md) | [de] Genaues Geburtsdatum |
| [birth_year](birth_year.md) | [de] Geburtsjahr |
| [citizenships](citizenships.md) | [de] Staatsbürgerschaften der Person |
| [committee](committee.md) | [en] Committee or board (e |
| [concerned_group](concerned_group.md) | [de] Link zu einer Gruppe, auf die sich die Zugehörigkeit bezieht |
| [concerned_person](concerned_person.md) | [de] Link zu einer Person, auf die sich die Zugehörigkeit bezieht |
| [contact_type](contact_type.md) | [de] Typ der Kontaktinformation |
| [contacts](contacts.md) | [en] Contact information (email, website, social media) |
| [country](country.md) | [de] ISO 3166 Ländercode |
| [date_actual](date_actual.md) | [de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens (oh... |
| [date_begin_actual](date_begin_actual.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitda... |
| [date_begin_planned](date_begin_planned.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer |
| [date_created](date_created.md) | [de] Das Datum, an dem eine Entität erstellt wurde |
| [date_end_actual](date_end_actual.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdaue... |
| [date_end_planned](date_end_planned.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer |
| [date_modified](date_modified.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde |
| [date_planned](date_planned.md) | [de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens (ohne Z... |
| [datetime_actual](datetime_actual.md) | [de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses ode... |
| [datetime_begin_actual](datetime_begin_actual.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorko... |
| [datetime_begin_planned](datetime_begin_planned.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommen... |
| [datetime_created](datetime_created.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde |
| [datetime_end_actual](datetime_end_actual.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkomm... |
| [datetime_end_planned](datetime_end_planned.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens ... |
| [datetime_modified](datetime_modified.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde |
| [datetime_planned](datetime_planned.md) | [de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vo... |
| [death_date](death_date.md) | [de] Genaues Todesdatum |
| [description](description.md) | [de] Kurze Beschreibung der Gruppierung |
| [district](district.md) | [de] Wahlkreis oder Wahlregion |
| [electoral_district](electoral_district.md) | [de] Link zum Wahlbezirk |
| [enterprise](enterprise.md) | [de] Name des Unternehmens |
| [enterprise_uid](enterprise_uid.md) | [de] UID des Unternehmens |
| [function_role](function_role.md) | [en] Function or role in the organization |
| [gender_code](gender_code.md) | [de] Geschlechtscode (z |
| [genders](genders.md) | [de] Geschlecht der Person |
| [global_uri](global_uri.md) | [de] Eine eindeutige, global gültige URI für die Entität |
| [group_type](group_type.md) | [de] Klasse der Gruppierung, wie z |
| [group_type_enum](group_type_enum.md) | [de] Link zum kontrollierten Vokabular für Gruppentypen |
| [groups](groups.md) | [de] Sammlung von Gruppen |
| [interest_links](interest_links.md) | [de] Sammlung von Interessenbindungen |
| [interest_type](interest_type.md) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verei... |
| [is_active](is_active.md) | [de] Gibt an, ob die Information aktuell gültig ist |
| [is_correspondence](is_correspondence.md) | [de] Gibt an, ob es sich um die bevorzugte Sprache handelt |
| [is_native](is_native.md) | [de] Gibt an, ob es sich um die Muttersprache handelt |
| [is_paid](is_paid.md) | [de] Gibt an, ob die Position bezahlt ist |
| [label](label.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... |
| [label_long](label_long.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel z... |
| [landing_page](landing_page.md) | [de] Website mit weiteren Informationen |
| [language](language.md) | [de] Sprachcode im ISO 639-1 Format |
| [language_proficiencies](language_proficiencies.md) | [de] Sprachkompetenzen der Person |
| [legal_form](legal_form.md) | [en] Legal form of the organization |
| [local_id](local_id.md) | [de] Lokaler Identifikator |
| [memberships](memberships.md) | [de] Sammlung von Mitgliedschaften |
| [multilingual_value](multilingual_value.md) | [de] Ein mehrsprachiger Wert mit Angabe der Sprache |
| [name_type](name_type.md) | [de] Typ des Namens |
| [names](names.md) | [en] Names of the person with type and value |
| [occupation_code](occupation_code.md) | [de] ISCO-19 Code der Tätigkeit |
| [occupations](occupations.md) | [de] Berufe oder Tätigkeiten der Person |
| [organization_address](organization_address.md) | [en] Address of the organization |
| [organization_label](organization_label.md) | [en] Label of the organization |
| [organization_uid](organization_uid.md) | [en] UID of the organization (for analysis with NOGA codes, etc |
| [parent_groups](parent_groups.md) | [de] Übergeordneten Gruppe |
| [party_color](party_color.md) | [de] Parteifarbe (optional für Parteien) |
| [persons](persons.md) | [de] Sammlung von Personen |
| [picture](picture.md) | [de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF) |
| [postal_code](postal_code.md) | [de] Postleitzahl |
| [postal_locality](postal_locality.md) | [de] Ort |
| [pronouns](pronouns.md) | [de] Von der Person verwendete Pronomen |
| [role_label](role_label.md) | [en] Descriptive label for the role when 'other' is selected in the RoleEnum |
| [role_type](role_type.md) | [en] Role of the person in the membership or function |
| [role_type_enum](role_type_enum.md) | [en] Role of the person in the membership or function |
| [spatial](spatial.md) | [de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z |
| [statutes_url](statutes_url.md) | [de] URL zu Parteistatuten (optional für Parteien) |
| [street_address](street_address.md) | [de] Strassenadresse |
| [training_code](training_code.md) | [de] ISCO-19 Code der Ausbildung oder Bildung |
| [training_type](training_type.md) | [de] Typ der Ausbildung oder Bildung |
| [trainings](trainings.md) | [de] Ausbildungen oder Bildungen der Person |
| [valid_from](valid_from.md) | [de] Das Datum, ab dem die Information gültig ist |
| [valid_through](valid_through.md) | [de] Das Datum, bis und mit dem die Information gültig ist |
| [value](value.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ... |
| [wikidata_uri](wikidata_uri.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AddressTypeEnum](AddressTypeEnum.md) | [en] Types of addresses |
| [ContactTypeEnum](ContactTypeEnum.md) | [en] Types of contact information |
| [GroupTypeEnum](GroupTypeEnum.md) | [en] Types of political groups and organizations |
| [InterestTypeEnum](InterestTypeEnum.md) | [en] Types of interest links (conflicts of interest, political financing) |
| [NameTypeEnum](NameTypeEnum.md) | [de] Kategorien von Namenstypen gemäss https://dam-api |
| [RoleEnum](RoleEnum.md) | [en] Roles a person can have within a membership |
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
