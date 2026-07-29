\newpage

<!-- ToDo: Michel -->

# Agenda, protocol and decisions

The agenda of a sitting is structured by agenda items. The agenda items count as the planning of a sitting and are no longer changed in the data once the sitting has started. The same data elements are then used to record the protocol and the decisions it contains.

If the agenda changes during a sitting, these changes are recorded in the protocol, and the agenda of the next sitting is adjusted accordingly.

## AgendaItem

### Purpose of the entity

AgendaItem structures the agenda of a sitting and connects the temporal organisation (Meeting) with the substantive affairs (Affairs from eCH-0295). It is the central entity for representing the course of a sitting.

### Hierarchy and structure

Agenda items can be organised hierarchically in order to represent the structure of complex agendas:

```
Meeting (sitting of 4 March 2024)
  ├─ AgendaItem 1: announcements and welcome
  ├─ AgendaItem 2: legislative deliberations
  │   ├─ AgendaItem 2.1: energy act (detailed deliberation)
  │   ├─ AgendaItem 2.2: energy act (final vote)
  │   └─ AgendaItem 2.3: health act (entry debate)
  └─ AgendaItem 3: miscellaneous
```

The hierarchy is represented via the field **parent_agenda_item**, which references the superordinate agenda item.

### Identification and numbering

- **id**: unique identifier
- **number**: agenda item number on the agenda (e.g. "2.1", "3")
- **position**: sort order (for the presentation)
- **title**: title of the agenda item

### Types of agenda items

The field **agenda_item_type** distinguishes different kinds:

- **item**: a regular agenda item with deliberation and, where applicable, a voting
- **item_group**: a group of agenda items (e.g. "legislative deliberations")
- **note**: informative entries without a voting (e.g. "announcements")

### Relation to parliamentary affairs

The field **affairs** references the corresponding parliamentary affairs according to eCH-0295. An agenda item can relate to several affairs:

- **Single affair**: an agenda item deals with a specific bill
- **Several affairs**: an agenda item combines related affairs
- **No affair**: administrative agenda items (e.g. "approval of the protocol")

**Example:** the agenda item "Energy act — final vote" references the affair "23.XXX Energy Act" in eCH-0295.

### Temporal planning

- **date_time**: planned point in time of the treatment
- **date_time_actual**: actual point in time of the treatment

This distinction is important because:
- the agenda is fixed in advance
- the actual course can deviate from it
- agenda items can be brought forward, postponed or adjourned

### Status and result

#### Status
The field **status** shows the processing state:
- "pending": not yet dealt with
- "in_progress": currently under deliberation
- "completed": treatment finished
- "postponed": adjourned to a later sitting
- "withdrawn": withdrawn

#### Result
The field **result** records the result of the treatment:
- "accepted": accepted
- "rejected": rejected
- "referred": referred back (e.g. to a committee)
- "noted": noted
- "no_decision": no decision taken

### Categorisation

The field **category** allows grouping according to substantive criteria:
- "Legislation"
- "Budget and finance"
- "Interpellations and questions"
- "Elections"
- "Miscellaneous"

This categorisation is not standardised and can vary from one federal unit to another.

### Resolutions on agenda items

The field **resolution** references the resolution(s) taken on this agenda item. A resolution documents the formal decision:

```
AgendaItem: "Energy act — final vote"
  └─ Resolution: "Acceptance of the energy act with 120 to 75 votes and 5 abstentions"
      └─ Voting: details of the voting
```

### Description and URL

- **description**: detailed description of the agenda item
- **url**: array of multilingual URLs to meeting documents:
  - dispatches and reports
  - motions
  - amendments
  - voting results

### Particularities of the various procedures

#### Legislative procedure
An affair passes through several agenda items:
1. Entry debate
2. Detailed deliberation
3. Final vote
4. Where applicable, elimination of differences between the chambers

#### Interpellations and questions
- Submission as an agenda item
- Answer of the government
- Where applicable, discussion

#### Elections
- Nomination as an agenda item
- Conduct of the election
- Announcement of the result

### Link to other entities

An AgendaItem is the central link between:

- **Meeting**: the sitting in which it is dealt with
- **Affairs** (eCH-0295): the substantive affairs
- **Resolution**: the formal decision
- **Voting**: the voting(s) on the agenda item
- **Speech**: statements and speeches on the agenda item

### Application examples

...

### Purposes of use

1. Structuring the course of the sitting and the agenda
2. Link between meetings and affairs (eCH-0295)
3. Documentation of status and result per agenda item
4. Basis for sitting protocols and publications

{{include:ech-0293_operations/output/docs/AgendaItem.md}}

{{include:ech-0293_operations/output/docs/AgendaItemTypeEnum.md}}

## Protocol

### Purpose of the entity

While the agenda items represent the **planning** of a sitting, the protocol records the **actual course** after the sitting. `Protocol` is a wrapper container kept exactly once per sitting (`Meeting`) that bundles the agenda items actually dealt with (`protocol_items`), votings, speeches as well as verbatim text segments and documents.

```
Meeting
  ├─ agenda_items   (before: planned agenda items)
  └─ protocol_ref   (after: the record)
        ├─ protocol_items  → ProtocolItem (like AgendaItem)
        ├─ votings
        ├─ speeches
        ├─ text_segments
        └─ documents
```

{{include:ech-0293_operations/output/docs/Protocol.md}}

### ProtocolItem (agenda item as recorded)

`ProtocolItem` inherits all fields of `AgendaItem` (`is_a: AgendaItem`) and represents an agenda item as it was actually recorded in the protocol.

{{include:ech-0293_operations/output/docs/ProtocolItem.md}}

## Joint debate (JointDebate)

### Purpose of the entity

`JointDebate` combines several agenda items that are deliberated together — for instance substantively related affairs dealt with in a single debate.

{{include:ech-0293_operations/output/docs/JointDebate.md}}

## Resolution

### Purpose of the entity

The Resolution entity records the formal decision on an agenda item. It documents **what** was decided, while Voting documents **how** (with which procedure and which ratio of votes) the decision was taken.

### Relation to AgendaItem and Voting

```
AgendaItem (Energy act — final vote)
  ├─ Resolution (acceptance of the energy act)
  └─ Voting (120 yes, 75 no, 5 abstentions)
```

An AgendaItem can have several Resolutions (e.g. in case of several votings on the same agenda item). Each Resolution typically references a Voting containing the voting details.

### Types of resolutions

The **resolution_type** field uses a controlled vocabulary:

#### accepted
The agenda item was accepted

**Application:**
- Bills were accepted
- Motions were approved
- Decisions were taken

#### rejected
The agenda item was rejected

**Application:**
- Bills were rejected
- Motions were dismissed
- Rejection decisions

#### referred_back
Referral back to another body

**Application:**
- Referral back to a committee for revision
- Referral back to the government
- Back to the other chamber (in bicameral systems)

#### noted
Noted

**Application:**
- Reports without a voting
- Announcements
- Informative agenda items

#### postponed
Adjourned

**Application:**
- Deferral of the treatment
- Not yet ready for a decision
- Further clarifications needed

#### withdrawn
Withdrawn

**Application:**
- The proposer withdraws the bill
- The affair is not pursued further

#### amended
Accepted with amendments

**Application:**
- Act accepted with amendments
- Modified version adopted
- Compromise solution

#### no_decision
No decision taken

**Application:**
- No majority for any motion
- Tie without a casting vote
- Not able to take decisions

### Design decision: why a separate Resolution entity?

**The alternative would have been:** storing the resolution type directly in AgendaItem.

**Reasons for a separate entity:**

1. **Several decisions per agenda item**: an agenda item can have several decisions (e.g. first an amendment, then the overall vote)

2. **Structured link to votings**: clear 1:1 relation between Resolution and Voting

3. **Multilingual decision texts**: a Resolution can contain detailed decision texts in several languages

4. **Temporal flexibility**: a Resolution can be recorded separately in time from the AgendaItem

### Decision text

- **title**: short summary of the decision
- **description**: detailed decision text

**Example:**
- title: "Acceptance of the energy act"
- description: "The National Council accepts the Federal Act on the Energy Transition in the version of the committee with 120 to 75 votes and 5 abstentions."

### Link to the voting

The field **voting_id** references the corresponding Voting containing the voting details:

- Ratio of votes
- Voting procedure
- Individual votes (in roll-call votings)

**Not all resolutions have a voting:**
- "Noted" often occurs without a formal voting
- Tacit acceptances
- Administrative decisions

### Timestamps

- **datetime_created**: point in time of the decision
- **datetime_modified**: last change (e.g. in case of corrections)

### URLs and documentation

The field **url** can reference further documents:
- Detailed decision texts
- Reasons
- Legal bases

### Use cases in different contexts

#### Legislative procedure
Several resolutions for different phases:
1. Resolution "entry" (accepted/rejected)
2. Resolution on article 1 (accepted/amended)
3. Resolution on article 2 (accepted)
4. Resolution overall vote (accepted/rejected)

#### Elimination of differences (bicameral system)
- Resolution "adherence to the version of the first chamber"
- Resolution "maintaining its own version"
- Resolution "acceptance of the compromise proposal"

#### Committee work
- Resolution "referral back to the committee with an additional mandate"
- Resolution "adoption of the committee report"

### Technical considerations

#### Granularity
The granularity of resolution recording varies:
- **Detailed**: every individual voting gets its own resolution
- **Aggregated**: only the final decision is recorded

The standard permits both approaches.

#### Multilingualism
In multilingual parliaments (CH, BE, etc.) decision texts have to be recorded in all official languages. This is done via MultilingualString arrays in title and description.

### Purposes of use

1. **Official documentation**: what was decided?
2. **Legal force**: formal proof of the decision
3. **Public information**: comprehensible summary of complex votings
4. **Affairs management**: tracking of decisions and their implementation
5. **Statistical evaluation**: acceptance and rejection rates

{{include:ech-0293_operations/output/docs/Resolution.md}}

{{include:ech-0293_operations/output/docs/ResolutionTypeEnum.md}}

## Motion

### Purpose

Records motions submitted during the sitting (amendments, procedural motions, etc.).

### Structure

- **motion_type**: type of the motion
  - **amendment**: amendment to a legal text
  - **procedural**: procedural motion (e.g. closing the debate)
  - **referral**: referral motion
  - **other**: other motions
- **title**: short title of the motion
- **description**: full text of the motion
- **proposer_person_id**: the person submitting the motion
- **seconder_person_id**: seconders (where required)
- **result**: result (accepted, rejected, withdrawn)

### Design decision

**Why a separate entity instead of just in AgendaItem?**
- An agenda item can contain several motions
- Motions have their own life cycle (submitted, seconded, voted on)
- Structured recording of proposer and supporters
- Separate votings per motion are possible

### Application

Linked with AgendaItem and optionally with Voting:

```
AgendaItem (Energy act — art. 15)
  ├─ Motion (amendment person A)
  │   └─ Voting (voting on the amendment)
  ├─ Motion (amendment person B)
  │   └─ Voting (voting on the amendment)
  └─ Voting (voting on the article as a whole)
```

{{include:ech-0293_operations/output/docs/Motion.md}}
