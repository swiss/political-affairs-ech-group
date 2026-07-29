\newpage

# Introduction

## Contexte : fonctionnement public des conseils

Aux niveaux fédéral, cantonal et communal, des conseils et des assemblées siègent, délibèrent sur des affaires politiques, prennent des décisions et contrôlent l'exécutif.

## La famille de normes « Affaires politiques »

La vie politique de la Suisse se déroule aux niveaux fédéral, cantonal et communal – dans les parlements et les assemblées communales, dans les exécutifs et les administrations, dans les procédures de consultation et les consultations publiques, ainsi qu'à travers la participation démocratique directe des personnes ayant le droit de vote. Le groupe spécialisé « Affaires politiques » de l'association eCH développe à cet effet une famille de normes coordonnées entre elles, qui structurent ces données par-delà les niveaux fédéraux. Les normes utilisent des éléments de données communs (eCH-0292) et se référencent mutuellement au moyen d'identifiants univoques.

La famille comprend :

- **eCH-0292 – Éléments de données communs (Meta) :** définit les éléments de données transversaux et les métaprocessus sur lesquels reposent les autres normes. eCH-0293 en reprend notamment les éléments d'identification et de date ainsi que la structure FRBR pour les documents liés.
- **eCH-0293 – Fonctionnement public des conseils (Operations) – la présente norme :** décrit le fonctionnement public des conseils – législatures et sessions, séances et points de l'ordre du jour, procès-verbaux et décisions, votes et élections, présences ainsi que prises de parole.
- **eCH-0294 – Acteurs politiques (Actors) :** définit les personnes, groupes et organes dans le contexte politique ainsi que leurs affiliations et liens d'intérêts. eCH-0293 référence ces acteurs au moyen d'`actor_id` – p. ex. quel parlement a siégé et quelle personne a voté.
- **eCH-0295 – Affaires parlementaires (Affairs) :** décrit le cycle de vie des affaires politiques. Les points de l'ordre du jour dans eCH-0293 renvoient à l'affaire correspondante au moyen d'`affair_id`.
- **eCH-0296 – Actes législatifs et textes de loi (Laws) :** consigne les résultats du processus parlementaire – les lois et actes législatifs adoptés.
- **eCH-0297 – Consultations publiques (Consultations) :** structure les procédures de consultation, qui constituent souvent le point de départ des affaires parlementaires.

L'objectif de cette famille de normes est de créer une structure utilisable en commun pour les données politiques et de mettre à la disposition des organisations qui publient des informations sur les affaires politiques un modèle de données robuste.

## Délimitation par rapport au groupe spécialisé « Droits politiques »

Outre le groupe spécialisé « Affaires politiques », l'association eCH compte le groupe spécialisé « Droits politiques ». Tous deux concernent le domaine politique, mais couvrent des domaines différents :

- **Affaires politiques** (la présente famille de normes) décrit le processus de formation de la volonté et de décision parlementaire et administratif : les acteurs (eCH-0294), le fonctionnement des conseils (eCH-0293), les affaires parlementaires (eCH-0295), les actes législatifs qui en découlent (eCH-0296) ainsi que les consultations en amont (eCH-0297).
- **Droits politiques** traite de l'exercice des droits politiques par les personnes ayant le droit de vote : registres des électeurs et des candidats, déroulement des votations et élections populaires, vote électronique (eVoting), cartes de vote ainsi que résultats des votations et des élections (notamment eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

Cette délimitation est particulièrement importante pour eCH-0293, puisque la norme modélise des votes et des élections. Ce qui est déterminant n'est pas de savoir qui a le droit de vote, mais **où la décision est prise** – dans l'assemblée réunie ou aux urnes :

- **Dans l'assemblée** – la présente norme : les votes et élections auxquels procède un organe siégeant dans le cadre d'une séance dotée d'un ordre du jour. En font partie les votes nominatifs et les votes finaux au parlement, tout comme l'élection de membres des autorités, de juges ou de présidences de commission par le conseil. Cela est consigné au moyen de `Voting`, `IndividualVote` et `Election`.
- **Aux urnes** – groupe spécialisé « Droits politiques » : les votations et élections populaires ainsi que les registres électoraux, le déroulement, les cartes de vote et les résultats. Ces éléments ne sont pas modélisés ici.

Se situent délibérément du côté de la présente norme les **Landsgemeinden et les assemblées communales** (`meeting_type: sitting`). Il s'agit certes d'assemblées des personnes ayant le droit de vote elles-mêmes, mais elles décident en tant qu'organe siégeant, avec ordre du jour, prises de parole et décisions – et sont donc représentées comme une séance de conseil.

Un second point de contact concerne les personnes élues : dans les résultats électoraux du groupe spécialisé « Droits politiques » figurent les candidats et les personnes élues. Dès qu'une personne exerce un mandat, elle est répertoriée dans eCH-0294 en tant qu'actrice ou acteur politique, avec ses rôles et ses affiliations – eCH-0293 la référence depuis là au moyen d'`actor_id`.
