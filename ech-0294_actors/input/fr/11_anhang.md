\newpage

# Annexe A – Références et bibliographie {.unnumbered}

Lorsqu'une version est indiquée, il s'agit de celle sur la base de laquelle la présente norme a été élaborée.

## Normes du groupe spécialisé « Affaires politiques » {.unnumbered}

Les normes du groupe spécialisé sont élaborées conjointement et se renvoient les unes aux autres. Elles portent actuellement toutes le statut « In Arbeit » (en cours d'élaboration ; état au 10 août 2026) ; aucune version n'est donc indiquée.

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0292|eCH-0292 : Métaprocessus relatifs aux affaires politiques – éléments de données communs : [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0293|eCH-0293 : Fonctionnement public des conseils : [https://www.ech.ch/de/ech/ech-0293](https://www.ech.ch/de/ech/ech-0293)|
|eCH-0295|eCH-0295 : Affaires parlementaires : [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0296|eCH-0296 : Actes législatifs et textes de loi : [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|eCH-0297|eCH-0297 : Consultations publiques : [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Autres normes eCH {.unnumbered}

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0011|eCH-0011 : Datenstandard Personendaten, version 9.0.0 (approuvée, 27.07.2023). Base des types de noms dans `NameTypeEnum` (`personNameData`) : [https://www.ech.ch/de/ech/ech-0011/9.0.0](https://www.ech.ch/de/ech/ech-0011/9.0.0)|
|eCH-0108|eCH-0108 : Datenstandard: Unternehmensstammdaten und Unternehmensregister, version 6.0.0 (approuvée, 04.04.2024). Définit le format d'échange de l'IDE (`organization_uid`) et constitue la norme à laquelle la liste de codes des formes juridiques de `LegalFormEnum` est conforme : [https://www.ech.ch/de/ech/ech-0108/6.0.0](https://www.ech.ch/de/ech/ech-0108/6.0.0)|

## Listes de codes et autres sources {.unnumbered}

| | |
|------------------|----------------------------------------------------------------------------------|
|I14Y|Plateforme d'interopérabilité de l'Office fédéral de la statistique. Source des listes de codes pour la forme juridique (`LegalFormEnum`) et le sexe (`GenderCodeEnum`) : [https://www.i14y.admin.ch](https://www.i14y.admin.ch)|
|LINDAS|Linked Data Service de l'administration fédérale suisse. Identifiants des unités spatiales suisses (pays, canton, district, commune) pour `spatial` et `ElectoralDistrict` : [https://ld.admin.ch](https://ld.admin.ch)|
|NOGA|Nomenclature générale des activités économiques de l'Office fédéral de la statistique. Permet des analyses via l'IDE des organisations référencées.|
|Wikidata|Base de connaissances libre. IRI d'entité (`http://www.wikidata.org/entity/Q…`) dans `wikidata_uri` : [https://www.wikidata.org](https://www.wikidata.org)|
|ISO 639-1|ISO (International Organization for Standardization). Codes de langue, utilisés dans le slot `language` de `MultilingualValue`.|
|schema.org|Vocabulaire commun pour les données structurées. Source de plusieurs affectations `slot_uri` : [https://schema.org](https://schema.org)|
|LinkML|Langage de modélisation dans lequel la présente norme est définie : [https://linkml.io](https://linkml.io)|

\newpage

# Annexe B – Collaboration & vérification {.unnumbered}

Groupe de spécialistes « Affaires politiques », sous-groupe « Acteurs politiques » :

| | |
|---|---|
|Julie Silberstein|Office fédéral de la statistique|
|Laurence Brandenberger|Université de Zurich, IPZ|
|Daniela Koller|Canton de Thurgovie|
|Thomas Roth||
|Stefan Oderbolz|EBP|
|Fabian Davolio|Services du Parlement|
|Orhan Saeedi|Canton de Bâle-Ville|
|Christian Gutknecht|Glue AG|
|Michael Luggen|Chancellerie fédérale|

<!-- TODO groupe de spécialistes : compléter/corriger les organisations et l'historique des versions. -->

| Version | Date | Auteur | Remarque |
|---|---|---|---|
| 1.0.0 | 2026-08-10 | Groupe de spécialistes « Affaires politiques » | Dépôt en tant que proposition |

# Annexe C – Abréviations et glossaire {.unnumbered}

| | |
|---|---|
|IDE|Numéro d'identification des entreprises. Clé univoque d'une entreprise suisse selon l'Office fédéral de la statistique.|
|I14Y|Plateforme d'interopérabilité de l'Office fédéral de la statistique ; source de plusieurs listes de codes.|
|IRI|Internationalized Resource Identifier. Extension de l'URI à l'ensemble du jeu de caractères Unicode.|
|JSON-LD|JSON for Linking Data. Sérialisation de données liées en JSON.|
|LINDAS|Linked Data Service de l'administration fédérale suisse.|
|LinkML|Linked Data Modeling Language. Langage de modélisation dans lequel la présente norme est définie.|
|LPD|Loi fédérale sur la protection des données, en vigueur depuis le 1er septembre 2023.|
|NOGA|Nomenclature générale des activités économiques de l'Office fédéral de la statistique.|
|RDF|Resource Description Framework. Modèle de données pour les données liées ; livré ici au format Turtle (.ttl).|
|URI|Uniform Resource Identifier. Identifiant univoque d'une ressource.|
|XSD|XML Schema Definition. Recommandation du W3C pour la définition de structures de documents XML.|

# Annexe D – Modifications par rapport à la version précédente {.unnumbered}

Il s'agit de la première version.

\newpage

# Annexe E – Liste des illustrations {.unnumbered}

Aucune

# Annexe F – Liste des tableaux {.unnumbered}

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \h \z \c "Tableau" </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Clic droit &gt; « Mettre à jour les champs » pour générer la liste des tableaux.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```
