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

Une adresse est rédigée dans `street_address`, `postal_code`, `postal_locality` et `country` et peut renvoyer, au moyen d'`address_uri`, au Répertoire officiel des adresses de bâtiments de swisstopo. Le dernier nombre de cette URI est l'EGAID, l'identifiant fédéral d'adresse de bâtiment ; `https://geo.ld.admin.ch/location/address/101009806` désigne ainsi « Rue de Genève 17, 1003 Lausanne » en tant qu'adresse de bâtiment officiellement répertoriée.

`address_uri` est facultatif. L'adresse rédigée seule est admise, mais le renvoi au moyen de l'EGAID est préférable : celle-ci constitue un identifiant univoque et stable dans le temps, alors que les noms de rue changent, que les communes fusionnent et que les numéros postaux sont redécoupés. Toutes les adresses ne figurent pas dans le répertoire, ainsi une adresse à l'étranger ; c'est pourquoi le slot reste facultatif.

Pour obtenir l'EGAID, on peut utiliser l'[API de recherche de geo.admin.ch](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Rue+de+Gen%C3%A8ve+17+1003+Lausanne&type=locations&origins=address) ou procéder à un rapprochement avec le [Répertoire officiel des adresses de bâtiments](https://www.swisstopo.admin.ch/fr/repertoire-officiel-des-adresses-de-batiments). Le résultat est saisi dans `address_uri`.

{{include:ech-0294_actors/output/docs/Address.md}}

{{include:ech-0294_actors/output/docs/AddressTypeEnum.md}}

{{include:ech-0294_actors/output/docs/Contact.md}}