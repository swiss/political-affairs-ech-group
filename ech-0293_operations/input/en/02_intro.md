\newpage

# Introduction

## The "Political Affairs" standard family

Political activity in Switzerland takes place at federal, cantonal and communal level – in parliaments and communal assemblies, in executives and administrations, in consultations and hearings, as well as through the direct-democratic participation of eligible voters. To this end, the "Political Affairs" specialist group of the eCH Association is developing a family of coordinated standards that structure this data across all federal levels. The standards use common data elements (eCH-0292) and reference one another via unique identifiers.

The family comprises:

- **eCH-0292 – Common Data Elements (Meta):** Defines the cross-cutting data elements and meta-processes on which the other standards build. eCH-0293 adopts from it, among other things, the identification and date elements as well as the FRBR structure for linked documents.
- **eCH-0293 – Public Council Operations (Operations) – this standard:** Describes public council operations – legislatures and sessions, meetings and agenda items, protocols and decisions, votings and elections, attendance as well as speeches.
- **eCH-0294 – Political Actors (Actors):** Defines persons, groups and bodies in the political context, as well as their memberships and interest links. eCH-0293 references these actors via `group_reference` and `person_reference` – for instance which parliament convened and which person voted.
- **eCH-0295 – Parliamentary Affairs (Affairs):** Describes the life cycle of political affairs. Agenda items in eCH-0293 point to the corresponding affair via `affair_id`.
- **eCH-0296 – Enactments and Legal Texts (Laws):** Records the results of the parliamentary process – the adopted laws and enactments.
- **eCH-0297 – Public Consultations (Consultations):** Structures consultation procedures, which are often the starting point for parliamentary affairs.

The aim of this standard family is to create a commonly usable structure for political data and to provide organisations that publish information on political affairs with a robust data model.

## Structure of a delivery

A delivery is a `Container`: an envelope with a `global_uri` of its own and one collection per class — `legislatures`, `sessions`, `meetings`, `protocols`, `votings`, `elections`, `individual_votes`, `attendances`, `individual_attendances`, `speeches` and `resolutions`. Agenda items have no collection of their own: they are delivered within their meeting or session (`agenda_items`). All collections are optional: those who only publish sittings deliver only `meetings`.

The entities sit side by side in a flat structure and are connected by references — `parent_meeting`, `parent_voting`, `parent_attendance` and so on — rather than nested inside one another. A single sitting can thus be delivered later without resending the entire legislature, and the same entity can be referenced from several places. Where nesting renders the connection better, it remains possible: the session takes its sittings as a list, the protocol its agenda items, votings and speeches.

{{include:ech-0293_operations/output/docs/Container.md}}

## Common elements

The three classes of the temporal organisation — Legislature, Session and Meeting — are deliberately built alike. The following fields have the same meaning on all levels.

**Identification.** `global_uri` is the identifier and is mandatory. `local_id` takes the id of the delivering system, `wikidata_uri` points to the Wikidata entry where one exists.

**Begin and end.** The temporal data is recorded twice: `date_begin_planned` and `date_end_planned` hold what was scheduled, `date_begin_actual` and `date_end_actual` what actually happened. Where the time of day matters, the `datetime_*` variants are available.

**Space and body.** `spatial` points to the spatial unit according to LINDAS — country, canton, district or commune, thus `https://ld.admin.ch/canton/2` rather than "BE". It is the same field with which eCH-0294 locates its groups, so that council operations and the actors who carry them point to the same resource. Who convenes within that spatial unit is stated by `group_reference`, a lightweight reference to the body according to eCH-0294.

**Linked documents.** `documents` links documents as FRBR works according to eCH-0292 — for the legislature, for instance, membership and affair registers, for the session the session programme, for the meeting the bulletin and annexes (the protocol, by contrast, via `has_protocol`).
