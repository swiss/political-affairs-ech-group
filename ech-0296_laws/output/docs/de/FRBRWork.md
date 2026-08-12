

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



















</div>