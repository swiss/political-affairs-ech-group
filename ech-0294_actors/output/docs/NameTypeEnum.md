---
search:
  boost: 2.0
---# Enum: NameTypeEnum 




_[de] Kategorien von Namenstypen gemäss https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master, URI gemäss I14Y Identifier aber als Klasse und nicht als Atribut. Beschreibungen und Übersetzungen gemäss I14Y._

_[en] Categories of name types according to https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master, URI according to I14Y identifier but as class and not as attribute. Descriptions and translations according to I14Y._

__



<div data-search-exclude markdown="1">

URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| PersonOfficialName | act:vocabulary/NameTypeEnum/PersonOfficialName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonOriginalName | act:vocabulary/NameTypeEnum/PersonOriginalName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonAllianceName | act:vocabulary/NameTypeEnum/PersonAllianceName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonNameOnForeignPassport | act:vocabulary/NameTypeEnum/PersonNameOnForeignPassport | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonAliasName | act:vocabulary/NameTypeEnum/PersonAliasName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonOtherName | act:vocabulary/NameTypeEnum/PersonOtherName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
| PersonDeclaredForeignerName | act:vocabulary/NameTypeEnum/PersonDeclaredForeignerName | [de] Gemäss amtlichen Katalog der Merkmale (Nr |
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
    description: '[de] Gemäss amtlichen Katalog der Merkmale (Nr. 213) Registerharmonisierung:
      Der Allianzname zeigt die Verbindung von zwei Personen auf, die verheiratet
      sind oder in einer eingetragenen Partnerschaft leben. Ein bereits verwendeter
      Allianzname kann nach Auflösung der Ehe oder der Partnerschaft weiterverwendet
      werden, wenn der amtliche Name bei der Auflösung nicht geändert wurde. Dabei
      wird dem amtlichen Namen mittels Bindestrich der Ledigname des Partners/der
      Partnerin oder der eigene Ledigname angehängt. Der Allianzname kann auf Antrag
      im Pass oder auf der Identitätskarte eingetragen werden.

      [fr] Selon le catalogue officiel des caractères (n° 213) de l''harmonisation
      des registres : Le nom d’alliance montre la relation entre deux personnes qui
      sont mariées ou vivent en partenariat enregistré. Un nom d’alliance déjà utilisé
      peut être conservé, après la dissolution du mariage ou du partenariat, si le
      nom officiel n’a pas été modifié lors de la dissolution. Il est accolé par un
      trait d’union au nom officiel et est formé avec le nom de célibataire du ou
      de la partenaire ou par le propre nom de célibataire de la personne. Sur demande,
      le nom d’alliance peut être inscrit dans le passeport ou sur la carte d’identité.

      [it] Secondo il catalogo ufficiale delle caratteristiche (n. 213) dell''armonizzazione
      dei registri: Il cognome d’affinità indica il legame tra due persone che sono
      coniugate o vivono in unione domestica registrata. Il cognome d’affinità può
      continuare ad essere impiegato dopo lo scioglimento del matrimonio o dell’unione
      domestica registrata solo se il cognome ufficiale non è stato modificato al
      momento dello scioglimento. In questo caso accanto al cognome ufficiale viene
      inserito il proprio cognome da celibe/nubile o quello del/la partner separato
      da trattino. Il cognome d’affinità può essere aggiunto sul passaporto o sulla
      carta d’identità, su richiesta.

      [en] According to the official catalogue of characters (No. 213) for the harmonisation
      of registers: The alliance name shows the relationship between two people who
      are married or living in a registered partnership. An alliance name that has
      already been used may be retained after the dissolution of the marriage or partnership
      if the official name has not been changed upon dissolution. It is attached to
      the official name with a hyphen and is formed with the partner''s maiden name
      or the person''s own maiden name. Upon request, the alliance name may be entered
      in the passport or on the identity card.

      '
    meaning: act:vocabulary/NameTypeEnum/PersonAllianceName
  PersonNameOnForeignPassport:
    text: PersonNameOnForeignPassport
    description: '[de] Gemäss amtlichen Katalog der Merkmale (Nr. 214) Registerharmonisierung:
      Für Personen mit ausländischer Nationalität. Dieser Name entspricht dem Eintrag
      im Reisepass gemäss der maschinenlesbaren Zone (MRZ) des Reisepasses. Enthält
      die MRZ abgekürzte Namen oder Vornamen, sind diese möglichst in voller Länge
      gemäss visuell lesbarer Zone des Ausweispapiers zu erfassen.

      [fr] Selon le catalogue officiel des caractères (n° 214) de l''harmonisation
      des registres : Pour les personnes de nationalité étrangère. Ce nom correspond
      à l’inscription marquée dans la zone lisible par machine du passeport. Si cette
      zone comprend des noms ou prénoms abrégés, ceux-ci doivent dans la mesure du
      possible être enregistrés de manière complète, selon l’inscription contenue
      dans le passeport.

      [it] Secondo il catalogo ufficiale delle caratteristiche (n. 214) dell''armonizzazione
      dei registri: Per persone di nazionalità straniera. Questo cognome corrisponde
      all’iscrizione nel passaporto nella parte a lettura ottica (MRZ). Se la parte
      a lettura ottica contiene cognomi o nomi abbreviati, essi vanno riportati possibilmente
      in forma estesa conformemente alla parte a lettura visiva del documento di identità.

      [en] According to the official catalogue of characters (No. 214) for the harmonisation
      of registers: For persons of foreign nationality. This name corresponds to the
      entry marked in the machine-readable zone of the passport. If this zone includes
      abbreviated surnames or first names, these must, as far as possible, be recorded
      in full, according to the entry in the passport.

      '
    meaning: act:vocabulary/NameTypeEnum/PersonNameOnForeignPassport
  PersonAliasName:
    text: PersonAliasName
    description: '[de] Gemäss amtlichen Katalog der Merkmale (Nr. 215) Registerharmonisierung:
      Name (z. B. Künstler- oder Ordensname), der aufgrund eines bewilligten Gesuchs
      geführt werden darf. Der Aliasname kann aus einem oder mehreren Teilen (z. B.
      auch aus Aliasvorname und Aliasname) bestehen.

      [fr] Selon le catalogue officiel des caractères (n° 215) de l''harmonisation
      des registres : Nom (p. ex. nom d’artiste, nom d’ordre religieux) qui, sur la
      base d’une demande acceptée, peut être utilisé par la personne. Le nom alias
      peut se composer d’une ou de plusieurs parties (p. ex. aussi du prénom alias
      et du nom alias).

      [it] Secondo il catalogo ufficiale delle caratteristiche (n. 215) dell''armonizzazione
      dei registri: Cognome (p. es. nome d’arte o nome religioso) che può essere portato
      in base a una domanda autorizzata. Lo pseudonimo può essere composto da una
      o più parti (p. es. anche un nome e un cognome).

      [en] According to the official character catalogue (No. 215) for the harmonisation
      of registers: Name (e.g. stage name, religious name) which, on the basis of
      an accepted application, may be used by the person. The alias name may consist
      of one or more parts (e.g. also the alias first name and alias surname).

      '
    meaning: act:vocabulary/NameTypeEnum/PersonAliasName
  PersonOtherName:
    text: PersonOtherName
    description: '[de] Gemäss amtlichen Katalog der Merkmale (Nr. 216) Registerharmonisierung:
      Weitere amtliche Namen gemäss schweizerischen Zivilstandsdokumenten (Art. 24
      Abs. 3 ZStV) oder ausländischen Dokumenten, welche weder Familiennamen noch
      Vornamen sind.

      [fr] Selon le catalogue officiel des caractères (n° 216) de l''harmonisation
      des registres : Autres noms officiels selon les documents suisses d’état civil
      (art. 24, al. 3 OEC) ou selon des documents étrangers, qui ne sont ni des noms
      de famille ni des prénoms.

      [it] Secondo il catalogo ufficiale delle caratteristiche (n. 216) dell''armonizzazione
      dei registri: Altri cognomi ufficiali secondo i documenti svizzeri dello stato
      civile (art. 24 cpv.3 OSC) o secondo i documenti stranieri, che non sono cognomi
      né nomi.

      [en] According to the official catalogue of characters (No. 216) for the harmonisation
      of registers: Other official names according to Swiss civil status documents
      (Art. 24, para. 3 OEC) or according to foreign documents, which are neither
      surnames nor first names.

      '
    meaning: act:vocabulary/NameTypeEnum/PersonOtherName
  PersonDeclaredForeignerName:
    text: PersonDeclaredForeignerName
    description: '[de] Gemäss amtlichen Katalog der Merkmale (Nr. 217) Registerharmonisierung:
      Für Personen mit ausländischer Nationalität, die keine offiziellen Dokumente
      besitzen (hauptsächlich im Asylbereich).

      [fr] Selon le catalogue officiel des caractères (n° 217) de l''harmonisation
      des registres : Pour les personnes de nationalité étrangère ne disposant pas
      de documents officiels (principalement dans le domaine de l’asile).

      [it] Secondo il catalogo ufficiale delle caratteristiche (n. 217) dell''armonizzazione
      dei registri: Per persone di nazionalità straniera che non possiedono documenti
      ufficiali (principalmente nel settore dell’asilo).

      [en] According to the official catalogue of characters (No. 217) for the harmonisation
      of registers: For foreign nationals who do not have official documents (mainly
      in the field of asylum).

      '
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

</div>