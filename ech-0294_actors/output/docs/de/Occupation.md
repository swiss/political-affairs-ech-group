

## Klasse: Occupation 


_Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Codes, ob die Tätigkeit bezahlt ist, und der zeitlichen Gültigkeit._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Tätigkeit bezahlt ist.  |
| occupation_code | 0..1 <br/> [String](String.md) | ISCO-19 Code der Tätigkeit.  |
| label | 0..1 <br/> [String](String.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| organization_uid | 0..1 <br/> [String](String.md) | UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.  |
| organization_name | 0..1 <br/> [String](String.md) | Name der Organisation oder des Unternehmens.  |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [occupation_code](occupation_code.md)
- [label](label.md)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [occupations](occupations.md) | range | [Occupation](Occupation.md) |














### Beispiele
#### Beispiel Occupation: swiss politicians Sofia Fisch Juristin

```yaml
occupations:
- label: Jurist*in
  is_active: true

```
#### Beispiel Occupation: swiss politicians Beat Jans Politiker

```yaml
occupations:
- label: Politiker
  valid_from: 1964-01-01
  is_active: true

```






</div>