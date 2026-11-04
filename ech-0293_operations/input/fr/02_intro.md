\newpage

# Introduction

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

## Structure d'une livraison

Une livraison est un `Container` : une enveloppe dotée de sa propre `global_uri` et d'une collection par classe — `legislatures`, `sessions`, `meetings`, `protocols`, `votings`, `elections`, `individual_votes`, `attendances`, `individual_attendances`, `speeches` et `resolutions`. Les points de l'ordre du jour n'ont pas de collection propre : ils sont livrés au sein de leur séance ou de leur session (`agenda_items`). Toutes les collections sont facultatives : qui ne publie que des séances ne livre que `meetings`.

Les entités y sont placées côte à côte, à plat, et reliées par des références — `parent_meeting`, `parent_voting`, `parent_attendance`, et ainsi de suite — plutôt qu'imbriquées les unes dans les autres. Il est ainsi possible de livrer après coup une séance isolée sans réémettre toute la législature, et de référencer la même entité depuis plusieurs endroits. Là où l'imbrication rend mieux le lien, elle reste possible : la session reprend ses séances sous forme de liste, le procès-verbal ses points de l'ordre du jour, ses votes et ses interventions.

{{include:ech-0293_operations/output/docs/Container.md}}

## Éléments communs

Les trois classes de l'organisation temporelle — Legislature, Session et Meeting — sont délibérément construites de la même manière. Les champs suivants ont la même signification à tous les niveaux.

**Identification.** `global_uri` est l'identifiant et est obligatoire. `local_id` reprend l'identifiant du système livreur, `wikidata_uri` renvoie à l'entrée Wikidata, lorsqu'elle existe.

**Début et fin.** Les indications temporelles sont consignées deux fois : `date_begin_planned` et `date_end_planned` retiennent ce qui était prévu, `date_begin_actual` et `date_end_actual` ce qui s'est effectivement passé. Lorsque l'heure importe, les variantes `datetime_*` sont à disposition.

**Espace et organe.** `spatial` renvoie à l'unité spatiale selon LINDAS — pays, canton, district ou commune, donc `https://ld.admin.ch/canton/2` et non « BE ». C'est le champ avec lequel eCH-0294 localise ses groupes, de sorte qu'un fonctionnement de conseil et les acteurs qui le portent renvoient à la même ressource. Qui siège au sein de cette unité spatiale est indiqué par `actor_id`, référence abrégée à l'organe selon eCH-0294.

**Documents liés.** `documents` relie des documents en tant que FRBR-Works selon eCH-0292 — pour la législature p. ex. les listes des membres et les répertoires des affaires, pour la session le programme de session, pour la séance le bulletin et les annexes (le procès-verbal, en revanche, via `has_protocol`).
