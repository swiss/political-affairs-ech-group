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