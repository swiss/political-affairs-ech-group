## Enum: GroupTypeEnum 




_Types of political groups and organizations. Three conventions apply._

__

_The value states the political function; the group's label keeps the designation used locally. Büro, Ratsleitung and Ufficio presidenziale are all recorded as council_bureau and thus stay comparable._

__

_Values that belong together share a prefix. The council_ family does not distinguish by council: a state chancellery and parliamentary services are both a council_secretariat, and which council a body belongs to is stated by its parent group. The same applies to the committee_ family, with committee as the base case._

__

_Legal form does not belong here but in legal_form._

__



<div data-search-exclude markdown="1">

URI: [act:GroupTypeEnum](https://ld.ech.ch/schema/0294/actors/GroupTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| party |  Political party at federal, cantonal, or municipal level. Each federal level is managed as its own group (e.g., national party, cantonal party, municipal party).  |
| | [act:enum/group_type/party](act:enum/group_type/party) |
| list |  Electoral list (can be part of a party or independent).  |
| | [act:enum/group_type/list](act:enum/group_type/list) |
| workgroup |  Ad-hoc working group, typically with a limited duration.  |
| | [act:enum/group_type/workgroup](act:enum/group_type/workgroup) |
| assembly |  Assembly of the persons entitled to vote acting as the legislative body, in particular the communal assembly ("Gemeindeversammlung"). Unlike a council, it is not an elected body.  |
| | [act:enum/group_type/assembly](act:enum/group_type/assembly) |
| council_legislative |  Parliament at federal, cantonal, or municipal level (e.g., Federal Assembly, National Council, Council of States, Grand Council, cantonal parliament, municipal parliament).  |
| | [act:enum/group_type/council_legislative](act:enum/group_type/council_legislative) |
| delegation |  Delegation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| committee |  Standing committee, including supervisory committees (e.g., CPC), subject commissions, parliamentary investigation commissions (PIC), and audit commissions.  |
| | [act:enum/group_type/committee](act:enum/group_type/committee) |
| committee_ad_hoc |  Committee set up for a single task and dissolved once it is completed, in contrast to a standing committee.  |
| | [act:enum/group_type/committee_ad_hoc](act:enum/group_type/committee_ad_hoc) |
| parliamentary_group |  Parliamentary faction.  |
| | [act:enum/group_type/parliamentary_group](act:enum/group_type/parliamentary_group) |
| council_bureau |  Body managing the business of a council, whatever it is called locally (bureau, council management, executive board). Used for the legislative as well as the executive council; the local designation is recorded in the label.  |
| | [act:enum/group_type/council_bureau](act:enum/group_type/council_bureau) |
| council_presidency |  Presidency of a council, for the legislative as well as the executive council.  |
| | [act:enum/group_type/council_presidency](act:enum/group_type/council_presidency) |
| council_executive |  Government / Executive as a collective body (e.g., Federal Council, Cantonal Government, City or Municipal Council).  |
| | [act:enum/group_type/council_executive](act:enum/group_type/council_executive) |
| department |  Government department.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Government office.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| committee_extraparliamentary |  Commission normally appointed by the government to advise the administration in its field and to give its business a first reading; some also hold decision-making powers of their own. What sets it apart from a parliamentary committee are its composition and its legal basis: its members are external experts and interest-group representatives rather than members of the council, and it rests on the law governing the organisation of the government and the administration rather than on parliament law. The type exists at federal and at cantonal level alike (e.g., the federal Competition Commission; the commissions extraparlementaires in the canton of Vaud). A committee whose members are members of the council is not covered by this value even when it is attached to the executive; it is recorded as a committee or an ad hoc committee with the executive council as its parent group.  |
| | [act:enum/group_type/committee_extraparliamentary](act:enum/group_type/committee_extraparliamentary) |
| interest_group |  Interest group from civil society.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| control_body |  Control or supervisory body (e.g., Federal Finance Control EFC, supervisory authority AB-BA).  |
| | [act:enum/group_type/control_body](act:enum/group_type/control_body) |
| council_secretariat |  Administrative unit serving a council, whatever it is called locally (parliamentary services, council secretariat, state, cantonal or municipal chancellery). Used for the legislative as well as the executive council: the state chancellery is the staff unit of the executive council, the parliamentary services are that of the legislative council.  |
| | [act:enum/group_type/council_secretariat](act:enum/group_type/council_secretariat) |
| court |  Court / Judiciary at any level (e.g., Federal Court, Cantonal Court, District Court).  |
| | [act:enum/group_type/court](act:enum/group_type/court) |
| association |  Association.  |
| | [act:enum/group_type/association](act:enum/group_type/association) |
| petition_carrier |  Petition carrier.  |
| | [act:enum/group_type/petition_carrier](act:enum/group_type/petition_carrier) |
| university |  University or educational institution as an outsourced provider of public tasks.  |
| | [act:enum/group_type/university](act:enum/group_type/university) |
| other |  Other group type not covered by standard categories.  |
| | [act:enum/group_type/other](act:enum/group_type/other) |







</div>