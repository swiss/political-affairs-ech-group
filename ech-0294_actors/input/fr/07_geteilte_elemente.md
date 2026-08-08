\newpage

# Éléments partagés

## Reference Classes

`PersonReference` et `GroupReference` sont utilisés pour référencer **localement** des personnes ou des groupes au sein d'une autre entité. Outre le lien proprement dit vers l'entité complète, seules les informations pertinentes au **moment de la mise en relation** sont enregistrées – il n'est donc pas nécessaire de répéter toutes les informations d'une personne ou d'un groupe à chaque mention.

Un exemple : une motion renvoie à la personne qui l'a déposée. En plus du lien vers l'entité complète de la personne, la motion enregistre localement des informations telles que le parti politique ou le rôle de la personne **au moment du dépôt**. Si la personne change ultérieurement de parti ou de rôle, l'information dans la motion demeure néanmoins correcte et immuable.

Cela sert trois objectifs :

- **Des données locales utiles** sans requêtes coûteuses sur l'entité complète
- **Aucune redondance**, car il n'est pas nécessaire de répéter toutes les informations à chaque mention
- **Un versionnement implicite**, car la référence locale demeure inchangée, même si l'entité liée change ultérieurement

Contrairement à une entité, une référence n'est pas identifiée en propre – elle ne fait que désigner une entité identifiée. C'est pourquoi le `global_uri` n'y est pas obligatoire : il est seulement exigé qu'au moins l'une des deux indications `local_id` ou `global_uri` soit renseignée. Un système qui ne connaît que l'identifiant local de l'entité référencée indique celui-ci ; il est résolu au sein de la même livraison. Au-delà de la livraison, c'est le `global_uri` qui fait le renvoi.

{{include:ech-0294_actors/output/docs/PersonReference.md}}

{{include:ech-0294_actors/output/docs/GroupReference.md}}

## Classes utilisées à plusieurs reprises

Une adresse est saisie de deux manières : comme renvoi au Répertoire officiel des adresses de bâtiments de swisstopo (`address_uri`) et comme adresse rédigée dans `street_address`, `postal_code`, `postal_locality` et `country`. Le dernier nombre de l'URI est l'EGAID, l'identifiant fédéral d'adresse de bâtiment – `https://geo.ld.admin.ch/location/address/101009806` désigne ainsi « Rue de Genève 17, 1003 Lausanne » en tant qu'adresse de bâtiment officiellement répertoriée.

Le renvoi est l'indication la plus stable : les noms de rue changent, les communes fusionnent, les numéros postaux sont redécoupés, mais l'EGAID demeure et permet des rapprochements avec le Registre des bâtiments et des logements ainsi qu'avec les géodonnées. L'adresse rédigée ne devient pas superflue, car elle contient souvent davantage que ce que connaît le répertoire – un nom d'organisation, une case postale, une mention « c/o ». L'exemple de la Fédération romande des consommateurs le montre bien : l'EGAID désigne l'adresse physique à la Rue de Genève 17, 1003 Lausanne, tandis que l'adresse rédigée indique la case postale 585 et son propre numéro postal 1001. Les deux indications sont correctes et aucune ne se déduit de l'autre.

Toutes les adresses ne figurent pas dans le répertoire, ainsi une adresse à l'étranger. `address_uri` est donc facultatif ; là où il est connu, il doit être renseigné.

{{include:ech-0294_actors/output/docs/Address.md}}

{{include:ech-0294_actors/output/docs/AddressTypeEnum.md}}

{{include:ech-0294_actors/output/docs/Contact.md}}