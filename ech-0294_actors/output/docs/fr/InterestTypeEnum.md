## Enum: InterestTypeEnum 




_Types de liens d'intérêts (conflits d'intérêts, financement politique)._




<div data-search-exclude markdown="1">

URI: [act:InterestTypeEnum](https://ld.ech.ch/schema/0294/actors/InterestTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| professional_activity |  Activité lucrative en dehors du mandat politique : emploi salarié, activité indépendante, entreprise propre dirigée à titre opérationnel. Pour les salariés, l'employeur et la fonction sont indiqués. Question de contrôle : est-ce là que la personne gagne sa vie ?  |
| | [act:enum/interest_type/professional_activity](act:enum/interest_type/professional_activity) |
| governing_body |  Siège dans un organe de direction, de surveillance ou de conseil d'une organisation poursuivant un but propre — conseil d'administration, conseil de fondation, comité consultatif —, indépendamment de la forme juridique et de la rémunération. Question de contrôle : la personne co-dirige-t-elle une organisation sans y être employée ?  |
| | [act:enum/interest_type/governing_body](act:enum/interest_type/governing_body) |
| interest_group_mandate |  Fonction permanente de direction ou de conseil pour un groupe d'intérêts ou une fédération — une organisation dont le but même est la représentation d'intérêts. C'est l'interlocuteur qui est déterminant, non la fonction : lorsque le but de l'organisation est de représenter des intérêts, cette valeur s'applique même si la fonction consiste en un siège dans un organe de direction. À la différence de `governing_body`, elle couvre en outre les mandats de conseil permanents sans siège dans un organe.  |
| | [act:enum/interest_type/interest_group_mandate](act:enum/interest_type/interest_group_mandate) |
| public_mandate |  Fonction ou siège dans la sphère publique à un autre niveau fédéral ou dans une autre collectivité : siège dans un exécutif ou un législatif communal, dans une commission scolaire ou une paroisse, de même que la participation à une commission ou à un autre organe de la Confédération, d'un canton, d'une commune ou de la coopération intercantonale et intercommunale. La plupart des registres ne distinguent pas les deux cas, raison pour laquelle le standard les réunit en une seule valeur. Le mandat pour lequel la déclaration est faite n'y figure jamais ; la question de savoir si la personne exerce le mandat comme représentante de sa propre collectivité relève de `is_ex_officio`.  |
| | [act:enum/interest_type/public_mandate](act:enum/interest_type/public_mandate) |
| association |  Simple appartenance à une association, une fédération ou une organisation d'intérêts, sans fonction dirigeante ni siège dans un organe. Lorsqu'une fonction est exercée, `governing_body` ou `interest_group_mandate` s'applique.  |
| | [act:enum/interest_type/association](act:enum/interest_type/association) |
| other |  Lien d'intérêts que ne couvre aucune des autres valeurs. La désignation publiée figure dans `function_role` ou `organization_name`, afin que l'entrée reste lisible.  |
| | [act:enum/interest_type/other](act:enum/interest_type/other) |







</div>