# operations

Schéma des séances pour différents corps législatifs


URI: https://ch.paf.link/schema/operations

Name: operations



## Classes

| Classe | Description |
| --- | --- |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |
| [Date](Date.md) | Une date assortie d'une indication de type (p |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |
| [Expression](Expression.md) | FRBR Expression : une version linguistique concrète d'un Work |
| [GroupReference](GroupReference.md) | Référence abrégée à un groupe avec les principales données d'identification a... |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Une classe mixin qui fournit des slots pour modéliser les dates de création e... |
| [HasIdentification](HasIdentification.md) | Une classe mixin qui fournit des slots pour l'identification d'une entité |
| [HasReferenceIdentification](HasReferenceIdentification.md) | Une classe mixin qui fournit les slots par lesquels une référence désigne l'e... |
| [HasTemporalValidity](HasTemporalValidity.md) | Une classe mixin qui fournit des slots pour modéliser la validité temporelle ... |
| [IndividualAttendance](IndividualAttendance.md) | Constatation individuelle de la présence d'une personne à une séance (rattach... |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |
| [IsEventWithDuration](IsEventWithDuration.md) | Une classe mixin qui fournit des slots pour modéliser des événements ou occur... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Une classe mixin qui fournit des slots pour modéliser des événements ou occur... |
| [IsProcessStep](IsProcessStep.md) | Une classe mixin pour une étape unique dans un processus |
| [JointDebate](JointDebate.md) | Points de l'ordre du jour traités conjointement |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |
| [Manifestation](Manifestation.md) | FRBR Manifestation : une forme de fichier concrète d'une Expression, adressab... |
| [Media](Media.md) | Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD o... |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |
| [Motion](Motion.md) | Une proposition formelle déposée au cours des délibérations |
| [MultilingualString](MultilingualString.md) | Une chaîne de caractères pouvant contenir du texte en plusieurs langues |
| [MultilingualUri](MultilingualUri.md) | Une URI accompagnée de la langue de la ressource vers laquelle elle renvoie |
| [MultilingualValue](MultilingualValue.md) | Une chaîne de caractères multilingue avec indication de la langue |
| [PersonReference](PersonReference.md) | Référence abrégée à une personne avec les principales données d'identificatio... |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |
| [Resolution](Resolution.md) | Une décision prise sur un point de l'ordre du jour, y compris les procédures ... |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |
| [TextSegment](TextSegment.md) | Un segment de texte tel qu'un renvoi ou un intertitre dans un procès-verbal d... |
| [TotalOther](TotalOther.md) | Décomptes de voix supplémentaires lorsque plusieurs options sont soumises au ... |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |
| [Work](Work.md) | FRBR Work : le document abstrait en tant que tel, indépendamment d'une versio... |
| [WorkContainer](WorkContainer.md) | Conteneur pour les documents (FRBR Works) de ce schéma |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) | Abréviation (peut être multilingue) |
| [actor_fullname](actor_fullname.md) | Nom complet de l'actrice ou de l'acteur, respectivement de la personne |
| [actor_id](actor_id.md) | Référence à la personne agissante (instantané au moment de la mise en relatio... |
| [actor_name](actor_name.md) | Nom de l'organe politique (p |
| [administrative_id](administrative_id.md) | Identifiant administratif du corps législatif, p |
| [affair_id](affair_id.md) | Le lien vers les affaires rattachées au point de l'ordre du jour |
| [agenda_item_category](agenda_item_category.md) | Catégorie pour les points de l'ordre du jour regroupés (p |
| [agenda_item_description](agenda_item_description.md) | Sous-titre ou description détaillée du point de l'ordre du jour |
| [agenda_item_ids](agenda_item_ids.md) | Les points de l'ordre du jour associés au vote |
| [agenda_item_number](agenda_item_number.md) | Numéro d'ordre du point de l'ordre du jour (type chaîne, afin de permettre le... |
| [agenda_item_position](agenda_item_position.md) | Position (nombre entier) du point de l'ordre du jour dans le déroulement de l... |
| [agenda_item_title](agenda_item_title.md) | Titre du point de l'ordre du jour |
| [agenda_item_type](agenda_item_type.md) | Type de point de l'ordre du jour, distinguant les points isolés des groupes d... |
| [agenda_items](agenda_items.md) | Ensemble des points de l'ordre du jour |
| [attendance_type](attendance_type.md) | Type de présence individuelle |
| [attendances](attendances.md) | Ensemble des listes de présence |
| [category](category.md) | Catégorie de l'élément |
| [count](count.md) | Le nombre de voix pour la catégorie « autres » |
| [date_actual](date_actual.md) | La date effective d'un événement ou d'une occurrence instantané (sans durée) |
| [date_begin_actual](date_begin_actual.md) | La date de début effective d'un événement ou d'une occurrence avec durée |
| [date_begin_planned](date_begin_planned.md) | La date de début planifiée d'un événement ou d'une occurrence avec durée |
| [date_created](date_created.md) | La date à laquelle une entité a été créée |
| [date_end_actual](date_end_actual.md) | La date de fin effective d'un événement ou d'une occurrence avec durée |
| [date_end_planned](date_end_planned.md) | La date de fin planifiée d'un événement ou d'une occurrence avec durée |
| [date_modified](date_modified.md) | La date à laquelle une entité a été modifiée pour la dernière fois |
| [date_planned](date_planned.md) | La date planifiée d'un événement ou d'une occurrence instantané (sans durée) |
| [date_type](date_type.md) | Signification de la date (p |
| [dates](dates.md) | Dates relatives à l'élément, chacune assortie d'une indication de type |
| [datetime_actual](datetime_actual.md) | La date et l'heure effectives d'un événement ou d'une occurrence instantané (... |
| [datetime_begin](datetime_begin.md) | La date et l'heure auxquelles la séance ou le vote commence |
| [datetime_begin_actual](datetime_begin_actual.md) | La date et l'heure de début effectives d'un événement ou d'une occurrence ave... |
| [datetime_begin_planned](datetime_begin_planned.md) | La date et l'heure de début planifiées d'un événement ou d'une occurrence ave... |
| [datetime_created](datetime_created.md) | La date et l'heure auxquelles une entité a été créée |
| [datetime_end](datetime_end.md) | La date et l'heure auxquelles la séance ou le vote se termine |
| [datetime_end_actual](datetime_end_actual.md) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec ... |
| [datetime_end_planned](datetime_end_planned.md) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec ... |
| [datetime_modified](datetime_modified.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois |
| [datetime_planned](datetime_planned.md) | La date et l'heure planifiées d'un événement ou d'une occurrence instantané (... |
| [description](description.md) | Texte descriptif de l'élément |
| [document_category](document_category.md) | Catégorie du document |
| [documents](documents.md) | Liste des documents (FRBR Works) liés à l'entité |
| [election_type](election_type.md) | Type de procédure d'élection |
| [elections](elections.md) | Ensemble des élections |
| [expression_description](expression_description.md) | Texte descriptif de la version linguistique |
| [expression_language](expression_language.md) | Code de langue au format ISO 639-1 |
| [expression_title](expression_title.md) | Titre de la version linguistique |
| [expressions](expressions.md) | Les versions linguistiques (Expressions) d'un Work |
| [format](format.md) | Le format de fichier de la manifestation (p |
| [global_uri](global_uri.md) | Une URI unique et globalement valide pour l'entité |
| [group_id](group_id.md) | Référence au groupe ou à l'organe (instantané au moment de la mise en relatio... |
| [group_label](group_label.md) | Nom de l'organe/du groupe au moment de la liaison |
| [group_name](group_name.md) | Nom du groupe ou de l'organe |
| [has_resolution](has_resolution.md) | La décision prise sur ce point de l'ordre du jour |
| [id](id.md) | Identifiant univoque de l'élément |
| [individual_attendances](individual_attendances.md) | Ensemble des constatations individuelles de présence |
| [individual_vote_type](individual_vote_type.md) | Type de voix exprimée (oui, non, abstention, n'a pas voté, etc |
| [individual_votes](individual_votes.md) | Ensemble des voix individuelles |
| [is_active](is_active.md) | Indique si l'information est actuellement valable |
| [label](label.md) | Attribuer un label à une information structurée (par ex |
| [label_abstention](label_abstention.md) | Signification d'une abstention |
| [label_long](label_long.md) | Attribuer un label étendu à une information structurée (par ex |
| [label_no](label_no.md) | Signification d'une voix « non » |
| [label_yes](label_yes.md) | Signification d'une voix « oui » |
| [landing_page](landing_page.md) | URL fournissant des informations complémentaires |
| [language](language.md) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex |
| [leading_actor_id](leading_actor_id.md) | Le département responsable du point de l'ordre du jour |
| [legislatures](legislatures.md) | Ensemble des législatures |
| [local_id](local_id.md) | Identifiant local |
| [location](location.md) | Lieu où se tient la séance (salle physique, visioconférence ou format hybride... |
| [majority_count](majority_count.md) | Nombre de voix requis pour atteindre le seuil de majorité déterminant |
| [majority_type](majority_type.md) | Type de majorité requise pour le vote (absolue, deux tiers, etc |
| [manifestation_url](manifestation_url.md) | URL sous laquelle la forme de fichier peut être consultée |
| [manifestations](manifestations.md) | Les formes de fichier (Manifestations) d'une Expression |
| [media_format](media_format.md) | Type MIME du fichier média |
| [media_type](media_type.md) | Type de média (audio, vidéo, document) |
| [media_url](media_url.md) | URL du fichier média (audio/vidéo) |
| [meeting_abbreviation](meeting_abbreviation.md) | Désignation abrégée de la session ou de la séance (p |
| [meeting_type](meeting_type.md) | Type de séance, p |
| [meetings](meetings.md) | Ensemble des séances |
| [multilingual_value](multilingual_value.md) | Une valeur multilingue avec indication de la langue |
| [name](name.md) | Désignation complète multilingue |
| [number](number.md) | Numéro courant, p |
| [optional](optional.md) | Indique si la séance ou le vote est facultatif |
| [parent_agenda_item](parent_agenda_item.md) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre d... |
| [parent_attendance](parent_attendance.md) | L'agrégat Attendance auquel appartient cette constatation individuelle de pré... |
| [parent_legislature](parent_legislature.md) | La législature dans le cadre de laquelle la séance a lieu |
| [parent_meeting](parent_meeting.md) | Identifiant de la séance liée qui regroupe la séance courante |
| [parent_type](parent_type.md) | Type de l'objet parent (séance, point de l'ordre du jour, intervention, affai... |
| [parent_voting](parent_voting.md) | L'identifiant du vote auquel se rattache la voix individuelle |
| [position](position.md) | Position (nombre entier) au sein de la séquence supérieure |
| [protocol_items](protocol_items.md) | Points de l'ordre du jour tels qu'ils ont effectivement été consignés au proc... |
| [protocol_ref](protocol_ref.md) | Le procès-verbal de cette séance, établi après celle-ci |
| [protocols](protocols.md) | Ensemble des procès-verbaux |
| [reason](reason.md) | Motif de l'absence ou du retard (texte libre, multilingue) |
| [remark](remark.md) | Remarque ou note en texte libre pour les cas particuliers ou pour un contexte... |
| [resolution_type](resolution_type.md) | Type de décision prise sur le point de l'ordre du jour |
| [resolutions](resolutions.md) | Ensemble des décisions |
| [result](result.md) | Résultat de la procédure |
| [result_text](result_text.md) | Texte libre décrivant le résultat du vote, p |
| [role](role.md) | Rôle de la personne (p |
| [seat_nr](seat_nr.md) | Le numéro de siège correspondant à la voix individuelle, le cas échéant |
| [sequential_number](sequential_number.md) | Numéro séquentiel de la séance, utilisé pour le tri |
| [sessions](sessions.md) | Ensemble des sessions |
| [spatial](spatial.md) | Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro OFS ... |
| [speaking_actor_id](speaking_actor_id.md) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de... |
| [speeches](speeches.md) | Ensemble des interventions |
| [start](start.md) | Indication de début ou position |
| [state](state.md) | État actuel de la séance (planifiée, annulée, reportée) |
| [state_id](state_id.md) | Identifiant d'état (renvoi à l'énumération des états ou à un état propre) |
| [state_name](state_name.md) | Description personnalisée de l'état de la séance |
| [status](status.md) | Désignation libre de l'état, utilisée là où l'énumération des états ne s'appl... |
| [text](text.md) | Contenu textuel de l'élément |
| [text_format](text_format.md) | Format du texte (text, html, html_with_timestamps) |
| [text_segments](text_segments.md) | Ensemble de segments de texte (p |
| [text_type](text_type.md) | Type de texte (version brute, version éditée) |
| [tie_breaker](tie_breaker.md) | Indique si une voix prépondérante a été utilisée lors du vote |
| [title](title.md) | Titre de l'élément |
| [total](total.md) | Nombre total de voix, sans les absents ni la voix de la présidence |
| [total_absent](total_absent.md) | Nombre total de membres absents |
| [total_count](total_count.md) | Nombre total de membres de l'organe (valeur de référence pour le calcul du qu... |
| [total_count_abstention](total_count_abstention.md) | Nombre total d'abstentions |
| [total_count_no](total_count_no.md) | Nombre total de voix « non » |
| [total_count_yes](total_count_yes.md) | Nombre total de voix « oui » |
| [total_excused](total_excused.md) | Nombre total d'absences excusées |
| [total_other](total_other.md) | Utilisé lorsque plusieurs options sont soumises au vote (p |
| [total_present](total_present.md) | Nombre total de membres présents |
| [type](type.md) | Désignation générique du type |
| [type_label](type_label.md) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliq... |
| [url](url.md) | Page d'accueil ou adresse web complémentaire, multilingue |
| [valid_from](valid_from.md) | La date à partir de laquelle l'information est valable |
| [valid_through](valid_through.md) | La date jusqu'à laquelle l'information est valable, incluse |
| [value](value.md) | La valeur proprement dite d'une information, en plus d'autres attributs tels ... |
| [version](version.md) | Numéro ou identifiant de version |
| [vote_procedures](vote_procedures.md) | Modalités du vote, p |
| [voting_title](voting_title.md) | Titre du vote, objet ou question soumise au vote |
| [voting_type](voting_type.md) | Type de procédure de vote (vote intermédiaire, vote final, vote secret, etc |
| [votings](votings.md) | Ensemble des votes |
| [weight](weight.md) | Le nombre de voix dont dispose la personne, le cas échéant (p |
| [wikidata_uri](wikidata_uri.md) | Une URI qui renvoie à une entité Wikidata, par ex |
| [work_type](work_type.md) | Type de document (p |
| [works](works.md) | Les documents (FRBR Works) contenus dans le conteneur |
| [xdate](xdate.md) | La valeur de date elle-même |


## Énumérations

| Énumération | Description |
| --- | --- |
| [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type de point de l'ordre du jour, distinguant les points isolés des points re... |
| [AttendanceTypeEnum](AttendanceTypeEnum.md) | Type de présence individuelle |
| [DateTypesEnum](DateTypesEnum.md) | Signification d'une indication de date |
| [DocumentCategoryEnum](DocumentCategoryEnum.md) | Catégories de classification des documents référencés dans les normes eCH 029... |
| [ElectionTypeEnum](ElectionTypeEnum.md) | Type de procédure d'élection |
| [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | Type de voix individuelle exprimée par un membre |
| [MajorityTypeEnum](MajorityTypeEnum.md) | Type de majorité requise pour le vote |
| [MeetingTypeEnum](MeetingTypeEnum.md) | Type de séance |
| [ResolutionTypeEnum](ResolutionTypeEnum.md) | Type de décision prise sur un point de l'ordre du jour |
| [StateEnum](StateEnum.md) | État de la séance |
| [VotingTypeEnum](VotingTypeEnum.md) | Type de procédure de vote |
| [WorkTypesEnum](WorkTypesEnum.md) | Type d'un document (FRBR Work) |


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
