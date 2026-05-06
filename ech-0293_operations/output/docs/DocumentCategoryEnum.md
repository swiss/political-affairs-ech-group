# Enum: DocumentCategoryEnum 




_[de] Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards 0292-0297 referenziert werden. Mehrsprachige Labels (DE/FR/IT/RM/EN) sind über `annotations` (Konvention `label_xx`) abgebildet; Erstvorschläge für FR/IT/RM stehen unter Plenum-Review._

_[en] Categories for classifying documents referenced in eCH standards 0292-0297. Multilingual labels (DE/FR/IT/RM/EN) are encoded via `annotations` (convention `label_xx`); first proposals for FR/IT/RM are pending plenum review._

__



URI: [ops:DocumentCategoryEnum](https://ch.paf.link/schema/operations/DocumentCategoryEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| protocol | meta:vocabulary/document_category/Protocol | [de] Protokolle aller Art | Title: Protocol<br>|
| voting_result | meta:vocabulary/document_category/VotingResult | [de] Abstimmungs- und Wahlergebnisse | Title: Voting result<br>|
| meeting_documents | meta:vocabulary/document_category/MeetingDocuments | [de] Sitzungsunterlagen, die zu Beginn einer Sitzung zu den Geschäften vorlie... | Title: Meeting documents<br>|
| meeting_planning | meta:vocabulary/document_category/MeetingPlanning | [de] Planungsdokumente für Sitzungen und Sessionen | Title: Meeting planning<br>|
| media_release | meta:vocabulary/document_category/MediaRelease | [de] Medienmitteilungen | Title: Media release<br>|
| group_documents | meta:vocabulary/document_category/GroupDocuments | [de] Unterlagen, die zu einer Gruppe (Kommission, Partei, Delegation etc | Title: Group documents<br>|
| member_directory | meta:vocabulary/document_category/MemberDirectory | [de] Mitgliederverzeichnisse | Title: Member directory<br>|
| person_documents | meta:vocabulary/document_category/PersonDocuments | [de] Personenbezogene Unterlagen | Title: Person documents<br>|
| interest_disclosure | meta:vocabulary/document_category/InterestDisclosure | [de] Register der Interessenbindungen von Ratsmitgliedern | Title: Interest disclosure<br>|
| other | meta:vocabulary/document_category/Other | [de] Dokumenttyp, der keiner der definierten Kategorien zugeordnet werden kan... | Title: Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [document_category](document_category.md) | [de] Kategorie des Dokuments |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: DocumentCategoryEnum
description: '[de] Kategorien zur Klassifikation von Dokumenten, die in den eCH Standards
  0292-0297 referenziert werden. Mehrsprachige Labels (DE/FR/IT/RM/EN) sind über `annotations`
  (Konvention `label_xx`) abgebildet; Erstvorschläge für FR/IT/RM stehen unter Plenum-Review.

  [en] Categories for classifying documents referenced in eCH standards 0292-0297.
  Multilingual labels (DE/FR/IT/RM/EN) are encoded via `annotations` (convention `label_xx`);
  first proposals for FR/IT/RM are pending plenum review.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  protocol:
    text: protocol
    description: '[de] Protokolle aller Art. Beispiele: Entscheidungsprotokoll, Wortprotokoll,
      Kurzprotokoll, Tagblatt, Wortlautdokument, Eröffnungsrede, Sprecherliste, Audio-
      und Videoaufnahmen.

      [en] Protocols of any kind. Examples: decision protocol, verbatim protocol,
      short protocol, daily journal (Tagblatt), opening speech, speaker list, audio
      and video recordings.

      '
    meaning: meta:vocabulary/document_category/Protocol
    annotations:
      label_de:
        tag: label_de
        value: Protokoll
      label_fr:
        tag: label_fr
        value: Procès-verbal
      label_it:
        tag: label_it
        value: Verbale
      label_rm:
        tag: label_rm
        value: Protocol
      label_en:
        tag: label_en
        value: Minutes
    title: Protocol
  voting_result:
    text: voting_result
    description: '[de] Abstimmungs- und Wahlergebnisse. Beispiele: Abstimmungsprotokoll,
      Wahlprotokoll, Protokolle namentlicher Abstimmungen.

      [en] Voting and election results. Examples: voting protocol, election protocol,
      roll-call voting protocols.

      '
    meaning: meta:vocabulary/document_category/VotingResult
    annotations:
      label_de:
        tag: label_de
        value: Abstimmungsergebnis
      label_fr:
        tag: label_fr
        value: Résultat du vote
      label_it:
        tag: label_it
        value: Risultato della votazione
      label_rm:
        tag: label_rm
        value: Resultat da votaziun
      label_en:
        tag: label_en
        value: Voting result
    title: Voting result
  meeting_documents:
    text: meeting_documents
    description: '[de] Sitzungsunterlagen, die zu Beginn einer Sitzung zu den Geschäften
      vorliegen. Beispiele: Traktandenliste, Tagesordnung, Sessionsprogramm, Sessionsvorschau,
      traktandierte Petitionen, Vorstossliste, Vereidigung/Gelübdenahme, Tagblattbeilagen,
      Geschäftsverzeichnis, Vorschau, Traktandenvorschau, Vorstoss Dringlichkeit.

      [en] Meeting documents available at the start of a meeting concerning the affairs.
      Examples: agenda list, daily agenda, session programme, session preview, agendaed
      petitions, motion list, oath ceremony, daily journal supplements, affairs directory.

      '
    meaning: meta:vocabulary/document_category/MeetingDocuments
    annotations:
      label_de:
        tag: label_de
        value: Sitzungsunterlagen
      label_fr:
        tag: label_fr
        value: Documents de séance
      label_it:
        tag: label_it
        value: Documenti di seduta
      label_rm:
        tag: label_rm
        value: Documents da sesida
      label_en:
        tag: label_en
        value: Meeting documents
    title: Meeting documents
  meeting_planning:
    text: meeting_planning
    description: '[de] Planungsdokumente für Sitzungen und Sessionen. Beispiele: Einladung,
      Sitzplan, Arbeitsplanung, Zeitbudget, Geschäftsplanung, Freitagsliste, Fristen
      für Einzelanträge, Liste der Zutrittsberechtigten, Veranstaltungen während der
      Session.

      [en] Planning documents for meetings and sessions. Examples: invitation, seating
      plan, work schedule, time budget, affairs planning, friday list, amendment deadlines,
      access authorization list, session events.

      '
    meaning: meta:vocabulary/document_category/MeetingPlanning
    annotations:
      label_de:
        tag: label_de
        value: Sitzungsplanung
      label_fr:
        tag: label_fr
        value: Planification de séance
      label_it:
        tag: label_it
        value: Pianificazione della seduta
      label_rm:
        tag: label_rm
        value: Planisaziun da sesida
      label_en:
        tag: label_en
        value: Meeting planning
    title: Meeting planning
  media_release:
    text: media_release
    description: '[de] Medienmitteilungen.

      [en] Press releases.

      '
    meaning: meta:vocabulary/document_category/MediaRelease
    annotations:
      label_de:
        tag: label_de
        value: Medienmitteilung
      label_fr:
        tag: label_fr
        value: Communiqué de presse
      label_it:
        tag: label_it
        value: Comunicato stampa
      label_rm:
        tag: label_rm
        value: Communicaziun da medias
      label_en:
        tag: label_en
        value: Media release
    title: Media release
  group_documents:
    text: group_documents
    description: '[de] Unterlagen, die zu einer Gruppe (Kommission, Partei, Delegation
      etc.) gehören. Beispiele: Statuten, Einsetzungsverfügungen, Kommissionszuweisungen,
      Jahresberichte, Berichte zu internationalen Aktivitäten.

      [en] Documents belonging to a group (committee, party, delegation, etc.). Examples:
      statutes, establishment decrees, committee allocations, annual reports, reports
      on international activities.

      '
    meaning: meta:vocabulary/document_category/GroupDocuments
    annotations:
      label_de:
        tag: label_de
        value: Gruppenunterlagen
      label_fr:
        tag: label_fr
        value: Documents de groupe
      label_it:
        tag: label_it
        value: Documenti di gruppo
      label_rm:
        tag: label_rm
        value: Documents da gruppa
      label_en:
        tag: label_en
        value: Group documents
    title: Group documents
  member_directory:
    text: member_directory
    description: '[de] Mitgliederverzeichnisse. Beispiele: Mitglieder der eidgenössischen
      Räte, Mitgliederverzeichnisse von Kommissionen, Gruppen und Freundschaftsgruppen,
      Liste aller Bundesrätinnen und Bundesräte.

      [en] Member directories. Examples: members of the federal councils, member directories
      of committees, groups and friendship groups, list of all Federal Councillors.

      '
    meaning: meta:vocabulary/document_category/MemberDirectory
    annotations:
      label_de:
        tag: label_de
        value: Mitgliederverzeichnis
      label_fr:
        tag: label_fr
        value: Liste des membres
      label_it:
        tag: label_it
        value: Elenco dei membri
      label_rm:
        tag: label_rm
        value: Glista dals commembers
      label_en:
        tag: label_en
        value: Member directory
    title: Member directory
  person_documents:
    text: person_documents
    description: '[de] Personenbezogene Unterlagen. Beispiele: Portraits der Ratsmitglieder,
      Fotos, Listen der persönlichen Mitarbeitenden.

      [en] Person-related documents. Examples: portraits of council members, photos,
      lists of personal staff.

      '
    meaning: meta:vocabulary/document_category/PersonDocuments
    annotations:
      label_de:
        tag: label_de
        value: Personenunterlagen
      label_fr:
        tag: label_fr
        value: Documents personnels
      label_it:
        tag: label_it
        value: Documenti personali
      label_rm:
        tag: label_rm
        value: Documents da persuna
      label_en:
        tag: label_en
        value: Person documents
    title: Person documents
  interest_disclosure:
    text: interest_disclosure
    description: '[de] Register der Interessenbindungen von Ratsmitgliedern. Beispiele:
      Register der Interessenbindungen Nationalrat, Register der Interessenbindungen
      Ständerat.

      [en] Registers of interest disclosures of council members. Examples: register
      of interest disclosures National Council, register of interest disclosures Council
      of States.

      '
    meaning: meta:vocabulary/document_category/InterestDisclosure
    annotations:
      label_de:
        tag: label_de
        value: Interessenbindungen
      label_fr:
        tag: label_fr
        value: Liens d'intérêts
      label_it:
        tag: label_it
        value: Relazioni d'interesse
      label_rm:
        tag: label_rm
        value: Colliaziuns d'interess
      label_en:
        tag: label_en
        value: Interest disclosures
    title: Interest disclosure
  other:
    text: other
    description: '[de] Dokumenttyp, der keiner der definierten Kategorien zugeordnet
      werden kann oder bei dem die Kategorie nicht bekannt ist. Default-Wert wenn
      `document_category` nicht explizit gesetzt wird.

      [en] Document type that cannot be assigned to any of the defined categories
      or where the category is unknown. Default value if `document_category` is not
      set explicitly.

      '
    meaning: meta:vocabulary/document_category/Other
    annotations:
      label_de:
        tag: label_de
        value: Andere
      label_fr:
        tag: label_fr
        value: Autre
      label_it:
        tag: label_it
        value: Altro
      label_rm:
        tag: label_rm
        value: Auter
      label_en:
        tag: label_en
        value: Other
    title: Other

```
</details>