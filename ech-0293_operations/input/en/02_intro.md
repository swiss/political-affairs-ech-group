\newpage

# Introduction

## The "Political Affairs" standard family

Political activity in Switzerland takes place at federal, cantonal and communal level – in parliaments and communal assemblies, in executives and administrations, in consultations and hearings, as well as through the direct-democratic participation of eligible voters. To this end, the "Political Affairs" specialist group of the eCH Association is developing a family of coordinated standards that structure this data across all federal levels. The standards use common data elements (eCH-0292) and reference one another via unique identifiers.

The family comprises:

- **eCH-0292 – Common Data Elements (Meta):** Defines the cross-cutting data elements and meta-processes on which the other standards build. eCH-0293 adopts from it, among other things, the identification and date elements as well as the FRBR structure for linked documents.
- **eCH-0293 – Public Council Operations (Operations) – this standard:** Describes public council operations – legislatures and sessions, meetings and agenda items, protocols and decisions, votings and elections, attendance as well as speeches.
- **eCH-0294 – Political Actors (Actors):** Defines persons, groups and bodies in the political context, as well as their memberships and interest links. eCH-0293 references these actors via `actor_id` – for instance which parliament convened and which person voted.
- **eCH-0295 – Parliamentary Affairs (Affairs):** Describes the life cycle of political affairs. Agenda items in eCH-0293 point to the corresponding affair via `affair_id`.
- **eCH-0296 – Enactments and Legal Texts (Laws):** Records the results of the parliamentary process – the adopted laws and enactments.
- **eCH-0297 – Public Consultations (Consultations):** Structures consultation procedures, which are often the starting point for parliamentary affairs.

The aim of this standard family is to create a commonly usable structure for political data and to provide organisations that publish information on political affairs with a robust data model.

## Structure of a delivery

A delivery is a `Container`: an envelope with a `global_uri` of its own and one collection per class — `legislatures`, `sessions`, `meetings`, `agenda_items`, `protocols`, `votings`, `elections`, `individual_votes`, `attendances`, `individual_attendances`, `speeches` and `resolutions`. All collections are optional: those who only publish sittings deliver only `meetings`.

The entities sit side by side in a flat structure and are connected by references — `parent_meeting`, `parent_voting`, `parent_attendance` and so on — rather than nested inside one another. A single sitting can thus be delivered later without resending the entire legislature, and the same entity can be referenced from several places. Where nesting renders the connection better, it remains possible: the session takes its sittings as a list, the protocol its agenda items, votings and speeches.

{{include:ech-0293_operations/output/docs/Container.md}}
