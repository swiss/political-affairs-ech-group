## Enum: VotingTypeEnum 




_Type de procédure de vote._




<div data-search-exclude markdown="1">

URI: [ops:VotingTypeEnum](https://ch.paf.link/schema/operations/VotingTypeEnum)

### Valeurs admissibles
| Valeur | Description |
|------------------------|----------------------------------------------------------------------------|
| preliminary_vote |  Vote intermédiaire au cours de la délibération, p. ex. sur l'entrée en matière, sur une proposition, opposition de deux propositions qui s'excluent mutuellement ou portent sur le même passage, vote éventuel lorsque plus de deux propositions portent sur un même objet, sur un article isolé d'une loi, ou vote sur l'ensemble après la première lecture d'un acte délibéré en deux lectures.  |
| | [ops:enum/voting_type/preliminary_vote](ops:enum/voting_type/preliminary_vote) |
| final_vote |  Vote final sur l'objet dans son ensemble, p. ex. après la dernière lecture d'un acte, vote sur l'ensemble d'un arrêté, adoption ou rejet d'un objet dans sa totalité, ou vote point par point sur une intervention parlementaire.  |
| | [ops:enum/voting_type/final_vote](ops:enum/voting_type/final_vote) |
| tie_breaker_president |  Voix prépondérante de la présidente ou du président en cas d'égalité des voix. La présidente ou le président ne participe pas aux votes, mais tranche en cas d'égalité. Si un vote secret aboutit à une égalité, c'est la proposition de l'organe préparatoire qui est réputée adoptée.  |
| | [ops:enum/voting_type/tie_breaker_president](ops:enum/voting_type/tie_breaker_president) |
| secret_vote |  Vote secret, p. ex. sur des objets particulièrement sensibles tels qu'un recours en grâce ou la levée de l'immunité, après une délibération secrète ou sur demande. Seul le résultat global est publié.  |
| | [ops:enum/voting_type/secret_vote](ops:enum/voting_type/secret_vote) |
| other |  Autre type de vote, précisé dans type_label — p. ex. un vote à choix multiple sur plusieurs propositions de même sens (voir TotalOther).  |
| | [ops:enum/voting_type/other](ops:enum/voting_type/other) |







</div>