\newpage

# Introduction

## Context: public council operations

At federal, cantonal and communal level, councils and assemblies convene, deliberate on political affairs, take decisions and scrutinise the executive.

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

## Distinction from the "Political Rights" specialist group

Alongside the "Political Affairs" specialist group, the eCH Association also maintains the "Political Rights" specialist group. Both concern the political domain, but cover different areas:

- **Political Affairs** (this standard family) describes the parliamentary and governmental process of forming opinions and reaching decisions: the actors (eCH-0294), council operations (eCH-0293), parliamentary affairs (eCH-0295), the enactments arising from them (eCH-0296), as well as the upstream consultations (eCH-0297).
- **Political Rights** deals with the exercise of political rights by eligible voters: voting and electoral registers, the conduct of popular votes and elections, electronic voting (eVoting), voting cards, as well as voting and election results (among others eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

This distinction matters particularly for eCH-0293, because the standard models votings and elections. What is decisive is not who is entitled to vote, but **where the decision is taken** – in the convened assembly or at the ballot box:

- **In the assembly** – this standard: votings and elections carried out by a convened body in the course of a sitting with an agenda. This includes roll-call votings and final votes in parliament as well as the election of authority members, judges or committee presidencies by the council. It is recorded via `Voting`, `IndividualVote` and `Election`.
- **At the ballot box** – "Political Rights" specialist group: popular votes and popular elections together with voting registers, conduct, voting cards and results. These are not modelled here.

Deliberately on the side of this standard are **Landsgemeinden and communal assemblies** (`meeting_type: sitting`). They are indeed assemblies of the eligible voters themselves, but they decide as a convened body with an agenda, speeches and resolutions – and are therefore represented like a council sitting.

A second point of contact concerns elected persons: candidates and elected persons appear in the election results of the "Political Rights" specialist group. As soon as persons hold a mandate, they are recorded in eCH-0294 as political actors with their roles and memberships – and eCH-0293 references them from there via `actor_id`.
