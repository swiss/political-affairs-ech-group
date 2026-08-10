

## Classe: InterestLink 


_Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne avec une organisation située en dehors du schéma des acteurs._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Référence abrégée à une personne, retenant ses caractéristiques au moment de la mise en relation.  |
| interest_type | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | Type de lien d'intérêts, suivant les catégories tenues par les registres de publicité (activité professionnelle, siège dans un organe de direction, mandat pour un groupe d'intérêts, fonction dans la sphère publique, appartenance).  |
| organization_name | 0..1 <br/> [String](String.md) | Nom de l'organisation ou de l'entreprise.  |
| organization_uid | 0..1 <br/> [String](String.md) | IDE de l'organisation issu du registre fédéral IDE (uid.admin.ch), dans le format d'échange d'eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par uid.admin.ch et n'est pas saisie ici.  |
| organization_address | 0..1 <br/> [String](String.md) | Adresse de l'organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Forme juridique de l'organisation. Voir le vocabulaire contrôlé : https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'activité est rémunérée.  |
| is_ex_officio | 0..1 <br/> [Boolean](Boolean.md) | Indique si la personne exerce le mandat pour le compte de la collectivité à laquelle elle appartient — donc en tant que représentante de celle-ci et non à titre privé. L'indication est indépendante du type de lien d'intérêts et se combine avec chacun d'eux : un même siège au conseil d'administration n'a pas la même portée selon que la commune y délègue une personne ou que celle-ci l'occupe à titre privé. Sont concernées avant tout les fonctions exécutives, car la représentation dans les organes des organisations concernées y va généralement de pair avec le dicastère.  |
| committee | 0..1 <br/> [String](String.md) | Comité ou organe au sein de l'organisation (p. ex. conseil d'administration, conseil de fondation, comité directeur, conseil de surveillance, comité consultatif, direction).  |
| function_role | 0..1 <br/> [String](String.md) | Fonction ou rôle dans l'organisation (p. ex. président/e, vice-président/e, membre, délégué, directeur/directrice, conseiller/ère).  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [organization_uid](organization_uid.md)
- [organization_name](organization_name.md)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |














### Exemples
#### Exemple InterestLink : Own company run operationally

```yaml
interest_links:
- global_uri: act:il_burkart_001
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
#### Exemple InterestLink : Foundation board mandate with the organisations UID

```yaml
interest_links:
- global_uri: act:il_burkart_007
  person_reference:
    global_uri: http://www.wikidata.org/entity/Q23060472
    label: Thierry Burkart
    group_label: FDP.Die Liberalen
  interest_type: governing_body
  organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
  organization_uid: CHE109810537
  legal_form: '0110'
  committee: Stiftungsrat
  function_role: Vizepräsident
  is_paid: false

```
#### Exemple InterestLink : Leading role for an interest group

```yaml
interest_links:
- global_uri: act:il_mauron_001
  person_reference:
    global_uri: >-
      https://www.fr.ch/parlinfo/membres-du-grand-conseil/5ee6eb9754704902bfd4b4ee01dcf327
    label: Pierre Mauron
    group_label: Parti socialiste
  interest_type: interest_group_mandate
  organization_name: ASLOCA Fribourg
  legal_form: '0109'
  committee: Comité
  function_role: Président

```
#### Exemple InterestLink : Cantonal link person from the same delivery

```yaml
interest_links:
- global_uri: act:il_beretta_001
  person_reference:
    local_id: 1269
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
    label: Gerri Beretta-Piccoli
  interest_type: governing_body
  organization_name: Fondazione Gruppo Intervento Maltrattamento Infantile (GIMI),
    Lugano
  legal_form: '0110'
  committee: Consiglio di fondazione
  function_role: Vice Presidente

```
#### Exemple InterestLink : Public office at another federal level

```yaml
interest_links:
- global_uri: act:il_dafond_001
  person_reference:
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=14
    label: Felice Dafond
    group_label: PLR
  interest_type: public_mandate
  organization_name: Municipio di Minusio
  legal_form: '0223'
  function_role: Sindaco

```
#### Exemple InterestLink : Board mandate without a UID and without payment information

```yaml
interest_links:
- global_uri: act:il_balaban_001
  person_reference:
    global_uri: https://ge.ch/grandconseil/gc/depute/2517/
    label: Stefan Balaban
    group_label: LJS
  interest_type: governing_body
  organization_name: X-net SA
  legal_form: '0106'
  committee: Conseil d'administration
  function_role: Membre

```
#### Exemple InterestLink : Mandate held as a delegate of the persons own commune

```yaml
interest_links:
- global_uri: act:il_zanini_001
  person_reference:
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=2160
    label: Cristina Zanini Barzaghi
    group_label: PS, GISO e FA
  interest_type: governing_body
  organization_name: Fondazione Giovanni Stamm
  legal_form: '0110'
  committee: Consiglio di amministrazione
  function_role: Membro
  is_ex_officio: true

```
#### Exemple InterestLink : Federation presidency  the counterpart decides not the function

```yaml
interest_links:
- global_uri: act:il_burkart_005
  person_reference:
    global_uri: http://www.wikidata.org/entity/Q23060472
    label: Thierry Burkart
    group_label: FDP.Die Liberalen
  interest_type: interest_group_mandate
  organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
  legal_form: '0109'
  committee: Zentralvorstand
  function_role: Präsident
  is_paid: true

```
#### Exemple InterestLink : The same value for a seat on a body

```yaml
interest_links:
- global_uri: act:il_quadranti_001
  person_reference:
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1487
    label: Matteo Quadranti
    group_label: Partito liberale radicale ticinese (PLR)
  interest_type: public_mandate
  organization_name: Commissione Cantonale Cultura
  function_role: Vice-presidente

```






</div>