# Actors Schema

Un schéma décrivant les acteurs politiques, y compris les personnes, les groupes, les affiliations et les liens d'intérêts.


URI: https://ld.ech.ch/schema/0294/actors

Name: actors-schema



## Classes

| Classe | Description |
| --- | --- |
| [Address](Address.md) | Une adresse avec un type (p |
| [Citizenship](Citizenship.md) | Nationalité (également utilisée pour la citoyenneté) d'une personne indiquant... |
| [Contact](Contact.md) | Informations de contact d'une personne indiquant un type (p |
| [Container](Container.md) | Conteneur pour les acteurs politiques, les groupes et les relations |
| [ElectoralDistrict](ElectoralDistrict.md) | Circonscription ou région électorale associée à une affiliation |
| [Gender](Gender.md) | Sexe d'une personne indiquant un code de sexe et la validité temporelle |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |
| [GroupType](GroupType.md) | Type de groupe (p |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Une classe mixin qui fournit des slots pour modéliser les dates de création e... |
| [HasIdentification](HasIdentification.md) | Une classe mixin qui fournit des slots pour l'identification d'une entité |
| [HasTemporalValidity](HasTemporalValidity.md) | Une classe mixin qui fournit des slots pour modéliser la validité temporelle ... |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |
| [IsEventWithDuration](IsEventWithDuration.md) | Une classe mixin qui fournit des slots pour modéliser des événements ou occur... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Une classe mixin qui fournit des slots pour modéliser des événements ou occur... |
| [IsProcessStep](IsProcessStep.md) | Une classe mixin pour une étape unique dans un processus |
| [LanguageProficiency](LanguageProficiency.md) | Compétences linguistiques d'une personne indiquant la langue et le fait qu'il... |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |
| [MultilingualValue](MultilingualValue.md) | Une chaîne de caractères multilingue avec indication de la langue |
| [Name](Name.md) | Un nom avec un type (p |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |
| [RoleType](RoleType.md) | Rôle d'une personne dans une affiliation ou une fonction (p |
| [Training](Training.md) | Formation ou éducation d'une personne indiquant un type (p |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) | Abréviation (peut être multilingue) |
| [address_type](address_type.md) | Type d'adresse |
| [address_uri](address_uri.md) | URI de l'adresse issue du répertoire fédéral des adresses de bâtiments |
| [addresses](addresses.md) | Adresses avec type (privée, professionnelle, locale) |
| [authorized_to_vote](authorized_to_vote.md) | Indique si la personne dispose du droit de vote au sein du groupe |
| [birth_date](birth_date.md) | Date de naissance exacte si disponible et publique |
| [birth_year](birth_year.md) | Année de naissance |
| [citizenships](citizenships.md) | Nationalités de la personne |
| [committee](committee.md) | Comité ou organe au sein de l'organisation (p |
| [contact_type](contact_type.md) | Type d'informations de contact |
| [contacts](contacts.md) | Informations de contact (e-mail, site web, réseaux sociaux) |
| [country](country.md) | Code de pays ISO 3166-1 alpha-2 |
| [date_actual](date_actual.md) | La date effective d'un événement ou d'une occurrence instantané (sans durée) |
| [date_begin_actual](date_begin_actual.md) | La date de début effective d'un événement ou d'une occurrence avec durée |
| [date_begin_planned](date_begin_planned.md) | La date de début planifiée d'un événement ou d'une occurrence avec durée |
| [date_created](date_created.md) | La date à laquelle une entité a été créée |
| [date_end_actual](date_end_actual.md) | La date de fin effective d'un événement ou d'une occurrence avec durée |
| [date_end_planned](date_end_planned.md) | La date de fin planifiée d'un événement ou d'une occurrence avec durée |
| [date_modified](date_modified.md) | La date à laquelle une entité a été modifiée pour la dernière fois |
| [date_planned](date_planned.md) | La date planifiée d'un événement ou d'une occurrence instantané (sans durée) |
| [datetime_actual](datetime_actual.md) | La date et l'heure effectives d'un événement ou d'une occurrence instantané (... |
| [datetime_begin_actual](datetime_begin_actual.md) | La date et l'heure de début effectives d'un événement ou d'une occurrence ave... |
| [datetime_begin_planned](datetime_begin_planned.md) | La date et l'heure de début planifiées d'un événement ou d'une occurrence ave... |
| [datetime_created](datetime_created.md) | La date et l'heure auxquelles une entité a été créée |
| [datetime_end_actual](datetime_end_actual.md) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec ... |
| [datetime_end_planned](datetime_end_planned.md) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec ... |
| [datetime_modified](datetime_modified.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois |
| [datetime_planned](datetime_planned.md) | La date et l'heure planifiées d'un événement ou d'une occurrence instantané (... |
| [death_date](death_date.md) | Date de décès exacte |
| [description](description.md) | Description de l'entité |
| [electoral_district](electoral_district.md) | Lien vers la circonscription électorale |
| [function_role](function_role.md) | Fonction ou rôle dans l'organisation (p |
| [gender_code](gender_code.md) | Code de sexe |
| [genders](genders.md) | Sexe de la personne |
| [global_uri](global_uri.md) | Une URI unique et globalement valide pour l'entité |
| [group_label](group_label.md) | Nom de l'organe/du groupe au moment de la liaison |
| [group_reference](group_reference.md) | Référence à un groupe avec des données instantanées au moment de la mise en r... |
| [group_type](group_type.md) | Type de groupe (p |
| [group_type_enum](group_type_enum.md) | Lien vers le vocabulaire contrôlé pour les types de groupes |
| [groups](groups.md) | Collection de groupes |
| [interest_links](interest_links.md) | Collection de liens d'intérêts |
| [interest_type](interest_type.md) | Type de lien d'intérêts (activité professionnelle, mandat politique, associat... |
| [is_active](is_active.md) | Indique si l'information est actuellement valable |
| [is_correspondence](is_correspondence.md) | Indique s'il s'agit de la langue préférée |
| [is_native](is_native.md) | Indique s'il s'agit de la langue maternelle |
| [is_paid](is_paid.md) | Indique si le poste est rémunéré |
| [label](label.md) | Attribuer un label à une information structurée (par ex |
| [label_long](label_long.md) | Attribuer un label étendu à une information structurée (par ex |
| [landing_page](landing_page.md) | Site web fournissant de plus amples informations |
| [language](language.md) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex |
| [language_proficiencies](language_proficiencies.md) | Compétences linguistiques de la personne |
| [legal_form](legal_form.md) | Forme juridique de l'organisation |
| [local_id](local_id.md) | Identifiant local |
| [memberships](memberships.md) | Collection d'affiliations |
| [multilingual_value](multilingual_value.md) | Une valeur multilingue avec indication de la langue |
| [name_type](name_type.md) | Type de nom selon eCH-0011 (personNameData) |
| [names](names.md) | Noms de la personne avec type et valeur |
| [occupation_code](occupation_code.md) | Code ISCO-19 du métier |
| [occupations](occupations.md) | Métiers ou professions de la personne |
| [organization_address](organization_address.md) | Adresse de l'organisation |
| [organization_name](organization_name.md) | Nom de l'organisation ou de l'entreprise |
| [organization_uid](organization_uid.md) | IDE de l'organisation (format eCH-0097 : CHE-XXX |
| [parent_groups](parent_groups.md) | Lien vers les groupes parents |
| [party_color](party_color.md) | Couleur du parti sous forme de valeur hexadécimale (facultatif pour les parti... |
| [person_reference](person_reference.md) | Référence à une personne avec des données instantanées au moment de la mise e... |
| [persons](persons.md) | Collection de personnes |
| [picture](picture.md) | Lien vers une image (de préférence : PNG, puis JPG, puis GIF) |
| [postal_code](postal_code.md) | Code postal |
| [postal_locality](postal_locality.md) | Localité |
| [pronouns](pronouns.md) | Pronoms utilisés par la personne |
| [remark](remark.md) | Remarque ou note en texte libre pour les cas particuliers ou pour un contexte... |
| [role_label](role_label.md) | Libellé descriptif du rôle lorsque « other » est sélectionné dans RoleEnum |
| [role_type](role_type.md) | Rôle de la personne dans l'affiliation ou la fonction |
| [role_type_enum](role_type_enum.md) | Rôle de la personne dans l'affiliation ou la fonction |
| [spatial](spatial.md) | Référence spatiale (numéro OFS de commune, numéro OFS de canton ou pays) |
| [statutes_url](statutes_url.md) | URL vers les statuts du parti (PDF ou page web ; facultatif pour les partis) |
| [street_address](street_address.md) | Adresse (rue) |
| [training_code](training_code.md) | Code ISCO-19 de la formation ou de l'éducation |
| [training_type](training_type.md) | Type de formation ou d'éducation |
| [trainings](trainings.md) | Formations ou éducations de la personne |
| [valid_from](valid_from.md) | La date à partir de laquelle l'information est valable |
| [valid_through](valid_through.md) | La date jusqu'à laquelle l'information est valable, incluse |
| [value](value.md) | La valeur proprement dite d'une information, en plus d'autres attributs tels ... |
| [wikidata_uri](wikidata_uri.md) | Une URI qui renvoie à une entité Wikidata, par ex |


## Énumérations

| Énumération | Description |
| --- | --- |
| [AddressTypeEnum](AddressTypeEnum.md) | Types d'adresses |
| [ContactTypeEnum](ContactTypeEnum.md) | Types d'informations de contact |
| [GenderCodeEnum](GenderCodeEnum.md) | Codes de sexe pour les personnes |
| [GroupTypeEnum](GroupTypeEnum.md) | Types de groupes et d'organisations politiques |
| [InterestTypeEnum](InterestTypeEnum.md) | Types de liens d'intérêts (conflits d'intérêts, financement politique) |
| [LegalFormEnum](LegalFormEnum.md) | Formes juridiques basées sur la liste de codes du registre fédéral IDE (eCH-0... |
| [NameTypeEnum](NameTypeEnum.md) | Catégories de types de noms selon eCH-0011 (personNameData) et https://dam-ap... |
| [RoleEnum](RoleEnum.md) | Rôles qu'une personne peut occuper dans le cadre d'une affiliation |
| [TrainingTypeEnum](TrainingTypeEnum.md) | Types de formation ou d'éducation basés sur la liste de codes suisse LEVEL_ED... |


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


## Sous-ensembles

| Sous-ensemble | Description |
| --- | --- |
