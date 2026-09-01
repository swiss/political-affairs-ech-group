

## Klasse: InterestLink 


_Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation ausserhalb des Akteur-Schemas._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält.  |
| interest_type | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | Art der Interessenbindung, den Kategorien der Offenlegungsregister folgend (berufliche Tätigkeit, Sitz in einem Führungsgremium, Mandat für eine Interessengruppe, Amt in der öffentlichen Hand, Mitgliedschaft).  |
| organization_name | * <br/> [MultilingualValue](MultilingualValue.md) | Name der Organisation oder des Unternehmens mit der Sprache, in der er publiziert wird. Zweisprachige Register führen den Namen in beiden Sprachen; erfasst wird pro Sprache ein Eintrag.  |
| organization_uid | 0..1 <br/> [String](String.md) | UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.  |
| organization_address | 0..1 <br/> [String](String.md) | Adresse der Organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Tätigkeit bezahlt ist.  |
| is_ex_officio | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Person das Mandat im Auftrag des Gemeinwesens wahrnimmt, dem sie angehört — also als dessen Vertretung und nicht privat. Die Angabe ist unabhängig vom Typ der Interessenbindung und lässt sich mit jedem Wert kombinieren: Derselbe Verwaltungsratssitz ist etwas anderes, wenn die Gemeinde jemanden dorthin delegiert, als wenn er privat gehalten wird. Betroffen sind vor allem Exekutivämter, weil die Vertretung in den Organen beteiligter Organisationen dort in der Regel mit dem Ressort einhergeht.  |
| committee | * <br/> [MultilingualValue](MultilingualValue.md) | Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung) mit der Sprache, in der es publiziert wird; erfasst wird pro Sprache ein Eintrag.  |
| function_role | * <br/> [MultilingualValue](MultilingualValue.md) | Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in) mit der Sprache, in der sie publiziert wird; erfasst wird pro Sprache ein Eintrag.  |
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

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |














### Beispiele
#### Beispiel InterestLink: Foundation board mandate with the organisations UID

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
#### Beispiel InterestLink: Mandate held as a delegate of the persons own commune

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
#### Beispiel InterestLink: Public office at another federal level

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
#### Beispiel InterestLink: Federation presidency  the counterpart decides not the function

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
#### Beispiel InterestLink: Cantonal link person from the same delivery

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
#### Beispiel InterestLink: Leading role for an interest group

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
#### Beispiel InterestLink: Own company run operationally

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
#### Beispiel InterestLink: The same value for a seat on a body

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
#### Beispiel InterestLink: Board mandate without a UID and without payment information

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






</div>