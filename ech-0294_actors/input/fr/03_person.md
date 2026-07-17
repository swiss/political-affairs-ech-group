\newpage

# Person

Le schéma Person décrit les personnes physiques dans le contexte politique.

- **Personne stable, caractéristiques valables dans le temps :** la `Person` elle-même ne porte aucune validité temporelle, contrairement à ses caractéristiques – nom, nationalité, sexe, profession, formation et circonscription électorale portent chacune leurs propres `valid_from`/`valid_through`. Ainsi, l'identité de la personne reste stable, tandis que certaines indications changent au fil du temps et que l'historique est conservé (p. ex. changement de nom lors d'un mariage ou changement de circonscription électorale).
- **Nom d'affichage obligatoire (`label`) en plus des noms structurés (`names`) :** chaque personne possède un nom abrégé obligatoire, afin qu'un nom d'affichage soit toujours disponible, même en cas d'indications incomplètes. Il est recommandé de combiner le nom officiel (`PersonOfficialName`) et le prénom usuel (`PersonCallFirstName`), complétés par l'année de naissance en cas d'homonymie. `label_long` reprend en outre les titres académiques ; la structure de noms détaillée et typée (`names`) est facultative, mais son utilisation est recommandée. Dans certains cas, l'emploi de types spécifiques, comme le nom officiel (`PersonOfficialName`), constitue une exigence légale.
- **Types de noms selon la systématique officielle :** les types de noms (`NameTypeEnum`) suivent l'harmonisation des registres de l'OFS, respectivement eCH-0011 (notamment nom officiel, nom d'origine, nom d'alliance, prénom usuel ainsi que des variantes pour les pièces d'identité étrangères). Les noms sont ainsi compatibles avec les registres officiels des personnes, et leur sémantique est claire.
- **`birth_year` comme alternative économe en données à `birth_date` :** si la date de naissance exacte n'est pas disponible ou n'est pas destinée à la publication, seule l'année de naissance peut être indiquée. Si une `birth_date` est disponible, elle prévaut.
- **Valeurs multiples plutôt que valeurs uniques :** les noms, les nationalités et les indications de sexe sont modélisés sous forme de listes avec validité temporelle – par exemple pour les doubles nationalités, les changements de nom ou une indication de sexe évolutive.
- **Harmonisation par-delà les niveaux fédéraux (objectif à long terme) :** la mise en relation d'une même personne à travers les niveaux fédéraux constitue un objectif important à long terme. La constitution d'une base de données centralisée des personnes ne relève pas du mandat du groupe spécialisé eCH. Comme une infrastructure ouverte et éprouvée existe déjà à cet effet, **Wikidata est recommandé comme identifiant transversal** (`wikidata_uri`) ; conjointement à des identifiants globalement univoques (URI), l'attribution peut ainsi être harmonisée progressivement à travers les systèmes.


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

{{include:ech-0294_actors/output/docs/ElectoralDistrict.md}}
