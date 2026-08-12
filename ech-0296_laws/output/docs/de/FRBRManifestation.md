

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



















</div>