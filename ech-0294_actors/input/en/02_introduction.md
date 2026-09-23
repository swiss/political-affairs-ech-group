\newpage

# Introduction

## Status

Proposal

## Scope of application

The standard governs the publication of data on political actors by the bodies that already keep this data today: parliamentary services, state chancelleries and municipal administrations at all levels of government. It covers in particular the following use cases:

- publication of the members of parliaments, governments and committees with their memberships, functions and terms of office
- publication of the registers of interests of members of parliament
- referencing persons, groups and bodies from the other standards of the "Political Affairs" family, for instance for speeches and votes in parliamentary operations (eCH-0293) or for the authorship of parliamentary affairs (eCH-0295)
- reuse of this data by the media, research and the public, comparable across levels of government

## The "Political Affairs" standard family

Political activity in Switzerland takes place at federal, cantonal and communal level – in parliaments and communal assemblies, in executives and administrations, in consultations and hearings, as well as through the direct-democratic participation of eligible voters. To this end, the "Political Affairs" specialist group of the eCH Association is developing a family of coordinated standards that structure this data across all federal levels. The standards use common data elements (eCH-0292) and reference one another via unique identifiers.

The family comprises:

- **eCH-0292 – Common Data Elements (Meta):** Defines the cross-cutting data elements and meta-processes on which the other standards build.
- **eCH-0293 – Public Council Operations (Operations):** Describes public council operations – meetings, agenda items, statements, as well as votes and elections.
- **eCH-0294 – Political Actors (Actors) – this standard:** Defines persons, groups and bodies in the political context, as well as their memberships and interest links. The other standards reference these actors via their identifiers.
- **eCH-0295 – Parliamentary Affairs (Affairs):** Describes the life cycle of political affairs.
- **eCH-0296 – Enactments and Legal Texts (Laws):** Records the results of the parliamentary process – the adopted laws and enactments.
- **eCH-0297 – Public Consultations (Consultations):** Structures consultation procedures, which are often the starting point for parliamentary affairs.

The aim of this standard family is to create a commonly usable structure for political data and to provide organisations that publish information on political affairs with a robust data model.

## Distinction from the "Political Rights" specialist group

Alongside the "Political Affairs" specialist group, the eCH Association also maintains the "Political Rights" specialist group. Both concern the political domain, but cover different areas:

- **Political Affairs** (this standard family) describes the parliamentary and governmental process of forming opinions and reaching decisions: the actors (eCH-0294), council operations (eCH-0293), parliamentary affairs (eCH-0295), the enactments arising from them (eCH-0296), as well as the upstream consultations (eCH-0297).
- **Political Rights** deals with the exercise of political rights by eligible voters: voting and electoral registers, the conduct of popular votes and elections, electronic voting (eVoting), voting cards, as well as voting and election results (among others eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

There are two points of contact:

- **Votes and elections:** eCH-0293 records votes and elections **within council operations** (e.g. recorded votes in parliament or the election of authority members by the council), whereas popular votes and popular elections, together with the associated registers, conduct and results, are covered by the "Political Rights" specialist group.
- **Elected persons:** Candidates and elected persons appear in the election results of the "Political Rights" specialist group. As soon as persons hold a mandate, they are recorded in eCH-0294 as political actors with their roles and memberships.

## The eCH-0294 standard – Political Actors: Persons, Groups and Bodies

This standard defines four main classes:

- **Person** – Natural persons in the political context
- **Group** – Committees, parties, parliamentary groups, councils, commissions, organisations, etc.
- **Membership** – Link between persons and groups
- **InterestLink** – Interest links of persons

`Membership` is the central connecting element between `Person` and `Group` and records in which parliament, in which commission, etc. a person is or was active. `InterestLink` enables the description of interest links.
