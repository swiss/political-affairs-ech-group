

## Klasse: FRBRDate 


_Ein Datumseintrag einer FRBR-Entität (akn:FRBRdate). Das @name-Attribut verwendet Fedlex/JoLux-Vokabular: jolux:dateEntryInForce, jolux:dateDocument, jolux:dateApplicability._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_value | 0..1 <br/> [Date](Date.md) | Ein ISO-8601-Datumswert (akn:FRBRdate/@date). |
| frbr_date_name | 0..1 <br/> [String](String.md)&nbsp;or&nbsp;<br />[FrbrDateNameEnum](FrbrDateNameEnum.md) | Art dieses Datums (akn:FRBRdate/@name). Fedlex verwendet das JoLux-Vokabular; die zulässigen Werte von FrbrDateNameEnum tragen die entsprechende ELI-Eigenschaft. Kantonale Publikationsstellen führen eigene Bezeichnungen, weshalb eine freie Zeichenkette zulässig bleibt.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](FRBRWork.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |
| [FRBRExpression](FRBRExpression.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |
| [FRBRManifestation](FRBRManifestation.md) | [frbr_dates](frbr_dates.md) | range | [FRBRDate](FRBRDate.md) |














### Beispiele
#### Beispiel FRBRDate: bgoe 1 3

```yaml
frbr_dates:
- date_value: '2023-11-01'
  frbr_date_name: jolux:dateApplicability

```
#### Beispiel FRBRDate: sr101 1 2

```yaml
frbr_dates:
- date_value: '1999-04-18'
  frbr_date_name: jolux:dateDocument

```
#### Beispiel FRBRDate: bgoe 1 1

```yaml
frbr_dates:
- date_value: '2006-07-01'
  frbr_date_name: jolux:dateEntryInForce

```
#### Beispiel FRBRDate: zh idg 1 1

```yaml
frbr_dates:
- date_value: '2007-02-12'
  frbr_date_name: ''

```
#### Beispiel FRBRDate: sr101 1 3

```yaml
frbr_dates:
- date_value: '2024-03-03'
  frbr_date_name: jolux:dateApplicability

```
#### Beispiel FRBRDate: bgoe 1 2

```yaml
frbr_dates:
- date_value: '2004-12-17'
  frbr_date_name: jolux:dateDocument

```
#### Beispiel FRBRDate: sr101 1 1

```yaml
frbr_dates:
- date_value: '2000-01-01'
  frbr_date_name: jolux:dateEntryInForce

```






</div>