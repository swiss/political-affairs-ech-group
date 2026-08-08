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

## La norme eCH-0294 – Acteurs politiques : personnes, groupes et organes

La présente norme définit quatre classes principales :

- **Person** – Personnes physiques dans le contexte politique
- **Group** – Organes, partis, groupes parlementaires, conseils, commissions, organisations, etc.
- **Membership** – Lien entre personnes et groupes
- **InterestLink** – Liens d'intérêts des personnes

`Membership` est l'élément de liaison central entre `Person` et `Group` et consigne dans quel parlement, dans quelle commission, etc. une personne est ou a été active. `InterestLink` permet de décrire les liens d'intérêts.
\newpage

# Person

Le schéma Person décrit les personnes physiques dans le contexte politique.

- **Personne stable, caractéristiques valables dans le temps :** la `Person` elle-même ne porte aucune validité temporelle, contrairement à ses caractéristiques – nom, nationalité, sexe, profession et formation portent chacune leurs propres `valid_from`/`valid_through`. Ainsi, l'identité de la personne reste stable, tandis que certaines indications changent au fil du temps et que l'historique est conservé (p. ex. changement de nom lors d'un mariage). La circonscription électorale, en revanche, n'est pas une caractéristique de la personne : elle est rattachée à la `Membership` (`electoral_district`) et hérite de la validité temporelle de celle-ci – un changement de circonscription se traduit donc par l'affiliation correspondante.
- **Nom d'affichage (`label`) obligatoire, structure de noms (`names`) facultative :** chaque personne possède un nom d'affichage court. Un nom est ainsi toujours disponible, même lorsque les indications sont incomplètes. Il est recommandé de combiner le nom officiel (`PersonOfficialName`) et le prénom usuel (`PersonCallFirstName`). Les titres académiques peuvent également être représentés au moyen de `label_long`.
- **Types de noms selon la systématique officielle :** les types de noms (`NameTypeEnum`) reprennent la systématique de l'harmonisation des registres (notamment nom officiel, nom d'origine, nom d'alliance, prénom usuel ainsi que des variantes pour les pièces d'identité étrangères). La référence est le [Catalogue officiel des caractères](https://www.bfs.admin.ch/bfs/fr/home/registres/registre-personnes/harmonisation-registres/nomenclatures.assetdetail.24565577.html), publié par l'Office fédéral de la statistique en vertu de l'art. 4 de la loi sur l'harmonisation de registres (LHR, RS 431.02) ; les numéros figurant dans les descriptions des valeurs (211–224) sont les numéros de caractères de ce catalogue. Le format d'échange correspondant est défini par la norme eCH [eCH-0011 Norme concernant les données concernant les personnes](https://www.ech.ch/fr/ech/ech-0011/9.0.0), sur laquelle la présente norme s'appuie. Les noms sont ainsi compatibles avec les registres officiels des personnes et leur sémantique est claire.
- **Date de naissance à deux niveaux de précision (`birth_year` / `birth_date`) :** si la date de naissance exacte n'est pas disponible ou n'est pas destinée à la publication, seule l'année de naissance peut être indiquée. Si une `birth_date` est disponible, elle prévaut.
- **Valeurs multiples plutôt que valeurs uniques :** les noms, les nationalités et les indications de sexe sont modélisés sous forme de listes avec validité temporelle – par exemple pour les doubles nationalités, les changements de nom ou une indication de sexe évolutive.
- **Sexe : codes officiels et catégorie ouverte (`GenderCodeEnum`) :** `male` et `female` correspondent aux valeurs de l'harmonisation des registres et renvoient, au moyen de `meaning`, aux concepts I14Y `sex/1` et `sex/2`. Pour `non_binary`, il n'existe délibérément aucune correspondance : la liste de codes officielle ne connaît comme troisième valeur que « indéterminé », ce qui signifie autre chose qu'une indication positive au-delà du masculin et du féminin. Si le sexe n'est pas connu, aucune entrée n'est donc créée — une entrée absente et `non_binary` doivent être clairement distinguées.
- **Harmonisation par-delà les niveaux fédéraux (objectif à long terme) :** la mise en relation d'une même personne à travers les niveaux fédéraux constitue un objectif important à long terme. La constitution d'une base de données centralisée des personnes dépasse les possibilités du groupe spécialisé eCH. Comme une infrastructure ouverte et éprouvée existe déjà à cet effet, **Wikidata est recommandé comme identifiant transversal** (`wikidata_uri`) ; conjointement à des identifiants globalement univoques (URI), l'attribution peut ainsi être harmonisée progressivement à travers les systèmes.




## Classe: Person 


_Une personne avec des identifiants, des noms, des adresses, des nationalités et des professions._




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
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](#HasCreationModificationDates) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |














### Exemples
#### Exemple : Variante de nom à côté du double nom officiel

```yaml
local_id: 280958
global_uri: https://parlament.winterthur.ch/behoerdenmitglieder/280958
label: Cristina Bozzi-Brunel
names:
- name_type: PersonFirstName
  value: Cristina
- name_type: PersonOfficialName
  value: Bozzi-Brunel
- name_type: PersonOriginalName
  value: Brunel

```
#### Exemple : Prénom usuel différent du prénom officiel

```yaml
local_id: 1269
global_uri: >-
  https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
label: Gerri Beretta-Piccoli
names:
- name_type: PersonFirstName
  value: Fausto
- name_type: PersonCallFirstName
  value: Gerri
- name_type: PersonOfficialName
  value: Beretta-Piccoli

```
#### Exemple : Indication de sexe non binaire avec profession et formation

```yaml
local_id: 72c7232be92944e3876f3b6723824ff9
global_uri: >-
  https://stadtrat.bern.ch/de/mitglieder/detail.php?gid=72c7232be92944e3876f3b6723824ff9
label: Sofia Fisch
birth_year: 1996
names:
- name_type: PersonFirstName
  value: Sofia
- name_type: PersonOfficialName
  value: Fisch
genders:
- gender_code: non_binary
  label: divers
occupations:
- label: Jurist*in
  is_active: true
trainings:
- training_type: '3223'
  value: MLaw

```
#### Exemple : Distinguer des personnes homonymes par le label

```yaml
local_id: 6447
global_uri: https://www.ur.ch/behoerdenmitglieder/6447
label: Alois Arnold (1981)
birth_year: 1981
names:
- name_type: PersonFirstName
  value: Alois
- name_type: PersonOfficialName
  value: Arnold

```
#### Exemple : Personne saisie de manière complète

```yaml
local_id: 4032
global_uri: https://www.admin.ch/de/beat-jans
wikidata_uri: http://www.wikidata.org/entity/Q813067
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
#### Exemple : Distinguer des personnes homonymes par le label (deuxième personne)

```yaml
local_id: 6370
global_uri: https://www.ur.ch/behoerdenmitglieder/6370
label: Alois Arnold (1965)
birth_year: 1965
names:
- name_type: PersonFirstName
  value: Alois
- name_type: PersonOfficialName
  value: Arnold

```






</div>



## Classe: Name 


_Un nom avec un type (p. ex. nom d'usage, nom officiel), une valeur et une validité temporelle._




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




_Catégories de types de noms selon eCH-0011 (personNameData) et le Catalogue officiel des caractères de l'harmonisation de registres (https://www.bfs.admin.ch/bfs/fr/home/registres/registre-personnes/harmonisation-registres/nomenclatures.assetdetail.24565577.html), URI selon l'identifiant I14Y mais en tant que classe et non en tant qu'attribut. Descriptions et traductions selon I14Y._




<div data-search-exclude markdown="1">

URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| PersonOfficialName |  Nom selon les documents officiels. Le nom officiel correspond au nom figurant dans le registre suisse de l'état civil. Pour les ressortissants étrangers n'ayant pas d'événement d'état civil en Suisse, le nom officiel correspond au nom figurant sur le passeport étranger ou la carte d'identité (voir « Nom selon le passeport étranger » ou les directives du SEM sur la détermination et l'orthographe des noms des ressortissants étrangers du 1er janvier 2012. En l'absence de documents officiels, voir également « Nom selon la déclaration » (p. ex. dans le cas de requérants d'asile). Le nom officiel peut se composer d'une ou de plusieurs parties. Selon le catalogue officiel des caractères (n° 211) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personOfficialName](https://register.ld.admin.ch/i14y/concept/personOfficialName) |
| PersonOriginalName |  Nom de filiation selon les documents officiels, qui correspond au nom porté par la personne avant son premier mariage ou son premier partenariat enregistré. Il peut également s'agir d'un nom de célibataire acquis par une décision de changement de nom (voir art. 24, al. 2 OEC, RS 211.112.2). Selon le catalogue officiel des caractères (n° 212) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personOriginalName](https://register.ld.admin.ch/i14y/concept/personOriginalName) |
| PersonAllianceName |  Le nom d'alliance montre le lien entre deux personnes mariées ou vivant en partenariat enregistré. Un nom d'alliance déjà utilisé peut être conservé après la dissolution du mariage ou du partenariat si le nom officiel n'a pas été modifié lors de la dissolution. Il est rattaché au nom officiel par un trait d'union et est formé avec le nom de célibataire du partenaire ou son propre nom de célibataire. Sur demande, le nom d'alliance peut être inscrit dans le passeport ou sur la carte d'identité. Selon le catalogue officiel des caractères (n° 213) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personAllianceName](https://register.ld.admin.ch/i14y/concept/personAllianceName) |
| PersonNameOnForeignPassport |  Pour les personnes de nationalité étrangère. Ce nom correspond à l'entrée figurant dans la zone lisible par machine du passeport. Si cette zone comporte des noms de famille ou des prénoms abrégés, ceux-ci doivent, dans la mesure du possible, être enregistrés dans leur intégralité, conformément à l'entrée figurant dans le passeport. Selon le catalogue officiel des caractères (n° 214) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport) |
| PersonAliasName |  Nom (p. ex. nom de scène, nom religieux) qui, sur la base d'une demande acceptée, peut être porté par la personne. Le nom d'alias peut se composer d'une ou de plusieurs parties (p. ex. également le prénom d'alias et le nom de famille d'alias). Selon le catalogue officiel des caractères (n° 215) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personAliasName](https://register.ld.admin.ch/i14y/concept/personAliasName) |
| PersonOtherName |  Autres noms officiels selon les documents d'état civil suisses (art. 24, al. 3 OEC) ou selon des documents étrangers, qui ne sont ni des noms de famille ni des prénoms. Selon le catalogue officiel des caractères (n° 216) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personOtherName](https://register.ld.admin.ch/i14y/concept/personOtherName) |
| PersonDeclaredForeignerName |  Pour les ressortissants étrangers qui ne disposent pas de documents officiels (principalement dans le domaine de l'asile). Selon le catalogue officiel des caractères (n° 217) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName) |
| PersonFirstName |  Prénoms tirés de l'acte de naissance, du registre de l'état civil (Infostar) dans l'ordre dans lequel ils apparaissent, ou tirés de documents d'identité étrangers. Selon le catalogue officiel des caractères (n° 221) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstName](https://register.ld.admin.ch/i14y/concept/personFirstName) |
| PersonCallFirstName |  Une personne a le droit de choisir un prénom usuel dans la liste de ses prénoms officiels. Le prénom usuel peut se composer d'un ou de plusieurs prénoms (parmi ceux figurant sous « prénoms officiels »). Selon le catalogue officiel des caractères (n° 222) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personCallFirstName](https://register.ld.admin.ch/i14y/concept/personCallFirstName) |
| PersonFirstNameOnForeignPassport |  Pour les personnes de nationalité étrangère. À utiliser en combinaison avec le nom tel qu'il figure sur le passeport étranger. Selon le catalogue officiel des caractères (n° 223) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport) |
| PersonDeclaredForeignerFirstName |  Pour les personnes de nationalité étrangère qui ne disposent pas de documents officiels (principalement dans le domaine de l'asile). À utiliser en combinaison avec le nom défini selon la déclaration. Selon le catalogue officiel des caractères (n° 224) pour l'harmonisation des registres.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName) |







</div>



## Classe: LanguageProficiency 


_Compétences linguistiques d'une personne indiquant la langue et le fait qu'il s'agisse ou non de la langue préférée ou de la langue maternelle._




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




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| gender_code | 1 <br/> [GenderCodeEnum](#GenderCodeEnum) | Code de sexe. Valeurs recommandées : male, female, non_binary.  |
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




_Codes de sexe pour les personnes. Si le sexe n'est pas connu, aucune entrée de sexe ne doit être ajoutée. Le code `non_binary` doit être utilisé avec un libellé afin de fournir de plus amples détails sur le sexe auto-déclaré._




<div data-search-exclude markdown="1">

URI: [act:GenderCodeEnum](https://ld.ech.ch/schema/0294/actors/GenderCodeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| male |  Masculin.  |
| | [https://register.ld.admin.ch/i14y/concept/sex/1](https://register.ld.admin.ch/i14y/concept/sex/1) |
| female |  Féminin.  |
| | [https://register.ld.admin.ch/i14y/concept/sex/2](https://register.ld.admin.ch/i14y/concept/sex/2) |
| non_binary |  Divers / non binaire.  |







</div>



## Classe: Occupation 


_Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si l'activité est rémunérée, ainsi que la validité temporelle._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indique si l'activité est rémunérée.  |
| occupation_code | 0..1 <br/> [String](#String) | Code ISCO-19 du métier.  |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| organization_uid | 0..1 <br/> [String](#String) | IDE de l'organisation issu du registre fédéral IDE (uid.admin.ch), dans le format d'échange d'eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par uid.admin.ch et n'est pas saisie ici.  |
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
#### Exemple : swiss politicians Sofia Fisch Juristin

```yaml
label: Jurist*in
is_active: true

```
#### Exemple : swiss politicians Beat Jans Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>



## Classe: Training 


_Formation ou éducation d'une personne indiquant un type (p. ex. diplôme scolaire, diplôme universitaire, service militaire), un libellé, un code ISCO-19 et la validité temporelle._




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







</div>

\newpage

# Groupes et organes (Groups)

Le schéma Group représente les groupes, organisations et corporations politiques.

- **Un modèle générique plutôt que de nombreuses classes spécialisées :** les parlements, partis, groupes parlementaires, commissions, départements, tribunaux et organisations de la société civile sont tous représentés par *une seule* classe `Group` et différenciés au moyen de `group_type`. Cela maintient le modèle simple et extensible sans modification du schéma – le législatif, l'exécutif, le judiciaire et la société civile peuvent ainsi être représentés de manière équivalente.
- **Groupes et sous-groupes au moyen de `parent_groups` :** les groupes subordonnés renvoient à leur groupe supérieur – p. ex. une commission du Conseil des États, une sous-commission au sein d'une commission, un parti cantonal sous son parti mère ou une autorité au sein d'une direction. La hiérarchie découle ainsi de ces renvois plutôt que d'une structure de niveaux fixe. Elle reste le plus souvent au sein d'un même `group_type` ; des renvois transversaux sont toutefois possibles (p. ex. un groupe parlementaire qui renvoie à son parlement). Seule la relation de subordination est déterminante : les partis qui portent un groupe parlementaire ne lui sont pas supérieurs. Leur rapport au groupe n'est délibérément pas représenté dans la norme – il ne s'agit pas d'une hiérarchie, et il n'en existe pas de forme générale robuste, les groupes parlementaires étant liés aux partis de manière plus ou moins étroite selon les conseils. Là où l'appartenance doit être visible, elle l'est par les affiliations des personnes. Le renvoi prend la forme d'une `GroupReference` – la même que celle par laquelle une affiliation désigne son groupe. Que le lien exprime un rapport de subordination est indiqué par le slot `parent_groups` lui-même ; la référence ne porte que l'adressage. Celui-ci peut se faire au moyen du `local_id` lorsque le groupe supérieur fait partie de la même livraison, ou du `global_uri` lorsqu'il se situe en dehors – un parti cantonal peut ainsi renvoyer à son parti national sans que celui-ci doive être livré. Lorsque les deux sont connus, les deux sont indiqués.
- **Validité temporelle également pour les groupes :** au moyen de `valid_from`/`valid_through`, il est possible de représenter p. ex. des commissions n'existant que durant une législature, ou des changements de nom et des fusions de partis.



## Classe: Group 


_Un groupe, une organisation ou une collectivité politique (p. ex. parti, commission, parlement, département)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](#GroupType) | Type de groupe (p. ex. parti, commission, parlement ou similaire). La désignation et la description exactes du groupe sont fournies via `label`.  |
| label | 1..* <br/> [MultilingualValue](#MultilingualValue) | Désignation du groupe avec la langue dans laquelle elle est publiée. Lorsqu'un groupe porte officiellement un nom dans plusieurs langues, une entrée est saisie par langue.  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abréviation (peut être multilingue).  |
| description | * <br/> [MultilingualValue](#MultilingualValue) | Description de l'entité.  |
| organization_uid | 0..1 <br/> [String](#String) | IDE de l'organisation issu du registre fédéral IDE (uid.admin.ch), dans le format d'échange d'eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par uid.admin.ch et n'est pas saisie ici.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Forme juridique de l'organisation. Voir le vocabulaire contrôlé : https://register.ld.admin.ch/i14y/concept/legalForm  |
| landing_page | * <br/> [MultilingualUri](#MultilingualUri) | Site web fournissant de plus amples informations. Lorsque le site est publié à une adresse propre par langue, une entrée est saisie par langue.  |
| parent_groups | * <br/> [GroupReference](#GroupReference) | Référence aux groupes supérieurs sous forme de GroupReference, c'est-à-dire indiquée au moyen de leur local_id ou de leur global_uri. Seule une véritable relation de subordination y a sa place : le parti faîtier d'un parti cantonal, la hiérarchie au sein de l'exécutif, une sous-commission rattachée à sa commission ou un groupe parlementaire rattaché à son parlement. (parentGroup est généralement utilisé au sein d'un même group_type, mais les liens intertypes sont autorisés, p. ex. groupe parlementaire → parlement.) Les partis qui portent un groupe parlementaire ne lui sont pas supérieurs et ne sont donc pas indiqués ici.  |
| spatial | 0..1 <br/> [String](#String) | Référence spatiale à une ressource LINDAS (numéro OFS de commune, numéro OFS de canton, district ou pays). Formats : commune : https://ld.admin.ch/municipality/1234, district : https://ld.admin.ch/district/2301, canton : https://ld.admin.ch/canton/23, pays : https://ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](#Contact) | Informations de contact (e-mail, site web, réseaux sociaux). Directive : l'e-mail est quasi obligatoire et devrait toujours être fourni lorsqu'il est disponible.  |
| addresses | * <br/> [Address](#Address) | Adresses avec type (privée, professionnelle, locale).  |
| statutes_url | 0..1 <br/> [String](#String) | URL vers les statuts du parti (PDF ou page web ; facultatif pour les partis).  |
| party_color | 0..1 <br/> [String](#String) | Couleur du parti sous forme de valeur hexadécimale (facultatif pour les partis, p. ex. « #FF0000 »).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
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














### Exemples
#### Exemple : Groupe parlementaire renvoyant au parlement dont il relève

```yaml
local_id: 1266
global_uri: https://grosserrat.bs.ch/gremien/parteien-und-fraktionen/mitte-evp
label:
- value: Die Mitte / Evangelische Volkspartei
  language: de
group_type:
  group_type_enum: parliamentary_group
  label:
  - value: Fraktion
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label: Grosser Rat Basel-Stadt

```
#### Exemple : Commission renvoyant à son conseil cantonal

```yaml
groups:
- local_id: 3
  global_uri: >-
    https://ar.ch/kantonsrat/kommissionen/staendige-kommissionen-des-kantonsrates/geschaeftspruefungskommission/
  label:
  - value: Geschäftsprüfungskommission
    language: de
  abbreviation:
  - value: GPK
    language: de
  group_type:
    group_type_enum: committee
    label:
    - value: Kommission
      language: de
  spatial: https://ld.admin.ch/canton/15
  parent_groups:
  - local_id: 34
    global_uri: https://www.ar.ch/kantonsrat/
    label: Kantonsrat Appenzell Ausserrhoden

- local_id: 34
  global_uri: https://www.ar.ch/kantonsrat/
  label:
  - value: Kantonsrat Appenzell Ausserrhoden
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/15

```
#### Exemple : Chancellerie d'État renvoyant à son gouvernement

```yaml
groups:
- local_id: 7172
  global_uri: https://www.bs.ch/regierungsrat/staatskanzlei
  label:
  - value: Staatskanzlei Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_secretariat
    label:
    - value: Staatskanzlei
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 1300
    global_uri: https://www.regierungsrat.bs.ch/
    label: Regierungsrat Basel-Stadt

- local_id: 1300
  global_uri: https://www.regierungsrat.bs.ch/
  label:
  - value: Regierungsrat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_executive
    label:
    - value: Regierung (Exekutivrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Exemple : Délégation bilingue auprès d'un organe intercantonal

```yaml
local_id: 5000
global_uri: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
label:
- value: Freiburger Delegation IPK strafrechtliche Einschliessung
  language: de
- value: Délégation FR à la CIP détention pénale
  language: fr
abbreviation:
- value: Del-StRFE
  language: de
- value: Del-DetPen
  language: fr
description:
- value: >-
    Die Interparlamentarische Aufsichtskommission strafrechtliche Einschliessung besteht
    aus 18 Grossrätinnen und Grossräten aus den sechs Vertragskantonen Freiburg, Genf,
    Jura, Neuenburg, Waadt und Wallis.
  language: de
- value: >-
    La Commission interparlementaire de contrôle détention pénale est composée de
    18 députés issus des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel,
    Vaud et Valais.
  language: fr
landing_page:
- value: https://www.fr.ch/de/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: de
- value: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: fr
group_type:
  group_type_enum: delegation
  label:
  - value: Delegation
    language: de
  - value: Délégation
    language: fr
spatial: https://ld.admin.ch/canton/10
valid_from: 2007-12-12

```
#### Exemple : Commission extraparlementaire dotée du pouvoir de décision

```yaml
global_uri: https://www.weko.admin.ch/
label:
- value: Wettbewerbskommission
  language: de
- value: Commission de la concurrence
  language: fr
- value: Commissione della concorrenza
  language: it
abbreviation:
- value: WEKO
  language: de
- value: COMCO
  language: fr
- value: COMCO
  language: it
landing_page:
- value: https://www.weko.admin.ch/de
  language: de
- value: https://www.weko.admin.ch/fr
  language: fr
- value: https://www.weko.admin.ch/it
  language: it
group_type:
  group_type_enum: committee_extraparliamentary
  label:
  - value: Ausserparlamentarische Kommission
    language: de
spatial: https://ld.admin.ch/country/CHE

```
#### Exemple : Parti cantonal renvoyant au parti national

```yaml
global_uri: https://www.evp-bs.ch/
label:
- value: Evangelische Volkspartei Basel-Stadt
  language: de
abbreviation:
- value: EVP BS
  language: de
group_type:
  group_type_enum: party
  label:
  - value: Partei
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- global_uri: https://www.evppev.ch/
  label: Evangelische Volkspartei der Schweiz
  abbreviation:
  - value: EVP
    language: de

```
#### Exemple : Parlement communal avec référence spatiale

```yaml
local_id: 700
global_uri: >-
  https://www.stadt.sg.ch/home/verwaltung-politik/demokratie-politik/stadtparlament.html
label:
- value: Stadtparlament St. Gallen
  language: de
group_type:
  group_type_enum: council_legislative
  label:
  - value: Parlament (Legislativrat)
    language: de
spatial: https://ld.admin.ch/municipality/3203

```
#### Exemple : Association avec IDE et forme juridique du registre du commerce

```yaml
global_uri: https://www.frc.ch/
organization_uid: CHE106063525
legal_form: '0109'
label:
- value: Fédération romande des consommateurs
  language: fr
abbreviation:
- value: FRC
  language: fr
group_type:
  group_type_enum: association
  label:
  - value: Verein
    language: de
spatial: https://ld.admin.ch/canton/22

```
#### Exemple : Bureau du conseil renvoyant à son parlement

```yaml
groups:
- local_id: 50
  global_uri: https://grosserrat.bs.ch/gremien/praesidium-und-buero
  label:
  - value: Büro des Grossen Rates
    language: de
  group_type:
    group_type_enum: council_bureau
    label:
    - value: Ratsbüro
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 33
    global_uri: https://www.grosserrat.bs.ch/
    label: Grosser Rat Basel-Stadt

- local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label:
  - value: Grosser Rat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Exemple : Parti cantonal constituant un groupe propre à son niveau fédéral

```yaml
global_uri: https://bs.die-mitte.ch/
label:
- value: Die Mitte Basel-Stadt
  language: de
group_type:
  group_type_enum: party
  label:
  - value: Partei
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- global_uri: https://www.die-mitte.ch/
  label: Die Mitte Schweiz

```
#### Exemple : Groupe d'intérêt avec nom trilingue et contact

```yaml
local_id: 6627
global_uri: https://www.parlament.ch/de/organe/gruppen/konsumenteninformation-und-schutz
label:
- value: Konsumenteninformation und -schutz
  language: de
- value: Information et défense des consommateurs
  language: fr
- value: Informazione e tutela dei consumatori
  language: it
description:
- value: >-
    L'intergroupe parlementaire « Information et défense des consommateurs » réunit
    toutes les sensibilités politiques. Cet intergroupe a pour mission d'informer
    et de sensibiliser les élu·e·s aux questions relatives à la défense des consommateur·rice·s
    en Suisse.
  language: fr
landing_page:
- value: https://www.parlament.ch/centers/documents/de/gruppen-der-bundesversammlung.pdf
  language: de
contacts:
- contact_type: email
  value: l.altwegg@frc.ch
  label: Sekretariat
- contact_type: phone
  value: +41 21 331 00 95
  label: Sekretariat
addresses:
- address_type: businessAddress
  address_uri: https://geo.ld.admin.ch/location/address/101009806
  street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
    585
  postal_code: '1001'
  postal_locality: Lausanne
  country: CH
group_type:
  group_type_enum: interest_group
  label:
  - value: Interessengruppe
    language: de
  - value: Groupe d'intérêt
    language: fr
  - value: Gruppo d'interesse
    language: it
spatial: https://ld.admin.ch/country/CHE
valid_from: 2012-01-01

```






</div>



## Classe: GroupType 


_Type de groupe (p. ex. parti, commission, parlement, département)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| group_type_enum | 0..1 <br/> [GroupTypeEnum](#GroupTypeEnum) | Lien vers le vocabulaire contrôlé pour les types de groupes.  |
| label | * <br/> [MultilingualValue](#MultilingualValue) | Désignation du type telle que l'emploie l'organe qui la publie, avec la langue dans laquelle elle est publiée. Lorsqu'un organe publie la désignation en plusieurs langues, une entrée est saisie par langue.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [group_type](#group_type) | range | [GroupType](#GroupType) |



















</div>

## Enum: GroupTypeEnum 




_Trois règles s'appliquent aux types de groupes et d'organisations politiques._


_La valeur désigne la fonction politique ; la désignation locale relève du libellé du groupe. Büro, Ratsleitung et Ufficio presidenziale reçoivent donc tous la valeur `council_bureau`._


_Les valeurs apparentées partagent un préfixe. La famille `council_` ne distingue pas selon le conseil : une chancellerie d'État et les services du parlement sont tous deux `council_secretariat`, le rattachement ressortant de `parent_groups`. Elle se subdivise en `council_presidency` pour la présidence, `council_bureau` pour l'organe de direction élargi à la représentation des groupes et `council_secretariat` pour l'unité administrative composée d'employés. La famille `committee_` suit le même modèle, avec `committee` comme cas de base._


_La forme juridique ne relève pas de ce vocabulaire, mais de `legal_form`._




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
| assembly |  Assemblée des personnes ayant le droit de vote en tant qu'organe législatif, en particulier l'assemblée communale et, au niveau cantonal, la Landsgemeinde. Contrairement à un conseil, elle n'est pas un organe élu.  |
| | [act:enum/group_type/assembly](act:enum/group_type/assembly) |
| council_legislative |  Parlement au niveau fédéral, cantonal ou communal (p. ex. Assemblée fédérale, Conseil national, Conseil des États, Grand Conseil, parlement cantonal, parlement communal).  |
| | [act:enum/group_type/council_legislative](act:enum/group_type/council_legislative) |
| delegation |  Délégation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| committee |  Commission permanente, y compris les commissions de surveillance (p. ex. CdG), les commissions thématiques, les commissions d'enquête parlementaire (CEP) et les commissions de vérification des comptes.  |
| | [act:enum/group_type/committee](act:enum/group_type/committee) |
| committee_ad_hoc |  Commission instituée pour une tâche unique et dissoute une fois celle-ci accomplie, par opposition à une commission permanente.  |
| | [act:enum/group_type/committee_ad_hoc](act:enum/group_type/committee_ad_hoc) |
| parliamentary_group |  Groupe parlementaire.  |
| | [act:enum/group_type/parliamentary_group](act:enum/group_type/parliamentary_group) |
| council_bureau |  Organe dirigeant la marche des affaires d'un conseil, quelle que soit sa désignation locale (bureau, direction du conseil, comité de direction). S'emploie aussi bien pour le conseil législatif que pour le conseil exécutif ; la désignation locale est consignée dans le libellé.  |
| | [act:enum/group_type/council_bureau](act:enum/group_type/council_bureau) |
| council_presidency |  Présidence d'un conseil, pour le conseil législatif comme pour le conseil exécutif.  |
| | [act:enum/group_type/council_presidency](act:enum/group_type/council_presidency) |
| council_executive |  Gouvernement / exécutif en tant qu'organe collégial (p. ex. Conseil fédéral, conseil d'État, conseil municipal ou conseil communal).  |
| | [act:enum/group_type/council_executive](act:enum/group_type/council_executive) |
| department |  Département gouvernemental.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Office gouvernemental.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| committee_extraparliamentary |  Commission généralement instituée par le gouvernement pour conseiller l'administration dans son domaine et pour examiner ses affaires au préalable ; certaines disposent en outre de compétences décisionnelles propres. Ce qui la distingue d'une commission parlementaire sont sa composition et sa base légale : ses membres sont des spécialistes externes et des représentantes et représentants d'intérêts plutôt que des membres du conseil, et elle se fonde sur le droit régissant l'organisation du gouvernement et de l'administration et non sur le droit parlementaire. Ce type existe tant au niveau fédéral qu'au niveau cantonal (p. ex. la Commission de la concurrence de la Confédération ; les commissions extraparlementaires du canton de Vaud). Une commission dont les membres sont des membres du conseil ne relève pas de cette valeur, même lorsqu'elle est rattachée à l'exécutif ; elle est saisie comme commission ou commission ad hoc avec le conseil exécutif comme groupe supérieur.  |
| | [act:enum/group_type/committee_extraparliamentary](act:enum/group_type/committee_extraparliamentary) |
| interest_group |  Groupe d'intérêts issu de la société civile.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| control_body |  Organe de contrôle ou de surveillance (p. ex. Contrôle fédéral des finances CDF, autorité de surveillance AS-MPC).  |
| | [act:enum/group_type/control_body](act:enum/group_type/control_body) |
| council_secretariat |  Unité administrative au service d'un conseil, quelle que soit sa désignation locale (services du parlement, secrétariat du conseil, chancellerie d'État, cantonale ou communale). S'emploie aussi bien pour le conseil législatif que pour le conseil exécutif : la chancellerie d'État est l'état-major du conseil exécutif, les services du parlement celui du conseil législatif.  |
| | [act:enum/group_type/council_secretariat](act:enum/group_type/council_secretariat) |
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
- **Circonscription électorale rattachée à l'affiliation et non à la personne (`electoral_district`) :** la circonscription ne décrit pas la personne, mais le mandat – une même personne peut être élue, au fil du temps ou à différents niveaux fédéraux, dans des circonscriptions différentes. `ElectoralDistrict` ne porte donc pas de validité temporelle propre, mais hérite des `valid_from`/`valid_through` de l'affiliation englobante. Pour l'identification, les ressources LINDAS des unités spatiales suisses sont prévues (voir `global_uri`).



## Classe: Membership 


_Une relation d'affiliation entre une personne et un groupe, représentant une appartenance formelle (p. ex. membre d'un parti, membre d'une commission, parlementaire). À distinguer de InterestLink, qui recouvre les liens d'intérêts externes et les conflits d'intérêts avec des organisations situées en dehors du schéma des acteurs._




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
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
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




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](#RoleEnum) | Rôle de la personne dans l'affiliation ou la fonction.  |
| role_label | * <br/> [MultilingualValue](#MultilingualValue) | Libellé de rôle spécifique. À utiliser lorsqu'un nom de rôle spécifique est nécessaire, même s'il existe une valeur sémantique appropriée dans `role_type_enum` ; fournir ce libellé lorsque « role_type_enum » est réglé sur « other ». La désignation est saisie avec la langue dans laquelle elle est publiée ; lorsqu'elle est publiée en plusieurs langues, une entrée est saisie par langue.  |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [role_type_enum](#role_type_enum)
- [role_label](#role_label)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [role_type](#role_type) | range | [RoleType](#RoleType) |




##### Règles


- Si le type de rôle est « other », un libellé descriptif doit être fourni.

















</div>

## Enum: RoleEnum 




_Rôles qu'une personne peut occuper dans le cadre d'une affiliation._




<div data-search-exclude markdown="1">

URI: [act:RoleEnum](https://ld.ech.ch/schema/0294/actors/RoleEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| member |  Membre ordinaire (par défaut).  |
| president |  Président ou président du groupe.  |
| deputy |  Rôle de suppléance ou de vice-présidence.  |
| other |  Autre rôle ; utiliser role_label pour un libellé descriptif.  |







</div>



## Classe: ElectoralDistrict 


_Circonscription ou région électorale associée à une affiliation. La validité temporelle est héritée de l'affiliation englobante._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Pour les références IRI, les ressources LINDAS doivent être utilisées. Les IRI des différents niveaux administratifs des unités spatiales suisses sont disponibles à l'adresse : https://ld.admin.ch/country/CHE. Sous les liens de la section schema:containsPlace, le niveau souhaité peut être sélectionné. Exemples pour chaque niveau administratif : - Pays - Suisse : https://ld.admin.ch/country/CHE - Canton - Argovie : https://ld.admin.ch/canton/19 - District - Brigue : https://ld.admin.ch/district/2301 - Commune - Versoix : https://ld.admin.ch/municipality/6644 <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [electoral_district](#electoral_district) | range | [ElectoralDistrict](#ElectoralDistrict) |



















</div>
\newpage

# Liens d'intérêts (Interest Links)

Le schéma InterestLink consigne les liens d'intérêts, les conflits d'intérêts et les imbrications des personnes avec des organisations. Il s'appuie sur les exigences de transparence applicables aux membres du parlement selon [Assemblée fédérale – Liens d'intérêts](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Délimitation par rapport aux affiliations (`Membership`) :** `InterestLink` représente les liens avec des organisations *extérieures* au schéma des acteurs (conflits d'intérêts, financement de la politique) – par opposition à l'appartenance formelle *au sein* du schéma, qui est consignée au moyen de `Membership`.
- **Classification obligatoire (`interest_type`) :** chaque lien est obligatoirement classé selon son type (activité professionnelle, mandats politiques, association), en s'appuyant sur les catégories de divulgation de l'Assemblée fédérale.
- **Organisation référençable par IDE (`organization_uid`) :** si l'organisation est enregistrée dans le registre IDE, elle est référencée au moyen de son IDE – ce qui permet des analyses, p. ex. à l'aide de codes NOGA. C'est le format d'échange d'eCH-0108 qui est saisi, soit `CHE` suivi de neuf chiffres sans séparateurs (`CHE106063525`). Pour les organisations sans IDE, `organization_name`/`organization_address` sont disponibles ; la forme juridique suit un vocabulaire contrôlé (`LegalFormEnum`).
- **Étendue et rémunération (`is_paid`, `committee`, `function_role`) :** outre l'organe et la fonction au sein de l'organisation, il est explicitement consigné si la position est rémunérée – un aspect central de la transparence.





## Classe: InterestLink 


_Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne avec une organisation située en dehors du schéma des acteurs._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Référence à une personne avec des données instantanées au moment de la mise en relation.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | Type de lien d'intérêts (activité professionnelle, mandat politique, association).  |
| organization_name | 0..1 <br/> [String](#String) | Nom de l'organisation ou de l'entreprise.  |
| organization_uid | 0..1 <br/> [String](#String) | IDE de l'organisation issu du registre fédéral IDE (uid.admin.ch), dans le format d'échange d'eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par uid.admin.ch et n'est pas saisie ici.  |
| organization_address | 0..1 <br/> [String](#String) | Adresse de l'organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Forme juridique de l'organisation. Voir le vocabulaire contrôlé : https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indique si l'activité est rémunérée.  |
| committee | 0..1 <br/> [String](#String) | Comité ou organe au sein de l'organisation (p. ex. conseil d'administration, conseil de fondation, comité directeur, conseil de surveillance, comité consultatif, direction).  |
| function_role | 0..1 <br/> [String](#String) | Fonction ou rôle dans l'organisation (p. ex. président/e, vice-président/e, membre, délégué, directeur/directrice, conseiller/ère).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](#HasIdentification) |
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
#### Exemple : Société propre, dirigée à titre opérationnel

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Burkart Advisory GmbH, Baden
legal_form: '0107'
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Exemple : Présidence non rémunérée d'une alliance politique

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Allianz Sicherheit Schweiz, Baden
legal_form: '0109'
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Exemple : Mandat d'administrateur dans une holding

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Birchmeier Holding AG, Döttingen
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : Mandat d'administrateur dans une société immobilière

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Bovida Real Estate AG, Baar
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Exemple : Affiliation à une association de branche

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: '0109'
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Exemple : Mandat au conseil de fondation avec IDE de l'organisation

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
organization_uid: CHE109810537
legal_form: '0110'
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```
#### Exemple : Mandat au comité consultatif sans fonction d'organe

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Stiebel Eltron AG, Lupfig
legal_form: '0106'
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Exemple : Participation bénévole à l'association porteuse d'un grand projet

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Verein Landesausstellung Svizra27, Aarau
legal_form: '0109'
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Exemple : Présidence d'une association économique

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: '0109'
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Exemple : Présidence d'un parti national

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FDP.Die Liberalen
legal_form: '0109'
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Exemple : Mandat d'administrateur dans une entreprise technologique

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: ELCA Group SA, Lausanne
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```






</div>

## Enum: InterestTypeEnum 




_Types de liens d'intérêts (conflits d'intérêts, financement politique)._




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




_Formes juridiques selon la liste de codes publiée par l'Office fédéral de la statistique sur la plateforme I14Y, conforme à eCH-0108 (données de base des entreprises et registre des entreprises). Voir https://register.ld.admin.ch/i14y/concept/legalForm_




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

Contrairement à une entité, une référence n'est pas identifiée en propre – elle ne fait que désigner une entité identifiée. C'est pourquoi le `global_uri` n'y est pas obligatoire : il est seulement exigé qu'au moins l'une des deux indications `local_id` ou `global_uri` soit renseignée. Un système qui ne connaît que l'identifiant local de l'entité référencée indique celui-ci ; il est résolu au sein de la même livraison. Au-delà de la livraison, c'est le `global_uri` qui fait le renvoi.



## Classe: PersonReference 


_Référence légère à une personne avec les principales données d'identification au moment de la liaison. Préserve l'exactitude historique même si la personne change ultérieurement. La personne référencée est désignée par `local_id` ou `global_uri` ; au moins l'un des deux est requis._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Nom d'affichage court obligatoire permettant d'identifier la personne au sein de l'organisation (par ex. avec l'ajout de l'année de naissance afin de distinguer les personnes portant le même nom).  |
| label_long | 0..1 <br/> [String](#String) | Nom d'affichage long facultatif comprenant les titres académiques et le nom officiel complet (par ex. « Dr. Maria Muster-Beispiel »).  |
| group_label | 0..1 <br/> [String](#String) | Nom de l'organe/du groupe au moment de la liaison.  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local de l'entité référencée. Il est résolu au sein de la même livraison. <br/><br/>Héritage : [HasReferenceIdentification](#HasReferenceIdentification) |
| global_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | L'URI unique et globalement valide de l'entité référencée. Contrairement à un local_id, elle est également résoluble au-delà de la livraison. <br/><br/>Héritage : [HasReferenceIdentification](#HasReferenceIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, p. ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasReferenceIdentification](#HasReferenceIdentification) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [local_id](#local_id)
- [global_uri](#global_uri)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |
| [InterestLink](#InterestLink) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |



















</div>



## Classe: GroupReference 


_Référence légère à un groupe avec les principales données d'identification au moment de la liaison. Le groupe référencé est désigné par `local_id` ou `global_uri` ; au moins l'un des deux est requis. Un `local_id` est résolu au sein de la même livraison, un `global_uri` également au-delà._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abréviation (peut être multilingue).  |
| local_id | 0..1 <br/> [String](#String) | Identifiant local de l'entité référencée. Il est résolu au sein de la même livraison. <br/><br/>Héritage : [HasReferenceIdentification](#HasReferenceIdentification) |
| global_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | L'URI unique et globalement valide de l'entité référencée. Contrairement à un local_id, elle est également résoluble au-delà de la livraison. <br/><br/>Héritage : [HasReferenceIdentification](#HasReferenceIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Une URI qui renvoie à une entité Wikidata, p. ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasReferenceIdentification](#HasReferenceIdentification) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [local_id](#local_id)
- [global_uri](#global_uri)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [parent_groups](#parent_groups) | range | [GroupReference](#GroupReference) |
| [Membership](#Membership) | [group_reference](#group_reference) | range | [GroupReference](#GroupReference) |



















</div>

## Classes utilisées à plusieurs reprises

Une adresse est rédigée dans `street_address`, `postal_code`, `postal_locality` et `country` et peut renvoyer, au moyen d'`address_uri`, au Répertoire officiel des adresses de bâtiments de swisstopo. Le dernier nombre de cette URI est l'EGAID, l'identifiant fédéral d'adresse de bâtiment ; `https://geo.ld.admin.ch/location/address/101009806` désigne ainsi « Rue de Genève 17, 1003 Lausanne » en tant qu'adresse de bâtiment officiellement répertoriée.

`address_uri` est facultatif. L'adresse rédigée seule est admise, mais le renvoi au moyen de l'EGAID est préférable : celle-ci constitue un identifiant univoque et stable dans le temps, alors que les noms de rue changent, que les communes fusionnent et que les numéros postaux sont redécoupés.

Pour obtenir l'EGAID, on peut utiliser l'[API de recherche de geo.admin.ch](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Rue+de+Gen%C3%A8ve+17+1003+Lausanne&type=locations&origins=address) ou procéder à un rapprochement avec le [Répertoire officiel des adresses de bâtiments](https://www.swisstopo.admin.ch/fr/repertoire-officiel-des-adresses-de-batiments). Le résultat est saisi dans `address_uri`.



## Classe: Address 


_Une adresse avec un type (p. ex. adresse privée, adresse professionnelle) et une valeur._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](#AddressTypeEnum) | Type d'adresse.  |
| address_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | URI de l'adresse issue du Répertoire officiel des adresses de bâtiments (swisstopo). Le dernier segment de l'URI est l'EGAID, l'identifiant fédéral d'adresse de bâtiment de ce répertoire. Exemple d'URI valide : https://geo.ld.admin.ch/location/address/101904050 — le même répertoire est consultable comme couche cartographique à l'adresse https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis  |
| street_address | 0..1 <br/> [String](#String) | Adresse (rue).  |
| postal_code | 0..1 <br/> [Integer](#Integer) | Code postal.  |
| postal_locality | 0..1 <br/> [String](#String) | Localité.  |
| country | 0..1 <br/> [String](#String) | Code de pays ISO 3166-1 alpha-2.  |

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
#### Exemple : swiss politicians Beat Jans 1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```
#### Exemple : groups Konsumenteninformation und -schutz 1

```yaml
address_type: businessAddress
address_uri: https://geo.ld.admin.ch/location/address/101009806
street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
  585
postal_code: '1001'
postal_locality: Lausanne
country: CH

```






</div>

## Enum: AddressTypeEnum 




_Types d'adresses._




<div data-search-exclude markdown="1">

URI: [act:AddressTypeEnum](https://ld.ech.ch/schema/0294/actors/AddressTypeEnum)

### Valeurs admissibles
| Valeur | Description |
| --- | --- |
| privateAddress |  Adresse privée.  |
| businessAddress |  Adresse professionnelle.  |
| localAddress |  Adresse locale.  |







</div>



## Classe: Contact 


_Informations de contact d'une personne indiquant un type (p. ex. e-mail, LinkedIn) et une valeur._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| contact_type | 1 <br/> [ContactTypeEnum](#ContactTypeEnum) | Type d'informations de contact.  |
| value | 1 <br/> [String](#String) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |
| label | 0..1 <br/> [String](#String) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [contacts](#contacts) | range | [Contact](#Contact) |
| [Group](#Group) | [contacts](#contacts) | range | [Contact](#Contact) |



















</div>
\newpage

# Annexe A – Références et bibliographie

La version indiquée est celle sur la base de laquelle la présente norme a été élaborée.

## Normes du groupe spécialisé « Affaires politiques »

| | |
|---|---|
|[eCH-0292]|eCH-0292 : Métaprocessus relatifs aux affaires politiques, version 1.0.0 – éléments de données communs : [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|[eCH-0293]|eCH-0293 : Fonctionnement public des conseils, version 1.0.0 : [https://www.ech.ch/de/ech/ech-0293](https://www.ech.ch/de/ech/ech-0293)|
|[eCH-0295]|eCH-0295 : Affaires parlementaires, version 1.0.0 : [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|[eCH-0296]|eCH-0296 : Actes législatifs et textes de loi, version 1.0.0 : [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|[eCH-0297]|eCH-0297 : Consultations publiques, version 1.0.0 : [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Autres normes eCH

| | |
|---|---|
|[eCH-0011]|eCH-0011 : Datenstandard Personendaten, version 9.0.0 (approuvée, 27.07.2023). Base des types de noms dans `NameTypeEnum` (`personNameData`) : [https://www.ech.ch/de/ech/ech-0011/9.0.0](https://www.ech.ch/de/ech/ech-0011/9.0.0)|
|[eCH-0108]|eCH-0108 : Datenstandard: Unternehmensstammdaten und Unternehmensregister, version 6.0.0 (approuvée, 04.04.2024). Définit le format d'échange de l'IDE (`organization_uid`) et constitue la norme à laquelle la liste de codes des formes juridiques de `LegalFormEnum` est conforme : [https://www.ech.ch/de/ech/ech-0108/6.0.0](https://www.ech.ch/de/ech/ech-0108/6.0.0)|

## Listes de codes et autres sources

| | |
|---|---|
|[I14Y]|Plateforme d'interopérabilité de l'Office fédéral de la statistique. Source des listes de codes pour la forme juridique (`LegalFormEnum`) et le sexe (`GenderCodeEnum`) : [https://www.i14y.admin.ch](https://www.i14y.admin.ch)|
|[LINDAS]|Linked Data Service de l'administration fédérale suisse. Identifiants des unités spatiales suisses (pays, canton, district, commune) pour `spatial` et `ElectoralDistrict` : [https://ld.admin.ch](https://ld.admin.ch)|
|[NOGA]|Nomenclature générale des activités économiques de l'Office fédéral de la statistique. Permet des analyses via l'IDE des organisations référencées.|
|[Wikidata]|Base de connaissances libre. IRI d'entité (`http://www.wikidata.org/entity/Q…`) dans `wikidata_uri` : [https://www.wikidata.org](https://www.wikidata.org)|
|[ISO 639-1]|ISO (International Organization for Standardization). Codes de langue, utilisés dans le slot `language` de `MultilingualValue`.|
|[schema.org]|Vocabulaire commun pour les données structurées. Source de plusieurs affectations `slot_uri` : [https://schema.org](https://schema.org)|
|[LinkML]|Langage de modélisation dans lequel la présente norme est définie : [https://linkml.io](https://linkml.io)|

