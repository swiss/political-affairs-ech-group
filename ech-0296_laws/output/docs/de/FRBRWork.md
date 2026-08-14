

## Klasse: FRBRWork 


_FRBR-Work-Ebene (akn:FRBRWork): der abstrakte Erlass unabhängig von Sprache und Version. Enthält ELI-URIs, Fedlex/JoLux-Daten, Autoren, Ländercode (CH), SR-Nummer und mehrsprachige Namen mit Kurzformen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| frbr_this | 0..1 <br/> [UriValueType](UriValueType.md) | Kanonische ELI-URI dieser FRBR-Entität (akn:FRBRthis/@value). |
| frbr_uri | 0..1 <br/> [UriValueType](UriValueType.md) | Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value). |
| frbr_dates | * <br/> [FRBRDate](FRBRDate.md) | Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für verschiedene Ereignistypen.  |
| frbr_authors | * <br/> [FRBRAuthor](FRBRAuthor.md) | Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor). |
| frbr_country | 0..1 <br/> [ValueType](ValueType.md) | Ländercode für diesen Erlass (akn:FRBRcountry/@value), z.B. 'CH'. |
| frbr_number | 0..1 <br/> [ValueType](ValueType.md) | SR-Nummer (akn:FRBRnumber/@value), z.B. '101'. |
| frbr_names | * <br/> [FRBRName](FRBRName.md) | Mehrsprachige Namenseinträge des FRBR-Works (akn:FRBRname). Ein Eintrag pro Sprache. |
| frbr_authoritative | 0..1 <br/> [ValueType](ValueType.md) | Ob dies die massgebliche Version ist (akn:FRBRauthoritative/@value). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Identification](Identification.md) | [frbr_work](frbr_work.md) | range | [FRBRWork](FRBRWork.md) |














### Beispiele
#### Beispiel FRBRWork: sr101 excerpt 1 1

```yaml
frbr_work:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
  frbr_dates:
  - date_value: '2000-01-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '1999-04-18'
    frbr_date_name: jolux:dateDocument
  - date_value: '2024-03-03'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  - href: '#ch.bk'
    as_role: '#rightsHolder'
  frbr_country:
    value: CH
  frbr_number:
    value: '101'
  frbr_names:
  - xml_lang: de
    value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April 1999
    short_form: BV
  - xml_lang: fr
    value: Constitution fédérale de la Confédération suisse du 18 avril 1999
    short_form: Cst.
  - xml_lang: it
    value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
    short_form: Cost.
  - xml_lang: rm
    value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
    short_form: Cst.
  frbr_authoritative:
    value: 'true'

```
#### Beispiel FRBRWork: bgoe excerpt 1 1

```yaml
frbr_work:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
  frbr_dates:
  - date_value: '2006-07-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '2004-12-17'
    frbr_date_name: jolux:dateDocument
  - date_value: '2023-11-01'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  - href: '#ch.bk'
    as_role: '#rightsHolder'
  frbr_country:
    value: CH
  frbr_number:
    value: '152.3'
  frbr_names:
  - xml_lang: de
    value: >-
      Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung
      (Öffentlichkeitsgesetz, BGÖ)
    short_form: BGÖ
  - xml_lang: fr
    value: >-
      Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans l'administration
      (Loi sur la transparence, LTrans)
    short_form: LTrans
  - xml_lang: it
    value: >-
      Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
      (Legge sulla trasparenza, LTras)
    short_form: LTras
  - xml_lang: rm
    value: >-
      Lescha federala dals 17 da december 2004 davart il princip da la transparenza
      da l'administraziun (Lescha da transparenza, LTrans)
    short_form: LTrans
  - xml_lang: en
    value: >-
      Federal Act of 17 December 2004 on Freedom of Information in the Administration
      (Freedom of Information Act, FoIA)
    short_form: FoIA
  frbr_authoritative:
    value: 'true'

```






</div>