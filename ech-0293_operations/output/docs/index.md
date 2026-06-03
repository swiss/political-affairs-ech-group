# operations

[en] Meeting Schema for various legislative bodies
[de] Sitzungs Schema für verschiedene gesetzgebende Körperschaften


URI: https://ch.paf.link/schema/operations

Name: operations



## Classes

| Class | Description |
| --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProtocolItem](ProtocolItem.md) | [en] An agenda item as actually recorded in the protocol |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |
| [Container](Container.md) |  |
| [Date](Date.md) |  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |
| [Expression](Expression.md) |  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |
| [HasTemporalValidity](HasTemporalValidity.md) | A mixin class that provides slots for modeling a temporal validity of informa... |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | A mixin class that provides slots for modeling instantaneous events or occurr... |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |
| [JointDebate](JointDebate.md) | [en] Agenda Items which are debated together |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |
| [Manifestation](Manifestation.md) |  |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [Protocol](Protocol.md) | [en] The minutes of a meeting, recorded after the meeting |
| [Resolution](Resolution.md) | [en] A resolutionor decision taken on an agenda item, including voting proced... |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |
| [TotalOther](TotalOther.md) | [en] Additional vote counts when multiple options are presented (e |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |
| [Work](Work.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) | Abbreviation (can be multilingual) |
| [actor_fullname](actor_fullname.md) | Full name of the actor/person |
| [actor_id](actor_id.md) | [en] Reference to the acting person (lightweight snapshot at time of linking) |
| [actor_name](actor_name.md) | [en] Name of the political body (e |
| [administrative_id](administrative_id.md) | [en] Administrative ID of the legislative body, such as a municipality, canto... |
| [affair_id](affair_id.md) | [en] The connection to the affairs (business items) of the agenda item |
| [agenda_item_category](agenda_item_category.md) | [en] Category for grouped agenda items (e |
| [agenda_item_description](agenda_item_description.md) | [en] Subtitle or detailed description of the agenda item |
| [agenda_item_ids](agenda_item_ids.md) | [en] The agenda items associated with the voting |
| [agenda_item_number](agenda_item_number.md) | [en] Sequential number of the agenda item (string type to support roman numer... |
| [agenda_item_position](agenda_item_position.md) | [en] Integer position of the agenda item in the meeting sequence |
| [agenda_item_title](agenda_item_title.md) | [en] Title of the agenda item |
| [agenda_item_type](agenda_item_type.md) | [en] Type of agenda item, distinguishing individual items from groups |
| [agenda_items](agenda_items.md) |  |
| [attendance_type](attendance_type.md) | Type of individual attendance |
| [attendances](attendances.md) | Collection of attendance records |
| [body_key](body_key.md) | [en] Key identifying the political body or jurisdiction (e |
| [category](category.md) |  |
| [count](count.md) | [en] The count of votes for the total other category |
| [date_actual](date_actual.md) | The actual date of an instantaneous event or occurrence (without time duratio... |
| [date_begin_actual](date_begin_actual.md) | The actual start date of an event or occurrence with time duration |
| [date_begin_planned](date_begin_planned.md) | The planned start date of an event or occurrence with time duration |
| [date_created](date_created.md) | The date when an entity was created |
| [date_end_actual](date_end_actual.md) | The actual end date of an event or occurrence with time duration |
| [date_end_planned](date_end_planned.md) | The planned end date of an event or occurrence with time duration |
| [date_modified](date_modified.md) | The date when an entity was last modified |
| [date_planned](date_planned.md) | The planned date of an instantaneous event or occurrence (without time durati... |
| [date_type](date_type.md) |  |
| [dates](dates.md) |  |
| [datetime_actual](datetime_actual.md) | The actual date and time of an instantaneous event or occurrence (without tim... |
| [datetime_begin](datetime_begin.md) | [en] The date and time when the meeting or voting begins |
| [datetime_begin_actual](datetime_begin_actual.md) | The actual start date and time of an event or occurrence with time duration |
| [datetime_begin_planned](datetime_begin_planned.md) | The planned start date and time of an event or occurrence with time duration |
| [datetime_created](datetime_created.md) | The date and time when an entity was created |
| [datetime_end](datetime_end.md) | [en] The date and time when the meeting or voting ends |
| [datetime_end_actual](datetime_end_actual.md) | The actual end date and time of an event or occurrence with time duration |
| [datetime_end_planned](datetime_end_planned.md) | The planned end date and time of an event or occurrence with time duration |
| [datetime_modified](datetime_modified.md) | The date and time when an entity was last modified |
| [datetime_planned](datetime_planned.md) | The planned date and time of an instantaneous event or occurrence (without ti... |
| [description](description.md) |  |
| [document_category](document_category.md) | [de] Kategorie des Dokuments |
| [documents](documents.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind |
| [election_type](election_type.md) | Type of election procedure |
| [elections](elections.md) | Collection of election records |
| [expressions](expressions.md) |  |
| [format](format.md) | [en] The file format of the manifestation (e |
| [global_uri](global_uri.md) | A unique, globally valid URI for the entity |
| [group_id](group_id.md) | [en] Reference to the group or body (lightweight snapshot at time of linking) |
| [group_label](group_label.md) | Name of the body/group at time of linking |
| [group_name](group_name.md) | Name of the group or body |
| [has_resolution](has_resolution.md) | [en] The resolutionor decision taken on this agenda item |
| [id](id.md) |  |
| [individual_attendances](individual_attendances.md) | Collection of individual attendance records |
| [individual_vote_type](individual_vote_type.md) | [en] Type of vote cast (yes, no, abstention, no vote, etc |
| [individual_votes](individual_votes.md) | Collection of individual vote records |
| [is_active](is_active.md) | Indicates whether the information is currently valid |
| [label](label.md) | Assign a label to a structured piece of information (e |
| [label_abstention](label_abstention.md) | [en] Meaning of an 'abstention' vote |
| [label_long](label_long.md) | Assign an extended label to a structured piece of information (e |
| [label_no](label_no.md) | [en] Meaning of a 'no' vote |
| [label_yes](label_yes.md) | [en] Meaning of a 'yes' vote |
| [landing_page](landing_page.md) | [en] URL providing further information |
| [language](language.md) | Language code in ISO 639-1 format (two lowercase letters, e |
| [leading_actor_id](leading_actor_id.md) | [en] The leading department for the agenda item |
| [legislatures](legislatures.md) |  |
| [local_id](local_id.md) | Local identifier |
| [location](location.md) |  |
| [majority_count](majority_count.md) | [en] Number of votes required for the relevant majority threshold |
| [majority_type](majority_type.md) | [en] Type of majority required for the vote (absolute, two-thirds, etc |
| [manifestations](manifestations.md) |  |
| [media_format](media_format.md) | MIME type of the media file |
| [media_type](media_type.md) | Type of media (audio, video, document) |
| [media_url](media_url.md) | URL to media file (audio/video) |
| [meeting_abbreviation](meeting_abbreviation.md) |  |
| [meeting_type](meeting_type.md) | Type of the meeting, e |
| [meetings](meetings.md) |  |
| [multilingual_value](multilingual_value.md) | A multilingual value with language specification |
| [name](name.md) |  |
| [number](number.md) |  |
| [optional](optional.md) | [en] Indicates if the meeting or voting is optional |
| [parent_agenda_item](parent_agenda_item.md) | [en] If needed, this slot builds a hierarchy of agenda items |
| [parent_attendance](parent_attendance.md) | [en] The Attendance aggregate this individual attendance record belongs to |
| [parent_legislature](parent_legislature.md) | [en] The legislative body in which the meeting is based |
| [parent_meeting](parent_meeting.md) | [en] The linked meeting ID that groups the current meeting |
| [parent_type](parent_type.md) | Type of parent object (meeting, agenda, speech, affair) |
| [parent_voting](parent_voting.md) | [en] The ID of the voting associated with the individual vote |
| [position](position.md) |  |
| [protocol](protocol.md) | [en] The protocol (minutes) of this meeting, recorded after the meeting |
| [protocol_items](protocol_items.md) | [en] Agenda items as actually recorded in the protocol |
| [protocols](protocols.md) | Collection of protocol records |
| [reason](reason.md) | [en] Reason for absence or lateness (free-text, multilingual) |
| [remark](remark.md) | Free-text remark or note for edge cases or additional context on a process st... |
| [resolution_type](resolution_type.md) | [en] Type of resolutiontaken on the agenda item |
| [resolutions](resolutions.md) | Collection of resolutionrecords |
| [result](result.md) |  |
| [result_text](result_text.md) | [en] Free text describing the outcome of the vote, e |
| [role](role.md) | Role of the person (e |
| [seat_nr](seat_nr.md) | [en] The seat number of the individual vote, if applicable |
| [sequential_number](sequential_number.md) | [en] Sequential number of the meeting, used for ordering |
| [sessions](sessions.md) |  |
| [speaking_actor_id](speaking_actor_id.md) | [en] The speaker or head of the department for the agenda item |
| [speeches](speeches.md) | Collection of speech records |
| [start](start.md) | Start indicator or position |
| [state](state.md) |  |
| [state_id](state_id.md) | State identifier (reference to state enum or custom state) |
| [state_name](state_name.md) | [en] Custom state description for the meeting |
| [status](status.md) |  |
| [text](text.md) |  |
| [text_format](text_format.md) | [en] Format of text (text, html, html_with_timestamps) |
| [text_segments](text_segments.md) | Collection of text segments (e |
| [text_type](text_type.md) | [en] Type of text (raw draft, edited version) |
| [tie_breaker](tie_breaker.md) | [en] Indicates if a tie-breaker was used in the voting |
| [title](title.md) |  |
| [total](total.md) | [en] Total number of votes, excluding absent and president's vote |
| [total_absent](total_absent.md) | [en] Total number of absent members |
| [total_count](total_count.md) | [en] Total number of members of the body (reference value for quorum calculat... |
| [total_count_abstention](total_count_abstention.md) | [en] Total number of abstentions |
| [total_count_no](total_count_no.md) | [en] Total number of 'no' votes |
| [total_count_yes](total_count_yes.md) | [en] Total number of 'yes' votes |
| [total_excused](total_excused.md) | Total number of excused absences |
| [total_other](total_other.md) | [en] Used when multiple options are presented for voting (e |
| [total_present](total_present.md) | Total number of members present |
| [type](type.md) |  |
| [type_label](type_label.md) | [en] Custom type label when standard type values don't apply |
| [url](url.md) |  |
| [valid_from](valid_from.md) | The date from which the information is valid |
| [valid_through](valid_through.md) | The date until which the information is valid, inclusive |
| [value](value.md) | The value of an information besides other attributes such as type, language, ... |
| [version](version.md) | Version number or identifier |
| [vote_procedures](vote_procedures.md) | [en] Procedures for voting, such as secret ballot or open vote |
| [voting_title](voting_title.md) | [en] Title or question being voted on |
| [voting_type](voting_type.md) | [en] Type of voting procedure (preliminary, final, secret, etc |
| [votings](votings.md) | Collection of voting records |
| [weight](weight.md) | [en] The number of votes held by the individual, if applicable (e |
| [wikidata_uri](wikidata_uri.md) | A URI that refers to a Wikidata entity, e |
| [work_type](work_type.md) |  |
| [works](works.md) |  |
| [xdate](xdate.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | [en] Type of agenda item, distinguishing individual items from grouped items |
| [AttendanceTypeEnum](AttendanceTypeEnum.md) | [en] Type of individual attendance |
| [DateTypesEnum](DateTypesEnum.md) |  |
| [DocumentCategoryEnum](DocumentCategoryEnum.md) | [de] Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards 0... |
| [ElectionTypeEnum](ElectionTypeEnum.md) | [en] Type of election procedure |
| [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | [en] Type of individual vote cast by a member |
| [MajorityTypeEnum](MajorityTypeEnum.md) | Type of majority required for the vote |
| [MeetingTypeEnum](MeetingTypeEnum.md) | Type of the meeting |
| [ResolutionTypeEnum](ResolutionTypeEnum.md) | [en] Type of resolutiontaken on an agenda item |
| [StateEnum](StateEnum.md) | State of the meeting |
| [VotingTypeEnum](VotingTypeEnum.md) | [en] Type of voting procedure |
| [WorkTypesEnum](WorkTypesEnum.md) |  |


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
