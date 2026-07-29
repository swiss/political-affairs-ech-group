\newpage

<!-- ToDo: Nicole -->

# Votings and elections

Parliamentary decisions are taken either by votings on substantive questions or by elections of persons. The standard clearly distinguishes these two mechanisms and additionally records, in open procedures, the individual voting behaviour of every member of parliament. Presidents of parliament generally do not take part in votings; they only vote in elections. In votings with a tie they cast the deciding vote.

## Voting

## Purpose of the entity

"Voting" records the voting process and the result of a formal decision in parliament. The entity documents the subject of the voting (the question), the procedure (how the vote was taken) and the result (with which ratio of votes).

## Types of votings

The standard distinguishes different voting types via the field **voting_type**:

### intermediate
Intermediate votings during the deliberation.

**Examples:**
- Voting on entering into an affair
- Voting on a motion
- Opposing two motions that exclude each other or that refer to the same passage of text
- Contingent voting when more than two motions relate to the same subject
- Voting on a single article of an act
- Overall vote after the first reading of an enactment deliberated in two readings

### final
The concluding voting on the entire bill

**Examples:**
- Final vote after the last reading of an enactment
- Overall vote on a decree
- Acceptance or rejection of a bill as a whole
- Point-by-point voting on a parliamentary initiative

### casting
Deciding vote of the chair in case of a tie. The chair does not take part in votings but has the deciding vote in case of a tie. In a secret voting, in case of a tie the motion of the preliminarily deliberating council body counts as accepted.

### secret
Secret casting of votes in votings and elections

**Application:**
- Election of persons
- Voting on a particularly sensitive substantive affair such as a pardon request or the lifting of immunity
- Voting after a confidential deliberation
- Secret voting upon request

## Structure of a voting

A voting is always assigned to a sitting phase and/or a sitting, an agenda item and an affair with an affair title and an affair number. It comprises the voting type, the subject of the voting (the question), the result and — in a non-secret voting — the individual votes of the members.
It can either:

```
AgendaItem (15) affair (Energy act — art. 15)
  └─ Voting (intermediate voting on art. 15)
      ├─ IndividualVote (person A: yes)
      ├─ IndividualVote (person B: no)
      └─ IndividualVote (person C: yes)
```


Example selection:
3 options: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
5 options: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=23f01ba9b3f3410cb9cfb85f32f3dfe0

## Voting procedures

The field **procedure** describes how the vote is conducted:

### Open procedures
- **show_of_hands**: show of hands (traditional)
- **standing**: standing up (rarer)
- **electronic**: electronic voting (frequent at federal and cantonal level)
- **roll_call**: roll-call voting with calling of names
- **remote_voting**: external casting of votes during crises (individual council members communicate their vote to the parliamentary presidency ahead of the sitting day. The externally cast votes are recorded simultaneously with the voting running in the council.)
- **circulation_voting**: circulation procedure during crises (the parliamentary presidency conducts the voting by circulation and informs about the result)
- **virtual_voting**: casting of votes at virtual sittings during crises.

### Secret procedures
- **secret_ballot**: secret ballot with voting slips
- **electronic_secret**: electronic secret voting

The choice of procedure determines whether individual votes can be recorded:
- Open procedures: individual votes can be documented
- Secret procedures: only the overall result is available


## Voting result

The result is recorded in two ways:

### Detailed figures
- **total_count_yes**: number of yes votes
- **total_count_no**: number of no votes
- **total_count_abstention**: number of abstentions
- **total_other**: numbers of votes for additional options where not only yes/no/abstention are available (see the section "Multiple options")
- **total_absent**: number of absent members (who could not vote)
- **total**: total number of voting members (without absentees and the presidency's vote)
- **majority_count**: number of votes required for the necessary majority

### Overall result
The result is described as free text in the field **result_text** (e.g. "Accepted with 120 to 75 votes and 5 abstentions"). The categorical decision (accepted / rejected / noted etc.) is not recorded on the voting itself but via the class **Resolution** (slot **resolution_type**) on the agenda item. In case of a tie, a possible deciding vote of the presidency is modelled via a separate voting (`voting_type: tie_breaker_president`) respectively a new voting.

**Example** (final vote, simple yes/no voting):
- total_count_yes: 120
- total_count_no: 75
- total_count_abstention: 5
- total_absent: 0
- total: 200
- result_text: "Accepted with 120 to 75 votes and 5 abstentions"
- Resolution.resolution_type: accepted

<!-- TODO: weitere komplexere Beispiele ergänzen — Ordnungsantrag, Wiederholung einer Abstimmung. (Cup-/Mehrfachabstimmung und Stichentscheid sind abgedeckt.) -->

### Multiple options (selection votings / "motions in the same direction")

Not every voting knows only yes, no and abstention. If several motions in the same direction relate to the same substantive question, the members vote on more than two variants simultaneously (in Zurich colloquially "cup voting", technically via several voting buttons). The prevailing variant is the one with the most votes.

Such procedures are represented as follows:

- **voting_type** = `other`, complemented by a meaningful **type_label** (e.g. "Motions in the same direction (multiple choice)").
- The standard fields **total_count_yes / total_count_no / total_count_abstention** remain empty, because the options do not correspond to yes/no/abstention.
- Instead, every selection option gets an entry in **total_other** (list of `TotalOther` with **count** and **label**). This allows any number of options with their respective vote counts to be recorded.
- At the level of the individual vote, **individual_vote_type** is set to `other` and the chosen option is recorded via **type_label** (e.g. "Selection A"); absent members get `not_voted`.
- As **majority_type**, `other` is used, because it is not a fixed threshold but the relative majority among the options that decides.

**Example** (City of Zurich communal council, 86th sitting of 28.02.2024, affair 2023/361 "Residential building Magnusstrasse 27, net additional credit") — motions in the same direction with four selection options:

| Option | Votes |
|--------|-------|
| Selection A (prevailing) | 75 |
| Selection B | 25 |
| Selection C | 12 |
| Selection D | 0 |
| Absent | 13 |

- Total cast: 112 (of 125 members)
- Result: selection A accepted (relative majority)

The complete modelling of this case can be found in `data_voting.yaml` (`ops:voting_zh_gr_2024_2023_361`).

## Majority types

The field **majority_type** defines the required majority:

### simple
Simple majority (more yes than no)

**Application:**
- Standard case for most decisions
- Abstentions do not count

**Example:** 100 yes, 80 no, 20 abstentions → accepted

### absolute
Absolute majority (more than half of all members)

**Application:**
- Elections
- Constitutional amendments in some cantons
- Particularly important decisions

**Example:** with 200 members at least 101 yes votes are required

### two_thirds
Two-thirds majority

**Application:**
- Urgency clauses at federal level
- Constitutional amendments in some cantons
- Lifting of immunity

**Example:** with 200 members at least 134 yes votes are required

### qualified
Qualified majority (other thresholds)

**Application:**
- Special requirements in individual cantons or communes
- The concrete quorum is indicated in **majority_threshold**

## Threshold

For qualified majorities, the field **majority_threshold** indicates the exact threshold (e.g. 0.6 for 60%).

## Quorum

The field **quorum** defines the minimum number of members present for the capacity to take decisions:

**Example:** a parliament with 200 members can take decisions if at least 100 members are present (quorum: 100).

## Roll-call votings
The field **named_vote** indicates whether the voting is a roll-call voting:

- **true**: the individual votes are recorded and published
- **false**: only the overall result is recorded

Roll-call votings are important for:
- transparency of voting behaviour
- analysis of voting patterns
- accountability towards the electorate

## Relation to individual votes

In roll-call votings the Voting entity references the individual IndividualVote entities:

```
Voting
  ├─ IndividualVote (person A)
  ├─ IndividualVote (person B)
  └─ ...
```

**Example:** name list in an accordion https://www.tagblatt.gr.be.ch/shareparl?agendaItemUid=e65d81c90d1d43deb19ef078f7e363f3&segmentType=vote&unitName=default&scroll=true&autoplay=false


## Description and documentation

- **description**: description of what was voted on (subject of the voting, voting question)
- **url**: multilingual URLs to voting details

## Timestamps

- **datetime_created**: point in time of conducting the voting
- **datetime_modified**: last update (e.g. in case of corrections to the voting protocol)


{{include:ech-0293_operations/output/docs/Voting.md}}

{{include:ech-0293_operations/output/docs/VotingTypeEnum.md}}

{{include:ech-0293_operations/output/docs/MajorityTypeEnum.md}}

## Individual Vote

## Purpose of the entity

IndividualVote records the voting behaviour of individual members of parliament in roll-call votings. The entity is only created if a voting is not conducted secretly (Voting.is_nominal = true).

## Relation to the voting

Every individual vote is part of a superordinate voting:

```
Voting (final vote energy act)
  ├─ IndividualVote (National Councillor Anna Müller: yes)
  ├─ IndividualVote (National Councillor Beat Schweizer: no)
  ├─ IndividualVote (National Councillor Carla Rossi: abstention)
  └─ ...
```

## Identification of the person

The voting person is referenced via the field **person_id**. This ID corresponds to a person according to the eCH-0294 Actors standard.

Additional identification data can be recorded as well:
- **person_name**: name of the person (for quick access)
- **person_number**: internal number (e.g. mandate number)
- **person_political_group**: parliamentary group affiliation
- **person_party**: party affiliation

## Types of votes

TODO: describe the handling of "other" votes, i.e. votes for options that are not yes, no or abstention.

The field **vote** records the type of the vote cast:

### yes
Yes vote (approval)

**Meaning:** the person approves the bill / the motion.

### no
No vote (rejection)

**Meaning:** the person rejects the bill / the motion.

### abstention
Abstention

**Meaning:** the person takes part in the voting but abstains. When voting electronically, they press the "abstention" button.

## Vote weight

The field **weight** records the weight of the vote:

- **Standard case**: 1.0 (one vote)
- **Special cases**: other values possible

### Use cases for a divergent vote weight

1. **Substitution**: in some systems a person can vote on behalf of an absent person (weight: 2.0)
3. **Communal assemblies**: in special cases legal entities can hold several votes
4. **Historical systems**: in some cantons different groups of persons formerly had different vote weights

## Group affiliation

The field **group_id** records the parliamentary group affiliation at the time of the voting:

**Benefit:**
- Analysis of voting behaviour by group
- Determination of party discipline
- Identification of coalitions

**Example:** in a voting on the energy act 90% of the SP group vote yes, 80% of the SVP group vote no.

## Position and order

The field **position** defines the grouping and sort order in the presentation:

**Application:**
- Alphabetical sorting by surname
- Sorting by parliamentary group
- Sorting by vote cast (first yes, then no, then abstentions)
- Grouping by parliamentary group, within the group by yes, no, abstentions and within the subgroup alphabetically

## Description and context

The field **description** can record additional information:

**Examples:**
- "Abstention due to a conflict of interest (board member of an energy company)"
- "Absent due to illness"

## Timestamps

- **datetime_created**: first publication
- **datetime_modified**: last update (e.g. in case of corrections to the publication)

## Attendance vs. casting a vote

Important difference:

- **Attendance** (another entity): records the general presence at a sitting
- **IndividualVote**: records the specific vote cast in a voting

A person can be present at a sitting (Attendance) but be recorded as "absent" or "did_not_vote" in individual votings (e.g. when briefly leaving the room).

## Roll-call vs. secret votings

IndividualVote entities are only recorded in roll-call (open) votings:

- **Roll-call voting**: every vote is recorded and is public
- **Secret voting**: only the overall result is recorded, no IndividualVotes

{{include:ech-0293_operations/output/docs/IndividualVote.md}}

{{include:ech-0293_operations/output/docs/IndividualVoteTypeEnum.md}}

## Election

## Term and meaning

An election denotes the designation of one or more persons to an office or a function by a parliamentary body. In contrast to votings, in which substantive questions are decided, elections concern decisions about persons.

## Difference: election vs. voting

| Criterion | Election | Voting |
|-----------|----------|--------|
| Subject | Persons | Substantive questions, bills |
| Result | Elected person(s) | Accepted / rejected |
| Procedure | Often secret | Often open |
| Majority | Mostly absolute | Mostly simple |

## Types of elections

The standard distinguishes different election types via the field **election_type**:

### open
Open election

**Characteristic:**
- The casting of votes is publicly visible
- Every member casts their vote openly
- It is traceable who elected whom

**Application:**
- Where transparency is desired
- In uncontested elections
- In smaller bodies

### secret
Secret election

**Characteristic:**
- The casting of votes is anonymous
- Voting slips or an electronic secret voting system
- It is not traceable who elected whom

**Application:**
- Elections of persons (standard)
- Where a free, uninfluenced decision is to be guaranteed
- Often prescribed by law

**Examples at federal level:**
- Election of the Federal Council
- Election of the federal judges
- Election of the committee presidencies

**Examples at cantonal level:**
- Election of the president of the parliament
- Election of the president of the government
- Election of the presidents of the highest cantonal courts
- Election of the judges
- Election of the state chancellor
- Election of the committee presidencies

### tacit
Tacit election

**Characteristic:**
- No formal voting required
- The election takes place by acclamation or consensus
- Only if no opposing votes are raised

**Application:**
- In case of unanimity
- Uncontested elections
- Re-elections without an opposing candidate

**Example:** re-election of a committee president without an opposing candidacy

## Assignment to agenda items

Every election is assigned to an agenda item:

```
AgendaItem (election of the Federal Council)
  └─ Election (election for department XY)
      ├─ Candidate A: 120 votes
      ├─ Candidate B: 75 votes
      └─ Blank ballots: 5
```

## Description and title

- **title**: title of the election (e.g. "Election of the WAK committee presidency")
- **description**: detailed description, context, special circumstances

## Election result

The field **result** records the result:

- **elected**: person(s) elected
- **not_elected**: no person elected (e.g. absolute majority not reached)
- **deferred**: election postponed
- **withdrawn**: election withdrawn

## Elected person(s)

The field **elected_person_id** contains the ID(s) of the elected person(s) according to eCH-0294 Actors.

In case of multiple elections (e.g. election of several committee members at once) several IDs can be recorded.

## Distribution of votes

In open elections or after publication of the results:

- **total_votes**: total number of votes cast
- **valid_votes**: valid votes
- **invalid_votes**: invalid votes
- **blank_votes**: blank ballots

Additionally details per candidate (via separate entities or as structured data).

## Election procedure

The field **procedure** describes the concrete procedure:

- **written_ballot**: written election with voting slips
- **electronic**: electronic election
- **show_of_hands**: show of hands (in open elections)
- **acclamation**: acclamation (in tacit elections)

## Majority requirements

The field **majority_type** defines the required majority:

### absolute
Absolute majority (more than half of those voting)

**Application:**
- Federal Council election
- Election of committee presidencies
- Standard case for elections of persons

**Example:** with 200 votes cast at least 101 votes are required

**Particularity:** if nobody reaches the absolute majority in the first round, a second round usually follows in which a simple majority suffices.

### simple
Simple majority (more votes than the other candidates)

**Application:**
- Second round after an unsuccessful first round
- Some committee elections

### qualified
Qualified majority

**Application:**
- Rarer in elections
- Special functions with increased requirements

## Rounds of voting

In elections requiring an absolute majority in the first round:

```
1st round (absolute majority required)
   └─ No candidate reaches the absolute majority

2nd round (simple majority suffices)
   └─ Candidate A elected
```

Every round is recorded as a separate Election entity, connected via the common agenda item.

## Timestamps

- **datetime_created**: point in time of conducting the election
- **datetime_modified**: last update

## URL and documentation

- **url**: multilingual URLs to election documents:
  - candidate profiles
  - election results
  - protocols

## Particularities of the various elections

### Federal Council election
- Secret election
- Absolute majority required (in the 1st round)
- By the United Federal Assembly

### Federal judge election
- Secret election
- Proportional principle (consideration of parties, regions, genders)

### Committee presidencies
- Election by the respective parliament
- Often less public

### Cantonal and communal level
- Great variety of election procedures
- Partly popular election instead of parliamentary election
- Differing majority requirements

## Transparency and confidentiality

Field of tension:
- **Secrecy of the ballot**: protection of the individual electoral decision
- **Transparency**: public interest in the election result

In secret elections:
- Only the overall result is published
- No IndividualVote entities
- Protection of the freedom of choice

In open elections:
- Individual votes cast can be recorded
- Higher transparency
- Potential social pressure effects

{{include:ech-0293_operations/output/docs/Election.md}}

{{include:ech-0293_operations/output/docs/ElectionTypeEnum.md}}
