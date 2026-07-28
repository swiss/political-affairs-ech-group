## Enum: GroupTypeEnum 




_Types de groupes et d'organisations politiques. Trois conventions régissent ce vocabulaire._

__

_Premièrement, la valeur désigne la fonction politique, tandis que la désignation employée localement est conservée dans le libellé du groupe. Le même organe s'appelle Büro dans un canton, Ratsleitung ou Geschäftsleitung dans un autre, Ufficio presidenziale au Tessin ; tous sont saisis comme council_bureau, afin qu'ils restent comparables par-delà les cantons et les niveaux, sans que la désignation locale se perde._

__

_Deuxièmement, les valeurs qui vont ensemble partagent un préfixe. La famille council_ regroupe les conseils et leurs organes et ne distingue délibérément pas selon le conseil : une chancellerie d'État sert l'exécutif, les services du parlement servent le législatif, mais les deux sont un council_secretariat. Le conseil auquel un organe se rattache ressort du groupe supérieur, non du type. La famille committee_ fonctionne de même, avec committee comme cas de base et committee_ad_hoc ainsi que committee_extraparliamentary comme variantes qualifiées._

__

_Troisièmement, ce vocabulaire ne consigne pas la forme juridique. Qu'une organisation soit une association, une fondation ou une société anonyme s'indique dans legal_form au moyen de la liste de codes du registre IDE fédéral ; group_type reste réservé à la fonction politique._

__



<div data-search-exclude markdown="1">

URI: [act:GroupTypeEnum](https://ld.ech.ch/schema/0294/actors/GroupTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| party |  Parti politique au niveau fédéral, cantonal ou communal. Chaque niveau fédéral est géré comme un groupe distinct (p. ex. parti national, parti cantonal, parti communal).  |
| | [act:enum/group_type/party](act:enum/group_type/party) |
| list |  Liste électorale (peut faire partie d'un parti ou être indépendante).  |
| | [act:enum/group_type/list](act:enum/group_type/list) |
| workgroup |  Groupe de travail ad hoc, généralement d'une durée limitée.  |
| | [act:enum/group_type/workgroup](act:enum/group_type/workgroup) |
| assembly |  Assemblée des personnes ayant le droit de vote en tant qu'organe législatif, en particulier l'assemblée communale. Contrairement à un conseil, elle n'est pas un organe élu.  |
| | [act:enum/group_type/assembly](act:enum/group_type/assembly) |
| council_legislative |  Parlement au niveau fédéral, cantonal ou communal (p. ex. Assemblée fédérale, Conseil national, Conseil des États, Grand Conseil, parlement cantonal, parlement communal).  |
| | [act:enum/group_type/council_legislative](act:enum/group_type/council_legislative) |
| delegation |  Délégation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| committee |  Commission permanente, y compris les commissions de surveillance (p. ex. CdG), les commissions thématiques, les commissions d'enquête parlementaire (CEP) et les commissions de vérification des comptes.  |
| | [act:enum/group_type/committee](act:enum/group_type/committee) |
| committee_ad_hoc |  Commission instituée pour une tâche unique et dissoute une fois celle-ci accomplie, par opposition à une commission permanente.  |
| | [act:enum/group_type/committee_ad_hoc](act:enum/group_type/committee_ad_hoc) |
| parliamentary_group |  Groupe parlementaire.  |
| | [act:enum/group_type/parliamentary_group](act:enum/group_type/parliamentary_group) |
| council_bureau |  Organe dirigeant la marche des affaires d'un conseil, quelle que soit sa désignation locale (bureau, direction du conseil, comité de direction). S'emploie aussi bien pour le conseil législatif que pour le conseil exécutif ; la désignation locale est consignée dans le libellé.  |
| | [act:enum/group_type/council_bureau](act:enum/group_type/council_bureau) |
| council_presidency |  Présidence d'un conseil, pour le conseil législatif comme pour le conseil exécutif.  |
| | [act:enum/group_type/council_presidency](act:enum/group_type/council_presidency) |
| council_executive |  Gouvernement / exécutif en tant qu'organe collégial (p. ex. Conseil fédéral, conseil d'État, conseil municipal ou conseil communal).  |
| | [act:enum/group_type/council_executive](act:enum/group_type/council_executive) |
| department |  Département gouvernemental.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Office gouvernemental.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| committee_extraparliamentary |  Commission généralement instituée par le gouvernement pour conseiller l'administration dans son domaine et pour examiner ses affaires au préalable ; certaines disposent en outre de compétences décisionnelles propres. Ce qui la distingue d'une commission parlementaire sont sa composition et sa base légale : ses membres sont des spécialistes externes et des représentantes et représentants d'intérêts plutôt que des membres du conseil, et elle se fonde sur le droit régissant l'organisation du gouvernement et de l'administration et non sur le droit parlementaire. Ce type existe tant au niveau fédéral qu'au niveau cantonal (p. ex. la Commission de la concurrence de la Confédération ; les commissions extraparlementaires du canton de Vaud). Une commission dont les membres sont des membres du conseil ne relève pas de cette valeur, même lorsqu'elle est rattachée à l'exécutif ; elle est saisie comme commission ou commission ad hoc avec le conseil exécutif comme groupe supérieur.  |
| | [act:enum/group_type/committee_extraparliamentary](act:enum/group_type/committee_extraparliamentary) |
| interest_group |  Groupe d'intérêts issu de la société civile.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| control_body |  Organe de contrôle ou de surveillance (p. ex. Contrôle fédéral des finances CDF, autorité de surveillance AS-MPC).  |
| | [act:enum/group_type/control_body](act:enum/group_type/control_body) |
| council_secretariat |  Unité administrative au service d'un conseil, quelle que soit sa désignation locale (services du parlement, secrétariat du conseil, chancellerie d'État, cantonale ou communale). S'emploie aussi bien pour le conseil législatif que pour le conseil exécutif : la chancellerie d'État est l'état-major du conseil exécutif, les services du parlement celui du conseil législatif.  |
| | [act:enum/group_type/council_secretariat](act:enum/group_type/council_secretariat) |
| court |  Tribunal / pouvoir judiciaire à tout niveau (p. ex. Tribunal fédéral, tribunal cantonal, tribunal de district).  |
| | [act:enum/group_type/court](act:enum/group_type/court) |
| association |  Association.  |
| | [act:enum/group_type/association](act:enum/group_type/association) |
| petition_carrier |  Porteur de pétition.  |
| | [act:enum/group_type/petition_carrier](act:enum/group_type/petition_carrier) |
| university |  Université ou établissement d'enseignement en tant que prestataire externalisé de tâches publiques.  |
| | [act:enum/group_type/university](act:enum/group_type/university) |
| other |  Autre type de groupe non couvert par les catégories standard.  |
| | [act:enum/group_type/other](act:enum/group_type/other) |







</div>