# eCH-0294 – Political Actors: Persons, Groups and Bodies

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
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, die einer Mitgliedschaft zugeordnet ist |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |
| [GroupReference](GroupReference.md) | Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikations... |
| [GroupType](GroupType.md) | Art der Gruppe (z |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderu... |
| [HasIdentification](HasIdentification.md) | Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügu... |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |
| [IsEventWithDuration](IsEventWithDuration.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkom... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen... |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |
| [LanguageProficiency](LanguageProficiency.md) | Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die be... |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |
| [MultilingualValue](MultilingualValue.md) | Ein mehrsprachiger String mit Angabe der Sprache |
| [Name](Name.md) | Ein Name mit einem Typ (z |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |
| [RoleType](RoleType.md) | Rolle einer Person in einer Mitgliedschaft oder Funktion (z |
| [Training](Training.md) | Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |



## Slots

| Slot | Beschreibung |
| --- | --- |
| [abbreviation](abbreviation.md) | Abkürzung (kann mehrsprachig sein) |
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
| [date_actual](date_actual.md) | Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommnissen (ohne... |
| [date_begin_actual](date_begin_actual.md) | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdaue... |
| [date_begin_planned](date_begin_planned.md) | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_created](date_created.md) | Das Datum, an dem eine Entität erstellt wurde |
| [date_end_actual](date_end_actual.md) | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_end_planned](date_end_planned.md) | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_modified](date_modified.md) | Das Datum, an dem eine Entität zuletzt geändert wurde |
| [date_planned](date_planned.md) | Das geplante Datum eines instantanen Ereignisses oder Vorkommnissen (ohne Zei... |
| [datetime_actual](datetime_actual.md) | Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses oder Vor... |
| [datetime_begin_actual](datetime_begin_actual.md) | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnis... |
| [datetime_begin_planned](datetime_begin_planned.md) | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen ... |
| [datetime_created](datetime_created.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde |
| [datetime_end_actual](datetime_end_actual.md) | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnisse... |
| [datetime_end_planned](datetime_end_planned.md) | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mi... |
| [datetime_modified](datetime_modified.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde |
| [datetime_planned](datetime_planned.md) | Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkomm... |
| [death_date](death_date.md) | Genaues Todesdatum |
| [description](description.md) | Kurze Beschreibung der Gruppierung |
| [electoral_district](electoral_district.md) | Link zum Wahlbezirk |
| [function_role](function_role.md) | Funktion oder Rolle in der Organisation (z |
| [gender_code](gender_code.md) | Geschlechtscode |
| [genders](genders.md) | Geschlecht der Person |
| [global_uri](global_uri.md) | Eine eindeutige, global gültige URI für die Entität |
| [group_label](group_label.md) | Name des Gremiums zum Zeitpunkt der Verknüpfung |
| [group_reference](group_reference.md) | Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung |
| [group_type](group_type.md) | Klasse der Gruppierung, wie z |
| [group_type_enum](group_type_enum.md) | Link zum kontrollierten Vokabular für Gruppentypen |
| [groups](groups.md) | Sammlung von Gruppen |
| [interest_links](interest_links.md) | Sammlung von Interessenbindungen |
| [interest_type](interest_type.md) | Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein) |
| [is_active](is_active.md) | Gibt an, ob die Information aktuell gültig ist |
| [is_correspondence](is_correspondence.md) | Gibt an, ob es sich um die bevorzugte Sprache handelt |
| [is_native](is_native.md) | Gibt an, ob es sich um die Muttersprache handelt |
| [is_paid](is_paid.md) | Gibt an, ob die Position bezahlt ist |
| [label](label.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw |
| [label_long](label_long.md) | Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu ver... |
| [landing_page](landing_page.md) | Website mit weiteren Informationen |
| [language](language.md) | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z |
| [language_proficiencies](language_proficiencies.md) | Sprachkompetenzen der Person |
| [legal_form](legal_form.md) | Rechtsform der Organisation |
| [local_id](local_id.md) | Lokaler Identifikator |
| [memberships](memberships.md) | Sammlung von Mitgliedschaften |
| [multilingual_value](multilingual_value.md) | Ein mehrsprachiger Wert mit Angabe der Sprache |
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
| [remark](remark.md) | Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext zu ei... |
| [role_label](role_label.md) | Spezifische Rollenbezeichnung |
| [role_type](role_type.md) | Rolle der Person in der Mitgliedschaft oder Funktion |
| [role_type_enum](role_type_enum.md) | Rolle der Person in der Mitgliedschaft oder Funktion |
| [spatial](spatial.md) | Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land) |
| [statutes_url](statutes_url.md) | URL zu Parteistatuten (PDF oder Webseite; optional für Parteien) |
| [street_address](street_address.md) | Strassenadresse |
| [training_code](training_code.md) | ISCO-19 Code der Ausbildung oder Bildung |
| [training_type](training_type.md) | Typ der Ausbildung oder Bildung |
| [trainings](trainings.md) | Ausbildungen oder Bildungen der Person |
| [valid_from](valid_from.md) | Das Datum, ab dem die Information gültig ist |
| [valid_through](valid_through.md) | Das Datum, bis und mit dem die Information gültig ist |
| [value](value.md) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Spr... |
| [wikidata_uri](wikidata_uri.md) | Eine URI, die auf eine Wikidata-Entität verweist, z |


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
