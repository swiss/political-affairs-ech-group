

## Klasse: FRBRExpression 


_FRBR-Expression-Ebene (akn:FRBRExpression): eine sprachspezifische Version des Erlasses. Identifiziert durch einen ELI-URI mit Sprachcode._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| frbr_this | 0..1 <br/> [UriValueType](UriValueType.md) | Kanonische ELI-URI dieser FRBR-Entität (akn:FRBRthis/@value). |
| frbr_uri | 0..1 <br/> [UriValueType](UriValueType.md) | Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value). |
| frbr_dates | * <br/> [FRBRDate](FRBRDate.md) | Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für verschiedene Ereignistypen.  |
| frbr_authors | * <br/> [FRBRAuthor](FRBRAuthor.md) | Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor). |
| frbr_authoritative | 0..1 <br/> [ValueType](ValueType.md) | Ob dies die massgebliche Version ist (akn:FRBRauthoritative/@value). |
| frbr_language | 0..1 <br/> [LanguageType](LanguageType.md) | Sprachcode dieser Expression (akn:FRBRlanguage/@language). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Identification](Identification.md) | [frbr_expression](frbr_expression.md) | range | [FRBRExpression](FRBRExpression.md) |














### Beispiele
#### Beispiel FRBRExpression: zh idg 1 1

```yaml
frbr_expression:
  frbr_this:
    value_uri: /akn/CH-ZH/act/2007-02-12/62-121/ger@/!main
  frbr_uri:
    value_uri: /akn/CH-ZH/act/2007-02-12/62-121/ger@
  frbr_dates:
  - date_value: '2007-02-12'
    frbr_date_name: ''
  frbr_authors:
  - href: '#SK'
    as_role: '#editor'
  - href: '#JI'
    as_role: '#coEditor'
  frbr_language:
    language_value: ger

```
#### Beispiel FRBRExpression: bgoe 1 1

```yaml
frbr_expression:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
  frbr_dates:
  - date_value: '2006-07-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '2004-12-17'
    frbr_date_name: jolux:dateDocument
  - … 1 weitere
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  - href: '#ch.bk'
    as_role: '#rightsHolder'
  frbr_language:
    language_value: de

```
#### Beispiel FRBRExpression: sr101 1 1

```yaml
frbr_expression:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
  frbr_dates:
  - date_value: '2000-01-01'
    frbr_date_name: jolux:dateEntryInForce
  - date_value: '1999-04-18'
    frbr_date_name: jolux:dateDocument
  - … 1 weitere
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  - href: '#ch.bk'
    as_role: '#rightsHolder'
  frbr_language:
    language_value: de

```






</div>