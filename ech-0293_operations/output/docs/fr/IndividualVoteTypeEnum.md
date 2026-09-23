## Enum: IndividualVoteTypeEnum 




_Type de voix individuelle exprimée par un membre._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| yes |  Oui : le membre approuve l'objet ou la proposition.  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  Non : le membre rejette l'objet ou la proposition.  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Abstention : le membre participe au vote mais s'abstient ; en cas de vote électronique, il presse le bouton « abstention ».  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  N'a pas voté : le membre n'a pas exprimé de voix, par exemple parce qu'il était présent sans voter ou absent.  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Voix prépondérante, exprimée par la présidente ou le président en cas d'égalité des voix (voir voting_type tie_breaker_president).  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Voix qui ne peut être placée sur l'axe oui/non — par exemple lors d'un vote à choix multiple, où le membre a voté, mais ni oui ni non ; l'option choisie est retenue dans type_label (p. ex. « Choix A »). Pendant de total_other sur le vote ; la voix individuelle reste ainsi exploitable sans qu'il faille une valeur d'énumération propre pour chaque mécanisme de choix cantonal.  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>