## Enum: DocumentCategoryEnum 




_[de] Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards 0292-0297 referenziert werden. Mehrsprachige Labels (DE/FR/IT/RM/EN) sind über `annotations` (Konvention `label_xx`) abgebildet; Erstvorschläge für FR/IT/RM stehen unter Plenum-Review._

_[en] Categories for classifying documents referenced in eCH standards 0292-0297. Multilingual labels (DE/FR/IT/RM/EN) are encoded via `annotations` (convention `label_xx`); first proposals for FR/IT/RM are pending plenum review._

__



<div data-search-exclude markdown="1">

URI: [ops:DocumentCategoryEnum](https://ch.paf.link/schema/operations/DocumentCategoryEnum)

### Permissible Values
| Value | Description | Additional Info |
| --- | --- | --- |
| protocol ([meta:vocabulary/document_category/Protocol](meta:vocabulary/document_category/Protocol)) | [de] Protokolle aller Art. Beispiele: Entscheidungsprotokoll, Wortprotokoll, Kurzprotokoll, Tagblatt, Wortlautdokument, Eröffnungsrede, Sprecherliste, Audio- und Videoaufnahmen. [en] Protocols of any kind. Examples: decision protocol, verbatim protocol, short protocol, daily journal (Tagblatt), opening speech, speaker list, audio and video recordings.  | Title: Protocol<br>|
| voting_result ([meta:vocabulary/document_category/VotingResult](meta:vocabulary/document_category/VotingResult)) | [de] Abstimmungs- und Wahlergebnisse. Beispiele: Abstimmungsprotokoll, Wahlprotokoll, Protokolle namentlicher Abstimmungen. [en] Voting and election results. Examples: voting protocol, election protocol, roll-call voting protocols.  | Title: Voting result<br>|
| meeting_documents ([meta:vocabulary/document_category/MeetingDocuments](meta:vocabulary/document_category/MeetingDocuments)) | [de] Sitzungsunterlagen, die zu Beginn einer Sitzung zu den Geschäften vorliegen. Beispiele: Traktandenliste, Tagesordnung, Sessionsprogramm, Sessionsvorschau, traktandierte Petitionen, Vorstossliste, Vereidigung/Gelübdenahme, Tagblattbeilagen, Geschäftsverzeichnis, Vorschau, Traktandenvorschau, Vorstoss Dringlichkeit. [en] Meeting documents available at the start of a meeting concerning the affairs. Examples: agenda list, daily agenda, session programme, session preview, agendaed petitions, motion list, oath ceremony, daily journal supplements, affairs directory.  | Title: Meeting documents<br>|
| meeting_planning ([meta:vocabulary/document_category/MeetingPlanning](meta:vocabulary/document_category/MeetingPlanning)) | [de] Planungsdokumente für Sitzungen und Sessionen. Beispiele: Einladung, Sitzplan, Arbeitsplanung, Zeitbudget, Geschäftsplanung, Freitagsliste, Fristen für Einzelanträge, Liste der Zutrittsberechtigten, Veranstaltungen während der Session. [en] Planning documents for meetings and sessions. Examples: invitation, seating plan, work schedule, time budget, affairs planning, friday list, amendment deadlines, access authorization list, session events.  | Title: Meeting planning<br>|
| media_release ([meta:vocabulary/document_category/MediaRelease](meta:vocabulary/document_category/MediaRelease)) | [de] Medienmitteilungen. [en] Press releases.  | Title: Media release<br>|
| group_documents ([meta:vocabulary/document_category/GroupDocuments](meta:vocabulary/document_category/GroupDocuments)) | [de] Unterlagen, die zu einer Gruppe (Kommission, Partei, Delegation etc.) gehören. Beispiele: Statuten, Einsetzungsverfügungen, Kommissionszuweisungen, Jahresberichte, Berichte zu internationalen Aktivitäten. [en] Documents belonging to a group (committee, party, delegation, etc.). Examples: statutes, establishment decrees, committee allocations, annual reports, reports on international activities.  | Title: Group documents<br>|
| member_directory ([meta:vocabulary/document_category/MemberDirectory](meta:vocabulary/document_category/MemberDirectory)) | [de] Mitgliederverzeichnisse. Beispiele: Mitglieder der eidgenössischen Räte, Mitgliederverzeichnisse von Kommissionen, Gruppen und Freundschaftsgruppen, Liste aller Bundesrätinnen und Bundesräte. [en] Member directories. Examples: members of the federal councils, member directories of committees, groups and friendship groups, list of all Federal Councillors.  | Title: Member directory<br>|
| person_documents ([meta:vocabulary/document_category/PersonDocuments](meta:vocabulary/document_category/PersonDocuments)) | [de] Personenbezogene Unterlagen. Beispiele: Portraits der Ratsmitglieder, Fotos, Listen der persönlichen Mitarbeitenden. [en] Person-related documents. Examples: portraits of council members, photos, lists of personal staff.  | Title: Person documents<br>|
| interest_disclosure ([meta:vocabulary/document_category/InterestDisclosure](meta:vocabulary/document_category/InterestDisclosure)) | [de] Register der Interessenbindungen von Ratsmitgliedern. Beispiele: Register der Interessenbindungen Nationalrat, Register der Interessenbindungen Ständerat. [en] Registers of interest disclosures of council members. Examples: register of interest disclosures National Council, register of interest disclosures Council of States.  | Title: Interest disclosure<br>|
| other ([meta:vocabulary/document_category/Other](meta:vocabulary/document_category/Other)) | [de] Dokumenttyp, der keiner der definierten Kategorien zugeordnet werden kann oder bei dem die Kategorie nicht bekannt ist. Default-Wert wenn `document_category` nicht explizit gesetzt wird. [en] Document type that cannot be assigned to any of the defined categories or where the category is unknown. Default value if `document_category` is not set explicitly.  | Title: Other<br>|







</div>