\newpage

# Memberships

The membership schema represents the relationship between persons and groups and is the central connecting element in the actor schema.

- **Distinction from interest links (`InterestLink`):** `Membership` records the *formal affiliation* of a person to a group within the actor schema (e.g. party, commission or parliament membership). Interest links and conflicts of interest with organisations *outside* the schema are deliberately kept separate and are represented via `InterestLink` (see the following chapter).
- **References with snapshot instead of embedding (`person_reference`/`group_reference`):** A membership refers to a person and a group via lightweight references and thereby records their most important identifying attributes at the time of linking. This keeps the entry historically correct even if the person or group changes later.
- **Activity explicit or derived (`is_active`):** Whether a membership is active can be set explicitly via `is_active` or derived from the temporal validity. If `is_active` is not set, activity is derived from `valid_from`/`valid_through`.
- **Membership ≠ voting right (`authorized_to_vote`):** The voting right is recorded separately from the membership – typically `false` for substitute members (except when on duty), observers, the secretariat and guests.
- **Role as a controlled vocabulary with free-text option (`role_type`):** The role in the group (e.g. member, presidency, deputy) is specified via a controlled vocabulary (`RoleEnum`); for roles not covered, the value `other` with a free-text designation is used.

{{include:ech-0294_actors/output/docs/Membership.md}}

{{include:ech-0294_actors/output/docs/RoleType.md}}

{{include:ech-0294_actors/output/docs/RoleEnum.md}}
