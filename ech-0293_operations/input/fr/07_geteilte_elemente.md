\newpage

# Éléments partagés

## Classes de référence

`PersonReference` et `GroupReference` désignent respectivement une personne et un groupe sans les décrire ici : ce qu'est une personne ou un organe est défini par eCH-0294 ; le fonctionnement des conseils ne fait qu'y renvoyer. Outre le renvoi, la référence retient les principales caractéristiques **au moment de la mise en relation** — pour une intervention, par exemple, le groupe parlementaire auquel la personne appartenait alors.

Cela sert trois objectifs :

- **Des données locales utiles** sans interrogation coûteuse de l'entité complète
- **Pas de redondance**, puisque toutes les indications ne doivent pas être répétées à chaque mention
- **Un versionnage implicite**, la référence restant inchangée même si la personne ou le groupe lié évolue par la suite

Contrairement à une entité, une référence n'est pas identifiée en propre — elle ne fait que désigner une entité identifiée. C'est pourquoi la `global_uri` n'y est pas obligatoire : il est seulement exigé qu'au moins l'une des deux indications `local_id` ou `global_uri` soit renseignée. Un système qui ne connaît de l'entité référencée que l'identifiant local indique celui-ci ; il est résolu au sein de la même livraison. Au-delà de la livraison, c'est la `global_uri` qui renvoie.

{{include:ech-0293_operations/output/docs/PersonReference.md}}

{{include:ech-0293_operations/output/docs/GroupReference.md}}

## Classes mixin

Trois classes ne portent pas de données propres : elles regroupent des slots qui se présentent de la même manière dans de nombreuses classes — l'identification d'une entité, ses dates de création et de modification ainsi que le déroulement temporel d'un événement, avec un début et une fin planifiés et effectifs. Elles proviennent du schéma commun du groupe spécialisé (eCH-0292) et sont intégrées par les normes de celui-ci, afin que les mêmes indications portent partout le même nom et fonctionnent de la même façon.

Un mixin n'est pas une superclasse : aucune instance d'une classe mixin n'est créée et rien n'en apparaît dans les données. Les tableaux d'attributs des classes énumèrent donc individuellement les slots hérités et en signalent la provenance par la mention « Héritage » — les trois sections suivantes expliquent ce qui se cache derrière cette indication.

{{include:ech-0293_operations/output/docs/HasIdentification.md}}

{{include:ech-0293_operations/output/docs/HasCreationModificationDates.md}}

{{include:ech-0293_operations/output/docs/IsEventWithDuration.md}}
