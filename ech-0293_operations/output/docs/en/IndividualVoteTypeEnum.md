## Enum: IndividualVoteTypeEnum 




_Type of individual vote cast by a member._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| yes |  Yes vote: the member approves the proposal or motion.  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  No vote: the member rejects the proposal or motion.  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Abstention: the member takes part in the voting but abstains; with electronic voting, by pressing the "abstention" button.  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  Not voted: the member did not cast a vote, for instance because they were present but did not vote or were absent.  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Tie-breaking vote, cast by the presiding member in case of a tie (see voting_type tie_breaker_president).  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Vote that cannot be placed on the yes/no axis — for instance in a multiple-choice voting, where the member voted but neither yes nor no; the chosen option is held in type_label (e.g. "Auswahl A"). Counterpart of total_other on the voting, which keeps the individual vote evaluable without a separate enumeration value for every cantonal selection mechanism.  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>