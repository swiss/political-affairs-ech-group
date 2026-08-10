

## Class: InterestLink 


_An interest link (conflict of interest, political financing) of a person to an organization outside the actor schema._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Reference to a person with snapshot data at time of linking.  |
| interest_type | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | Type of interest link, following the categories the disclosure registers maintain (professional activity, seat on a governing body, mandate for an interest group, public mandate, membership).  |
| organization_name | * <br/> [MultilingualValue](MultilingualValue.md) | Name of the organization or enterprise, with the language it is published in. Bilingual registers state the name in both languages; one entry is recorded per language.  |
| organization_uid | 0..1 <br/> [String](String.md) | UID of the organization from the federal UID register (uid.admin.ch), in the exchange format of eCH-0108: CHE followed by nine digits, without separators (e.g. CHE106063525). The last digit is a check digit calculated modulo 11. The dotted form CHE-106.063.525 is the presentation used by uid.admin.ch and is not recorded here.  |
| organization_address | 0..1 <br/> [String](String.md) | Address of the organization.  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Legal form of the organization. See controlled vocabulary: https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the activity is paid.  |
| is_ex_officio | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the person holds the mandate on behalf of the public body they belong to, i.e. as its delegate, rather than in a private capacity. The indication is independent of the interest type and can be combined with any of them: the same seat on a board of directors is one thing when the commune delegates a person there and quite another when they hold it privately. It concerns executive offices above all, since a delegation to the bodies of the organisations a public body holds an interest in usually comes with the department.  |
| committee | * <br/> [MultilingualValue](MultilingualValue.md) | Committee or board within the organization (e.g., Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung), with the language it is published in; one entry is recorded per language.  |
| function_role | * <br/> [MultilingualValue](MultilingualValue.md) | Function or role in the organization (e.g., Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in), with the language it is published in; one entry is recorded per language.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |

##### Constraints


At least one of the following must be set:

- [organization_uid](organization_uid.md)
- [organization_name](organization_name.md)










### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |














### Examples
#### Example InterestLink: Own company run operationally

```yaml
interest_links:
- global_uri: act:il_burkart_001
  person_reference:
    global_uri: http://www.wikidata.org/entity/Q23060472
    label: Thierry Burkart
    group_label: FDP.Die Liberalen
  interest_type: professional_activity
  organization_name:
  - value: Burkart Advisory GmbH, Baden
    language: de
  legal_form: '0107'
  committee:
  - value: Geschäftsleitung
    language: de
  function_role:
  - value: Geschäftsführer
    language: de
  is_paid: true

```
#### Example InterestLink: Foundation board mandate with the organisations UID

```yaml
interest_links:
- global_uri: act:il_burkart_007
  person_reference:
    global_uri: http://www.wikidata.org/entity/Q23060472
    label: Thierry Burkart
    group_label: FDP.Die Liberalen
  interest_type: governing_body
  organization_name:
  - value: FONDATION SUISSE DE DEMINAGE (FSD), Genf
    language: de
  organization_uid: CHE109810537
  legal_form: '0110'
  committee:
  - value: Stiftungsrat
    language: de
  function_role:
  - value: Vizepräsident
    language: de
  is_paid: false

```
#### Example InterestLink: Leading role for an interest group

```yaml
interest_links:
- global_uri: act:il_mauron_001
  person_reference:
    global_uri: >-
      https://www.fr.ch/parlinfo/membres-du-grand-conseil/5ee6eb9754704902bfd4b4ee01dcf327
    label: Pierre Mauron
    group_label: Parti socialiste
  interest_type: interest_group_mandate
  organization_name:
  - value: ASLOCA Fribourg
    language: fr
  - value: ASLOCA Freiburg
    language: de
  legal_form: '0109'
  committee:
  - value: Comité
    language: fr
  - value: Vorstand
    language: de
  function_role:
  - value: Président
    language: fr
  - value: Präsident
    language: de

```
#### Example InterestLink: Cantonal link person from the same delivery

```yaml
interest_links:
- global_uri: act:il_beretta_001
  person_reference:
    local_id: 1269
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
    label: Gerri Beretta-Piccoli
  interest_type: governing_body
  organization_name:
  - value: Fondazione Gruppo Intervento Maltrattamento Infantile (GIMI), Lugano
    language: it
  legal_form: '0110'
  committee:
  - value: Consiglio di fondazione
    language: it
  function_role:
  - value: Vice Presidente
    language: it

```
#### Example InterestLink: Public office at another federal level

```yaml
interest_links:
- global_uri: act:il_dafond_001
  person_reference:
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=14
    label: Felice Dafond
    group_label: PLR
  interest_type: public_mandate
  organization_name:
  - value: Municipio di Minusio
    language: it
  legal_form: '0223'
  function_role:
  - value: Sindaco
    language: it

```
#### Example InterestLink: Board mandate without a UID and without payment information

```yaml
interest_links:
- global_uri: act:il_balaban_001
  person_reference:
    global_uri: https://ge.ch/grandconseil/gc/depute/2517/
    label: Stefan Balaban
    group_label: LJS
  interest_type: governing_body
  organization_name:
  - value: X-net SA
    language: fr
  legal_form: '0106'
  committee:
  - value: Conseil d'administration
    language: fr
  function_role:
  - value: Membre
    language: fr

```
#### Example InterestLink: Mandate held as a delegate of the persons own commune

```yaml
interest_links:
- global_uri: act:il_zanini_001
  person_reference:
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=2160
    label: Cristina Zanini Barzaghi
    group_label: PS, GISO e FA
  interest_type: governing_body
  organization_name:
  - value: Fondazione Giovanni Stamm
    language: it
  legal_form: '0110'
  committee:
  - value: Consiglio di amministrazione
    language: it
  function_role:
  - value: Membro
    language: it
  is_ex_officio: true

```
#### Example InterestLink: Federation presidency  the counterpart decides not the function

```yaml
interest_links:
- global_uri: act:il_burkart_005
  person_reference:
    global_uri: http://www.wikidata.org/entity/Q23060472
    label: Thierry Burkart
    group_label: FDP.Die Liberalen
  interest_type: interest_group_mandate
  organization_name:
  - value: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
    language: de
  legal_form: '0109'
  committee:
  - value: Zentralvorstand
    language: de
  function_role:
  - value: Präsident
    language: de
  is_paid: true

```
#### Example InterestLink: The same value for a seat on a body

```yaml
interest_links:
- global_uri: act:il_quadranti_001
  person_reference:
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1487
    label: Matteo Quadranti
    group_label: Partito liberale radicale ticinese (PLR)
  interest_type: public_mandate
  organization_name:
  - value: Commissione Cantonale Cultura
    language: it
  function_role:
  - value: Vice-presidente
    language: it

```






</div>