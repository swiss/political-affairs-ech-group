

## Klasse: FRBRDate 


_Ein Datumseintrag einer FRBR-Entität (akn:FRBRdate). Das @name-Attribut verwendet Fedlex/JoLux-Vokabular: jolux:dateEntryInForce, jolux:dateDocument, jolux:dateApplicability._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_value | 0..1 <br/> [Date](Date.md) | Ein ISO-8601-Datumswert (akn:FRBRdate/@date). |
| frbr_date_name | 0..1 <br/> [String](String.md) | Datumstyp (akn:FRBRdate/@name), mit Fedlex/JoLux-Vokabular, z.B. 'jolux:dateEntryInForce', 'jolux:dateDocument', 'jolux:dateApplicability'.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](FRBRWork.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |
| [FRBRExpression](FRBRExpression.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |
| [FRBRManifestation](FRBRManifestation.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |














### Beispiele
#### Beispiel FRBRDate: sr101 excerpt 1 2

```yaml
frbr_dates:
- date_value: '1999-04-18'
  frbr_date_name: jolux:dateDocument

```
#### Beispiel FRBRDate: bgoe excerpt 1 2

```yaml
frbr_dates:
- date_value: '2023-11-01'
  frbr_date_name: jolux:dateApplicability

```
#### Beispiel FRBRDate: sr101 excerpt 1 3

```yaml
frbr_dates:
- date_value: '2024-03-03'
  frbr_date_name: jolux:dateApplicability

```
#### Beispiel FRBRDate: bgoe excerpt 1 3

```yaml
frbr_dates:
- date_value: '2023-11-01'
  frbr_date_name: jolux:dateApplicability

```
#### Beispiel FRBRDate: bgoe excerpt 1 1

```yaml
frbr_dates:
- date_value: '2023-11-01'
  frbr_date_name: jolux:dateApplicability

```
#### Beispiel FRBRDate: sr101 excerpt 1 1

```yaml
frbr_dates:
- date_value: '2024-03-03'
  frbr_date_name: jolux:dateApplicability

```






</div>