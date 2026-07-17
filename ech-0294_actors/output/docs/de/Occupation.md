

## Klasse: Occupation 


_Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Codes, ob die Position bezahlt ist, und der zeitlichen Gültigkeit._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Position bezahlt ist.  |
| occupation_code | 0..1 <br/> [String](String.md) | ISCO-19 Code der Tätigkeit.  |
| label | 0..1 <br/> [String](String.md) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| organization_uid | 0..1 <br/> [String](String.md) | UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen UID-Register (uid.admin.ch).  |
| organization_name | 0..1 <br/> [String](String.md) | Name der Organisation oder des Unternehmens.  |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [occupations](occupations.md) | range | [Occupation](Occupation.md) |














### Beispiele
#### Beispiel: Occupation-swiss_politicians_Beat_Jans_Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>