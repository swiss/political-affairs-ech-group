\newpage

# Affiliations (Memberships)

Le schéma Membership représente la relation entre personnes et groupes et constitue l'élément de liaison central du schéma des acteurs.

- **Délimitation par rapport aux liens d'intérêts (`InterestLink`) :** `Membership` consigne l'*appartenance formelle* d'une personne à un groupe au sein du schéma des acteurs (p. ex. affiliation à un parti, à une commission ou à un parlement). Les liens d'intérêts et les conflits d'intérêts avec des organisations *extérieures* au schéma en sont délibérément séparés et sont représentés au moyen d'`InterestLink` (voir le chapitre suivant).
- **Référence avec instantané plutôt qu'intégration (`person_reference`/`group_reference`) :** une affiliation renvoie à la personne et au groupe et consigne à cette occasion leurs principales caractéristiques d'identification au moment de la mise en relation. L'enregistrement demeure ainsi historiquement correct, même si la personne ou le groupe change ultérieurement.
- **Activité explicite ou déduite (`is_active`) :** le fait qu'une affiliation soit active peut être défini explicitement au moyen d'`is_active` ou déduit de la validité temporelle. Si `is_active` n'est pas défini, l'activité découle de `valid_from`/`valid_through`.
- **Affiliation ≠ droit de vote (`authorized_to_vote`) :** le droit de vote est géré séparément de l'affiliation – typiquement `false` pour les membres suppléants (sauf lorsqu'ils sont en fonction), les personnes observatrices, le secrétariat et les invités.
- **Rôle comme vocabulaire contrôlé avec option en texte libre (`role_type`) :** le rôle au sein du groupe (p. ex. membre, présidence, suppléance) est indiqué au moyen d'un vocabulaire contrôlé (`RoleEnum`) ; pour les rôles non couverts, la valeur `other` est utilisée, assortie d'une désignation libre.
- **Circonscription électorale rattachée à l'affiliation et non à la personne (`electoral_district`) :** la circonscription ne décrit pas la personne, mais le mandat – une même personne peut être élue, au fil du temps ou à différents niveaux fédéraux, dans des circonscriptions différentes. `ElectoralDistrict` ne porte donc pas de validité temporelle propre, mais hérite des `valid_from`/`valid_through` de l'affiliation englobante. Pour l'identification, les ressources LINDAS des unités spatiales suisses sont prévues (voir `global_uri`). Qu'une circonscription soit identifiable de la sorte dépend de sa coïncidence avec une unité spatiale officielle : dans le canton de Bâle-Ville, les circonscriptions de Riehen et de Bettingen sont des communes et disposent d'une ressource LINDAS, tandis que Grossbasel-Ost, Grossbasel-West et Kleinbasel regroupent des quartiers de la commune de Bâle et n'en ont pas. Les circonscriptions sans équivalent officiel reçoivent un identifiant dans l'espace de noms de l'organe qui les publie.

{{include:ech-0294_actors/output/docs/Membership.md}}

{{include:ech-0294_actors/output/docs/RoleType.md}}

{{include:ech-0294_actors/output/docs/RoleEnum.md}}

{{include:ech-0294_actors/output/docs/ElectoralDistrict.md}}