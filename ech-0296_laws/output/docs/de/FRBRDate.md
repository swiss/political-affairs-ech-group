

## Klasse: FRBRDate 


_Ein Datumseintrag einer FRBR-Entität (akn:FRBRdate). Das @name-Attribut verwendet Fedlex/JoLux-Vokabular: jolux:dateEntryInForce, jolux:dateDocument, jolux:dateApplicability._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date | 0..1 <br/> [date](date.md) | Ein ISO-8601-Datumswert (akn:FRBRdate/@date). |
| frbr_date_name | 0..1 <br/> [String](String.md) | Datumstyp (akn:FRBRdate/@name), mit Fedlex/JoLux-Vokabular, z.B. 'jolux:dateEntryInForce', 'jolux:dateDocument', 'jolux:dateApplicability'.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](FRBRWork.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |
| [FRBRExpression](FRBRExpression.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |
| [FRBRManifestation](FRBRManifestation.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |



















</div>