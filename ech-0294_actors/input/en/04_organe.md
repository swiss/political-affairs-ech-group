\newpage

# Groups and Bodies (Groups)

The group schema represents political groups, organisations and corporate bodies.

- **One generic model instead of many special classes:** Parliaments, parties, parliamentary groups, committees, departments, courts and civil-society organisations are all represented as *one* class `Group` and distinguished via `group_type`. This keeps the model simple and extensible without schema changes – the legislature, executive, judiciary and civil society can thus all be represented equally.
- **Groups and sub-groups via `parent_groups`:** Subordinate groups reference their superordinate group – e.g. a committee of the Council of States, a subcommittee within a committee, a cantonal party under its parent party, or an authority within a directorate. The hierarchy thus arises from these references rather than from a fixed level structure. It usually remains within the same `group_type`; however, cross-type and multiple references are possible (e.g. a parliamentary group that references both its parliament and its party). The reference takes the form of a `GroupReference` – the same form in which a membership names its group. That the link expresses a superordinate/subordinate relation is stated by the `parent_groups` slot itself; the reference merely carries the addressing. That addressing may use the `local_id` where the parent group is part of the same delivery, or the `global_uri` where it lies outside it – a cantonal party can thus reference its national party without that party having to be delivered. Because the reference can additionally carry a label, a list of several parent groups also remains readable.
- **Temporal validity for groups as well:** Using `valid_from`/`valid_through`, it is possible to represent, for example, committees that exist only during a legislative period, or renamings and mergers of parties.

{{include:ech-0294_actors/output/docs/Group.md}}

{{include:ech-0294_actors/output/docs/GroupType.md}}

{{include:ech-0294_actors/output/docs/GroupTypeEnum.md}}
