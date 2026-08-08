# operations

Sitzungs-Schema für verschiedene gesetzgebende Körperschaften


URI: https://ch.paf.link/schema/operations

Name: operations



## Klassen

| Klasse | Beschreibung |
| --- | --- |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |
| [Date](Date.md) | Ein Datum mit Typangabe (z |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |
| [GroupReference](GroupReference.md) | Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikations... |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderu... |
| [HasIdentification](HasIdentification.md) | Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügu... |
| [HasReferenceIdentification](HasReferenceIdentification.md) | Eine Mixin-Klasse, welche die Slots bereitstellt, mit denen eine Referenz die... |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |
| [IsEventWithDuration](IsEventWithDuration.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkom... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen... |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |
| [JointDebate](JointDebate.md) | Traktanden die gemeinsam behandelt werden |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |
| [Manifestation](Manifestation.md) | FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL a... |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |
| [Motion](Motion.md) | Ein formeller Antrag, der während der Verhandlungen eingereicht wird |
| [MultilingualString](MultilingualString.md) | Ein String, der Text in mehreren Sprachen enthalten kann |
| [MultilingualUri](MultilingualUri.md) | Eine URI zusammen mit der Sprache der Ressource, auf die sie verweist |
| [MultilingualValue](MultilingualValue.md) | Ein mehrsprachiger String mit Angabe der Sprache |
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |
| [Resolution](Resolution.md) | Eine Resolution oder Entscheidung zu einem Traktandum, einschliesslich Abstim... |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |
| [TextSegment](TextSegment.md) | Ein Textsegment wie Querverweise oder Zwischentitel in Sitzungsprotokollen |
| [TotalOther](TotalOther.md) | Zusätzliche Stimmzahlen, wenn mehrere Optionen zur Abstimmung gestellt werden... |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |
| [WorkContainer](WorkContainer.md) | Container für die Dokumente (FRBR Works) dieses Schemas |



## Slots

| Slot | Beschreibung |
| --- | --- |
| [abbreviation](abbreviation.md) | Abkürzung (kann mehrsprachig sein) |
| [actor_fullname](actor_fullname.md) | Vollständiger Name der Akteurin oder des Akteurs bzw |
| [actor_id](actor_id.md) | Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt d... |
| [actor_name](actor_name.md) | Name des politischen Organs (z |
| [administrative_id](administrative_id.md) | Verwaltungs-ID des gesetzgebenden Körpers, wie z |
| [affair_id](affair_id.md) | Die Verbindung zu den Geschäften des Traktandums |
| [agenda_item_category](agenda_item_category.md) | Kategorie für gruppierte Traktanden (z |
| [agenda_item_description](agenda_item_description.md) | Untertitel oder ausführliche Beschreibung des Traktandums |
| [agenda_item_ids](agenda_item_ids.md) | Die Traktanden, die mit der Abstimmung verbunden sind |
| [agenda_item_number](agenda_item_number.md) | Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern) |
| [agenda_item_position](agenda_item_position.md) | Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge |
| [agenda_item_title](agenda_item_title.md) | Titel des Traktandums |
| [agenda_item_type](agenda_item_type.md) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen |
| [agenda_items](agenda_items.md) | Sammlung der Traktanden |
| [attendance_type](attendance_type.md) | Art der individuellen Anwesenheit |
| [attendances](attendances.md) | Sammlung der Anwesenheitslisten |
| [body_key](body_key.md) | Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit... |
| [category](category.md) | Kategorie des Elements |
| [count](count.md) | Die Anzahl der Stimmen für die Kategorie „Andere“ |
| [date_actual](date_actual.md) | Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommnissen (ohne... |
| [date_begin_actual](date_begin_actual.md) | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdaue... |
| [date_begin_planned](date_begin_planned.md) | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_created](date_created.md) | Das Datum, an dem eine Entität erstellt wurde |
| [date_end_actual](date_end_actual.md) | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_end_planned](date_end_planned.md) | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer |
| [date_modified](date_modified.md) | Das Datum, an dem eine Entität zuletzt geändert wurde |
| [date_planned](date_planned.md) | Das geplante Datum eines instantanen Ereignisses oder Vorkommnissen (ohne Zei... |
| [date_type](date_type.md) | Bedeutung des Datums (z |
| [dates](dates.md) | Datumsangaben zum Element, jeweils mit Typangabe |
| [datetime_actual](datetime_actual.md) | Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses oder Vor... |
| [datetime_begin](datetime_begin.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt |
| [datetime_begin_actual](datetime_begin_actual.md) | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnis... |
| [datetime_begin_planned](datetime_begin_planned.md) | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen ... |
| [datetime_created](datetime_created.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde |
| [datetime_end](datetime_end.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet |
| [datetime_end_actual](datetime_end_actual.md) | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnisse... |
| [datetime_end_planned](datetime_end_planned.md) | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mi... |
| [datetime_modified](datetime_modified.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde |
| [datetime_planned](datetime_planned.md) | Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkomm... |
| [description](description.md) | Beschreibender Text zum Element |
| [document_category](document_category.md) | Kategorie des Dokuments |
| [documents](documents.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind |
| [election_type](election_type.md) | Art des Wahlverfahrens |
| [elections](elections.md) | Sammlung der Wahlen |
| [expression_description](expression_description.md) | Beschreibender Text zur Sprachfassung |
| [expression_language](expression_language.md) | Sprachcode im ISO 639-1-Format |
| [expression_title](expression_title.md) | Titel der Sprachfassung |
| [expressions](expressions.md) | Die Sprachfassungen (Expressions) eines Works |
| [format](format.md) | Das Dateiformat der Manifestation (z |
| [global_uri](global_uri.md) | Eine eindeutige, global gültige URI für die Entität |
| [group_id](group_id.md) | Referenz auf die Gruppe oder das Gremium (leichtgewichtiger Snapshot zum Zeit... |
| [group_label](group_label.md) | Name des Gremiums zum Zeitpunkt der Verknüpfung |
| [group_name](group_name.md) | Name der Gruppe oder des Gremiums |
| [has_resolution](has_resolution.md) | Die Resolution oder Entscheidung zu diesem Traktandum |
| [id](id.md) | Eindeutiger Identifikator des Elements |
| [individual_attendances](individual_attendances.md) | Sammlung der einzelnen Anwesenheitsfeststellungen |
| [individual_vote_type](individual_vote_type.md) | Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc |
| [individual_votes](individual_votes.md) | Sammlung der Einzelstimmen |
| [is_active](is_active.md) | Gibt an, ob die Information aktuell gültig ist |
| [label](label.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw |
| [label_abstention](label_abstention.md) | Bedeutung einer Enthaltungsstimme |
| [label_long](label_long.md) | Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu ver... |
| [label_no](label_no.md) | Bedeutung einer „Nein“-Stimme |
| [label_yes](label_yes.md) | Bedeutung einer „Ja“-Stimme |
| [landing_page](landing_page.md) | URL mit weiteren Informationen |
| [language](language.md) | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z |
| [leading_actor_id](leading_actor_id.md) | Das federführende Departement für das Traktandum |
| [legislatures](legislatures.md) | Sammlung der Legislaturperioden |
| [local_id](local_id.md) | Lokaler Identifikator |
| [location](location.md) | Ort, an dem die Sitzung stattfindet (physischer Raum, Videokonferenz oder hyb... |
| [majority_count](majority_count.md) | Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind |
| [majority_type](majority_type.md) | Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw |
| [manifestation_url](manifestation_url.md) | URL, unter der die Dateiform abgerufen werden kann |
| [manifestations](manifestations.md) | Die Dateiformen (Manifestations) einer Expression |
| [media_format](media_format.md) | MIME-Typ der Mediendatei |
| [media_type](media_type.md) | Art des Mediums (Audio, Video, Dokument) |
| [media_url](media_url.md) | URL zur Mediendatei (Audio/Video) |
| [meeting_abbreviation](meeting_abbreviation.md) | Kurzbezeichnung der Session oder Sitzung (z |
| [meeting_type](meeting_type.md) | Art der Sitzung, z |
| [meetings](meetings.md) | Sammlung der Sitzungen |
| [multilingual_value](multilingual_value.md) | Ein mehrsprachiger Wert mit Angabe der Sprache |
| [name](name.md) | Mehrsprachige vollständige Bezeichnung |
| [number](number.md) | Laufende Nummer, z |
| [optional](optional.md) | Gibt an, ob die Sitzung oder Abstimmung optional ist |
| [parent_agenda_item](parent_agenda_item.md) | Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf |
| [parent_attendance](parent_attendance.md) | Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört |
| [parent_legislature](parent_legislature.md) | Der gesetzgebende Körper, auf dem die Sitzung basiert |
| [parent_meeting](parent_meeting.md) | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert |
| [parent_type](parent_type.md) | Typ des übergeordneten Objekts (Sitzung, Traktandum, Wortmeldung, Geschäft) |
| [parent_voting](parent_voting.md) | Die ID der Abstimmung, die mit der Einzelstimme verbunden ist |
| [position](position.md) | Ganzzahlige Position innerhalb der übergeordneten Reihenfolge |
| [protocol_items](protocol_items.md) | Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden |
| [protocol_ref](protocol_ref.md) | Das nach der Sitzung erstellte Protokoll dieser Sitzung |
| [protocols](protocols.md) | Sammlung der Protokolle |
| [reason](reason.md) | Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig) |
| [remark](remark.md) | Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext zu ei... |
| [resolution_type](resolution_type.md) | Art der Resolution zum Traktandum |
| [resolutions](resolutions.md) | Sammlung der Resolutionen |
| [result](result.md) | Ergebnis des Verfahrens |
| [result_text](result_text.md) | Freitext zur Beschreibung des Ergebnisses der Abstimmung, z |
| [role](role.md) | Rolle der Person (z |
| [seat_nr](seat_nr.md) | Die Sitznummer der Einzelstimme, falls zutreffend |
| [sequential_number](sequential_number.md) | Laufende Nummer der Sitzung, die zur Sortierung verwendet wird |
| [sessions](sessions.md) | Sammlung der Sessionen |
| [speaking_actor_id](speaking_actor_id.md) | Der Sprecher oder die Sprecherin bzw |
| [speeches](speeches.md) | Sammlung der Wortmeldungen |
| [start](start.md) | Startangabe oder Position |
| [state](state.md) | Aktueller Status der Sitzung (geplant, abgesagt, verschoben) |
| [state_id](state_id.md) | Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen Zu... |
| [state_name](state_name.md) | Benutzerdefinierte Zustandsbeschreibung für die Sitzung |
| [status](status.md) | Freie Statusbezeichnung, dort verwendet, wo das Status-Enum nicht zutrifft |
| [text](text.md) | Textinhalt des Elements |
| [text_format](text_format.md) | Format des Textes (text, html, html_with_timestamps) |
| [text_segments](text_segments.md) | Sammlung von Textsegmenten (z |
| [text_type](text_type.md) | Typ des Textes (Rohfassung, bearbeitete Fassung) |
| [tie_breaker](tie_breaker.md) | Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde |
| [title](title.md) | Titel des Elements |
| [total](total.md) | Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen |
| [total_absent](total_absent.md) | Gesamtzahl abwesender Mitglieder |
| [total_count](total_count.md) | Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnunge... |
| [total_count_abstention](total_count_abstention.md) | Gesamtzahl der Enthaltungen |
| [total_count_no](total_count_no.md) | Gesamtzahl der „Nein“-Stimmen |
| [total_count_yes](total_count_yes.md) | Gesamtzahl der „Ja“-Stimmen |
| [total_excused](total_excused.md) | Gesamtzahl der entschuldigten Abwesenheiten |
| [total_other](total_other.md) | Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z |
| [total_present](total_present.md) | Gesamtzahl der anwesenden Mitglieder |
| [type](type.md) | Generische Typbezeichnung |
| [type_label](type_label.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen |
| [url](url.md) | Landing Page oder weiterführende Webadresse, mehrsprachig |
| [valid_from](valid_from.md) | Das Datum, ab dem die Information gültig ist |
| [valid_through](valid_through.md) | Das Datum, bis und mit dem die Information gültig ist |
| [value](value.md) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Spr... |
| [version](version.md) | Versionsnummer oder Versionskennung |
| [vote_procedures](vote_procedures.md) | Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung |
| [voting_title](voting_title.md) | Abstimmungstitel bzw |
| [voting_type](voting_type.md) | Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc |
| [votings](votings.md) | Sammlung der Abstimmungen |
| [weight](weight.md) | Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z |
| [wikidata_uri](wikidata_uri.md) | Eine URI, die auf eine Wikidata-Entität verweist, z |
| [work_type](work_type.md) | Art des Dokuments (z |
| [works](works.md) | Die im Container enthaltenen Dokumente (FRBR Works) |
| [xdate](xdate.md) | Der Datumswert selbst |


## Enums

| Aufzählung | Beschreibung |
| --- | --- |
| [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Art des Traktandums, unterscheidet einzelne von gruppierten Traktanden |
| [AttendanceTypeEnum](AttendanceTypeEnum.md) | Art der individuellen Anwesenheit |
| [DateTypesEnum](DateTypesEnum.md) | Bedeutung einer Datumsangabe |
| [DocumentCategoryEnum](DocumentCategoryEnum.md) | Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards 0292-0... |
| [ElectionTypeEnum](ElectionTypeEnum.md) | Art des Wahlverfahrens |
| [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) | Art der Einzelstimme eines Mitglieds |
| [MajorityTypeEnum](MajorityTypeEnum.md) | Art der für die Abstimmung erforderlichen Mehrheit |
| [MeetingTypeEnum](MeetingTypeEnum.md) | Art der Sitzung |
| [ResolutionTypeEnum](ResolutionTypeEnum.md) | Art der Resolution zu einem Traktandum |
| [StateEnum](StateEnum.md) | Status der Sitzung |
| [VotingTypeEnum](VotingTypeEnum.md) | Art des Abstimmungsverfahrens |
| [WorkTypesEnum](WorkTypesEnum.md) | Art eines Dokuments (FRBR Work) |


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
