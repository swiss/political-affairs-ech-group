\newpage

# Groupes et organes (Groups)

Le schéma Group représente les groupes, organisations et corporations politiques.

- **Un modèle générique plutôt que de nombreuses classes spécialisées :** les parlements, partis, groupes parlementaires, commissions, départements, tribunaux et organisations de la société civile sont tous représentés par *une seule* classe `Group` et différenciés au moyen de `group_type`. Cela maintient le modèle simple et extensible sans modification du schéma – le législatif, l'exécutif, le judiciaire et la société civile peuvent ainsi être représentés de manière équivalente.
- **Groupes et sous-groupes au moyen de `parent_groups` :** les groupes subordonnés renvoient à leur groupe supérieur – p. ex. une commission du Conseil des États, une sous-commission au sein d'une commission, un parti cantonal sous son parti mère ou une autorité au sein d'une direction. La hiérarchie découle ainsi de ces renvois plutôt que d'une structure de niveaux fixe. Elle reste le plus souvent au sein d'un même `group_type` ; des renvois transversaux et multiples sont toutefois possibles (p. ex. un groupe parlementaire qui renvoie à la fois à son parlement et à son parti).
- **Validité temporelle également pour les groupes :** au moyen de `valid_from`/`valid_through`, il est possible de représenter p. ex. des commissions n'existant que durant une législature, ou des changements de nom et des fusions de partis.

{{include:ech-0294_actors/output/docs/Group.md}}

{{include:ech-0294_actors/output/docs/GroupType.md}}

{{include:ech-0294_actors/output/docs/GroupTypeEnum.md}}