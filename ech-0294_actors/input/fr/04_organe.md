\newpage

# Groupes et organes (Groups)

Le schéma Group représente les groupes, organisations et corporations politiques.

- **Un modèle générique plutôt que de nombreuses classes spécialisées :** les parlements, partis, groupes parlementaires, commissions, départements, tribunaux et organisations de la société civile sont tous représentés par *une seule* classe `Group` et différenciés au moyen de `group_type`. Cela maintient le modèle simple et extensible sans modification du schéma – le législatif, l'exécutif, le judiciaire et la société civile peuvent ainsi être représentés de manière équivalente.
- **Groupes et sous-groupes au moyen de `parent_groups` :** les groupes subordonnés renvoient à leur groupe supérieur – p. ex. une commission du Conseil des États, une sous-commission au sein d'une commission, un parti cantonal sous son parti mère ou une autorité au sein d'une direction. La hiérarchie découle ainsi de ces renvois plutôt que d'une structure de niveaux fixe. Elle reste le plus souvent au sein d'un même `group_type` ; des renvois transversaux et multiples sont toutefois possibles (p. ex. un groupe parlementaire qui renvoie à la fois à son parlement et à son parti). Le renvoi prend la forme d'une `GroupReference` – la même que celle par laquelle une affiliation désigne son groupe. Que le lien exprime un rapport de subordination est indiqué par le slot `parent_groups` lui-même ; la référence ne porte que l'adressage. Celui-ci peut se faire au moyen du `local_id` lorsque le groupe supérieur fait partie de la même livraison, ou du `global_uri` lorsqu'il se situe en dehors – un parti cantonal peut ainsi renvoyer à son parti national sans que celui-ci doive être livré. Comme la référence peut en outre porter un libellé, une liste de plusieurs groupes supérieurs reste lisible.
- **Validité temporelle également pour les groupes :** au moyen de `valid_from`/`valid_through`, il est possible de représenter p. ex. des commissions n'existant que durant une législature, ou des changements de nom et des fusions de partis.

{{include:ech-0294_actors/output/docs/Group.md}}

{{include:ech-0294_actors/output/docs/GroupType.md}}

{{include:ech-0294_actors/output/docs/GroupTypeEnum.md}}