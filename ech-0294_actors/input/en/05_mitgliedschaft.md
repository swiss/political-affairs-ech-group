\newpage

# Memberships

The membership schema represents the relationship between persons and groups and is the central connecting element in the actor schema.

- **Distinction from interest links (`InterestLink`):** `Membership` records the *formal affiliation* of a person to a group within the actor schema (e.g. party, commission or parliament membership). Interest links and conflicts of interest with organisations *outside* the schema are deliberately kept separate and are represented via `InterestLink` (see the following chapter).
- **Reference with snapshot instead of embedding (`person_reference`/`group_reference`):** A membership refers to a person and a group and thereby records their most important identifying attributes at the time of linking. This keeps the entry historically correct even if the person or group changes later.
- **Activity explicit or derived (`is_active`):** Whether a membership is active can be set explicitly via `is_active` or derived from the temporal validity. If `is_active` is not set, activity is derived from `valid_from`/`valid_through`.
- **Membership ≠ voting right (`authorized_to_vote`):** The voting right is recorded separately from the membership – typically `false` for substitute members (except when on duty), observers, the secretariat and guests.
- **Role as a controlled vocabulary with free-text option (`role_type`):** The role in the group (e.g. member, presidency, deputy) is specified via a controlled vocabulary (`RoleEnum`); for roles not covered, the value `other` with a free-text designation is used.
- **Electoral district on the membership rather than on the person (`electoral_district`):** The electoral district describes the mandate, not the person – the same person may be elected from different districts over time or at different federal levels. `ElectoralDistrict` therefore carries no temporal validity of its own but inherits the `valid_from`/`valid_through` of the enclosing membership. For identification, the LINDAS resources for Swiss spatial units are intended (see `global_uri`). Whether a district can be identified that way depends on it coinciding with an official spatial unit: in the canton of Basel-Stadt the districts of Riehen and Bettingen are municipalities and have a LINDAS resource, whereas Grossbasel-Ost, Grossbasel-West and Kleinbasel group together neighbourhoods of the municipality of Basel and have none. Districts without an official counterpart are given an identifier in the namespace of the publishing body.

{{include:ech-0294_actors/output/docs/Membership.md}}

{{include:ech-0294_actors/output/docs/RoleType.md}}

{{include:ech-0294_actors/output/docs/RoleEnum.md}}

{{include:ech-0294_actors/output/docs/ElectoralDistrict.md}}
