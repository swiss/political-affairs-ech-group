# operations

Sitzungs-Schema für verschiedene gesetzgebende Körperschaften


URI: https://ch.paf.link/schema/operations

Name: operations



## Klassen

| Klasse | Beschreibung |
| --- | --- |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |
| [Date](Date.md) | Ein Datum mit Typangabe (z |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |
| [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum... |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderu... |
| [HasIdentification](HasIdentification.md) | Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügu... |
| [HasReferenceIdentification](HasReferenceIdentification.md) | Eine Mixin-Klasse, welche die Slots bereitstellt, mit denen eine Referenz die... |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |
| [IndividualVote](IndividualVote.md) | Die Stimme, die ein einzelnes Mitglied in einer Abstimmung abgibt |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |
| [IsEventWithDuration](IsEventWithDuration.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkom... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen... |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |
| [JointDebate](JointDebate.md) | Eine gemeinsame Beratung: Mehrere Traktanden werden zusammen behandelt, etwa ... |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |
| [Manifestation](Manifestation.md) | FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL a... |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |
| [Motion](Motion.md) | Ein formaler Antrag, der während der Beratung gestellt wird, etwa ein Änderun... |
| [MultilingualString](MultilingualString.md) | Ein String, der Text in mehreren Sprachen enthalten kann |
| [MultilingualUri](MultilingualUri.md) | Eine URI zusammen mit der Sprache der Ressource, auf die sie verweist |
| [MultilingualValue](MultilingualValue.md) | Ein mehrsprachiger String mit Angabe der Sprache |
| [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum... |
| [Protocol](Protocol.md) | Das Protokoll einer Sitzung, nach der Sitzung erstellt und pro Sitzung genau ... |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |
| [Resolution](Resolution.md) | Der formale Beschluss zu einem Traktandum, einschliesslich der angewandten Ab... |
| [Session](Session.md) | Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislatu... |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |
| [TextSegment](TextSegment.md) | Ein Textsegment wie Querverweise oder Zwischentitel |
| [TotalOther](TotalOther.md) | Stimmenzahl für eine Option einer Auswahlabstimmung |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |
| [WorkContainer](WorkContainer.md) | Container für die Dokumente (FRBR Works) dieses Schemas |



## Slots

| Slot | Beschreibung |
| --- | --- |
| [abbreviation](abbreviation.md) | Abkürzung (kann mehrsprachig sein) |
| [actor_fullname](actor_fullname.md) | Vollständiger Name der Akteurin oder des Akteurs bzw |
| [actor_id](actor_id.md) | Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfu... |
| [actor_name](actor_name.md) | Name des politischen Organs im Klartext (z |
| [administrative_id](administrative_id.md) | Verwaltungs-ID des gesetzgebenden Körpers, wie z |
| [affair_id](affair_id.md) | Identifikator des Geschäfts (eCH-0295), auf das sich der Eintrag bezieht |
| [agenda_item_category](agenda_item_category.md) | Freie Kategorisierung des Traktandums nach Inhalt oder Gruppierung, z |
| [agenda_item_description](agenda_item_description.md) | Untertitel oder ausführliche Beschreibung des Traktandums |
| [agenda_item_ids](agenda_item_ids.md) | Die Traktanden, die mit der Abstimmung verbunden sind |
| [agenda_item_number](agenda_item_number.md) | Nummer des Traktandums auf der Traktandenliste, z |
| [agenda_item_position](agenda_item_position.md) | Ganzzahlige Position des Traktandums im Sitzungsablauf, massgebend für Sortie... |
| [agenda_item_title](agenda_item_title.md) | Titel des Traktandums |
| [agenda_item_type](agenda_item_type.md) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen |
| [agenda_items](agenda_items.md) | Für diese Sitzung oder Session geplante Traktanden, eingebettet als Liste |
| [attendance_type](attendance_type.md) | Art der individuellen Anwesenheit |
| [attendances](attendances.md) | Sammlung der Anwesenheitslisten |
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
| [group_id](group_id.md) | Referenz auf die Gruppe oder das Gremium (Momentaufnahme zum Zeitpunkt der Ve... |
| [group_label](group_label.md) | Name des Gremiums zum Zeitpunkt der Verknüpfung |
| [group_name](group_name.md) | Name der Gruppe oder des Gremiums im Klartext, zusätzlich zur Referenz `group... |
| [has_protocol](has_protocol.md) | Referenz auf das nach der Sitzung erstellte Protokoll dieser Sitzung |
| [has_resolution](has_resolution.md) | Der formale Beschluss zu diesem Traktandum, z |
| [id](id.md) | Eindeutiger Identifikator des Elements |
| [individual_attendances](individual_attendances.md) | Sammlung der einzelnen Anwesenheitsfeststellungen |
| [individual_vote_type](individual_vote_type.md) | Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc |
| [individual_votes](individual_votes.md) | Sammlung der Einzelstimmen |
| [is_active](is_active.md) | Gibt an, ob die Information aktuell gültig ist |
| [joint_agenda_item_ids](joint_agenda_item_ids.md) | Identifikatoren der gemeinsam behandelten Traktanden (AgendaItem oder Protoco... |
| [joint_debates](joint_debates.md) | An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum die ... |
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
| [location](location.md) | Ort, an dem die Sitzung stattfindet — der physische Raum („Bundeshaus, Nation... |
| [majority_count](majority_count.md) | Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind |
| [majority_type](majority_type.md) | Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw |
| [manifestation_url](manifestation_url.md) | URL, unter der die Dateiform abgerufen werden kann |
| [manifestations](manifestations.md) | Die Dateiformen (Manifestations) einer Expression |
| [media_format](media_format.md) | MIME-Typ der Mediendatei |
| [media_type](media_type.md) | Art des Mediums (Audio, Video, Dokument) |
| [media_url](media_url.md) | URL zur Mediendatei (Audio/Video) |
| [meeting_abbreviation](meeting_abbreviation.md) | Kurzbezeichnung der Session oder Sitzung (z |
| [meetings](meetings.md) | Sammlung der Sitzungen |
| [multilingual_value](multilingual_value.md) | Ein mehrsprachiger Wert mit Angabe der Sprache |
| [name](name.md) | Mehrsprachige vollständige Bezeichnung |
| [number](number.md) | Nummer der Session oder Sitzung, wie sie das Organ vergibt, z |
| [optional](optional.md) | Gibt an, ob die Sitzung oder Abstimmung optional ist |
| [parent_agenda_item](parent_agenda_item.md) | Identifikator des Traktandums, zu dem dieser Eintrag gehört |
| [parent_attendance](parent_attendance.md) | Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört |
| [parent_legislature](parent_legislature.md) | Identifikator der Legislaturperiode, zu der die Session oder Sitzung gehört |
| [parent_meeting](parent_meeting.md) | Identifikator der Sitzung, zu der dieser Eintrag gehört |
| [parent_protocol](parent_protocol.md) | Das Protokoll, in dem die Abstimmung oder Wahl festgehalten ist |
| [parent_protocol_item](parent_protocol_item.md) | Das protokollierte Traktandum (ProtocolItem), unter dem abgestimmt oder gewäh... |
| [parent_session](parent_session.md) | Identifikator der Session, zu der die Sitzung gehört |
| [parent_type](parent_type.md) | Typ des übergeordneten Objekts (Sitzung, Traktandum, Wortmeldung, Geschäft) |
| [parent_voting](parent_voting.md) | Die ID der Abstimmung, die mit der Einzelstimme verbunden ist |
| [position](position.md) | Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z |
| [protocol_items](protocol_items.md) | Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden |
| [protocols](protocols.md) | Sammlung der Protokolle |
| [reason](reason.md) | Grund für Abwesenheit, Verspätung oder Vertretung (Freitext, mehrsprachig) |
| [remark](remark.md) | Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext zu ei... |
| [resolution_type](resolution_type.md) | Art der Resolution zum Traktandum |
| [resolutions](resolutions.md) | Sammlung der Resolutionen |
| [result](result.md) | Ergebnis des Verfahrens |
| [result_text](result_text.md) | Freitext, der das Ergebnis beschreibt, z |
| [role](role.md) | Rolle der Person (z |
| [seat_nr](seat_nr.md) | Die Sitznummer der Einzelstimme, falls zutreffend |
| [sequential_number](sequential_number.md) | Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung ver... |
| [sessions](sessions.md) | Sammlung der Sessionen |
| [spatial](spatial.md) | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantons... |
| [speaking_actor_id](speaking_actor_id.md) | Der Sprecher oder die Sprecherin bzw |
| [speeches](speeches.md) | Sammlung der Wortmeldungen |
| [start](start.md) | Startangabe oder Position |
| [state](state.md) | Ob die Sitzung überhaupt wie vorgesehen stattfindet (geplant, abgesagt, versc... |
| [state_id](state_id.md) | Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum oder auf ... |
| [state_name](state_name.md) | Abweichende, freitextliche Statusbezeichnung, wo die Status-Aufzählung nicht ... |
| [status](status.md) | Freie Statusbezeichnung, dort verwendet, wo das Status-Enum nicht zutrifft |
| [text](text.md) | Textinhalt des Elements |
| [text_format](text_format.md) | Format des Textes (text, html, html_with_timestamps) |
| [text_segments](text_segments.md) | Sammlung von Textsegmenten (z |
| [text_type](text_type.md) | Typ des Textes (Rohfassung, bearbeitete Fassung) |
| [tie_breaker](tie_breaker.md) | Gibt an, ob das Ergebnis bei Stimmengleichheit durch den Stichentscheid der P... |
| [title](title.md) | Titel des Elements |
| [total](total.md) | Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen |
| [total_absent](total_absent.md) | Anzahl abwesender Mitglieder, die nicht teilnehmen konnten |
| [total_count](total_count.md) | Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnunge... |
| [total_count_abstention](total_count_abstention.md) | Gesamtzahl der Enthaltungen |
| [total_count_no](total_count_no.md) | Gesamtzahl der „Nein“-Stimmen |
| [total_count_yes](total_count_yes.md) | Gesamtzahl der „Ja“-Stimmen |
| [total_excused](total_excused.md) | Gesamtzahl der entschuldigten Abwesenheiten |
| [total_other](total_other.md) | Stimmenzahlen für die Optionen einer Auswahlabstimmung, ein Eintrag pro Optio... |
| [total_present](total_present.md) | Gesamtzahl der anwesenden Mitglieder |
| [type](type.md) | Generische Typbezeichnung |
| [type_label](type_label.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen |
| [url](url.md) | Landing Page oder weiterführende Webadresse, mehrsprachig |
| [valid_from](valid_from.md) | Das Datum, ab dem die Information gültig ist |
| [valid_through](valid_through.md) | Das Datum, bis und mit dem die Information gültig ist |
| [value](value.md) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Spr... |
| [version](version.md) | Versionsnummer oder Versionskennung |
| [vote_procedures](vote_procedures.md) | Verfahren, in denen abgestimmt wurde |
| [voting_title](voting_title.md) | Abstimmungstitel bzw |
| [voting_type](voting_type.md) | Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc |
| [votings](votings.md) | Sammlung der Abstimmungen |
| [weight](weight.md) | Stimmgewicht des Mitglieds; im Normalfall 1 |
| [wikidata_uri](wikidata_uri.md) | Eine URI, die auf eine Wikidata-Entität verweist, z |
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
| [ResolutionTypeEnum](ResolutionTypeEnum.md) | Art der Resolution zu einem Traktandum |
| [StateEnum](StateEnum.md) | Status der Sitzung |
| [VotingTypeEnum](VotingTypeEnum.md) | Art des Abstimmungsverfahrens |


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
