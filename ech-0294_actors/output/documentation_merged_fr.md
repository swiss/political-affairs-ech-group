---
title: "eCH-0294 Acteurs politiques : personnes, groupes et organes"
lang: fr
toc: false
---

|**Nom**|**Acteurs politiques : personnes, groupes et organes**|
|---|---|
|**Numéro eCH**|eCH-0294|
|**Catégorie**|Norme|
|**Degré de maturité**|Défini|
|**Version**|1.0.0|
|**Statut**|Proposition|
|**Décidé le**||
|**Date de publication**|2026-07-22|
|**Remplace la version**||
|**Conditions préalables**||
|**Annexes**|-|
|**Langues**|Allemand (original) - Anglais (modèle de données)|
|**Auteurs**|Groupe spécialisé Affaires politiques : Julie Silberstein, Laurence Brandenberger, Daniela Koller, Thomas Roth, Stefan Oderbolz, Fabian Davolio, Orhan Saeedi, Christian Gutknecht, Michael Luggen|
|**Éditeur / Distribution**|Association eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Résumé

La norme eCH-0294 « Acteurs politiques : personnes, groupes et organes » définit un modèle de données uniforme pour la publication structurée des acteurs politiques en Suisse. Il englobe les personnes physiques, les groupes et organes politiques, les affiliations entre personnes et groupes ainsi que les liens d'intérêts. L'objectif est de mettre à disposition, par-delà les niveaux fédéraux, des informations comparables, lisibles par machine et réutilisables, afin d'améliorer la transparence, la traçabilité et la capacité d'analyse des processus politiques.

La norme s'adresse aux organismes publics de tous les niveaux étatiques, aux acteurs politiques, aux médias, à la recherche et au public, et crée une base pour des systèmes d'information politiques interopérables en Suisse.

\newpage

# Table des matières

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Clic droit &gt; « Mettre à jour les champs » pour générer la table des matières.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

\newpage

# Introduction

## La famille de normes « Affaires politiques »

La vie politique de la Suisse se déroule aux niveaux fédéral, cantonal et communal – dans les parlements et les assemblées communales, dans les exécutifs et les administrations, dans les procédures de consultation et les consultations publiques, ainsi qu'à travers la participation démocratique directe des personnes ayant le droit de vote. Le groupe spécialisé « Affaires politiques » de l'association eCH développe à cet effet une famille de normes coordonnées entre elles, qui structurent ces données par-delà les niveaux fédéraux. Les normes utilisent des éléments de données communs (eCH-0292) et se référencent mutuellement au moyen d'identifiants univoques.

La famille comprend :

- **eCH-0292 – Éléments de données communs (Meta) :** définit les éléments de données transversaux et les métaprocessus sur lesquels reposent les autres normes.
- **eCH-0293 – Fonctionnement public des conseils (Operations) :** décrit le fonctionnement public des conseils – séances, points de l'ordre du jour, prises de parole ainsi que votes et élections.
- **eCH-0294 – Acteurs politiques (Actors) – la présente norme :** définit les personnes, groupes et organes dans le contexte politique ainsi que leurs affiliations et liens d'intérêts. Les autres normes référencent ces acteurs au moyen de leurs identifiants.
- **eCH-0295 – Affaires parlementaires (Affairs) :** décrit le cycle de vie des affaires politiques.
- **eCH-0296 – Actes législatifs et textes de loi (Laws) :** consigne les résultats du processus parlementaire – les lois et actes législatifs adoptés.
- **eCH-0297 – Consultations publiques (Consultations) :** structure les procédures de consultation, qui constituent souvent le point de départ des affaires parlementaires.

L'objectif de cette famille de normes est de créer une structure utilisable en commun pour les données politiques et de mettre à la disposition des organisations qui publient des informations sur les affaires politiques un modèle de données robuste.

## Délimitation par rapport au groupe spécialisé « Droits politiques »

Outre le groupe spécialisé « Affaires politiques », l'association eCH compte le groupe spécialisé « Droits politiques ». Tous deux concernent le domaine politique, mais couvrent des domaines différents :

- **Affaires politiques** (la présente famille de normes) décrit le processus de formation de la volonté et de décision parlementaire et administratif : les acteurs (eCH-0294), le fonctionnement des conseils (eCH-0293), les affaires parlementaires (eCH-0295), les actes législatifs qui en découlent (eCH-0296) ainsi que les consultations en amont (eCH-0297).
- **Droits politiques** traite de l'exercice des droits politiques par les personnes ayant le droit de vote : registres des électeurs et des candidats, déroulement des votations et élections populaires, vote électronique (eVoting), cartes de vote ainsi que résultats des votations et des élections (notamment eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

Des points de contact existent à deux endroits :

- **Votes et élections :** eCH-0293 consigne les votes et élections **au sein du fonctionnement des conseils** (p. ex. les votes nominaux au parlement ou l'élection des membres des autorités par le conseil), tandis que les votations et élections populaires ainsi que les registres, le déroulement et les résultats correspondants sont couverts par le groupe spécialisé « Droits politiques ».
- **Personnes élues :** dans les résultats électoraux du groupe spécialisé « Droits politiques » figurent les candidats et les personnes élues. Dès qu'une personne exerce un mandat, elle est répertoriée dans eCH-0294 en tant qu'actrice ou acteur politique, avec ses rôles et ses affiliations.

## La norme eCH-0294 – Acteurs politiques

La présente norme définit quatre classes principales :

- **Person** – Personnes physiques dans le contexte politique
- **Group** – Organes, partis, groupes parlementaires, conseils, commissions, organisations, etc.
- **Membership** – Lien entre personnes et groupes
- **InterestLink** – Liens d'intérêts des personnes

`Membership` est l'élément de liaison central entre `Person` et `Group` et consigne dans quel parlement, dans quelle commission, etc. une personne est ou a été active. `InterestLink` permet de décrire les liens d'intérêts.
\newpage

# Person

Le schéma Person décrit les personnes physiques dans le contexte politique.

- **Personne stable, caractéristiques valables dans le temps :** la `Person` elle-même ne porte aucune validité temporelle, contrairement à ses caractéristiques – nom, nationalité, sexe, profession, formation et circonscription électorale portent chacune leurs propres `valid_from`/`valid_through`. Ainsi, l'identité de la personne reste stable, tandis que certaines indications changent au fil du temps et que l'historique est conservé (p. ex. changement de nom lors d'un mariage ou changement de circonscription électorale).
- **Nom d'affichage obligatoire (`label`) en plus des noms structurés (`names`) :** chaque personne possède un nom abrégé obligatoire, afin qu'un nom d'affichage soit toujours disponible, même en cas d'indications incomplètes. Il est recommandé de combiner le nom officiel (`PersonOfficialName`) et le prénom usuel (`PersonCallFirstName`), complétés par l'année de naissance en cas d'homonymie. `label_long` reprend en outre les titres académiques ; la structure de noms détaillée et typée (`names`) est facultative, mais son utilisation est recommandée. Dans certains cas, l'emploi de types spécifiques, comme le nom officiel (`PersonOfficialName`), constitue une exigence légale.
- **Types de noms selon la systématique officielle :** les types de noms (`NameTypeEnum`) suivent l'harmonisation des registres de l'OFS, respectivement eCH-0011 (notamment nom officiel, nom d'origine, nom d'alliance, prénom usuel ainsi que des variantes pour les pièces d'identité étrangères). Les noms sont ainsi compatibles avec les registres officiels des personnes, et leur sémantique est claire.
- **`birth_year` comme alternative économe en données à `birth_date` :** si la date de naissance exacte n'est pas disponible ou n'est pas destinée à la publication, seule l'année de naissance peut être indiquée. Si une `birth_date` est disponible, elle prévaut.
- **Valeurs multiples plutôt que valeurs uniques :** les noms, les nationalités et les indications de sexe sont modélisés sous forme de listes avec validité temporelle – par exemple pour les doubles nationalités, les changements de nom ou une indication de sexe évolutive.
- **Harmonisation par-delà les niveaux fédéraux (objectif à long terme) :** la mise en relation d'une même personne à travers les niveaux fédéraux constitue un objectif important à long terme. La constitution d'une base de données centralisée des personnes ne relève pas du mandat du groupe spécialisé eCH. Comme une infrastructure ouverte et éprouvée existe déjà à cet effet, **Wikidata est recommandé comme identifiant transversal** (`wikidata_uri`) ; conjointement à des identifiants globalement univoques (URI), l'attribution peut ainsi être harmonisée progressivement à travers les systèmes.




## Classe: Person 


_Une personne avec des identifiants, des noms, des adresses, des nationalités et des professions._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Nom d'affichage court et obligatoire permettant d'identifier la personne au sein de l'organisation (p. ex. avec l'ajout de l'année de naissance afin de distinguer des personnes portant le même nom). Recommandé : PersonOfficialName combiné avec PersonCallFirstName.  |
| label_long | 0..1 <br/> [String](#String) | Nom d'affichage long et facultatif comprenant les titres académiques et le nom officiel complet (p. ex. « Dr. Maria Muster-Beispiel »).  |
| birth_year | 0..1 <br/> [Integer](#Integer) | Année de naissance. À utiliser uniquement lorsqu'aucune `birthDate` complète n'est disponible.  |
| birth_date | 0..1 <br/> [Date](#Date) | Date de naissance exacte si disponible et publique. Ce champ prime sur le champ `birthYear`.  |
| death_date | 0..1 <br/> [Date](#Date) | Date de décès exacte.  |
| picture | 0..1 <br/> [Uri](#Uri) | Lien vers une image (de préférence : PNG, puis JPG, puis GIF).  |
| names | * <br/> [Name](#Name) | Noms de la personne avec type et valeur.  |
| addresses | * <br/> [Address](#Address) | Adresses avec type (privée, professionnelle, locale).  |
| language_proficiencies | * <br/> [LanguageProficiency](#LanguageProficiency) | Compétences linguistiques de la personne.  |
| citizenships | * <br/> [Citizenship](#Citizenship) | Nationalités de la personne.  |
| genders | * <br/> [Gender](#Gender) | Sexe de la personne.  |
| occupations | * <br/> [Occupation](#Occupation) | Métiers ou professions de la personne.  |
| trainings | * <br/> [Training](#Training) | Formations ou éducations de la personne. Directive : n'indiquer en principe que la qualification la plus élevée obtenue.  |
| contacts | * <br/> [Contact](#Contact) | Informations de contact (e-mail, site web, réseaux sociaux). Directive : l'e-mail est quasi obligatoire et devrait toujours être fourni lorsqu'il est disponible.  |
| interest_links | * <br/> [InterestLink](#InterestLink) | Collection de liens d'intérêts.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |














### Exemples
#### Exemple : Person-swiss_politicians_Beat_Jans

```yaml
local_id: 4032
global_uri: https://data-example.parlament.ch/person/4032
wikidata_uri: https://www.wikidata.org/wiki/Q813067
label: Beat Jans
label_long: Beat Jans, dipl. nat. ETH
birth_year: 1964
birth_date: 1964-07-12
picture: https://commons.wikimedia.org/wiki/File:Beat_Jans_(2026)_(cropped).jpg
names:
- name_type: PersonFirstName
  value: Beat
- name_type: PersonOfficialName
  value: Jans
  valid_from: 1964-07-12
addresses:
- address_type: businessAddress
  postal_locality: Basel-Stadt
language_proficiencies:
- language: de
  is_correspondence: true
  is_native: true
citizenships:
- country: CH
  valid_from: 1964-07-12
genders:
- gender_code: male
  valid_from: 1964-07-12
occupations:
- label: Politiker
  valid_from: 1964-01-01
  is_active: true
trainings:
- training_type: '3223'
  value: dipl. nat. ETH
contacts:
- contact_type: email
  value: beat.jans@admin.ch
- contact_type: contact_website
  value: http://www.beat-jans.ch

```






</div>



## Classe: Name 


_Un nom avec un type (p. ex. nom d'usage, nom officiel), une valeur et une validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| name_type | 1 <br/> [NameTypeEnum](#NameTypeEnum) | Type de nom selon eCH-0011 (personNameData).  |
| value | 1 <br/> [String](#String) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [names](#names) | range | [Name](#Name) |



















</div>

## Enum: NameTypeEnum 




_Catégories de types de noms selon eCH-0011 (personNameData) et https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master, URI selon l'identifiant I14Y mais en tant que classe et non en tant qu'attribut. Descriptions et traductions selon I14Y._

__



<div data-search-exclude markdown="1">

URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| PersonOfficialName |  Selon le catalogue officiel des caractères (n° 211) pour l'harmonisation des registres : nom selon les documents officiels. Le nom officiel correspond au nom figurant dans le registre suisse de l'état civil. Pour les ressortissants étrangers n'ayant pas d'événement d'état civil en Suisse, le nom officiel correspond au nom figurant sur le passeport étranger ou la carte d'identité (voir « Nom selon le passeport étranger » ou les directives du SEM sur la détermination et l'orthographe des noms des ressortissants étrangers du 1er janvier 2012. En l'absence de documents officiels, voir également « Nom selon la déclaration » (p. ex. dans le cas de requérants d'asile). Le nom officiel peut se composer d'une ou de plusieurs parties.  |
| | [https://register.ld.admin.ch/i14y/concept/personOfficialName](https://register.ld.admin.ch/i14y/concept/personOfficialName) |
| PersonOriginalName |  Selon le catalogue officiel des caractères (n° 212) pour l'harmonisation des registres : nom de filiation selon les documents officiels, qui correspond au nom porté par la personne avant son premier mariage ou son premier partenariat enregistré. Il peut également s'agir d'un nom de célibataire acquis par une décision de changement de nom (voir art. 24, al. 2 OEC, RS 211.112.2).  |
| | [https://register.ld.admin.ch/i14y/concept/personOriginalName](https://register.ld.admin.ch/i14y/concept/personOriginalName) |
| PersonAllianceName |  Selon le catalogue officiel des caractères (n° 213) pour l'harmonisation des registres : le nom d'alliance montre le lien entre deux personnes mariées ou vivant en partenariat enregistré. Un nom d'alliance déjà utilisé peut être conservé après la dissolution du mariage ou du partenariat si le nom officiel n'a pas été modifié lors de la dissolution. Il est rattaché au nom officiel par un trait d'union et est formé avec le nom de célibataire du partenaire ou son propre nom de célibataire. Sur demande, le nom d'alliance peut être inscrit dans le passeport ou sur la carte d'identité.  |
| | [https://register.ld.admin.ch/i14y/concept/personAllianceName](https://register.ld.admin.ch/i14y/concept/personAllianceName) |
| PersonNameOnForeignPassport |  Selon le catalogue officiel des caractères (n° 214) pour l'harmonisation des registres : pour les personnes de nationalité étrangère. Ce nom correspond à l'entrée figurant dans la zone lisible par machine du passeport. Si cette zone comporte des noms de famille ou des prénoms abrégés, ceux-ci doivent, dans la mesure du possible, être enregistrés dans leur intégralité, conformément à l'entrée figurant dans le passeport.  |
| | [https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport) |
| PersonAliasName |  Selon le catalogue officiel des caractères (n° 215) pour l'harmonisation des registres : nom (p. ex. nom de scène, nom religieux) qui, sur la base d'une demande acceptée, peut être porté par la personne. Le nom d'alias peut se composer d'une ou de plusieurs parties (p. ex. également le prénom d'alias et le nom de famille d'alias).  |
| | [https://register.ld.admin.ch/i14y/concept/personAliasName](https://register.ld.admin.ch/i14y/concept/personAliasName) |
| PersonOtherName |  Selon le catalogue officiel des caractères (n° 216) pour l'harmonisation des registres : autres noms officiels selon les documents d'état civil suisses (art. 24, al. 3 OEC) ou selon des documents étrangers, qui ne sont ni des noms de famille ni des prénoms.  |
| | [https://register.ld.admin.ch/i14y/concept/personOtherName](https://register.ld.admin.ch/i14y/concept/personOtherName) |
| PersonDeclaredForeignerName |  Selon le catalogue officiel des caractères (n° 217) pour l'harmonisation des registres : pour les ressortissants étrangers qui ne disposent pas de documents officiels (principalement dans le domaine de l'asile).  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName) |
| PersonFirstName |  Prénoms tirés de l'acte de naissance, du registre de l'état civil (Infostar) dans l'ordre dans lequel ils apparaissent, ou tirés de documents d'identité étrangers.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstName](https://register.ld.admin.ch/i14y/concept/personFirstName) |
| PersonCallFirstName |  Une personne a le droit de choisir un prénom usuel dans la liste de ses prénoms officiels. Le prénom usuel peut se composer d'un ou de plusieurs prénoms (parmi ceux figurant sous « prénoms officiels »).  |
| | [https://register.ld.admin.ch/i14y/concept/personCallFirstName](https://register.ld.admin.ch/i14y/concept/personCallFirstName) |
| PersonFirstNameOnForeignPassport |  Pour les personnes de nationalité étrangère. À utiliser en combinaison avec le nom tel qu'il figure sur le passeport étranger.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport) |
| PersonDeclaredForeignerFirstName |  Pour les personnes de nationalité étrangère qui ne disposent pas de documents officiels (principalement dans le domaine de l'asile). À utiliser en combinaison avec le nom défini selon la déclaration.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName) |







</div>



## Classe: LanguageProficiency 


_Compétences linguistiques d'une personne indiquant la langue et le fait qu'il s'agisse ou non de la langue préférée ou de la langue maternelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| language | 1 <br/> [String](#String) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |
| is_correspondence | 0..1 <br/> [Boolean](#Boolean) | Indique s'il s'agit de la langue préférée.  |
| is_native | 0..1 <br/> [Boolean](#Boolean) | Indique s'il s'agit de la langue maternelle.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [language_proficiencies](#language_proficiencies) | range | [LanguageProficiency](#LanguageProficiency) |



















</div>



## Classe: Citizenship 


_Nationalité (également utilisée pour la citoyenneté) d'une personne indiquant le pays et la validité temporelle. Si aucun `valid_from` n'est fourni, cette information n'est pas connue. S'il est établi que la nationalité est valable depuis la naissance, la date de naissance doit être répétée ici. En l'absence de `valid_through`, la nationalité est toujours en vigueur._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| country | 1 <br/> [String](#String) | Code de pays ISO 3166-1 alpha-2.  |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [citizenships](#citizenships) | range | [Citizenship](#Citizenship) |



















</div>



## Classe: Gender 


_Sexe d'une personne indiquant un code de sexe et la validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| gender_code | 1 <br/> [GenderCodeEnum](#GenderCodeEnum) | Code de sexe. Valeurs recommandées : male, female, diverse.  |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| pronouns | * <br/> [String](#String) | Pronoms utilisés par la personne.  |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [genders](#genders) | range | [Gender](#Gender) |



















</div>

## Enum: GenderCodeEnum 




_Codes de sexe pour les personnes. Si le sexe n'est pas connu, aucune entrée de sexe ne doit être ajoutée. Le code `diverse` doit être utilisé avec un libellé afin de fournir de plus amples détails sur le sexe auto-déclaré._

__



<div data-search-exclude markdown="1">

URI: [act:GenderCodeEnum](https://ld.ech.ch/schema/0294/actors/GenderCodeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| male |  Masculin.  |
| |  |
| female |  Féminin.  |
| |  |
| diverse |  Divers / non binaire.  |
| |  |







</div>



## Classe: Occupation 


_Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si le poste est rémunéré, ainsi que la validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indique si le poste est rémunéré.  |
| occupation_code | 0..1 <br/> [String](#String) | Code ISCO-19 du métier.  |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| organization_uid | 0..1 <br/> [String](#String) | IDE de l'organisation (format eCH-0097 : CHE-XXX.XXX.XXX) issu du registre fédéral IDE (uid.admin.ch).  |
| organization_name | 0..1 <br/> [String](#String) | Nom de l'organisation ou de l'entreprise.  |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [occupation_code](#occupation_code)
- [label](#label)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [occupations](#occupations) | range | [Occupation](#Occupation) |














### Exemples
#### Exemple : Occupation-swiss_politicians_Beat_Jans_Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>



## Classe: Training 


_Formation ou éducation d'une personne indiquant un type (p. ex. diplôme scolaire, diplôme universitaire, service militaire), un libellé, un code ISCO-19 et la validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| training_type | 0..1 <br/> [TrainingTypeEnum](#TrainingTypeEnum) | Type de formation ou d'éducation.  |
| training_code | 0..1 <br/> [String](#String) | Code ISCO-19 de la formation ou de l'éducation.  |
| value | 0..1 <br/> [String](#String) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [training_type](#training_type)
- [training_code](#training_code)
- [value](#value)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [trainings](#trainings) | range | [Training](#Training) |



















</div>

## Enum: TrainingTypeEnum 




_Types de formation ou d'éducation basés sur la liste de codes suisse LEVEL_EDUC de l'OFS._

__



<div data-search-exclude markdown="1">

URI: [act:TrainingTypeEnum](https://ld.ech.ch/schema/0294/actors/TrainingTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| 10 |  École obligatoire au maximum. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/10](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/10) |
| 110 |  Aucune formation. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/110](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/110) |
| 120 |  École obligatoire inachevée. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/120](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/120) |
| 130 |  École obligatoire. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/130](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/130) |
| 140 |  Formation d'un an / offre de transition. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/140](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/140) |
| 20 |  Degré secondaire II. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/20](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/20) |
| 22 |  Degré secondaire II - formation professionnelle. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/22](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/22) |
| 220 |  Apprentissage en entreprise (CFC/AFP) / formation professionnelle élémentaire / école professionnelle / école de commerce. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/220](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/220) |
| 2210 |  Apprentissage en entreprise (AFP) 2 ans / formation prof. élémentaire / école professionnelle / école de commerce. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2210](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2210) |
| 2211 |  Apprentissage en entreprise d'une durée de 2 ans (AFP) / formation professionnelle élémentaire. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2211](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2211) |
| 2212 |  École professionnelle / école de commerce d'une durée de 2 ans. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2212](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2212) |
| 2220 |  Apprentissage en entreprise (CFC) 3-4 ans / école professionnelle / école de commerce. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2220](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2220) |
| 2221 |  Apprentissage en entreprise d'une durée de 3 à 4 ans (CFC). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2221](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2221) |
| 2222 |  École professionnelle / école de commerce d'une durée de 3 a 4 ans. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2222](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2222) |
| 24 |  Degré secondaire II - formation générale. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/24](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/24) |
| 241 |  École de culture générale / école de degré diplôme. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/241](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/241) |
| 2411 |  École de culture générale / école de degré diplôme d'une durée de 2 ans. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2411](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2411) |
| 2412 |  École de culture générale / école de degré diplôme d'une durée de 3 ans. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2412](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2412) |
| 242 |  Maturité ou école normale. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/242](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/242) |
| 2421 |  Maturité gymnasiale. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2421](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2421) |
| 2422 |  Brevet d'enseignement. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2422](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2422) |
| 243 |  Maturité professionnelle / spécialisée. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/243](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/243) |
| 2431 |  Maturité professionnelle. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2431](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2431) |
| 2432 |  Maturité spécialisée. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2432](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2432) |
| 30 |  Degré tertiaire. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/30](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/30) |
| 31 |  Formation professionnelle supérieure. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/31](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/31) |
| 310 |  Examen professionnel avec brevet fédéral / examen professionnel supérieur avec diplôme fédéral/maîtrise. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/310](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/310) |
| 311 |  Examen professionnel avec brevet fédéral. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/311](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/311) |
| 312 |  Examen professionnel supérieur avec diplôme fédéral/maîtrise. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/312](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/312) |
| 313 |  École supérieure (ES). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/313](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/313) |
| 3131 |  École supérieure (ES) 2 ans plein temps ou 3 ans temps partiel. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3131](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3131) |
| 3132 |  École supérieure (ES) 3 ans plein temps ou 4 ans temps partiel. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3132](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3132) |
| 32 |  Haute école. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/32](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/32) |
| 321 |  Bachelor université, EPF, haute école spécialisée, haute école pédagogique (y compris diplôme HES/HEP). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/321](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/321) |
| 3211 |  Bachelor haute école spécialisée (y compris diplôme HES). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3211](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3211) |
| 3212 |  Bachelor haute école pédagogique (y compris diplôme HEP). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3212](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3212) |
| 3213 |  Bachelor université, EPF. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3213](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3213) |
| 322 |  Master université, EPF, haute école spécialisée, haute école pédagogique (y compris licence/diplôme). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/322](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/322) |
| 3221 |  Master haute école spécialisée. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3221](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3221) |
| 3222 |  Master haute école pédagogique. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3222](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3222) |
| 3223 |  Master université, EPF (y compris licence/diplôme université/EPF). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3223](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3223) |
| 323 |  Doctorat / habilitation. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/323](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/323) |
| military |  Service militaire (armée suisse). Indiquer le grade atteint dans le champ `value`. |
| |  |







</div>



## Classe: ElectoralDistrict 


_Circonscription ou région électorale associée à une affiliation. La validité temporelle est héritée de l'affiliation englobante._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Pour les références IRI, les ressources LINDAS doivent être utilisées. Les IRI des différents niveaux administratifs des unités spatiales suisses sont disponibles à l'adresse : https://ld.admin.ch/country/CHE. Sous les liens de la section schema:containsPlace, le niveau souhaité peut être sélectionné. Exemples pour chaque niveau administratif : - Pays - Suisse : https://ld.admin.ch/country/CHE - Canton - Argovie : https://ld.admin.ch/canton/19 - District - Brigue : https://ld.admin.ch/district/2301 - Commune - Versoix : https://ld.admin.ch/municipality/6644 <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [electoral_district](#electoral_district) | range | [ElectoralDistrict](#ElectoralDistrict) |



















</div>

\newpage

# Groupes et organes (Groups)

Le schéma Group représente les groupes, organisations et corporations politiques.

- **Un modèle générique plutôt que de nombreuses classes spécialisées :** les parlements, partis, groupes parlementaires, commissions, départements, tribunaux et organisations de la société civile sont tous représentés par *une seule* classe `Group` et différenciés au moyen de `group_type`. Cela maintient le modèle simple et extensible sans modification du schéma – le législatif, l'exécutif, le judiciaire et la société civile peuvent ainsi être représentés de manière équivalente.
- **Groupes et sous-groupes au moyen de `parent_groups` :** les groupes subordonnés renvoient à leur groupe supérieur – p. ex. une commission du Conseil des États, une sous-commission au sein d'une commission, un parti cantonal sous son parti mère ou une autorité au sein d'une direction. La hiérarchie découle ainsi de ces renvois plutôt que d'une structure de niveaux fixe. Elle reste le plus souvent au sein d'un même `group_type` ; des renvois transversaux et multiples sont toutefois possibles (p. ex. un groupe parlementaire qui renvoie à la fois à son parlement et à son parti).
- **Validité temporelle également pour les groupes :** au moyen de `valid_from`/`valid_through`, il est possible de représenter p. ex. des commissions n'existant que durant une législature, ou des changements de nom et des fusions de partis.



## Classe: Group 


_Un groupe, une organisation ou une collectivité politique (p. ex. parti, commission, parlement, département)._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](#GroupType) | Type de groupe (p. ex. parti, commission, parlement ou similaire). La désignation et la description exactes du groupe sont fournies via `label`.  |
| label | 1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abréviation (peut être multilingue).  |
| description | * <br/> [MultilingualValue](#MultilingualValue) | Description de l'entité.  |
| landing_page | 0..1 <br/> [Uri](#Uri) | Site web fournissant de plus amples informations.  |
| parent_groups | * <br/> [Uriorcurie](#Uriorcurie) | Lien vers les groupes parents. Par exemple, le parti faîtier pour les partis cantonaux, ou pour décrire la hiérarchie au sein de l'exécutif. Utilisé également pour rattacher des sous-commissions à des commissions, ou des groupes parlementaires à la fois à leur parlement et à leur parti. (parentGroup est généralement utilisé au sein d'un même group_type, mais les liens intertypes sont autorisés, p. ex. groupe parlementaire → parlement et groupe parlementaire → parti.)  |
| spatial | 0..1 <br/> [String](#String) | Référence spatiale (numéro OFS de commune, numéro OFS de canton ou pays). Formats : commune : ld.admin.ch/municipality/1234, canton : ld.admin.ch/canton/23, pays : ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](#Contact) | Informations de contact (e-mail, site web, réseaux sociaux). Directive : l'e-mail est quasi obligatoire et devrait toujours être fourni lorsqu'il est disponible.  |
| addresses | * <br/> [Address](#Address) | Adresses avec type (privée, professionnelle, locale).  |
| statutes_url | 0..1 <br/> [String](#String) | URL vers les statuts du parti (PDF ou page web ; facultatif pour les partis).  |
| party_color | 0..1 <br/> [String](#String) | Couleur du parti sous forme de valeur hexadécimale (facultatif pour les partis, p. ex. « #FF0000 »).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [groups](#groups) | range | [Group](#Group) |



















</div>



## Classe: GroupType 


_Type de groupe (p. ex. parti, commission, parlement, département)._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| group_type_enum | 0..1 <br/> [GroupTypeEnum](#GroupTypeEnum) | Lien vers le vocabulaire contrôlé pour les types de groupes.  |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [group_type](#group_type) | range | [GroupType](#GroupType) |



















</div>

## Enum: GroupTypeEnum 




_Types de groupes et d'organisations politiques._

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
| parliament |  Parlement au niveau fédéral, cantonal ou communal (p. ex. Assemblée fédérale, Conseil national, Conseil des États, Grand Conseil, parlement cantonal, parlement communal).  |
| | [act:enum/group_type/parliament](act:enum/group_type/parliament) |
| delegation |  Délégation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| commission |  Commission (permanente ou ad hoc), y compris les commissions de surveillance (p. ex. CdG), les commissions thématiques, les commissions d'enquête parlementaire (CEP) et les commissions de vérification des comptes.  |
| | [act:enum/group_type/commission](act:enum/group_type/commission) |
| faction |  Groupe parlementaire.  |
| | [act:enum/group_type/faction](act:enum/group_type/faction) |
| parliamentary_bureau |  Bureau du parlement.  |
| | [act:enum/group_type/parliamentary_bureau](act:enum/group_type/parliamentary_bureau) |
| presidency |  Présidence du parlement.  |
| | [act:enum/group_type/presidency](act:enum/group_type/presidency) |
| government |  Gouvernement / exécutif en tant qu'organe collégial (p. ex. Conseil fédéral, conseil d'État, conseil municipal ou conseil communal).  |
| | [act:enum/group_type/government](act:enum/group_type/government) |
| department |  Département gouvernemental.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Office gouvernemental.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| extraparliamentary_commission |  Commission extraparlementaire dotée d'un mandat gouvernemental (p. ex. Conseil de banque de la Banque nationale suisse, FINMA).  |
| | [act:enum/group_type/extraparliamentary_commission](act:enum/group_type/extraparliamentary_commission) |
| interest_group |  Groupe d'intérêts issu de la société civile.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| control_body |  Organe de contrôle ou de surveillance (p. ex. Contrôle fédéral des finances CDF, autorité de surveillance AS-MPC).  |
| | [act:enum/group_type/control_body](act:enum/group_type/control_body) |
| parliamentary_services |  Services du parlement.  |
| | [act:enum/group_type/parliamentary_services](act:enum/group_type/parliamentary_services) |
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
\newpage

# Affiliations (Memberships)

Le schéma Membership représente la relation entre personnes et groupes et constitue l'élément de liaison central du schéma des acteurs.

- **Délimitation par rapport aux liens d'intérêts (`InterestLink`) :** `Membership` consigne l'*appartenance formelle* d'une personne à un groupe au sein du schéma des acteurs (p. ex. affiliation à un parti, à une commission ou à un parlement). Les liens d'intérêts et les conflits d'intérêts avec des organisations *extérieures* au schéma en sont délibérément séparés et sont représentés au moyen d'`InterestLink` (voir le chapitre suivant).
- **Références avec instantané plutôt qu'intégration (`person_reference`/`group_reference`) :** une affiliation renvoie à la personne et au groupe au moyen de références légères et consigne à cette occasion leurs principales caractéristiques d'identification au moment de la mise en relation. L'enregistrement demeure ainsi historiquement correct, même si la personne ou le groupe change ultérieurement.
- **Activité explicite ou déduite (`is_active`) :** le fait qu'une affiliation soit active peut être défini explicitement au moyen d'`is_active` ou déduit de la validité temporelle. Si `is_active` n'est pas défini, l'activité découle de `valid_from`/`valid_through`.
- **Affiliation ≠ droit de vote (`authorized_to_vote`) :** le droit de vote est géré séparément de l'affiliation – typiquement `false` pour les membres suppléants (sauf lorsqu'ils sont en fonction), les personnes observatrices, le secrétariat et les invités.
- **Rôle comme vocabulaire contrôlé avec option en texte libre (`role_type`) :** le rôle au sein du groupe (p. ex. membre, présidence, suppléance) est indiqué au moyen d'un vocabulaire contrôlé (`RoleEnum`) ; pour les rôles non couverts, la valeur `other` est utilisée, assortie d'une désignation libre.



## Classe: Membership 


_Une relation d'affiliation entre une personne et un groupe, représentant une appartenance formelle (p. ex. membre d'un parti, membre d'une commission, parlementaire). À distinguer de InterestLink, qui recouvre les liens d'intérêts externes et les conflits d'intérêts avec des organisations situées en dehors du schéma des acteurs._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Référence à une personne avec des données instantanées au moment de la mise en relation.  |
| group_reference | 1 <br/> [GroupReference](#GroupReference) | Référence à un groupe avec des données instantanées au moment de la mise en relation.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) | Lien vers la circonscription électorale.  |
| role_type | 0..1 <br/> [RoleType](#RoleType) | Rôle de la personne dans l'affiliation ou la fonction.  |
| authorized_to_vote | 0..1 <br/> [Boolean](#Boolean) | Indique si la personne dispose du droit de vote au sein du groupe. Généralement false pour les membres suppléants (lorsqu'ils ne remplacent personne), les observateurs, les secrétaires et les invités.  |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'affiliation est actuellement active. Peut compléter ou remplacer `valid_from`/`valid_through`. Si cette valeur n'est pas renseignée, l'activité est déduite des champs de validité temporelle.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [memberships](#memberships) | range | [Membership](#Membership) |



















</div>



## Classe: RoleType 


_Rôle d'une personne dans une affiliation ou une fonction (p. ex. membre, président, suppléant). Si un rôle ne figure pas dans le vocabulaire RoleEnum proposé, la valeur « other » peut être utilisée, et un libellé descriptif doit être fourni dans le slot `role_label`. Le libellé peut également être utilisé lorsqu'une désignation spécifique est nécessaire, même s'il existe une valeur sémantique appropriée dans `role_type_enum` ; il doit être fourni lorsque `role_type_enum` est réglé sur « other »._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](#RoleEnum) | Rôle de la personne dans l'affiliation ou la fonction.  |
| label | 0..1 <br/> [String](#String) | Libellé de rôle spécifique. À utiliser lorsqu'un nom de rôle spécifique est nécessaire, même s'il existe une valeur sémantique appropriée dans `role_type_enum` ; fournir ce libellé lorsque `role_type_enum` est réglé sur « other ».  |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [role_type_enum](#role_type_enum)
- [label](#label)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [role_type](#role_type) | range | [RoleType](#RoleType) |




##### Règles


- Si le type de rôle est « other », un libellé descriptif doit être fourni.

















</div>

## Enum: RoleEnum 




_Rôles qu'une personne peut occuper dans le cadre d'une affiliation._

__



<div data-search-exclude markdown="1">

URI: [act:RoleEnum](https://ld.ech.ch/schema/0294/actors/RoleEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| member |  Membre ordinaire (par défaut).  |
| |  |
| president |  Président ou président du groupe.  |
| |  |
| stellvertreter |  Rôle de suppléant/vice (stellvertreter).  |
| |  |
| other |  Autre rôle ; utiliser role_label pour un libellé descriptif.  |
| |  |







</div>
\newpage

# Liens d'intérêts (Interest Links)

Le schéma InterestLink consigne les liens d'intérêts, les conflits d'intérêts et les imbrications des personnes avec des organisations. Il s'appuie sur les exigences de transparence applicables aux membres du parlement selon [Assemblée fédérale – Liens d'intérêts](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Délimitation par rapport aux affiliations (`Membership`) :** `InterestLink` représente les liens avec des organisations *extérieures* au schéma des acteurs (conflits d'intérêts, financement de la politique) – par opposition à l'appartenance formelle *au sein* du schéma, qui est consignée au moyen de `Membership`.
- **Classification obligatoire (`interest_type`) :** chaque lien est obligatoirement classé selon son type (activité professionnelle, mandats politiques, association), en s'appuyant sur les catégories de divulgation de l'Assemblée fédérale.
- **Organisation référençable par IDE (`organization_uid`) :** si l'organisation est enregistrée dans le registre IDE, elle est référencée au moyen de son IDE (eCH-0097, `CHE-XXX.XXX.XXX`) – ce qui permet des analyses, p. ex. à l'aide de codes NOGA. Pour les organisations sans IDE, `organization_name`/`organization_address` sont disponibles ; la forme juridique suit un vocabulaire contrôlé (`LegalFormEnum`).
- **Étendue et rémunération (`is_paid`, `committee`, `function_role`) :** outre l'organe et la fonction au sein de l'organisation, il est explicitement consigné si la position est rémunérée – un aspect central de la transparence.





## Classe: InterestLink 


_Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne avec une organisation située en dehors du schéma des acteurs._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Référence à une personne avec des données instantanées au moment de la mise en relation.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | Type de lien d'intérêts (activité professionnelle, mandat politique, association).  |
| organization_name | 0..1 <br/> [String](#String) | Nom de l'organisation ou de l'entreprise.  |
| organization_uid | 0..1 <br/> [String](#String) | IDE de l'organisation (format eCH-0097 : CHE-XXX.XXX.XXX) issu du registre fédéral IDE (uid.admin.ch).  |
| organization_address | 0..1 <br/> [String](#String) | Adresse de l'organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Forme juridique de l'organisation. Voir le vocabulaire contrôlé : https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indique si le poste est rémunéré.  |
| committee | 0..1 <br/> [String](#String) | Comité ou organe au sein de l'organisation (p. ex. conseil d'administration, conseil de fondation, comité directeur, conseil de surveillance, comité consultatif, direction).  |
| function_role | 0..1 <br/> [String](#String) | Fonction ou rôle dans l'organisation (p. ex. président/e, vice-président/e, membre, délégué, directeur/directrice, conseiller/ère).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](#HasTemporalValidity) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [organization_uid](#organization_uid)
- [organization_name](#organization_name)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |
| [Person](#Person) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |














### Exemples
#### Exemple : InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Allianz Sicherheit Schweiz, Baden
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Exemple : InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Burkart Advisory GmbH, Baden
legal_form: '0107'
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Stiebel Eltron AG, Lupfig
legal_form: '0106'
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Birchmeier Holding AG, Döttingen
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Verein Landesausstellung Svizra27, Aarau
legal_form: 0109
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Exemple : InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: 0109
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: 0109
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Bovida Real Estate AG, Baar
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: ELCA Group SA, Lausanne
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FDP.Die Liberalen
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Exemple : InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: '0110'
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```






</div>

## Enum: InterestTypeEnum 




_Types de liens d'intérêts (conflits d'intérêts, financement politique)._

__



<div data-search-exclude markdown="1">

URI: [act:InterestTypeEnum](https://ld.ech.ch/schema/0294/actors/InterestTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| professional_activity |  Activité professionnelle en dehors du mandat politique (p. ex. emploi salarié, activité indépendante, conseil, mandats d'administrateur dans des entreprises privées).  |
| | [act:enum/interest_type/professional_activity](act:enum/interest_type/professional_activity) |
| political_office |  Mandat ou fonction politique à d'autres niveaux fédéraux ou dans d'autres collectivités (p. ex. appartenance à un parlement cantonal/communal, conseil d'État, commission extraparlementaire).  |
| | [act:enum/interest_type/political_office](act:enum/interest_type/political_office) |
| association |  Appartenance à des associations, des fédérations ou des organisations d'intérêts (p. ex. associations de branche, associations professionnelles, organisations de lobbying, fondations, associations d'utilité publique).  |
| | [act:enum/interest_type/association](act:enum/interest_type/association) |







</div>

## Enum: LegalFormEnum 




_Formes juridiques basées sur la liste de codes du registre fédéral IDE (eCH-0108). Voir https://register.ld.admin.ch/i14y/concept/legalForm_

__



<div data-search-exclude markdown="1">

URI: [act:LegalFormEnum](https://ld.ech.ch/schema/0294/actors/LegalFormEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| 0101 |  Entreprise individuelle. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0101](https://register.ld.admin.ch/i14y/concept/legalForm/0101) |
| 0103 |  Société en nom collectif (SNC). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0103](https://register.ld.admin.ch/i14y/concept/legalForm/0103) |
| 0104 |  Société en commandite (SCm). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0104](https://register.ld.admin.ch/i14y/concept/legalForm/0104) |
| 0105 |  Société en commandite par actions (SCmA). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0105](https://register.ld.admin.ch/i14y/concept/legalForm/0105) |
| 0106 |  Société anonyme (SA). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0106](https://register.ld.admin.ch/i14y/concept/legalForm/0106) |
| 0107 |  Société à responsabilité limitée (Sàrl). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0107](https://register.ld.admin.ch/i14y/concept/legalForm/0107) |
| 0108 |  Société coopérative. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0108](https://register.ld.admin.ch/i14y/concept/legalForm/0108) |
| 0109 |  Association. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0109](https://register.ld.admin.ch/i14y/concept/legalForm/0109) |
| 0110 |  Fondation. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0110](https://register.ld.admin.ch/i14y/concept/legalForm/0110) |
| 0111 |  Succursale d'une entreprise étrangère. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0111](https://register.ld.admin.ch/i14y/concept/legalForm/0111) |
| 0113 |  Forme juridique particulière. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0113](https://register.ld.admin.ch/i14y/concept/legalForm/0113) |
| 0114 |  Société en commandite de placements collectifs (SCmPC). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0114](https://register.ld.admin.ch/i14y/concept/legalForm/0114) |
| 0115 |  Société d'investissement à capital variable (SICAV). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0115](https://register.ld.admin.ch/i14y/concept/legalForm/0115) |
| 0116 |  Société d'investissement à capital fixe (SICAF). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0116](https://register.ld.admin.ch/i14y/concept/legalForm/0116) |
| 0117 |  Institut de droit public. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0117](https://register.ld.admin.ch/i14y/concept/legalForm/0117) |
| 0118 |  Procuration non-commerciale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0118](https://register.ld.admin.ch/i14y/concept/legalForm/0118) |
| 0119 |  Représentant d'indivision. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0119](https://register.ld.admin.ch/i14y/concept/legalForm/0119) |
| 0151 |  Succursale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0151](https://register.ld.admin.ch/i14y/concept/legalForm/0151) |
| 0220 |  Unité de l'administration fédérale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0220](https://register.ld.admin.ch/i14y/concept/legalForm/0220) |
| 0221 |  Unité de l'administration cantonale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0221](https://register.ld.admin.ch/i14y/concept/legalForm/0221) |
| 0222 |  Unité de l'administration du district. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0222](https://register.ld.admin.ch/i14y/concept/legalForm/0222) |
| 0223 |  Unité de l'administration communale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0223](https://register.ld.admin.ch/i14y/concept/legalForm/0223) |
| 0224 |  Autre unité de l'administration de droit public. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0224](https://register.ld.admin.ch/i14y/concept/legalForm/0224) |
| 0230 |  Institution de droit public fédérale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0230](https://register.ld.admin.ch/i14y/concept/legalForm/0230) |
| 0231 |  Institution de droit public cantonale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0231](https://register.ld.admin.ch/i14y/concept/legalForm/0231) |
| 0232 |  Institution de droit public du district. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0232](https://register.ld.admin.ch/i14y/concept/legalForm/0232) |
| 0233 |  Institution de droit public communale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0233](https://register.ld.admin.ch/i14y/concept/legalForm/0233) |
| 0234 |  Autre institution de droit public. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0234](https://register.ld.admin.ch/i14y/concept/legalForm/0234) |
| 0302 |  Société simple. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0302](https://register.ld.admin.ch/i14y/concept/legalForm/0302) |
| 0312 |  Établissement stable ou représentant suisse d'une entreprise étrangère. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0312](https://register.ld.admin.ch/i14y/concept/legalForm/0312) |
| 0327 |  Entreprise publique étrangère. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0327](https://register.ld.admin.ch/i14y/concept/legalForm/0327) |
| 0328 |  Administration publique étrangère. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0328](https://register.ld.admin.ch/i14y/concept/legalForm/0328) |
| 0329 |  Organisation internationale. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0329](https://register.ld.admin.ch/i14y/concept/legalForm/0329) |
| 0355 |  Autre société coopérative. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0355](https://register.ld.admin.ch/i14y/concept/legalForm/0355) |
| 0361 |  Trust. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0361](https://register.ld.admin.ch/i14y/concept/legalForm/0361) |
| 0362 |  Fonds. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0362](https://register.ld.admin.ch/i14y/concept/legalForm/0362) |
| 0441 |  Entreprise étrangère. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0441](https://register.ld.admin.ch/i14y/concept/legalForm/0441) |
| 0571 |  Forme juridique non déterminée ou inconnue. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0571](https://register.ld.admin.ch/i14y/concept/legalForm/0571) |







</div>
\newpage

# Éléments partagés

## Reference Classes

`PersonReference` et `GroupReference` sont utilisés pour référencer **localement** des personnes ou des groupes au sein d'une autre entité. Outre le lien proprement dit vers l'entité complète, seules les informations pertinentes au **moment de la mise en relation** sont enregistrées – il n'est donc pas nécessaire de répéter toutes les informations d'une personne ou d'un groupe à chaque mention.

Un exemple : une motion renvoie à la personne qui l'a déposée. En plus du lien vers l'entité complète de la personne, la motion enregistre localement des informations telles que le parti politique ou le rôle de la personne **au moment du dépôt**. Si la personne change ultérieurement de parti ou de rôle, l'information dans la motion demeure néanmoins correcte et immuable.

Cela sert trois objectifs :

- **Des données locales utiles** sans requêtes coûteuses sur l'entité complète
- **Aucune redondance**, car il n'est pas nécessaire de répéter toutes les informations à chaque mention
- **Un versionnement implicite**, car la référence locale demeure inchangée, même si l'entité liée change ultérieurement



## Classe: PersonReference 


_Référence légère à une personne avec les principales données d'identification au moment de la liaison. Préserve l'exactitude historique même si la personne change ultérieurement._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Nom d'affichage court obligatoire permettant d'identifier la personne au sein de l'organisation (par ex. avec l'ajout de l'année de naissance afin de distinguer les personnes portant le même nom).  |
| label_long | 0..1 <br/> [String](#String) | Nom d'affichage long facultatif comprenant les titres académiques et le nom officiel complet (par ex. « Dr. Maria Muster-Beispiel »).  |
| group_label | 0..1 <br/> [String](#String) | Nom de l'organe/du groupe au moment de la liaison.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |
| [InterestLink](#InterestLink) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |



















</div>



## Classe: GroupReference 


_Référence légère à un groupe avec les principales données d'identification au moment de la liaison._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abréviation (peut être multilingue).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [group_reference](#group_reference) | range | [GroupReference](#GroupReference) |



















</div>

## Classes utilisées à plusieurs reprises



## Classe: Address 


_Une adresse avec un type (p. ex. adresse privée, adresse professionnelle) et une valeur._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](#AddressTypeEnum) | Type d'adresse.  |
| address_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | URI de l'adresse issue du répertoire fédéral des adresses de bâtiments. La couche est accessible à l'adresse https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis. Exemple d'URI valide : https://geo.ld.admin.ch/location/address/101904050  |
| street_address | 0..1 <br/> [String](#String) | Adresse (rue).  |
| postal_code | 0..1 <br/> [Integer](#Integer) | Code postal.  |
| postal_locality | 0..1 <br/> [String](#String) | Localité.  |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [postal_locality](#postal_locality)
- [address_uri](#address_uri)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [addresses](#addresses) | range | [Address](#Address) |
| [Group](#Group) | [addresses](#addresses) | range | [Address](#Address) |














### Exemples
#### Exemple : Address-swiss_politicians_Beat_Jans_1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```






</div>

## Enum: AddressTypeEnum 




_Types d'adresses._

__



<div data-search-exclude markdown="1">

URI: [act:AddressTypeEnum](https://ld.ech.ch/schema/0294/actors/AddressTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| privateAddress |  Adresse privée.  |
| |  |
| businessAddress |  Adresse professionnelle.  |
| |  |
| localAddress |  Adresse locale.  |
| |  |







</div>



## Classe: Contact 


_Informations de contact d'une personne indiquant un type (p. ex. e-mail, LinkedIn) et une valeur._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| contact_type | 1 <br/> [ContactTypeEnum](#ContactTypeEnum) | Type d'informations de contact.  |
| value | 1 <br/> [String](#String) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [contacts](#contacts) | range | [Contact](#Contact) |
| [Group](#Group) | [contacts](#contacts) | range | [Contact](#Contact) |



















</div>
