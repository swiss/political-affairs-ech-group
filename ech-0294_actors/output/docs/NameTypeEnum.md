# Enum: NameTypeEnum 




_[en] Categories of name types._

_[de] Kategorien von Namenstypen gemäss https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master resp. I14Y: https://www.i14y.admin.ch/de/catalog/concepts/5fd27bff-8bd7-49d9-a4e3-c68e4f791cef/description._

__



URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| personOfficialName | None | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| familyNameOnForeignPassport | None | [en] Family name on foreign passport |
| callName | None | [en] Call name |
| officialGivenName | None | [en] Official given name |
| officialLastName | None | [en] Official last name |
| officialMiddleName | None | [en] Official middle name |




## Slots

| Name | Description |
| ---  | --- |
| [name_type](name_type.md) | [de] Typ des Namens |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors






## LinkML Source

<details>
```yaml
name: NameTypeEnum
description: '[en] Categories of name types.

  [de] Kategorien von Namenstypen gemäss https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master
  resp. I14Y: https://www.i14y.admin.ch/de/catalog/concepts/5fd27bff-8bd7-49d9-a4e3-c68e4f791cef/description.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
permissible_values:
  personOfficialName:
    text: personOfficialName
    description: "[de] Gemäss amtlichen Katalog der Merkmale (Nr. 211) Registerharmonisierung:\
      \ Name gemäss amtlichen Unterlagen. Der amtliche Name entspricht dem Namen im\
      \ schweizerischen Zivilstandsregister. Bei ausländischen Personen ohne Zivilstandsereignis\
      \ in der Schweiz entspricht dieser Name dem Namen im ausländischen Pass oder\
      \ auf der Identitätskarte (siehe 214 sowie Weisung des SEM über die Bestimmung\
      \ und Schreibweise der Namen von ausländischen Staatsangehörigen vom 1. Januar\
      \ 2012. Im Ausnahmefall siehe auch \"Name nach Deklaration\" (z. B. Asyl), wenn\
      \ keine amtlichen Dokumente vorliegen). Der amtliche Name kann aus einem oder\
      \ mehreren Teilen bestehen.  \n[en] According to the official catalogue of characters\
      \ (No. 211) for the harmonisation of registers: Name according to official documents.\
      \ The official name corresponds to the name appearing in the Swiss civil register.\
      \ For foreign nationals with no civil status events in Switzerland, the official\
      \ name corresponds to the name appearing on the foreign passport or identity\
      \ card (see ‘Name according to foreign passport’ or SEM guidelines on the determination\
      \ and spelling of names of foreign nationals dated 1 January 2012. If no official\
      \ documents exist, see also ‘Name according to declaration’ (e.g. in the case\
      \ of asylum seekers). The official name may consist of one or more parts.\n"
  familyNameOnForeignPassport:
    text: familyNameOnForeignPassport
    description: '[en] Family name on foreign passport.

      [de] Familienname auf ausländischem Pass.

      '
  callName:
    text: callName
    description: '[en] Call name.

      [de] Rufname.

      '
  officialGivenName:
    text: officialGivenName
    description: '[en] Official given name.

      [de] Offizieller Vorname.

      '
  officialLastName:
    text: officialLastName
    description: '[en] Official last name.

      [de] Offizieller Nachname.

      '
  officialMiddleName:
    text: officialMiddleName
    description: '[en] Official middle name.

      [de] Offizieller Mittelname.

      '

```
</details>