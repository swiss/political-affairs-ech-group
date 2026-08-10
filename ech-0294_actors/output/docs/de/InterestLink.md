

## Klasse: InterestLink 


_Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation ausserhalb des Akteur-Schemas._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält.  |
| interest_type | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).  |
| organization_name | 0..1 <br/> [String](String.md) | Name der Organisation oder des Unternehmens.  |
| organization_uid | 0..1 <br/> [String](String.md) | UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.  |
| organization_address | 0..1 <br/> [String](String.md) | Adresse der Organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Tätigkeit bezahlt ist.  |
| committee | 0..1 <br/> [String](String.md) | Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung).  |
| function_role | 0..1 <br/> [String](String.md) | Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in).  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [organization_uid](organization_uid.md)
- [organization_name](organization_name.md)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |














### Beispiele
#### Beispiel InterestLink: Own company run operationally

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
#### Beispiel InterestLink: Board mandate in a holding company

```yaml
interest_links:
- global_uri: act:il_burkart_002
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
#### Beispiel InterestLink: Foundation board mandate with the organisations UID

```yaml
interest_links:
- global_uri: act:il_burkart_007
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
#### Beispiel InterestLink: Leading role for an interest group

```yaml
interest_links:
- global_uri: act:il_mauron_001
  person_reference:
    global_uri: >-
      https://www.fr.ch/parlinfo/membres-du-grand-conseil/5ee6eb9754704902bfd4b4ee01dcf327
    label: Pierre Mauron
    group_label: Parti socialiste
  interest_type: association
  organization_name: ASLOCA Fribourg
  legal_form: '0109'
  committee: Comité
  function_role: Président

```
#### Beispiel InterestLink: Presidency of a trade association

```yaml
interest_links:
- global_uri: act:il_burkart_005
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
#### Beispiel InterestLink: Political office at another federal level

```yaml
interest_links:
- global_uri: act:il_dafond_001
  person_reference:
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=14
    label: Felice Dafond
    group_label: PLR
  interest_type: political_office
  organization_name: Municipio di Minusio
  legal_form: '0223'
  function_role: Sindaco

```
#### Beispiel InterestLink: Cantonal link person from the same delivery

```yaml
interest_links:
- global_uri: act:il_beretta_001
  person_reference:
    local_id: 1269
    global_uri: >-
      https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
    label: Gerri Beretta-Piccoli
  interest_type: association
  organization_name: Fondazione Gruppo Intervento Maltrattamento Infantile (GIMI),
    Lugano
  legal_form: '0110'
  committee: Consiglio di fondazione
  function_role: Vice Presidente

```
#### Beispiel InterestLink: Board mandate without a UID and without payment information

```yaml
interest_links:
- global_uri: act:il_balaban_001
  person_reference:
    global_uri: https://ge.ch/grandconseil/gc/depute/2517/
    label: Stefan Balaban
    group_label: LJS
  interest_type: professional_activity
  organization_name: X-net SA
  legal_form: '0106'
  committee: Conseil d'administration
  function_role: Membre

```






</div>