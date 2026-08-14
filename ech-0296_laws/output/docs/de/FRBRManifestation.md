

## Klasse: FRBRManifestation 


_FRBR-Manifestations-Ebene (akn:FRBRManifestation): ein spezifisches Dateiformat der Expression. Für Fedlex XML-Dateien ist der Formatwert 'xml'. Das optionale Attribut fedlex:generator ist nur hier erlaubt (FLX-XF-002)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| frbr_this | 0..1 <br/> [UriValueType](UriValueType.md) | Kanonische ELI-URI dieser FRBR-Entität (akn:FRBRthis/@value). |
| frbr_uri | 0..1 <br/> [UriValueType](UriValueType.md) | Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value). |
| frbr_dates | * <br/> [FRBRDate](FRBRDate.md) | Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für verschiedene Ereignistypen.  |
| frbr_authors | * <br/> [FRBRAuthor](FRBRAuthor.md) | Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor). |
| frbr_format | 0..1 <br/> [FormatType](FormatType.md) | Dateiformat dieser Manifestation (akn:FRBRformat/@value), typischerweise 'xml'. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Identification](Identification.md) | [frbr_manifestation](frbr_manifestation.md) | range | [FRBRManifestation](FRBRManifestation.md) |














### Beispiele
#### Beispiel FRBRManifestation: bgoe excerpt 1 1

```yaml
frbr_manifestation:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
  frbr_dates:
  - date_value: '2023-11-01'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  frbr_format:
    value: xml
    fedlex_generator: 2024-q4-rel-1.6.5

```
#### Beispiel FRBRManifestation: sr101 excerpt 1 1

```yaml
frbr_manifestation:
  frbr_this:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
  frbr_uri:
    value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
  frbr_dates:
  - date_value: '2024-03-03'
    frbr_date_name: jolux:dateApplicability
  frbr_authors:
  - href: '#ch.bk'
    as_role: '#publisher'
  frbr_format:
    value: xml

```






</div>