\newpage

# Person

The person schema describes natural persons in the political context.

- **Stable person, temporally valid attributes:** The `Person` itself carries no temporal validity, but its attributes do – name, citizenship, gender, occupation and training each carry their own `valid_from`/`valid_through`. This keeps the identity of the person stable while individual details change over time and the history is preserved (e.g. a change of name upon marriage). The electoral district, by contrast, is not an attribute of the person: it is attached to the `Membership` (`electoral_district`) and inherits its temporal validity – a change of electoral district is therefore reflected in the respective membership.
- **Display name (`label`) mandatory, name structure (`names`) optional:** Every person has a short display name. This means a name is always available, even when the details are incomplete. The recommended combination is the official name (`PersonOfficialName`) and the call name (`PersonCallFirstName`). Academic titles can also be represented via `label_long`.
- **Name types according to the official taxonomy:** The name types (`NameTypeEnum`) follow the register harmonisation of the FSO, respectively eCH-0011 (including official name, original name, alliance name, call name, as well as variants for foreign identity documents). This makes the names compatible with the official person registers, and their semantics clear.
- **Date of birth at two levels of precision (`birth_year` / `birth_date`):** If the exact date of birth is not available or not intended for publication, only the year of birth may be given. If a `birth_date` is available, it takes precedence.
- **Multiple values instead of single values:** Names, citizenships and gender entries are modelled as lists with temporal validity – for example for dual citizenships, changes of name or a changing gender entry.
- **Harmonisation across federal levels (long-term goal):** Linking the same person across the federal levels is an important long-term goal. Building a central person database is beyond the means of the eCH specialist group. Since an open, established infrastructure already exists for this purpose, **Wikidata is recommended as a cross-cutting identifier** (`wikidata_uri`); together with globally unique identifiers (URIs), the mapping can thus be harmonised step by step across the systems.


{{include:ech-0294_actors/output/docs/Person.md}}

{{include:ech-0294_actors/output/docs/Name.md}}

{{include:ech-0294_actors/output/docs/NameTypeEnum.md}}

{{include:ech-0294_actors/output/docs/LanguageProficiency.md}}

{{include:ech-0294_actors/output/docs/Citizenship.md}}

{{include:ech-0294_actors/output/docs/Gender.md}}

{{include:ech-0294_actors/output/docs/GenderCodeEnum.md}}

{{include:ech-0294_actors/output/docs/Occupation.md}}

{{include:ech-0294_actors/output/docs/Training.md}}

{{include:ech-0294_actors/output/docs/TrainingTypeEnum.md}}
