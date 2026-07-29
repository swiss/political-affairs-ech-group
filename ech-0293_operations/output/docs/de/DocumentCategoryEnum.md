## Enum: DocumentCategoryEnum 




_Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards 0292-0297 referenziert werden. Mehrsprachige Labels (DE/FR/IT/RM/EN) sind über `annotations` (Konvention `label_xx`) abgebildet; Erstvorschläge für FR/IT/RM stehen unter Plenum-Review._




<div data-search-exclude markdown="1">

URI: [ops:DocumentCategoryEnum](https://ch.paf.link/schema/operations/DocumentCategoryEnum)

### Zulässige Werte
| Wert | Beschreibung | Zusätzliche Info |
| --- | --- | --- |
| protocol ([meta:vocabulary/document_category/Protocol](meta:vocabulary/document_category/Protocol)) | Protokolle aller Art. Beispiele: Entscheidungsprotokoll, Wortprotokoll, Kurzprotokoll, Tagblatt, Wortlautdokument, Eröffnungsrede, Sprecherliste, Audio- und Videoaufnahmen.  | Title: Protocol<br>|
| voting_result ([meta:vocabulary/document_category/VotingResult](meta:vocabulary/document_category/VotingResult)) | Abstimmungs- und Wahlergebnisse. Beispiele: Abstimmungsprotokoll, Wahlprotokoll, Protokolle namentlicher Abstimmungen.  | Title: Voting result<br>|
| meeting_documents ([meta:vocabulary/document_category/MeetingDocuments](meta:vocabulary/document_category/MeetingDocuments)) | Sitzungsunterlagen, die zu Beginn einer Sitzung zu den Geschäften vorliegen. Beispiele: Traktandenliste, Tagesordnung, Sessionsprogramm, Sessionsvorschau, traktandierte Petitionen, Vorstossliste, Vereidigung/Gelübdenahme, Tagblattbeilagen, Geschäftsverzeichnis, Vorschau, Traktandenvorschau, Vorstoss Dringlichkeit.  | Title: Meeting documents<br>|
| meeting_planning ([meta:vocabulary/document_category/MeetingPlanning](meta:vocabulary/document_category/MeetingPlanning)) | Planungsdokumente für Sitzungen und Sessionen. Beispiele: Einladung, Sitzplan, Arbeitsplanung, Zeitbudget, Geschäftsplanung, Freitagsliste, Fristen für Einzelanträge, Liste der Zutrittsberechtigten, Veranstaltungen während der Session.  | Title: Meeting planning<br>|
| media_release ([meta:vocabulary/document_category/MediaRelease](meta:vocabulary/document_category/MediaRelease)) | Medienmitteilungen.  | Title: Media release<br>|
| group_documents ([meta:vocabulary/document_category/GroupDocuments](meta:vocabulary/document_category/GroupDocuments)) | Unterlagen, die zu einer Gruppe (Kommission, Partei, Delegation etc.) gehören. Beispiele: Statuten, Einsetzungsverfügungen, Kommissionszuweisungen, Jahresberichte, Berichte zu internationalen Aktivitäten.  | Title: Group documents<br>|
| member_directory ([meta:vocabulary/document_category/MemberDirectory](meta:vocabulary/document_category/MemberDirectory)) | Mitgliederverzeichnisse. Beispiele: Mitglieder der eidgenössischen Räte, Mitgliederverzeichnisse von Kommissionen, Gruppen und Freundschaftsgruppen, Liste aller Bundesrätinnen und Bundesräte.  | Title: Member directory<br>|
| person_documents ([meta:vocabulary/document_category/PersonDocuments](meta:vocabulary/document_category/PersonDocuments)) | Personenbezogene Unterlagen. Beispiele: Portraits der Ratsmitglieder, Fotos, Listen der persönlichen Mitarbeitenden.  | Title: Person documents<br>|
| interest_disclosure ([meta:vocabulary/document_category/InterestDisclosure](meta:vocabulary/document_category/InterestDisclosure)) | Register der Interessenbindungen von Ratsmitgliedern. Beispiele: Register der Interessenbindungen Nationalrat, Register der Interessenbindungen Ständerat.  | Title: Interest disclosure<br>|
| other ([meta:vocabulary/document_category/Other](meta:vocabulary/document_category/Other)) | Dokumenttyp, der keiner der definierten Kategorien zugeordnet werden kann oder bei dem die Kategorie nicht bekannt ist. Default-Wert wenn `document_category` nicht explizit gesetzt wird.  | Title: Other<br>|







</div>