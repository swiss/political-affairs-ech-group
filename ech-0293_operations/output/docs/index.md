# operations

[en] Meeting Schema for various legislative bodies
[de] Sitzungs Schema für verschiedene gesetzgebende Körperschaften


URI: https://ch.paf.link/schema/operations

Name: operations



## Classes

| Class | Description |
| --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |
| [Container](Container.md) |  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |
| [HasCreationModificationDates](HasCreationModificationDates.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Ä... |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |
| [HasTemporalValidity](HasTemporalValidity.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gülti... |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereign... |
| [JointDebate](JointDebate.md) | [en] Agenda Items which are debated together |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |
| [MultilingualValue](MultilingualValue.md) | [de] Ein mehrsprachiger String mit Angabe der Sprache |
| [Resolution](Resolution.md) | [en] A resolutionor decision taken on an agenda item, including voting proced... |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |
| [TotalOther](TotalOther.md) | [en] Additional vote counts when multiple options are presented (e |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) |  |
| [actor_fullname](actor_fullname.md) | Full name of the actor/person |
| [actor_id](actor_id.md) | [en] The political body organized by the term of office (e |
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
| [date_actual](date_actual.md) | [de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens (oh... |
| [date_begin_actual](date_begin_actual.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitda... |
| [date_begin_planned](date_begin_planned.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer |
| [date_created](date_created.md) | [de] Das Datum, an dem eine Entität erstellt wurde |
| [date_end_actual](date_end_actual.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdaue... |
| [date_end_planned](date_end_planned.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer |
| [date_modified](date_modified.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde |
| [date_planned](date_planned.md) | [de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens (ohne Z... |
| [datetime_actual](datetime_actual.md) | [de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses ode... |
| [datetime_begin](datetime_begin.md) | [en] The date and time when the meeting or voting begins |
| [datetime_begin_actual](datetime_begin_actual.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorko... |
| [datetime_begin_planned](datetime_begin_planned.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommen... |
| [datetime_created](datetime_created.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde |
| [datetime_end](datetime_end.md) | [en] The date and time when the meeting or voting ends |
| [datetime_end_actual](datetime_end_actual.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkomm... |
| [datetime_end_planned](datetime_end_planned.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens ... |
| [datetime_modified](datetime_modified.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde |
| [datetime_planned](datetime_planned.md) | [de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vo... |
| [description](description.md) |  |
| [election_type](election_type.md) | Type of election procedure |
| [elections](elections.md) | Collection of election records |
| [global_uri](global_uri.md) | [de] Eine eindeutige, global gültige URI für die Entität |
| [group_id](group_id.md) | Identifier of the group or body |
| [group_name](group_name.md) | Name of the group or body |
| [has_resolution](has_resolution.md) | [en] The resolutionor decision taken on this agenda item |
| [individual_attendances](individual_attendances.md) | Collection of individual attendance records |
| [individual_vote_type](individual_vote_type.md) | [en] Type of vote cast (yes, no, abstention, absent, etc |
| [individual_votes](individual_votes.md) | Collection of individual vote records |
| [is_active](is_active.md) | [de] Gibt an, ob die Information aktuell gültig ist |
| [label](label.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... |
| [label_abstention](label_abstention.md) | [en] Meaning of an 'abstention' vote |
| [label_long](label_long.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel z... |
| [label_no](label_no.md) | [en] Meaning of a 'no' vote |
| [label_yes](label_yes.md) | [en] Meaning of a 'yes' vote |
| [landing_page](landing_page.md) | [en] URL providing further information |
| [language](language.md) | [de] Sprachcode im ISO 639-1 Format |
| [leading_actor_id](leading_actor_id.md) | [en] The leading department for the agenda item |
| [legislatures](legislatures.md) |  |
| [local_id](local_id.md) | [de] Lokaler Identifikator |
| [location](location.md) |  |
| [majority_count](majority_count.md) | [en] Number of votes required for the relevant majority threshold |
| [majority_type](majority_type.md) | [en] Type of majority required for the vote (absolute, two-thirds, etc |
| [media_format](media_format.md) | MIME type of the media file |
| [media_type](media_type.md) | Type of media (audio, video, document) |
| [media_url](media_url.md) | URL to media file (audio/video) |
| [meeting_type](meeting_type.md) | Type of the meeting, e |
| [meetings](meetings.md) |  |
| [multilingual_value](multilingual_value.md) | [de] Ein mehrsprachiger Wert mit Angabe der Sprache |
| [name](name.md) |  |
| [number](number.md) |  |
| [optional](optional.md) | [en] Indicates if the meeting or voting is optional |
| [parent_agenda_item](parent_agenda_item.md) | [en] If needed, this slot builds a hierarchy of agenda items |
| [parent_legislature](parent_legislature.md) | [en] The legislative body in which the meeting is based |
| [parent_meeting](parent_meeting.md) | [en] The linked meeting ID that groups the current meeting |
| [parent_type](parent_type.md) | Type of parent object (meeting, agenda, speech, affair) |
| [parent_voting](parent_voting.md) | [en] The ID of the voting associated with the individual vote |
| [position](position.md) |  |
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
| [text_type](text_type.md) | [en] Type of text (raw draft, edited version) |
| [tie_breaker](tie_breaker.md) | [en] Indicates if a tie-breaker was used in the voting |
| [title](title.md) |  |
| [total](total.md) | [en] Total number of votes, excluding absent and president's vote |
| [total_absent](total_absent.md) | [en] Total number of absent members |
| [total_count_abstention](total_count_abstention.md) | [en] Total number of abstentions |
| [total_count_no](total_count_no.md) | [en] Total number of 'no' votes |
| [total_count_yes](total_count_yes.md) | [en] Total number of 'yes' votes |
| [total_excused](total_excused.md) | Total number of excused absences |
| [total_other](total_other.md) | [en] Used when multiple options are presented for voting (e |
| [total_present](total_present.md) | Total number of members present |
| [type](type.md) |  |
| [type_label](type_label.md) | [en] Custom type label when standard type values don't apply |
| [url](url.md) |  |
| [valid_from](valid_from.md) | [de] Das Datum, ab dem die Information gültig ist |
| [valid_through](valid_through.md) | [de] Das Datum, bis und mit dem die Information gültig ist |
| [value](value.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ... |
| [version](version.md) | Version number or identifier |
| [vote_procedures](vote_procedures.md) | [en] Procedures for voting, such as secret ballot or open vote |
| [voting_title](voting_title.md) | [en] Title or question being voted on |
| [voting_type](voting_type.md) | [en] Type of voting procedure (preliminary, final, secret, etc |
| [votings](votings.md) | Collection of voting records |
| [weight](weight.md) | [en] The number of votes held by the individual, if applicable (e |
| [wikidata_uri](wikidata_uri.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | [en] Type of agenda item, distinguishing individual items from grouped items |
| [AttendanceTypeEnum](AttendanceTypeEnum.md) | [en] Type of individual attendance |
| [ElectionTypeEnum](ElectionTypeEnum.md) | [en] Type of election procedure |
| [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | [en] Type of individual vote cast by a member |
| [MajorityTypeEnum](MajorityTypeEnum.md) | Type of majority required for the vote |
| [MeetingTypeEnum](MeetingTypeEnum.md) | Type of the meeting |
| [ResolutionTypeEnum](ResolutionTypeEnum.md) | [en] Type of resolutiontaken on an agenda item |
| [StateEnum](StateEnum.md) | State of the meeting |
| [VotingTypeEnum](VotingTypeEnum.md) | [en] Type of voting procedure |


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
