\newpage

# Person

Le schéma Person décrit les personnes physiques dans le contexte politique.

- **Personne stable, caractéristiques valables dans le temps :** la `Person` elle-même ne porte aucune validité temporelle, contrairement à ses caractéristiques – nom, nationalité, sexe, profession et formation portent chacune leurs propres `valid_from`/`valid_through`. Ainsi, l'identité de la personne reste stable, tandis que certaines indications changent au fil du temps et que l'historique est conservé (p. ex. changement de nom lors d'un mariage). La circonscription électorale, en revanche, n'est pas une caractéristique de la personne : elle est rattachée à la `Membership` (`electoral_district`) et hérite de la validité temporelle de celle-ci – un changement de circonscription se traduit donc par l'affiliation correspondante.
- **Nom d'affichage (`label`) obligatoire, structure de noms (`names`) facultative :** chaque personne possède un nom d'affichage court. Un nom est ainsi toujours disponible, même lorsque les indications sont incomplètes. Il est recommandé de combiner le nom officiel (`PersonOfficialName`) et le prénom usuel (`PersonCallFirstName`). Les titres académiques peuvent également être représentés au moyen de `label_long`.
- **Types de noms selon la systématique officielle :** les types de noms (`NameTypeEnum`) suivent l'harmonisation des registres de l'OFS, respectivement eCH-0011 (notamment nom officiel, nom d'origine, nom d'alliance, prénom usuel ainsi que des variantes pour les pièces d'identité étrangères). Les noms sont ainsi compatibles avec les registres officiels des personnes, et leur sémantique est claire.
- **Date de naissance à deux niveaux de précision (`birth_year` / `birth_date`) :** si la date de naissance exacte n'est pas disponible ou n'est pas destinée à la publication, seule l'année de naissance peut être indiquée. Si une `birth_date` est disponible, elle prévaut.
- **Valeurs multiples plutôt que valeurs uniques :** les noms, les nationalités et les indications de sexe sont modélisés sous forme de listes avec validité temporelle – par exemple pour les doubles nationalités, les changements de nom ou une indication de sexe évolutive.
- **Harmonisation par-delà les niveaux fédéraux (objectif à long terme) :** la mise en relation d'une même personne à travers les niveaux fédéraux constitue un objectif important à long terme. La constitution d'une base de données centralisée des personnes dépasse les possibilités du groupe spécialisé eCH. Comme une infrastructure ouverte et éprouvée existe déjà à cet effet, **Wikidata est recommandé comme identifiant transversal** (`wikidata_uri`) ; conjointement à des identifiants globalement univoques (URI), l'attribution peut ainsi être harmonisée progressivement à travers les systèmes.


{{include:ech-0294_actors/output/docs/Person.md}}

{{include:ech-0294_actors/output/docs/Name.md}}

{{include:ech-0294_actors/output/docs/NameTypeEnum.md}}

{{include:ech-0294_actors/output/docs/LanguageProficiency.md}}

{{include:ech-0294_actors/output/docs/Citizenship.md}}

{{include:ech-0294_actors/output/docs/Gender.md}}

{{include:ech-0294_actors/output/docs/GenderCodeEnum.md}}

{{include:ech-0294_actors/output/docs/Occupation.md}}

{{include:ech-0294_actors/output/docs/Training.md}}

{{include:ech-0294_actors/output/docs/TrainingTypeEnum.md}}
