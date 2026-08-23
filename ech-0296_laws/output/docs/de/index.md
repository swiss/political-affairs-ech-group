# eCH-0296 Erlasse und Gesetzestexte

LinkML-Schema für das Fedlex-spezifische Subset von AkomaNtoso 3.0 für schweizerische Bundeserlasse (eCH-0296). Modelliert die vollständige Dokumentenstruktur (act, FRBR-Metadaten, Vorspann, Hauptteil, Gesetzeshierarchie, Artikelinhalt) und kodiert alle Fedlex-Schematron-Constraints (AKN-fedlex-1.sch) als Annotierungen.


URI: https://ld.ech.ch/schema/0296/laws

Name: ech-0296-laws-schema



## Klassen

| Klasse | Beschreibung |
| --- | --- |
| [Act](Act.md) | Das Erlasselement (akn:act) |
| [ActBody](ActBody.md) | Der Hauptteil des Erlasses (akn:body) mit der Gesetzeshierarchie |
| [ActiveModifications](ActiveModifications.md) | Die Änderungen, die dieser Erlass an anderen vornimmt |
| [ActMeta](ActMeta.md) | Metadaten-Abschnitt des Erlasses (akn:meta) |
| [Analysis](Analysis.md) | Der Analyseblock: welche Änderungen dieser Erlass vornimmt und erfährt |
| [Article](Article.md) | Ein Artikel, die primäre legislative Einheit (akn:article) |
| [Attachment](Attachment.md) | Ein einzelnes beigefügtes Dokument |
| [Attachments](Attachments.md) | Dem Erlass beigefügte Dokumente |
| [Block](Block.md) | Ein generischer Block (akn:block), dessen @name den Zweck nennt; trägt gemisc... |
| [BlockElement](BlockElement.md) | Abstrakte Basis für ein Element auf Blockebene: die Absätze, Aufzählungen und... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BlockList](BlockList.md) | Eine Auflistung von nummerierten oder buchstabierten Punkten (akn:blockList),... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BlockParagraph](BlockParagraph.md) | Ein Fliesstext-Absatz in Content (akn:p) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Citations](Citations.md) | Die Erwägungen des Vorspruchs — worauf sich der Erlass beruft |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Formula](Formula.md) | Eine Eingangs- oder Schlussformel des Vorspruchs (akn:formula) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Table](Table.md) | Ein Tabellen-Element innerhalb von Content (akn:table) |
| [BlockListItem](BlockListItem.md) | Ein einzelner Punkt in einer Auflistung (akn:item) |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |
| [Cell](Cell.md) | Abstrakte Basis für eine Zelle einer Tabellenzeile: eine Datenzelle (akn:td) ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TableCell](TableCell.md) | Eine Zelle in einer Tabellenzeile (akn:td) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TableHeaderCell](TableHeaderCell.md) | Eine Kopfzelle einer Tabellenzeile (akn:th) |
| [Chapter](Chapter.md) | Kapitel-Ebene eines Erlasses (akn:chapter) |
| [Citation](Citation.md) | Eine einzelne Erwägung |
| [Component](Component.md) | Ein einzelnes beiliegendes Dokument (akn:component) |
| [ComponentRef](ComponentRef.md) | Verweis auf einen anderswo gehaltenen Dokumentbestandteil (akn:componentRef) |
| [Components](Components.md) | Behälter für die Dokumente, die einem Erlass beiliegen (akn:components) — etw... |
| [Conclusions](Conclusions.md) | Die Schlussformel eines Erlasses: Ort, Datum und Unterschriften |
| [Container](Container.md) | Ein generischer Behälter (akn:container), dessen @name den Zweck nennt |
| [Content](Content.md) | Der Inhalt eines Absatzes (akn:content) |
| [Doc](Doc.md) | Ein beiliegendes Dokument (akn:doc) |
| [FedlexDocument](FedlexDocument.md) | Wurzelelement eines Fedlex AkomaNtoso-Dokuments (akn:akomaNtoso) |
| [FormatType](FormatType.md) | Halter für akn:FRBRformat: ein @value (typischerweise 'xml') plus das optiona... |
| [FRBRAuthor](FRBRAuthor.md) | Ein Autoren- oder Rechteinhaber-Eintrag einer FRBR-Entität (akn:FRBRauthor) |
| [FRBRDate](FRBRDate.md) | Ein Datumseintrag einer FRBR-Entität (akn:FRBRdate) |
| [FRBRExpression](FRBRExpression.md) | FRBR-Expression-Ebene (akn:FRBRExpression): eine sprachspezifische Version de... |
| [FRBRManifestation](FRBRManifestation.md) | FRBR-Manifestations-Ebene (akn:FRBRManifestation): ein spezifisches Dateiform... |
| [FRBRName](FRBRName.md) | Ein mehrsprachiger Namenseintrag des FRBR-Works (akn:FRBRname) |
| [FRBRWork](FRBRWork.md) | FRBR-Work-Ebene (akn:FRBRWork): der abstrakte Erlass unabhängig von Sprache u... |
| [Identification](Identification.md) | FRBR-Identifikationsblock (akn:identification) mit Work-, Expression- und Man... |
| [InlineElement](InlineElement.md) | Abstrakte Basis für ein modelliertes Inline-Markup-Element in gemischtem Inha... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Abbr](Abbr.md) | Die Abkürzung des Erlasses |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ActiveRef](ActiveRef.md) | Verweis auf einen Erlass, den dieses Dokument ändert |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AuthorialNote](AuthorialNote.md) | Eine Fussnote des Autors (akn:authorialNote) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[B](B.md) | Fett-Inline-Markup (akn:b) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Br](Br.md) | Ein Zeilenumbruch (akn:br) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DateInline](DateInline.md) | Ein Datum im Fliesstext, mit dem maschinenlesbaren Wert in @date |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Def](Def.md) | Ein im Text definierter Begriff |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DocDate](DocDate.md) | Ein Datum im Vorspann, mit dem maschinenlesbaren Wert in @date |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DocketNumber](DocketNumber.md) | Die Ordnungsnummer des Erlasses, wie sie kantonale Sammlungen führen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DocNumber](DocNumber.md) | Die Dokumentnummer im Vorspann |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DocTitle](DocTitle.md) | Der Dokumenttitel im Vorspann |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eol](Eol.md) | Ein Zeilenende innerhalb eines Absatzes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[I](I.md) | Kursiv-Inline-Markup (akn:i) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Inline](Inline.md) | Ein benanntes präsentationsbezogenes Inline (akn:inline), z |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NoteRef](NoteRef.md) | Verweis auf eine in den Metadaten gehaltene Anmerkung |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](Person.md) | Eine Person, mit Verweis auf ihre Deklaration und die innegehabte Rolle |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Placeholder](Placeholder.md) | Ein Platzhalter für entfernten Inhalt (akn:placeholder) mit dem Erweiterungsa... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ref](Ref.md) | Eine Inline-Referenz (akn:ref) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Role](Role.md) | Eine Rolle, die eine Person innehat, mit Verweis auf ihre Deklaration |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ShortTitle](ShortTitle.md) | Der Kurztitel des Erlasses |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Signature](Signature.md) | Eine Unterschriftszeile |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Span](Span.md) | Generischer Inline-Bereich (akn:span) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sup](Sup.md) | Hochgestelltes Inline-Markup (akn:sup) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TextRun](TextRun.md) | Ein einfacher Textabschnitt in gemischtem Inhalt |
| [LanguageType](LanguageType.md) | Halter mit einem einzelnen @language-Attribut (akn:FRBRlanguage) |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |
| [MainBody](MainBody.md) | Hauptteil eines beiliegenden Dokuments (akn:mainBody) |
| [MixedText](MixedText.md) | Wiederverwendbarer Halter für gemischten Inhalt: eine geordnete Folge aus Tex... |
| [ModDestination](ModDestination.md) | Die Stelle, die geändert wird |
| [Modification](Modification.md) | Abstrakte Basis für eine im Analyseblock vermerkte Änderung |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ForceMod](ForceMod.md) | Eine Änderung der Rechtskraft: ein Erlass oder ein Teil davon tritt in Kraft,... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TextualMod](TextualMod.md) | Eine Textänderung: der Wortlaut eines anderen Erlasses wird eingefügt, ersetz... |
| [ModNew](ModNew.md) | Der Text, wie er nach der Änderung lautet |
| [ModOld](ModOld.md) | Der Text, wie er vor der Änderung lautete |
| [ModSource](ModSource.md) | Die Stelle, welche die Änderung bewirkt |
| [Note](Note.md) | Eine einzelne Anmerkung |
| [Notes](Notes.md) | Anmerkungsblock der Metadaten mit den Anmerkungen, auf die ein Erlass verweis... |
| [OriginalRef](OriginalRef.md) | Verweis auf die ursprüngliche Fassung des Erlasses (akn:original) |
| [Paragraph](Paragraph.md) | Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph) |
| [Part](Part.md) | Teil-Ebene eines Erlasses (akn:part) |
| [PassiveModifications](PassiveModifications.md) | Die Änderungen, die andere Erlasse an diesem vornehmen |
| [Preamble](Preamble.md) | Die Präambel des Erlasses (akn:preamble) mit einleitenden Fliesstext-Absätzen... |
| [Preface](Preface.md) | Der Vorspann des Erlasses (akn:preface) mit Dokumentnummer und -titel |
| [PrefaceP](PrefaceP.md) | Ein Vorspann-Absatz (akn:p) |
| [Proviso](Proviso.md) | Ein Vorbehalt im Hauptteil eines Erlasses (akn:proviso) |
| [References](References.md) | Benannte Referenz-Definitionen für das gesamte Dokument (akn:references) |
| [Section](Section.md) | Abschnitt-Ebene (akn:section) |
| [Subchapter](Subchapter.md) | Unterkapitel-Ebene (akn:subchapter) |
| [Subdivision](Subdivision.md) | Ein Unterabschnitt in einem Artikel, der zusammengehörige Absätze gruppiert (... |
| [Subsection](Subsection.md) | Unterabschnitt-Ebene (akn:subsection) |
| [TableRow](TableRow.md) | Eine Zeile in einer AkomaNtoso-Tabelle (akn:tr) |
| [TemporalData](TemporalData.md) | Die Zeitgruppen, auf die sich eine Änderung bezieht |
| [TemporalGroup](TemporalGroup.md) | Ein benannter Zeitraum, auf den sich eine Änderung über @period bezieht |
| [TimeInterval](TimeInterval.md) | Ein Intervall zwischen zwei Daten |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |
| [TLCConcept](TLCConcept.md) | Ein Begriff, auf den das Dokument verweist (akn:TLCConcept), etwa ein zeitlic... |
| [TLCOrganization](TLCOrganization.md) | Eine benannte Organisation als Referenz im Dokument (akn:TLCOrganization) |
| [TLCReference](TLCReference.md) | Eine generische benannte Referenz im Dokument (akn:TLCReference) |
| [TLCRole](TLCRole.md) | Eine benannte Rolle als Referenz im Dokument (akn:TLCRole) |
| [Transitional](Transitional.md) | Eine Übergangsbestimmung im Hauptteil eines Erlasses (akn:transitional) |
| [UriValueType](UriValueType.md) | Halter mit einem @value-Attribut vom Typ ELI-URI (AKN valueType) |
| [ValueType](ValueType.md) | Einfacher Halter mit einem einzelnen @value-Attribut (AKN valueType) |



## Slots

| Slot | Beschreibung |
| --- | --- |
| [act_name](act_name.md) | Typ des Erlasses (akn:act/@name) |
| [act_ref](act_ref.md) | Der Erlass (akn:act) |
| [active_modifications](active_modifications.md) | Die Änderungen, die dieser Erlass an anderen vornimmt (akn:activeModification... |
| [active_refs](active_refs.md) | Verweise auf die Erlasse, die dieses Dokument ändert (akn:activeRef) |
| [analysis_ref](analysis_ref.md) | Der Analyseblock der Metadaten (akn:analysis) |
| [articles](articles.md) | Artikel-Kindelemente (akn:article) |
| [as_attr](as_attr.md) | Rolle, in der die Person handelt (@as) |
| [as_role](as_role.md) | Rolle des Autors (akn:FRBRauthor/@as), als Anker-Referenz, z |
| [attachment_list](attachment_list.md) | Die beigefügten Dokumente (akn:attachment) |
| [attachments_ref](attachments_ref.md) | Die dem Erlass beigefügten Dokumente (akn:attachments) |
| [block_lists](block_lists.md) | Auflistungs-Elemente (akn:blockList) innerhalb von Content |
| [block_name](block_name.md) | Zweck des Blocks (akn:block/@name) |
| [block_paragraphs](block_paragraphs.md) | Block-Absatz-Elemente (akn:p) innerhalb von Content |
| [blocks](blocks.md) | Blöcke innerhalb des Behälters (akn:block) |
| [body](body.md) | Hauptteil des Erlasses (akn:body) |
| [books](books.md) | Buch-Kindelemente (akn:book) |
| [border](border.md) | Das @border-Attribut auf akn:table (HTML-artige Darstellung) |
| [chapters](chapters.md) | Kapitel-Kindelemente (akn:chapter) |
| [citation_list](citation_list.md) | Die Erwägungen selbst (akn:citation) |
| [colspan](colspan.md) | Das @colspan-Attribut auf akn:td (HTML-artige Darstellung) |
| [component_list](component_list.md) | Die beiliegenden Dokumente (akn:component) |
| [component_refs](component_refs.md) | Verweise auf anderswo gehaltene Bestandteile (akn:componentRef) |
| [components_ref](components_ref.md) | Die diesem Erlass beiliegenden Dokumente (akn:components) |
| [conclusions_ref](conclusions_ref.md) | Die Schlussformel des Erlasses (akn:conclusions) |
| [container_name](container_name.md) | Zweck des Behälters (akn:container/@name) |
| [containers](containers.md) | Behälter des Vorspanns (akn:container) |
| [content_blocks](content_blocks.md) | Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie sie i... |
| [content_ref](content_ref.md) | Inhaltselement innerhalb eines Absatzes (akn:content) |
| [date_attr](date_attr.md) | Das Datum, das dieses Element auszeichnet, nach ISO 8601 (@date) |
| [date_value](date_value.md) | Ein ISO-8601-Datumswert (akn:FRBRdate/@date) |
| [doc_name](doc_name.md) | Art des beiliegenden Dokuments (akn:doc/@name) |
| [doc_ref](doc_ref.md) | Das beiliegende Dokument selbst (akn:doc) |
| [eId](eId.md) | Eindeutiger Element-Identifier im Dokument (@eId) |
| [element_type](element_type.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: Inline... |
| [end_ref](end_ref.md) | Anker des Datums, an dem das Intervall endet (@end); leer, solange es offen i... |
| [fedlex_generator](fedlex_generator.md) | Fedlex-Erweiterungsattribut fedlex:generator bei akn:FRBRformat[@value='xml'] |
| [fedlex_message](fedlex_message.md) | Fedlex-Erweiterungsattribut fedlex:message auf akn:placeholder, das entfernte... |
| [fedlex_role](fedlex_role.md) | Fedlex-Erweiterungsattribut fedlex:role |
| [fedlex_rs](fedlex_rs.md) | Fedlex-Erweiterungsattribut fedlex:rs auf akn:ref: die SR-Nummer des referenz... |
| [fedlex_rs_uri](fedlex_rs_uri.md) | Fedlex-Erweiterungsattribut fedlex:rs-uri auf akn:ref: die ELI-URI des SR-Ein... |
| [frbr_authoritative](frbr_authoritative.md) | Ob dies die massgebliche Version ist (akn:FRBRauthoritative/@value) |
| [frbr_authors](frbr_authors.md) | Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor) |
| [frbr_country](frbr_country.md) | Ländercode für diesen Erlass (akn:FRBRcountry/@value), z |
| [frbr_date_name](frbr_date_name.md) | Art dieses Datums (akn:FRBRdate/@name) |
| [frbr_dates](frbr_dates.md) | Datumseinträge dieser FRBR-Entität (akn:FRBRdate) |
| [frbr_expression](frbr_expression.md) | FRBR-Expression-Ebenen-Beschreibung (akn:FRBRExpression) |
| [frbr_format](frbr_format.md) | Dateiformat dieser Manifestation (akn:FRBRformat/@value), typischerweise 'xml... |
| [frbr_language](frbr_language.md) | Sprachcode dieser Expression (akn:FRBRlanguage/@language) |
| [frbr_manifestation](frbr_manifestation.md) | FRBR-Manifestations-Ebenen-Beschreibung (akn:FRBRManifestation) |
| [frbr_names](frbr_names.md) | Mehrsprachige Namenseinträge des FRBR-Works (akn:FRBRname) |
| [frbr_number](frbr_number.md) | SR-Nummer (akn:FRBRnumber/@value), z |
| [frbr_subtype](frbr_subtype.md) | Untertyp des Werks (akn:FRBRsubtype), z |
| [frbr_this](frbr_this.md) | Kanonische ELI-URI dieser FRBR-Entität (akn:FRBRthis/@value) |
| [frbr_uri](frbr_uri.md) | Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value) |
| [frbr_work](frbr_work.md) | FRBR-Work-Ebenen-Beschreibung (akn:FRBRWork) |
| [heading](heading.md) | Überschrift für ein Strukturelement (akn:heading) |
| [href](href.md) | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs |
| [identification_ref](identification_ref.md) | FRBR-Identifikationsblock (akn:identification) |
| [inline_content](inline_content.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Marku... |
| [items](items.md) | Punkte einer Auflistung (akn:item) |
| [language_value](language_value.md) | Das @language-Attribut von akn:FRBRlanguage, z |
| [levels](levels.md) | Transparente Level-Kindelemente (akn:level) |
| [list_introduction](list_introduction.md) | Optionaler Einleitungstext vor einer Auflistung (akn:listIntroduction) |
| [main_body](main_body.md) | Hauptteil des beiliegenden Dokuments (akn:mainBody) |
| [marker](marker.md) | Das gedruckte Zeichen eines Anmerkungsverweises (@marker) |
| [meta](meta.md) | Metadaten-Abschnitt des Erlasses (akn:meta) |
| [mod_destinations](mod_destinations.md) | Die Stellen, die geändert werden (akn:destination) |
| [mod_new](mod_new.md) | Der neue Wortlaut (akn:new) |
| [mod_old](mod_old.md) | Der bisherige Wortlaut (akn:old) |
| [mod_sources](mod_sources.md) | Die Stellen, welche die Änderung bewirken (akn:source) |
| [mod_type](mod_type.md) | Art der Änderung (@type); die zulässigen Werte sind die von Akoma Ntoso |
| [modifications](modifications.md) | Die Änderungen in der Reihenfolge ihrer Aufzeichnung (akn:textualMod, akn:for... |
| [name_attr](name_attr.md) | Das @name-Attribut auf akn:inline, z |
| [name_attr2](name_attr2.md) | Zweck der Formel (@name) |
| [note_list](note_list.md) | Die Anmerkungen selbst (akn:note) |
| [notes_ref](notes_ref.md) | Der Anmerkungsblock der Metadaten (akn:notes) |
| [num](num.md) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num) |
| [original_ref](original_ref.md) | Verweis auf die ursprüngliche Fassung (akn:original) |
| [paragraphs](paragraphs.md) | Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschn... |
| [parts](parts.md) | Teil-Kindelemente (akn:part) |
| [passive_modifications](passive_modifications.md) | Die Änderungen, die andere Erlasse an diesem vornehmen (akn:passiveModificati... |
| [period](period.md) | Die Zeitgruppe, in der die Änderung gilt (@period) |
| [pos](pos.md) | Lage der Änderung zum Ziel (@pos), z |
| [preamble_ref](preamble_ref.md) | Präambel des Erlasses (akn:preamble) |
| [preface_paragraphs](preface_paragraphs.md) | Die akn:p-Absätze des Vorspanns, die docNumber/docTitle umschliessen |
| [preface_ref](preface_ref.md) | Vorspann des Erlasses (akn:preface) |
| [provisos](provisos.md) | Vorbehalt-Elemente (akn:proviso) |
| [references_ref](references_ref.md) | Referenzen-Abschnitt der Metadaten (akn:references) |
| [refers_to](refers_to.md) | Anker, der nennt, worauf sich das Element bezieht (@refersTo) |
| [sections](sections.md) | Abschnitt-Kindelemente (akn:section) |
| [short_form](short_form.md) | Kurzform-Abkürzung des Gesetzesnamens (@shortForm), z |
| [show_as](show_as.md) | Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs) |
| [source](source.md) | Anker-Referenz auf die verantwortliche Organisation (@source), z |
| [src](src.md) | Ort des verwiesenen Bestandteils (@src) |
| [start_ref](start_ref.md) | Anker des Datums, an dem das Intervall beginnt (@start) |
| [status](status.md) | Bearbeitungsstand des Elements (@status), z |
| [style](style.md) | Darstellungsangabe des Elements (@style) |
| [subchapters](subchapters.md) | Unterkapitel-Kindelemente (akn:subchapter) |
| [subdivisions](subdivisions.md) | Unterabschnitt-Kindelemente (akn:subdivision) innerhalb eines Artikels |
| [subheading](subheading.md) | Unterüberschrift für ein Strukturelement (akn:subheading) |
| [subsections](subsections.md) | Unterabschnitt-Kindelemente (akn:subsection) |
| [table_cells](table_cells.md) | Zellen einer Tabellenzeile in Lesereihenfolge: Datenzellen und Kopfzellen (ak... |
| [table_rows](table_rows.md) | Zeilen in einer Tabelle (akn:tr) |
| [tables](tables.md) | Tabellen-Elemente (akn:table) innerhalb von Content |
| [temporal_data_ref](temporal_data_ref.md) | Die Zeitangaben der Metadaten (akn:temporalData) |
| [temporal_groups](temporal_groups.md) | Die Zeitgruppen (akn:temporalGroup) |
| [text](text.md) | Die Zeichendaten eines TextRun; wird als Textknoten in gemischtem Inhalt ausg... |
| [time_intervals](time_intervals.md) | Die Intervalle dieser Gruppe (akn:timeInterval) |
| [title_attr](title_attr.md) | Menschenlesbare Bezeichnung der ausgezeichneten Stelle (@title) |
| [titles](titles.md) | Titel-Kindelemente (akn:title) |
| [tlc_concepts](tlc_concepts.md) | Begriffe, auf die das Dokument verweist (akn:TLCConcept) |
| [tlc_organizations](tlc_organizations.md) | Benannte Organisations-Referenzen im Dokument (akn:TLCOrganization) |
| [tlc_references](tlc_references.md) | Generische benannte Referenzen im Dokument (akn:TLCReference) |
| [tlc_roles](tlc_roles.md) | Benannte Rollen-Referenzen im Dokument (akn:TLCRole) |
| [transitionals](transitionals.md) | Übergangsbestimmungs-Elemente (akn:transitional) |
| [up_to](up_to.md) | Ende eines Zielbereichs (@upTo) |
| [value](value.md) | Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwende... |
| [value_uri](value_uri.md) | Ein @value-Attribut vom Typ ELI-URI (akn:FRBRthis/@value, akn:FRBRuri/@value) |
| [xml_lang](xml_lang.md) | XML-Sprachattribut (xml:lang), z |


## Enums

| Aufzählung | Beschreibung |
| --- | --- |
| [ActTypeEnum](ActTypeEnum.md) | Art des Erlasses, ausgedrückt im @name-Attribut von akn:act |
| [BlockNameEnum](BlockNameEnum.md) | Zwecke, die Fedlex in akn:block/@name verwendet |
| [ContainerNameEnum](ContainerNameEnum.md) | Zwecke, die Fedlex in akn:container/@name verwendet |
| [DocNameEnum](DocNameEnum.md) | Arten beiliegender Dokumente, die Fedlex in akn:doc/@name verwendet |
| [DocumentLanguageEnum](DocumentLanguageEnum.md) | Sprachcodes für schweizerische Bundesdokumente |
| [FedlexRoleEnum](FedlexRoleEnum.md) | Erlaubte Werte für das Fedlex-Erweiterungsattribut fedlex:role (FLX-XF-003) |
| [FrbrDateNameEnum](FrbrDateNameEnum.md) | Datumsarten, die Fedlex in akn:FRBRdate/@name verwendet, aus dem JoLux-Vokabu... |
| [ModTypeEnum](ModTypeEnum.md) | Änderungsarten, die Akoma Ntoso definiert: die textlichen aus der Liste Textu... |


## Typen

| Typ | Beschreibung |
| --- | --- |
| [AnchorRef](AnchorRef.md) | Eine Dokument-interne Referenz im Format '#id', die auf ein eId oder TLC-Elem... |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [EIdType](EIdType.md) | Eindeutiger Element-Identifier innerhalb eines AkomaNtoso-Dokuments (@eId) |
| [ELIURI](ELIURI.md) | Ein European Legislation Identifier (ELI) URI, wie von Fedlex verwendet |
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
| [XmlContent](XmlContent.md) | Gemischter XML-Inhalt: Text mit optionalem Inline-Markup |


## Subsets

| Subset | Beschreibung |
| --- | --- |
