

## Klasse: MultilingualValue 


_Ein mehrsprachiger String mit Angabe der Sprache._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| value | 1 <br/> [String](String.md) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.  |
| language | 0..1 <br/> [String](String.md) | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr", "it", "en").  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Group](Group.md) | [label](label.md) | range | [MultilingualValue](MultilingualValue.md) |
| [Group](Group.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |
| [Group](Group.md) | [description](description.md) | range | [MultilingualValue](MultilingualValue.md) |
| [ElectoralDistrict](ElectoralDistrict.md) | [label](label.md) | range | [MultilingualValue](MultilingualValue.md) |
| [GroupType](GroupType.md) | [label](label.md) | range | [MultilingualValue](MultilingualValue.md) |
| [RoleType](RoleType.md) | [role_label](role_label.md) | range | [MultilingualValue](MultilingualValue.md) |
| [GroupReference](GroupReference.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |



















</div>