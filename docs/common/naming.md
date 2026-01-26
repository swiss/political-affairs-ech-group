# Naming Conventions and URI Concept

This document describes the naming conventions and URI concept used in the data schemata developed by the eCH Specialist Group Political Affairs.

## Naming Conventions

### Classes

- PascalCase
- singular
- English

Examples: `Container`, `Legislature`, `MeetingItem`

### Slots

- snake_case
- singular or plural depending on the number of allowed elements
- English
- if plural is used, a singular `slot_uri` in camelCase is needed (e.g. `meeting_items` --> `slot_uri: ops:meetingItem`)

Examples: `id`, `body_key`, `meeting_items`

**Attention**:

Avoid using classes and slots with the only difference in capitalization, because there will be documentation files generated (e.g. `Meeting.md` and `meeting.md`) that will lead to troubles on case-insensitive file systems (e.g. Win and Mac). In the case of wanting to state that some entity has an object of class Meeting, use `has_meeting` or `has_meetings` depending on the number of allowed objects (remember to set `slot_uri` always in singular).

### Dates and Times

Dates and times are a very important part of political affairs data. When working with dates and times in LinkML, consider the following best practices:

- Use the `date` range for dates without time and the `datetime` range for dates with time.
- Start attributes with `date_` or `datetime_` to make it clear what type of data is expected and to group dates together in alphabetical order.
- If a range of dates is needed, two separate attributes should be used, e.g. `date_begin` and `date_end`.
- If a date is planned or expected but not yet fixed, use `date_planned` to indicate this. This can be combined with `date_actual` for the actual date once it is known.

So, basically the following possible attributes for dates can be used (and all can also exist with time using `datetime` instead of `date`):

- `date_actual`: Some event took place on this date (instantaneous)
- `date_planned`: Some event is planned for this date (instantaneous)
- `date_begin_actual`: Some event started on this date (interval start)
- `date_begin_planned`: Some event is planned to start on this date (interval start)
- `date_end_actual`: Some event ended on this date (interval end)
- `date_end_planned`: Some event is planned to end on this date (interval end)
- `date_created`: The entry for the object was created on this date (instantaneous)
- `date_modified`: The entry for the object was last modified on this date (instantaneous)

## URI Concept

For schema related entities, URIs from https://ld.ech.ch are used. This domain is not yet established but the work of the eCH Specialist Group Political Affairs should help to establish it, so that it can also be used by other eCH Specialist Groups in the future.

### URI for a Schema

https://ld.ech.ch/[subgroup-number]/[schema-name]
e.g. https://ld.ech.ch/0292/meta

### URI for a Class in Schema

https://ld.ech.ch/[subgroup-number]/[schema-name]/[ClassName]
e.g. https://ld.ech.ch/0292/meta/Work

### URI for a Predicate in Schema

https://ld.ech.ch/[subgroup-number]/[schema-name]/[predicateName]
e.g. https://ld.ech.ch/0292/meta/workType

### URI for an Enumeration

https://ld.ech.ch/[subgroup-number]/vocabulary/[enumeration-name]
e.g. https://ld.ech.ch/0292/vocabulary/work-type

### URI for Actual Data

Actual data will not be published under https://ld.ech.ch but under the domain of the respective data provider. There are already some established domains for linked data in Switzerland, e.g.

- Canton of Zurich: https://ld.zh.ch
- Canton of Basel Stadt: https://ld.bs.ch
- City of Zurich: https://ld.stadt-zuerich.ch

Proposals for URIs for actual data:

- Document ([FRBR](https://en.wikipedia.org/wiki/Functional_Requirements_for_Bibliographic_Records) Work): https://ld.bs.ch/[org]/document/[id] e.g. https://ld.bs.ch/gc/document/2026/5c19038b-abbe-415a-87c7-406f7ab75ab2 (gc = Grand Council of Basel Stadt)
- Meeting: https://ld.bs.ch/[org]/meeting/[year]/[type]/[id] e.g. https://ld.bs.ch/gc/meeting/2026/session/7f5c373b-ff94-48a5-99bc-5e97eeb81865 (gc = Grand Council of Basel Stadt)

If IDs are used within URIs, they should be persistent and not dependent on the currently used system. UUIDs are a good choice for this purpose.

See also [Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/).
