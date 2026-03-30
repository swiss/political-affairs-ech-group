# Enum: NameTypeEnum 




_[de] Kategorien von Namenstypen gemäss https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master, URI gemäss I14Y Identifier aber als Klasse und nicht als Atribut. Beschreibungen und Übersetzungen gemäss I14Y._

_[en] Categories of name types according to https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master, URI according to I14Y identifier but as class and not as attribute. Descriptions and translations according to I14Y._

__



URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| PersonOfficialName | act:vocabulary/NameTypeEnum/PersonOfficialName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonOriginalName | act:vocabulary/NameTypeEnum/PersonOriginalName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonAllianceName | act:vocabulary/NameTypeEnum/PersonAllianceName |  |
| PersonNameOnForeignPassport | act:vocabulary/NameTypeEnum/PersonNameOnForeignPassport |  |
| PersonAliasName | act:vocabulary/NameTypeEnum/PersonAliasName |  |
| PersonOtherName | act:vocabulary/NameTypeEnum/PersonOtherName |  |
| PersonDeclaredForeignerName | act:vocabulary/NameTypeEnum/PersonDeclaredForeignerName |  |
| PersonFirstName | act:vocabulary/NameTypeEnum/PersonFirstName |  |
| PersonCallFirstName | act:vocabulary/NameTypeEnum/PersonCallFirstName |  |
| PersonFirstNameOnForeignPassport | act:vocabulary/NameTypeEnum/PersonFirstNameOnForeignPassport |  |
| PersonDeclaredForeignerFirstName | act:vocabulary/NameTypeEnum/PersonDeclaredForeignerFirstName |  |




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
description: '[de] Kategorien von Namenstypen gemäss https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master,
  URI gemäss I14Y Identifier aber als Klasse und nicht als Atribut. Beschreibungen
  und Übersetzungen gemäss I14Y.

  [en] Categories of name types according to https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master,
  URI according to I14Y identifier but as class and not as attribute. Descriptions
  and translations according to I14Y.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
permissible_values:
  PersonOfficialName:
    text: PersonOfficialName
    description: "[de] Gemäss amtlichen Katalog der Merkmale (Nr. 211) Registerharmonisierung:\
      \ Name gemäss amtlichen Unterlagen. Der amtliche Name entspricht dem Namen im\
      \ schweizerischen Zivilstandsregister. Bei ausländischen Personen ohne Zivilstandsereignis\
      \ in der Schweiz entspricht dieser Name dem Namen im ausländischen Pass oder\
      \ auf der Identitätskarte (siehe 214 sowie Weisung des SEM über die Bestimmung\
      \ und Schreibweise der Namen von ausländischen Staatsangehörigen vom 1. Januar\
      \ 2012. Im Ausnahmefall siehe auch \"Name nach Deklaration\" (z. B. Asyl), wenn\
      \ keine amtlichen Dokumente vorliegen). Der amtliche Name kann aus einem oder\
      \ mehreren Teilen bestehen.  \n[fr] Selon le catalogue officiel des caractères\
      \ (n° 211) de l'harmonisation des registres : Nom selon les documents officiels.\
      \ Le nom officiel correspond au nom figurant dans le registre suisse de l’état\
      \ civil. Pour les personnes de nationalité étrangère sans événement d’état civil\
      \ en Suisse, le nom officiel correspond au nom figurant sur le passeport étranger\
      \ ou la carte d’identité (voir \"Nom selon le passeport étranger\" ou directives\
      \ du SEM sur la détermination et l’orthographe des noms de ressortissants étrangers\
      \ du 1er janvier 2012. Si des documents officiels n’existent pas, voir aussi\
      \ \"Nom selon déclaration\" (par ex. en cas d’asile). Le nom officiel peut se\
      \ composer d’une ou de plusieurs parties.\n[it] Secondo il catalogo ufficiale\
      \ delle caratteristiche (n. 211) dell'armonizzazione dei registri: Cognome secondo\
      \ i documenti ufficiali. Il cognome ufficiale corrisponde a quello riportato\
      \ nel registro svizzero dello stato civile. Per le persone straniere senza evento\
      \ dello stato civile in Svizzera il cognome ufficiale corrisponde a quello indicato\
      \ sul passaporto straniero o sulla carta d’identità (si veda \"Cognome sul passaporto\
      \ straniero\" e l’istruzione della SEM sulla determinazione e l’ortografia dei\
      \ nomi di cittadini stranieri del 1° gennaio 2012. In casi eccezionali si veda\
      \ anche la voce \"Cognome dichiarato\" (es. asilo), in mancanza di documenti\
      \ ufficiali). Il cognome ufficiale può anche essere composto.\n[en] According\
      \ to the official catalogue of characters (No. 211) for the harmonisation of\
      \ registers: Name according to official documents. The official name corresponds\
      \ to the name appearing in the Swiss civil register. For foreign nationals with\
      \ no civil status events in Switzerland, the official name corresponds to the\
      \ name appearing on the foreign passport or identity card (see ‘Name according\
      \ to foreign passport’ or SEM guidelines on the determination and spelling of\
      \ names of foreign nationals dated 1 January 2012. If no official documents\
      \ exist, see also ‘Name according to declaration’ (e.g. in the case of asylum\
      \ seekers). The official name may consist of one or more parts.\n"
    meaning: act:vocabulary/NameTypeEnum/PersonOfficialName
  PersonOriginalName:
    text: PersonOriginalName
    description: "[de] Gemäss amtlichen Katalog der Merkmale (Nr. 212) Registerharmonisierung:\
      \ Angestammter Name gemäss amtlichen Unterlagen, den eine Person unmittelbar\
      \ vor ihrer ersten Eheschliessung oder Begründung einer eingetragenen Partnerschaft\
      \ geführt hat oder, gestützt auf einen Namensänderungsentscheid, als neuen Ledignamen\
      \ erworben hat (Art. 24 Abs. 2 ZStV, SR 211.112.2).\n[fr] Selon le catalogue\
      \ officiel des caractères (n° 212) de l'harmonisation des registres : Nom de\
      \ filiation selon les documents officiels, lequel correspond au nom de la personne\
      \ avant son premier mariage ou partenariat enregistré. Il peut aussi s’agir\
      \ d’un nom de célibataire acquis par décision de changement de nom (cf. art.\
      \ 24, al. 2 OEC, RS 211.112.2). \n[it] Secondo il catalogo ufficiale delle caratteristiche\
      \ (n. 212) dell'armonizzazione dei registri: Cognome riportato sulla documentazione\
      \ ufficiale che una persona aveva immediatamente prima della celebrazione del\
      \ primo matrimonio o della costituzione della prima unione domestica registrata\
      \ o che ha acquisito come nuovo cognome da celibe / nubile in seguito alla decisione\
      \ concernente il cambiamento del cognome (art. 24 cpv. 2 OSC, RS 211.112.2).\n\
      [en] According to the official catalogue of characters (No. 212) for the harmonisation\
      \ of registers: Name of filiation according to official documents, which corresponds\
      \ to the person's name before their first marriage or registered partnership.\
      \ It may also be a maiden name acquired by decision to change one's name (see\
      \ Art. 24, para. 2 OEC, RS 211.112.2).\n"
    meaning: act:vocabulary/NameTypeEnum/PersonOriginalName
  PersonAllianceName:
    text: PersonAllianceName
    meaning: act:vocabulary/NameTypeEnum/PersonAllianceName
  PersonNameOnForeignPassport:
    text: PersonNameOnForeignPassport
    meaning: act:vocabulary/NameTypeEnum/PersonNameOnForeignPassport
  PersonAliasName:
    text: PersonAliasName
    meaning: act:vocabulary/NameTypeEnum/PersonAliasName
  PersonOtherName:
    text: PersonOtherName
    meaning: act:vocabulary/NameTypeEnum/PersonOtherName
  PersonDeclaredForeignerName:
    text: PersonDeclaredForeignerName
    meaning: act:vocabulary/NameTypeEnum/PersonDeclaredForeignerName
  PersonFirstName:
    text: PersonFirstName
    meaning: act:vocabulary/NameTypeEnum/PersonFirstName
  PersonCallFirstName:
    text: PersonCallFirstName
    meaning: act:vocabulary/NameTypeEnum/PersonCallFirstName
  PersonFirstNameOnForeignPassport:
    text: PersonFirstNameOnForeignPassport
    meaning: act:vocabulary/NameTypeEnum/PersonFirstNameOnForeignPassport
  PersonDeclaredForeignerFirstName:
    text: PersonDeclaredForeignerFirstName
    meaning: act:vocabulary/NameTypeEnum/PersonDeclaredForeignerFirstName

```
</details>