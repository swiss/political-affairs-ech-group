---
title: "eCH-0294 Politische Akteure: Personen, Gruppen und Organe"
lang: de
toc: false
---

|**Name**|**Politische Akteure: Personen, Gruppen und Organe**|
|---|---|
|**eCH-Nummer**|eCH-0294|
|**Kategorie**|Standard|
|**Reifegrad**|Definiert|
|**Version**|1.0.0|
|**Status**|Vorschlag|
|**Beschluss am**||
|**Ausgabedatum**|2026-07-22|
|**Ersetzt Version**||
|**Voraussetzungen**||
|**Beilagen**|-|
|**Sprachen**|Deutsch (Original) - English (Datamodel)|
|**Autoren**|Fachgruppe Politische Geschäfte: Julie Silberstein, Laurence Brandenberger, Daniela Koller, Thomas Roth, Stefan Oderbolz, Fabian Davolio, Orhan Saeedi, Christian Gutknecht, Michael Luggen|
|**Herausgeber / Vertrieb**|Verein eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Abstrakt

Der Standard eCH-0294 „Politische Akteure: Personen, Gruppen und Organe“ definiert ein einheitliches Datenmodell zur strukturierten Publikation politischer Akteure in der Schweiz. Er umfasst natürliche Personen, politische Gruppen und Organe, Mitgliedschaften zwischen Personen und Gruppen sowie Interessenbindungen. Ziel ist es, föderal übergreifend vergleichbare, maschinenlesbare und nachnutzbare Informationen bereitzustellen, um Transparenz, Nachvollziehbarkeit und Analysefähigkeit politischer Prozesse zu verbessern.

Der Standard richtet sich an öffentliche Stellen aller Staatsebenen, politische Akteure, Medien, Forschung und Öffentlichkeit und schafft eine Grundlage für interoperable politische Informationssysteme in der Schweiz.

\newpage

# Inhaltsverzeichnis

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Rechtsklick &gt; „Felder aktualisieren“, um das Inhaltsverzeichnis zu erzeugen.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```


\newpage

# Einleitung

## Die Standardfamilie „Politische Geschäfte"

Das politische Geschehen der Schweiz findet auf Bundes-, Kantons- und Gemeindeebene statt – in Parlamenten und Gemeindeversammlungen, in Exekutiven und Verwaltungen, in Vernehmlassungen und Konsultationen sowie über die direktdemokratische Mitwirkung der Stimmberechtigten. Die Fachgruppe „Politische Geschäfte" des Vereins eCH entwickelt dafür eine Familie aufeinander abgestimmter Standards, welche diese Daten föderal übergreifend strukturieren. Die Standards nutzen gemeinsame Datenelemente (eCH-0292) und referenzieren sich gegenseitig über eindeutige Identifikatoren.

Die Familie umfasst:

- **eCH-0292 – Gemeinsame Datenelemente (Meta):** Definiert die übergreifend genutzten Datenelemente und Metaprozesse, auf denen die übrigen Standards aufbauen.
- **eCH-0293 – Öffentlicher Ratsbetrieb (Operations):** Beschreibt den öffentlichen Ratsbetrieb – Sitzungen, Traktanden, Wortmeldungen sowie Abstimmungen und Wahlen.
- **eCH-0294 – Politische Akteure (Actors) – dieser Standard:** Definiert Personen, Gruppen und Organe im politischen Kontext sowie deren Mitgliedschaften und Interessenbindungen. Die übrigen Standards referenzieren diese Akteure über ihre Identifikatoren.
- **eCH-0295 – Parlamentarische Geschäfte (Affairs):** Beschreibt den Lebenszyklus politischer Geschäfte.
- **eCH-0296 – Erlasse und Gesetzestexte (Laws):** Erfasst die Resultate des parlamentarischen Prozesses – die verabschiedeten Gesetze und Erlasse.
- **eCH-0297 – Öffentliche Konsultationen (Consultations):** Strukturiert Vernehmlassungsverfahren, die oft Ausgangspunkt für parlamentarische Geschäfte sind.

Ziel dieser Standardfamilie ist es, eine gemeinsam nutzbare Struktur für politische Daten zu schaffen und Organisationen, die Informationen zu politischen Geschäften veröffentlichen, ein tragfähiges Datenmodell an die Hand zu geben.

## Abgrenzung zur Fachgruppe „Politische Rechte"

Neben der Fachgruppe „Politische Geschäfte" besteht beim Verein eCH die Fachgruppe „Politische Rechte". Beide betreffen den politischen Bereich, decken aber unterschiedliche Domänen ab:

- **Politische Geschäfte** (diese Standardfamilie) beschreibt den parlamentarischen und behördlichen Willensbildungs- und Entscheidungsprozess: die Akteure (eCH-0294), den Ratsbetrieb (eCH-0293), die parlamentarischen Geschäfte (eCH-0295), die daraus hervorgehenden Erlasse (eCH-0296) sowie die vorgelagerten Vernehmlassungen (eCH-0297).
- **Politische Rechte** befasst sich mit der Ausübung der politischen Rechte durch die Stimmberechtigten: Stimm- und Wahlregister, die Durchführung von Volksabstimmungen und Wahlen, die elektronische Stimmabgabe (eVoting), Stimmrechtsausweise sowie Abstimmungs- und Wahlergebnisse (u.a. eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

Berührungspunkte bestehen an zwei Stellen:

- **Abstimmungen und Wahlen:** eCH-0293 erfasst Abstimmungen und Wahlen **innerhalb des Ratsbetriebs** (z.B. namentliche Abstimmungen im Parlament oder die Wahl von Behördenmitgliedern durch den Rat), während Volksabstimmungen und Volkswahlen samt der zugehörigen Register, Durchführung und Ergebnisse von der Fachgruppe „Politische Rechte" abgedeckt werden.
- **Gewählte Personen:** In den Wahlergebnissen der Fachgruppe „Politische Rechte" erscheinen Kandidierende und Gewählte. Sobald Personen ein Mandat innehaben, werden sie in eCH-0294 als politische Akteurinnen und Akteure mit ihren Rollen und Mitgliedschaften geführt.

## Der Standard eCH-0294 – Politische Akteure: Personen, Gruppen und Organe

Dieser Standard definiert vier Hauptklassen:

- **Person** – Natürliche Personen im politischen Kontext
- **Group** – Gremien, Parteien, Fraktionen, Räte, Kommissionen, Organisationen etc.
- **Membership** – Verbindung zwischen Personen und Gruppen
- **InterestLink** – Interessenbindungen von Personen

`Membership` ist das zentrale Bindeglied zwischen `Person` und `Group` und hält fest, in welchem Parlament, in welcher Kommission etc. eine Person aktiv ist oder war. `InterestLink` ermöglicht die Beschreibung von Interessenbindungen.
\newpage

# Person

Das Personenschema beschreibt natürliche Personen im politischen Kontext.

- **Stabile Person, zeitlich gültige Merkmale:** Die `Person` selbst trägt keine zeitliche Gültigkeit, ihre Merkmale hingegen schon – Name, Staatsangehörigkeit, Geschlecht, Beruf und Ausbildung tragen je eigene `valid_from`/`valid_through`. So bleibt die Identität der Person stabil, während sich einzelne Angaben über die Zeit ändern und die Historie erhalten bleibt (z. B. Namensänderung bei Heirat). Der Wahlkreis ist demgegenüber kein Personenmerkmal: Er hängt an der `Membership` (`electoral_district`) und erbt deren zeitliche Gültigkeit – ein Wechsel des Wahlkreises bildet sich damit über die jeweilige Mitgliedschaft ab.
- **Anzeigename (`label`) obligatorisch, Namensstruktur (`names`) optional:** Jede Person hat einen kurzen Anzeigenamen. So ist auch bei unvollständigen Angaben immer ein Name vorhanden. Empfohlen wird die Kombination aus amtlichem Namen (`PersonOfficialName`) und Rufname (`PersonCallFirstName`). Über `label_long` können auch akademische Titel abgebildet werden.
- **Namenstypen nach amtlicher Systematik:** Die Namenstypen (`NameTypeEnum`) übernehmen die Systematik der Registerharmonisierung (u. a. amtlicher Name, angestammter Name, Allianzname, Rufname sowie Varianten für ausländische Ausweise). Massgebend ist der [Amtliche Katalog der Merkmale](https://www.bfs.admin.ch/bfs/de/home/register/personenregister/registerharmonisierung/nomenklaturen.assetdetail.24565576.html), den das Bundesamt für Statistik gestützt auf Art. 4 des Registerharmonisierungsgesetzes (RHG, SR 431.02) herausgibt; die Nummern in den Wertbeschreibungen (211–224) sind die Merkmalsnummern dieses Katalogs. Das zugehörige Austauschformat definiert der eCH-Standard [eCH-0011 Datenstandard Personendaten](https://www.ech.ch/de/ech/ech-0011/9.0.0), auf den dieser Standard damit aufsetzt. Die Namen sind so mit den amtlichen Personenregistern kompatibel und ihre Semantik ist klar.
- **Geburtsdatum in zwei Genauigkeitsstufen (`birth_year` / `birth_date`):** Ist das genaue Geburtsdatum nicht verfügbar oder nicht zur Veröffentlichung bestimmt, kann nur das Geburtsjahr angegeben werden. Liegt ein `birth_date` vor, hat es Vorrang.
- **Mehrfachwerte statt Einzelwerte:** Namen, Staatsangehörigkeiten und Geschlechtsangaben sind als Listen mit zeitlicher Gültigkeit modelliert – etwa für Doppelbürgerschaften, Namensänderungen oder eine sich ändernde Geschlechtsangabe.
- **Geschlecht: amtliche Codes plus offene Kategorie (`GenderCodeEnum`):** `male` und `female` entsprechen den Werten der Registerharmonisierung und verweisen über `meaning` auf die I14Y-Konzepte `sex/1` und `sex/2`. Für `non_binary` gibt es dort bewusst keine Entsprechung: Die amtliche Codeliste kennt als dritten Wert nur „unbestimmt", was etwas anderes bedeutet als eine positive Angabe jenseits von männlich und weiblich. Ist das Geschlecht nicht bekannt, wird deshalb gar kein Eintrag gesetzt — ein fehlender Eintrag und `non_binary` sind klar zu unterscheiden.
- **Harmonisierung über föderale Ebenen (Langzeitziel):** Die Verknüpfung derselben Person über die föderalen Ebenen hinweg ist ein wichtiges Langzeitziel. Der Aufbau einer zentralen Personendatenbank liegt ausserhalb der Möglichkeiten der eCH-Fachgruppe. Da für diesen Zweck bereits eine offene, etablierte Infrastruktur besteht, wird **Wikidata als übergreifender Identifikator empfohlen** (`wikidata_uri`); zusammen mit global eindeutigen Identifikatoren (URIs) lässt sich die Zuordnung so schrittweise über die Systeme hinweg harmonisieren.




## Klasse: Person 


_Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Obligatorischer Kurzname zur Identifikation der Person innerhalb der Organisation (z.B. mit Geburtsjahr zur Unterscheidung von Personen mit gleichem Namen). Bevorzugt: PersonOfficialName (amtlicher Name) kombiniert mit PersonCallFirstName (Rufname).  |
| label_long | 0..1 <br/> [String](#String) | Optionaler langer Anzeigename mit akademischen Titeln und vollständigem amtlichem Namen (z.B. "Dr. Maria Muster-Beispiel").  |
| birth_year | 0..1 <br/> [Integer](#Integer) | Geburtsjahr. Nur zu verwenden, wenn kein vollständiges `birthDate` vorhanden ist.  |
| birth_date | 0..1 <br/> [Date](#Date) | Genaues Geburtsdatum, sofern verfügbar und öffentlich. Dieses Feld hat Vorrang vor dem Feld `birthYear`.  |
| death_date | 0..1 <br/> [Date](#Date) | Genaues Todesdatum.  |
| picture | 0..1 <br/> [Uri](#Uri) | Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF).  |
| names | * <br/> [Name](#Name) | Namen der Person mit Typ und Wert.  |
| addresses | * <br/> [Address](#Address) | Adressen mit Typ (privat, geschäftlich, lokal).  |
| language_proficiencies | * <br/> [LanguageProficiency](#LanguageProficiency) | Sprachkompetenzen der Person.  |
| citizenships | * <br/> [Citizenship](#Citizenship) | Staatsbürgerschaften der Person.  |
| genders | * <br/> [Gender](#Gender) | Geschlecht der Person.  |
| occupations | * <br/> [Occupation](#Occupation) | Berufe oder Tätigkeiten der Person.  |
| trainings | * <br/> [Training](#Training) | Ausbildungen oder Bildungen der Person. Richtlinie: Im Grundsatz nur die höchste Ausbildung angeben.  |
| contacts | * <br/> [Contact](#Contact) | Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.  |
| interest_links | * <br/> [InterestLink](#InterestLink) | Sammlung von Interessenbindungen.  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |














### Beispiele
#### Beispiel: Namensvariante neben dem amtlichen Doppelnamen

```yaml
local_id: 280958
global_uri: https://parlament.winterthur.ch/behoerdenmitglieder/280958
label: Cristina Bozzi-Brunel
names:
- name_type: PersonFirstName
  value: Cristina
- name_type: PersonOfficialName
  value: Bozzi-Brunel
- name_type: PersonOriginalName
  value: Brunel

```
#### Beispiel: Rufname weicht vom amtlichen Vornamen ab

```yaml
local_id: 1269
global_uri: >-
  https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
label: Gerri Beretta-Piccoli
names:
- name_type: PersonFirstName
  value: Fausto
- name_type: PersonCallFirstName
  value: Gerri
- name_type: PersonOfficialName
  value: Beretta-Piccoli

```
#### Beispiel: Nicht-binäre Geschlechtsangabe mit Beruf und Abschluss

```yaml
local_id: 72c7232be92944e3876f3b6723824ff9
global_uri: >-
  https://stadtrat.bern.ch/de/mitglieder/detail.php?gid=72c7232be92944e3876f3b6723824ff9
label: Sofia Fisch
birth_year: 1996
names:
- name_type: PersonFirstName
  value: Sofia
- name_type: PersonOfficialName
  value: Fisch
genders:
- gender_code: non_binary
  label: divers
occupations:
- label: Jurist*in
  is_active: true
trainings:
- training_type: '3223'
  value: MLaw

```
#### Beispiel: Gleichnamige Personen über das Label unterscheiden

```yaml
local_id: 6447
global_uri: https://www.ur.ch/behoerdenmitglieder/6447
label: Alois Arnold (1981)
birth_year: 1981
names:
- name_type: PersonFirstName
  value: Alois
- name_type: PersonOfficialName
  value: Arnold

```
#### Beispiel: Vollständig erfasste Person

```yaml
local_id: 4032
global_uri: https://www.admin.ch/de/beat-jans
wikidata_uri: http://www.wikidata.org/entity/Q813067
label: Beat Jans
label_long: Beat Jans, dipl. nat. ETH
birth_year: 1964
birth_date: 1964-07-12
picture: https://commons.wikimedia.org/wiki/File:Beat_Jans_(2026)_(cropped).jpg
names:
- name_type: PersonFirstName
  value: Beat
- name_type: PersonOfficialName
  value: Jans
  valid_from: 1964-07-12
addresses:
- address_type: businessAddress
  postal_locality: Basel-Stadt
language_proficiencies:
- language: de
  is_correspondence: true
  is_native: true
citizenships:
- country: CH
  valid_from: 1964-07-12
genders:
- gender_code: male
  valid_from: 1964-07-12
occupations:
- label: Politiker
  valid_from: 1964-01-01
  is_active: true
trainings:
- training_type: '3223'
  value: dipl. nat. ETH
contacts:
- contact_type: email
  value: beat.jans@admin.ch
- contact_type: contact_website
  value: http://www.beat-jans.ch

```
#### Beispiel: Gleichnamige Personen über das Label unterscheiden (zweite Person)

```yaml
local_id: 6370
global_uri: https://www.ur.ch/behoerdenmitglieder/6370
label: Alois Arnold (1965)
birth_year: 1965
names:
- name_type: PersonFirstName
  value: Alois
- name_type: PersonOfficialName
  value: Arnold

```






</div>



## Klasse: Name 


_Ein Name mit einem Typ (z.B. Rufname, amtlicher Name) und einem Wert und einer zeitlichen Gültigkeit._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| name_type | 1 <br/> [NameTypeEnum](#NameTypeEnum) | Typ des Namens gemäss eCH-0011 (personNameData).  |
| value | 1 <br/> [String](#String) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [names](#names) | range | [Name](#Name) |



















</div>

## Enum: NameTypeEnum 




_Kategorien von Namenstypen gemäss eCH-0011 (personNameData) und dem Amtlichen Katalog der Merkmale der Registerharmonisierung (https://www.bfs.admin.ch/bfs/de/home/register/personenregister/registerharmonisierung/nomenklaturen.assetdetail.24565576.html), URI gemäss I14Y Identifier aber als Klasse und nicht als Attribut. Beschreibungen und Übersetzungen gemäss I14Y._




<div data-search-exclude markdown="1">

URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| PersonOfficialName |  Name gemäss amtlichen Unterlagen. Der amtliche Name entspricht dem Namen im schweizerischen Zivilstandsregister. Bei ausländischen Personen ohne Zivilstandsereignis in der Schweiz entspricht dieser Name dem Namen im ausländischen Pass oder auf der Identitätskarte (siehe 214 sowie Weisung des SEM über die Bestimmung und Schreibweise der Namen von ausländischen Staatsangehörigen vom 1. Januar 2012. Im Ausnahmefall siehe auch "Name nach Deklaration" (z. B. Asyl), wenn keine amtlichen Dokumente vorliegen). Der amtliche Name kann aus einem oder mehreren Teilen bestehen. Gemäss amtlichen Katalog der Merkmale (Nr. 211) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personOfficialName](https://register.ld.admin.ch/i14y/concept/personOfficialName) |
| PersonOriginalName |  Angestammter Name gemäss amtlichen Unterlagen, den eine Person unmittelbar vor ihrer ersten Eheschliessung oder Begründung einer eingetragenen Partnerschaft geführt hat oder, gestützt auf einen Namensänderungsentscheid, als neuen Ledignamen erworben hat (Art. 24 Abs. 2 ZStV, SR 211.112.2). Gemäss amtlichen Katalog der Merkmale (Nr. 212) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personOriginalName](https://register.ld.admin.ch/i14y/concept/personOriginalName) |
| PersonAllianceName |  Der Allianzname zeigt die Verbindung von zwei Personen auf, die verheiratet sind oder in einer eingetragenen Partnerschaft leben. Ein bereits verwendeter Allianzname kann nach Auflösung der Ehe oder der Partnerschaft weiterverwendet werden, wenn der amtliche Name bei der Auflösung nicht geändert wurde. Dabei wird dem amtlichen Namen mittels Bindestrich der Ledigname des Partners/der Partnerin oder der eigene Ledigname angehängt. Der Allianzname kann auf Antrag im Pass oder auf der Identitätskarte eingetragen werden. Gemäss amtlichen Katalog der Merkmale (Nr. 213) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personAllianceName](https://register.ld.admin.ch/i14y/concept/personAllianceName) |
| PersonNameOnForeignPassport |  Für Personen mit ausländischer Nationalität. Dieser Name entspricht dem Eintrag im Reisepass gemäss der maschinenlesbaren Zone (MRZ) des Reisepasses. Enthält die MRZ abgekürzte Namen oder Vornamen, sind diese möglichst in voller Länge gemäss visuell lesbarer Zone des Ausweispapieres zu erfassen. Gemäss amtlichen Katalog der Merkmale (Nr. 214) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport) |
| PersonAliasName |  Name (z. B. Künstler- oder Ordensname), der aufgrund eines bewilligten Gesuchs geführt werden darf. Der Aliasname kann aus einem oder mehreren Teilen (z. B. auch aus Aliasvorname und Aliasname) bestehen. Gemäss amtlichen Katalog der Merkmale (Nr. 215) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personAliasName](https://register.ld.admin.ch/i14y/concept/personAliasName) |
| PersonOtherName |  Weitere amtliche Namen gemäss schweizerischen Zivilstandsdokumenten (Art. 24 Abs. 3 ZStV) oder ausländischen Dokumenten, welche weder Familiennamen noch Vornamen sind. Gemäss amtlichen Katalog der Merkmale (Nr. 216) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personOtherName](https://register.ld.admin.ch/i14y/concept/personOtherName) |
| PersonDeclaredForeignerName |  Für Personen mit ausländischer Nationalität, die keine offiziellen Dokumente besitzen (hauptsächlich im Asylbereich). Gemäss amtlichen Katalog der Merkmale (Nr. 217) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName) |
| PersonFirstName |  Vornamen gemäss Geburtsurkunde oder Zivilstandsregister/Infostar in der aufgeführten Reihenfolge bzw. gemäss ausländischen Ausweispapieren. Gemäss amtlichen Katalog der Merkmale (Nr. 221) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstName](https://register.ld.admin.ch/i14y/concept/personFirstName) |
| PersonCallFirstName |  Eine Person hat das Recht, aus der Liste ihrer amtlichen Vornamen einen Rufnamen auszuwählen. Der Rufname kann aus einem oder mehreren Vornamen (aus den "amtlichen Vornamen") bestehen. Gemäss amtlichen Katalog der Merkmale (Nr. 222) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personCallFirstName](https://register.ld.admin.ch/i14y/concept/personCallFirstName) |
| PersonFirstNameOnForeignPassport |  Für Personen mit ausländischer Nationalität. Zu benutzen in Verbindung mit dem Namen im ausländischen Pass. Gemäss amtlichen Katalog der Merkmale (Nr. 223) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport) |
| PersonDeclaredForeignerFirstName |  Für Personen mit ausländischer Nationalität, die keine amtlichen Dokumente besitzen (hauptsächlich im Asylbereich). Zu benutzen in Verbindung mit dem Namen gemäss Deklaration. Gemäss amtlichen Katalog der Merkmale (Nr. 224) Registerharmonisierung.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName) |







</div>



## Klasse: LanguageProficiency 


_Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die bevorzugte Sprache oder die Muttersprache handelt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| language | 1 <br/> [String](#String) | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr", "it", "en").  |
| is_correspondence | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob es sich um die bevorzugte Sprache handelt.  |
| is_native | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob es sich um die Muttersprache handelt.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [language_proficiencies](#language_proficiencies) | range | [LanguageProficiency](#LanguageProficiency) |



















</div>



## Klasse: Citizenship 


_Staatsangehörigkeit (wird auch für Nationalität verwendet) einer Person unter Angabe des Landes und der zeitlichen Gültigkeit. Wenn kein `valid_from` angegeben ist, ist diese Information nicht bekannt. Ist bekannt, dass die Staatsangehörigkeit seit der Geburt gültig ist, ist das Geburtsdatum hier anzugeben. Wenn kein `valid_through` angegeben ist, ist die Staatsangehörigkeit weiterhin gültig._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| country | 1 <br/> [String](#String) | ISO 3166-1 alpha-2 Ländercode.  |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [citizenships](#citizenships) | range | [Citizenship](#Citizenship) |



















</div>



## Klasse: Gender 


_Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen Gültigkeit._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| gender_code | 1 <br/> [GenderCodeEnum](#GenderCodeEnum) | Geschlechtscode. Empfohlene Werte: male, female, non_binary.  |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| pronouns | * <br/> [String](#String) | Von der Person verwendete Pronomen.  |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [genders](#genders) | range | [Gender](#Gender) |



















</div>

## Enum: GenderCodeEnum 




_Geschlechtscodes für Personen. Wenn das Geschlecht nicht bekannt ist, soll kein Geschlechtseintrag hinzugefügt werden. Der Code `non_binary` soll zusammen mit einer Bezeichnung verwendet werden, um weitere Angaben zum selbst deklarierten Geschlecht bereitzustellen._




<div data-search-exclude markdown="1">

URI: [act:GenderCodeEnum](https://ld.ech.ch/schema/0294/actors/GenderCodeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| male |  Männlich. |
| | [https://register.ld.admin.ch/i14y/concept/sex/1](https://register.ld.admin.ch/i14y/concept/sex/1) |
| female |  Weiblich. |
| | [https://register.ld.admin.ch/i14y/concept/sex/2](https://register.ld.admin.ch/i14y/concept/sex/2) |
| non_binary |  Divers / nicht-binär. |







</div>



## Klasse: Occupation 


_Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Codes, ob die Tätigkeit bezahlt ist, und der zeitlichen Gültigkeit._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Tätigkeit bezahlt ist.  |
| occupation_code | 0..1 <br/> [String](#String) | ISCO-19 Code der Tätigkeit.  |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| organization_uid | 0..1 <br/> [String](#String) | UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.  |
| organization_name | 0..1 <br/> [String](#String) | Name der Organisation oder des Unternehmens.  |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [occupation_code](#occupation_code)
- [label](#label)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [occupations](#occupations) | range | [Occupation](#Occupation) |














### Beispiele
#### Beispiel: swiss politicians Sofia Fisch Juristin

```yaml
label: Jurist*in
is_active: true

```
#### Beispiel: swiss politicians Beat Jans Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>



## Klasse: Training 


_Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B. Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19 Codes und der zeitlichen Gültigkeit._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| training_type | 0..1 <br/> [TrainingTypeEnum](#TrainingTypeEnum) | Typ der Ausbildung oder Bildung.  |
| training_code | 0..1 <br/> [String](#String) | ISCO-19 Code der Ausbildung oder Bildung.  |
| value | 0..1 <br/> [String](#String) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [training_type](#training_type)
- [training_code](#training_code)
- [value](#value)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [trainings](#trainings) | range | [Training](#Training) |



















</div>

## Enum: TrainingTypeEnum 




_Ausbildungs- oder Bildungstypen basierend auf der BFS LEVEL_EDUC Codeliste._




<div data-search-exclude markdown="1">

URI: [act:TrainingTypeEnum](https://ld.ech.ch/schema/0294/actors/TrainingTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| 10 |  Maximal obligatorische Schule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/10](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/10) |
| 110 |  Keine Ausbildung. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/110](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/110) |
| 120 |  Obligatorische Schule besucht, aber nicht abgeschlossen. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/120](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/120) |
| 130 |  Obligatorische Schule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/130](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/130) |
| 140 |  1-jährige Ausbildung / Brückenangebot. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/140](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/140) |
| 20 |  Sekundarstufe II. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/20](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/20) |
| 22 |  Sekundarstufe II - Berufsbildung. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/22](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/22) |
| 220 |  Berufslehre im Betrieb (EFZ / EBA) / Anlehre / Berufsschule / Handelsschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/220](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/220) |
| 2210 |  2-jährige Berufslehre im Betrieb (EBA) / Anlehre / Berufsschule / Handelsschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2210](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2210) |
| 2211 |  2-jährige Berufslehre im Betrieb (EBA) / Anlehre. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2211](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2211) |
| 2212 |  2-jährige Berufsschule / Handelsschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2212](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2212) |
| 2220 |  3- bis 4-jährige Berufslehre im Betrieb (EFZ) / Berufsschule / Handelsschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2220](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2220) |
| 2221 |  3- bis 4-jährige Berufslehre im Betrieb (EFZ). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2221](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2221) |
| 2222 |  3- bis 4-jährige Berufsschule / Handelsschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2222](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2222) |
| 24 |  Sekundarstufe II - Allgemeinbildung. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/24](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/24) |
| 241 |  Fachmittelschule / Diplommittelschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/241](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/241) |
| 2411 |  2-jährige Fachmittelschule / Diplommittelschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2411](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2411) |
| 2412 |  3-jährige Fachmittelschule / Diplommittelschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2412](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2412) |
| 242 |  Gymnasiale Maturität / Lehrkräfteseminar. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/242](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/242) |
| 2421 |  Gymnasiale Maturität. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2421](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2421) |
| 2422 |  Lehrkräfteseminar. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2422](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2422) |
| 243 |  Berufs- oder Fachmaturität. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/243](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/243) |
| 2431 |  Berufsmaturität. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2431](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2431) |
| 2432 |  Fachmaturität. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2432](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2432) |
| 30 |  Tertiärstufe. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/30](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/30) |
| 31 |  Höhere Berufsbildung. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/31](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/31) |
| 310 |  Berufsprüfung mit eidg. Fachausweis / Höhere Fachprüfung mit eidg. Diplom / Meisterdiplom. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/310](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/310) |
| 311 |  Berufsprüfung mit eidg. Fachausweis. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/311](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/311) |
| 312 |  Höhere Fachprüfung mit eidg. Diplom / Meisterdiplom. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/312](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/312) |
| 313 |  Höhere Fachschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/313](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/313) |
| 3131 |  Höhere Fachschule (HF) 2 Jahre Voll- oder 3 Jahre Teilzeitstudium. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3131](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3131) |
| 3132 |  Höhere Fachschule (HF) 3 Jahre Voll- oder 4 Jahre Teilzeitstudium. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3132](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3132) |
| 32 |  Hochschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/32](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/32) |
| 321 |  Bachelor Universität, ETH, Fachhochschule, pädagogische Hochschule (inklusive Diplom FH / PH). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/321](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/321) |
| 3211 |  Bachelor Fachhochschule (inklusive Diplom FH). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3211](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3211) |
| 3212 |  Bachelor pädagogische Hochschule (inklusive Diplom PH). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3212](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3212) |
| 3213 |  Bachelor Universität, ETH. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3213](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3213) |
| 322 |  Master Universität, ETH, Fachhochschule, pädagogische Hochschule (inklusive Lizentiat / Diplom). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/322](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/322) |
| 3221 |  Master Fachhochschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3221](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3221) |
| 3222 |  Master pädagogische Hochschule. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3222](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3222) |
| 3223 |  Master Universität, ETH (inklusive Lizentiat / Diplom Universität / ETH). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3223](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3223) |
| 323 |  Doktorat / Habilitation. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/323](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/323) |
| military |  Militärdienst (Schweizer Armee). Den erreichten Grad im Feld `value` angeben. |







</div>

\newpage

# Gruppen und Organe (Groups)

Das Group-Schema bildet politische Gruppen, Organisationen und Körperschaften ab.

- **Ein generisches Modell statt vieler Spezialklassen:** Parlamente, Parteien, Fraktionen, Kommissionen, Departemente, Gerichte und zivilgesellschaftliche Organisationen werden alle als *eine* Klasse `Group` abgebildet und über `group_type` unterschieden. Das hält das Modell einfach und ohne Schemaänderung erweiterbar – Legislative, Exekutive, Judikative und Zivilgesellschaft sind damit gleichermassen abbildbar.
- **Gruppen und Sub-Gruppen über `parent_groups`:** Untergeordnete Gruppen verweisen auf ihre übergeordnete Gruppe – z. B. eine Kommission des Ständerats, eine Subkommission innerhalb einer Kommission, eine Kantonalpartei unter ihrer Mutterpartei oder eine Behörde innerhalb einer Direktion. Die Hierarchie entsteht so aus diesen Verweisen statt aus einer festen Ebenenstruktur. Sie bleibt meist innerhalb desselben `group_type`; typenübergreifende Verweise sind aber möglich (z. B. eine Fraktion, die auf ihr Parlament verweist). Massgebend ist dabei allein die Über-/Unterordnung: Die Parteien, welche eine Fraktion tragen, sind ihr nicht übergeordnet. Ihr Verhältnis zur Fraktion bleibt im Standard bewusst unabgebildet – es ist keine Hierarchie, und eine tragfähige allgemeine Form dafür gibt es nicht, weil Fraktionen je nach Rat unterschiedlich eng an Parteien gebunden sind. Wo die Zugehörigkeit sichtbar sein muss, tut sie es über die Mitgliedschaften der einzelnen Personen. Der Verweis erfolgt als `GroupReference` – dieselbe Form, mit der eine Mitgliedschaft ihre Gruppe benennt. Dass es sich um eine Über-/Unterordnung handelt, sagt dabei der Slot `parent_groups` selbst; die Referenz trägt nur die Adressierung. Diese kann über die `local_id` erfolgen, wenn die übergeordnete Gruppe Teil derselben Lieferung ist, oder über die `global_uri`, wenn sie ausserhalb liegt – eine Kantonalpartei kann so auf ihre Bundespartei verweisen, ohne dass diese mitgeliefert werden muss. Sind beide bekannt, werden beide angegeben.
- **Zeitliche Gültigkeit auch für Gruppen:** Über `valid_from`/`valid_through` lassen sich z. B. nur während einer Legislatur bestehende Kommissionen oder Umbenennungen und Fusionen von Parteien abbilden.



## Klasse: Group 


_Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](#GroupType) | Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Benennung und Beschreibung der Gruppierung wird über `label` gemacht.  |
| label | 1..* <br/> [MultilingualValue](#MultilingualValue) | Bezeichnung der Gruppe mit der Sprache, in der sie publiziert wird. Ist eine Gruppe amtlich in mehreren Sprachen benannt, wird pro Sprache ein Eintrag erfasst.  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abkürzung (kann mehrsprachig sein).  |
| description | * <br/> [MultilingualValue](#MultilingualValue) | Kurze Beschreibung der Gruppierung.  |
| organization_uid | 0..1 <br/> [String](#String) | UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm  |
| landing_page | * <br/> [MultilingualUri](#MultilingualUri) | Website mit weiteren Informationen. Wird die Website je Sprache unter einer eigenen Adresse publiziert, wird pro Sprache ein Eintrag erfasst.  |
| parent_groups | * <br/> [GroupReference](#GroupReference) | Verweis auf die übergeordneten Gruppen als GroupReference, also angegeben über deren local_id oder deren global_uri. Hierher gehört nur eine echte Über-/Unterordnung: die Mutterpartei einer Kantonalpartei, die Hierarchie in der Exekutive, eine Subkommission unter ihrer Kommission oder eine Fraktion unter ihrem Parlament. (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament.) Die eine Fraktion tragenden Parteien sind ihr nicht übergeordnet und werden hier deshalb nicht angegeben.  |
| spatial | 0..1 <br/> [String](#String) | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](#Contact) | Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.  |
| addresses | * <br/> [Address](#Address) | Adressen mit Typ (privat, geschäftlich, lokal).  |
| statutes_url | 0..1 <br/> [String](#String) | URL zu Parteistatuten (PDF oder Webseite; optional für Parteien).  |
| party_color | 0..1 <br/> [String](#String) | Parteifarbe als Hexadezimalwert (optional für Parteien, z.B. "#FF0000").  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [groups](#groups) | range | [Group](#Group) |














### Beispiele
#### Beispiel: Fraktion mit Verweis auf das übergeordnete Parlament

```yaml
local_id: 1266
global_uri: https://grosserrat.bs.ch/gremien/parteien-und-fraktionen/mitte-evp
label:
- value: Die Mitte / Evangelische Volkspartei
  language: de
group_type:
  group_type_enum: parliamentary_group
  label:
  - value: Fraktion
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label: Grosser Rat Basel-Stadt

```
#### Beispiel: Kommission mit Verweis auf ihren Kantonsrat

```yaml
groups:
- local_id: 3
  global_uri: >-
    https://ar.ch/kantonsrat/kommissionen/staendige-kommissionen-des-kantonsrates/geschaeftspruefungskommission/
  label:
  - value: Geschäftsprüfungskommission
    language: de
  abbreviation:
  - value: GPK
    language: de
  group_type:
    group_type_enum: committee
    label:
    - value: Kommission
      language: de
  spatial: https://ld.admin.ch/canton/15
  parent_groups:
  - local_id: 34
    global_uri: https://www.ar.ch/kantonsrat/
    label: Kantonsrat Appenzell Ausserrhoden

- local_id: 34
  global_uri: https://www.ar.ch/kantonsrat/
  label:
  - value: Kantonsrat Appenzell Ausserrhoden
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/15

```
#### Beispiel: Staatskanzlei mit Verweis auf ihre Regierung

```yaml
groups:
- local_id: 7172
  global_uri: https://www.bs.ch/regierungsrat/staatskanzlei
  label:
  - value: Staatskanzlei Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_secretariat
    label:
    - value: Staatskanzlei
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 1300
    global_uri: https://www.regierungsrat.bs.ch/
    label: Regierungsrat Basel-Stadt

- local_id: 1300
  global_uri: https://www.regierungsrat.bs.ch/
  label:
  - value: Regierungsrat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_executive
    label:
    - value: Regierung (Exekutivrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Beispiel: Zweisprachige Delegation in ein interkantonales Gremium

```yaml
local_id: 5000
global_uri: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
label:
- value: Freiburger Delegation IPK strafrechtliche Einschliessung
  language: de
- value: Délégation FR à la CIP détention pénale
  language: fr
abbreviation:
- value: Del-StRFE
  language: de
- value: Del-DetPen
  language: fr
description:
- value: >-
    Die Interparlamentarische Aufsichtskommission strafrechtliche Einschliessung besteht
    aus 18 Grossrätinnen und Grossräten aus den sechs Vertragskantonen Freiburg, Genf,
    Jura, Neuenburg, Waadt und Wallis.
  language: de
- value: >-
    La Commission interparlementaire de contrôle détention pénale est composée de
    18 députés issus des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel,
    Vaud et Valais.
  language: fr
landing_page:
- value: https://www.fr.ch/de/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: de
- value: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: fr
group_type:
  group_type_enum: delegation
  label:
  - value: Delegation
    language: de
  - value: Délégation
    language: fr
spatial: https://ld.admin.ch/canton/10
valid_from: 2007-12-12

```
#### Beispiel: Ausserparlamentarische Kommission mit Entscheidbefugnis

```yaml
global_uri: https://www.weko.admin.ch/
label:
- value: Wettbewerbskommission
  language: de
- value: Commission de la concurrence
  language: fr
- value: Commissione della concorrenza
  language: it
abbreviation:
- value: WEKO
  language: de
- value: COMCO
  language: fr
- value: COMCO
  language: it
landing_page:
- value: https://www.weko.admin.ch/de
  language: de
- value: https://www.weko.admin.ch/fr
  language: fr
- value: https://www.weko.admin.ch/it
  language: it
group_type:
  group_type_enum: committee_extraparliamentary
  label:
  - value: Ausserparlamentarische Kommission
    language: de
spatial: https://ld.admin.ch/country/CHE

```
#### Beispiel: Kantonalpartei mit Verweis auf die Bundespartei

```yaml
global_uri: https://www.evp-bs.ch/
label:
- value: Evangelische Volkspartei Basel-Stadt
  language: de
abbreviation:
- value: EVP BS
  language: de
group_type:
  group_type_enum: party
  label:
  - value: Partei
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- global_uri: https://www.evppev.ch/
  label: Evangelische Volkspartei der Schweiz
  abbreviation:
  - value: EVP
    language: de

```
#### Beispiel: Gemeindeparlament mit räumlicher Referenz

```yaml
local_id: 700
global_uri: >-
  https://www.stadt.sg.ch/home/verwaltung-politik/demokratie-politik/stadtparlament.html
label:
- value: Stadtparlament St. Gallen
  language: de
group_type:
  group_type_enum: council_legislative
  label:
  - value: Parlament (Legislativrat)
    language: de
spatial: https://ld.admin.ch/municipality/3203

```
#### Beispiel: Verein mit UID und Rechtsform aus dem Handelsregister

```yaml
global_uri: https://www.frc.ch/
organization_uid: CHE106063525
legal_form: '0109'
label:
- value: Fédération romande des consommateurs
  language: fr
abbreviation:
- value: FRC
  language: fr
group_type:
  group_type_enum: association
  label:
  - value: Verein
    language: de
spatial: https://ld.admin.ch/canton/22

```
#### Beispiel: Ratsbüro mit Verweis auf sein Parlament

```yaml
groups:
- local_id: 50
  global_uri: https://grosserrat.bs.ch/gremien/praesidium-und-buero
  label:
  - value: Büro des Grossen Rates
    language: de
  group_type:
    group_type_enum: council_bureau
    label:
    - value: Ratsbüro
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 33
    global_uri: https://www.grosserrat.bs.ch/
    label: Grosser Rat Basel-Stadt

- local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label:
  - value: Grosser Rat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Beispiel: Kantonalpartei als eigene Gruppe der föderalen Ebene

```yaml
global_uri: https://bs.die-mitte.ch/
label:
- value: Die Mitte Basel-Stadt
  language: de
group_type:
  group_type_enum: party
  label:
  - value: Partei
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- global_uri: https://www.die-mitte.ch/
  label: Die Mitte Schweiz

```
#### Beispiel: Interessengruppe mit dreisprachigem Namen und Kontakt

```yaml
local_id: 6627
global_uri: https://www.parlament.ch/de/organe/gruppen/konsumenteninformation-und-schutz
label:
- value: Konsumenteninformation und -schutz
  language: de
- value: Information et défense des consommateurs
  language: fr
- value: Informazione e tutela dei consumatori
  language: it
description:
- value: >-
    L'intergroupe parlementaire « Information et défense des consommateurs » réunit
    toutes les sensibilités politiques. Cet intergroupe a pour mission d'informer
    et de sensibiliser les élu·e·s aux questions relatives à la défense des consommateur·rice·s
    en Suisse.
  language: fr
landing_page:
- value: https://www.parlament.ch/centers/documents/de/gruppen-der-bundesversammlung.pdf
  language: de
contacts:
- contact_type: email
  value: l.altwegg@frc.ch
  label: Sekretariat
- contact_type: phone
  value: +41 21 331 00 95
  label: Sekretariat
addresses:
- address_type: businessAddress
  address_uri: https://geo.ld.admin.ch/location/address/101009806
  street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
    585
  postal_code: '1001'
  postal_locality: Lausanne
  country: CH
group_type:
  group_type_enum: interest_group
  label:
  - value: Interessengruppe
    language: de
  - value: Groupe d'intérêt
    language: fr
  - value: Gruppo d'interesse
    language: it
spatial: https://ld.admin.ch/country/CHE
valid_from: 2012-01-01

```






</div>



## Klasse: GroupType 


_Art der Gruppe (z.B. Partei, Kommission, Parlament, Departement)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| group_type_enum | 1 <br/> [GroupTypeEnum](#GroupTypeEnum) | Link zum kontrollierten Vokabular für Gruppentypen.  |
| label | * <br/> [MultilingualValue](#MultilingualValue) | Bezeichnung des Typs, wie ihn die publizierende Stelle verwendet, mit der Sprache, in der sie publiziert wird. Publiziert eine Stelle die Bezeichnung in mehreren Sprachen, wird pro Sprache ein Eintrag erfasst.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [group_type](#group_type) | range | [GroupType](#GroupType) |



















</div>

## Enum: GroupTypeEnum 




_Kontrolliertes Vokabular für die Art einer Gruppe. Es umfasst die Räte und ihre Organe, Versammlungen, Kommissionen und Delegationen, Parteien, Fraktionen und Wahllisten, die Einheiten der Verwaltung, Gerichte und Aufsichtsorgane sowie Organisationen ausserhalb des Staates._


_Ein `group_type` muss immer gesetzt werden. Massgebend ist die politische Funktion, nicht die örtliche Bezeichnung; diese wird im Label festgehalten. Findet sich kein passender Wert, wird `other` gesetzt._


_Die Rechtsform gehört nicht in dieses Vokabular, sondern in `legal_form`._




<div data-search-exclude markdown="1">

URI: [act:GroupTypeEnum](https://ld.ech.ch/schema/0294/actors/GroupTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| party |  Politische Partei auf Bundes-, Kantons- oder Gemeindeebene. Jede föderale Ebene wird als eigene Gruppe geführt (z.B. Bundespartei, Kantonspartei, Gemeindesektion).  |
| | [act:enum/group_type/party](act:enum/group_type/party) |
| list |  Wahlliste (kann Teil einer Partei sein oder unabhängig).  |
| | [act:enum/group_type/list](act:enum/group_type/list) |
| workgroup |  Ad-hoc-Arbeitsgruppe, typischerweise mit begrenzter Laufzeit.  |
| | [act:enum/group_type/workgroup](act:enum/group_type/workgroup) |
| assembly |  Versammlung der Stimmberechtigten als gesetzgebendes Organ, insbesondere die Gemeindeversammlung und, auf Kantonsebene, die Landsgemeinde. Anders als ein Rat ist sie kein gewähltes Gremium.  |
| | [act:enum/group_type/assembly](act:enum/group_type/assembly) |
| council_legislative |  Parlament auf Bundes-, Kantons- oder Gemeindeebene (z.B. Bundesversammlung, Nationalrat, Ständerat, Grosser Rat, Kantonsrat, Gemeindeparlament).  |
| | [act:enum/group_type/council_legislative](act:enum/group_type/council_legislative) |
| delegation |  Delegation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| committee |  Ständige Kommission, einschliesslich Aufsichtskommissionen (z.B. GPK), Sachkommissionen, Parlamentarische Untersuchungskommissionen (PUK) und Rechnungsprüfungskommissionen.  |
| | [act:enum/group_type/committee](act:enum/group_type/committee) |
| committee_ad_hoc |  Kommission, die für eine einzelne Aufgabe eingesetzt und nach deren Erledigung wieder aufgelöst wird, im Unterschied zur ständigen Kommission.  |
| | [act:enum/group_type/committee_ad_hoc](act:enum/group_type/committee_ad_hoc) |
| parliamentary_group |  Parlamentsfraktion.  |
| | [act:enum/group_type/parliamentary_group](act:enum/group_type/parliamentary_group) |
| council_bureau |  Organ, das den Geschäftsgang eines Rates leitet, unabhängig von der örtlichen Bezeichnung (Büro, Ratsleitung, Geschäftsleitung). Wird für den Legislativ- wie für den Exekutivrat verwendet; die örtliche Benennung wird im Label festgehalten.  |
| | [act:enum/group_type/council_bureau](act:enum/group_type/council_bureau) |
| council_presidency |  Präsidium eines Rates, für den Legislativ- wie für den Exekutivrat.  |
| | [act:enum/group_type/council_presidency](act:enum/group_type/council_presidency) |
| council_executive |  Regierung / Exekutive als Gesamtorgan (z.B. Bundesrat, Regierungsrat, Stadtrat / Gemeinderat).  |
| | [act:enum/group_type/council_executive](act:enum/group_type/council_executive) |
| department |  Departement, z.B. Departement oder Direktion.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Amt, häufig die Einheit unterhalb des Departements.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| committee_extraparliamentary |  Kommission, die in der Regel von der Regierung eingesetzt wird, um die Verwaltung fachlich zu beraten und deren Geschäfte vorzuberaten; einzelne verfügen darüber hinaus über eigene Entscheidbefugnisse. Sie unterscheidet sich von einer parlamentarischen Kommission durch Zusammensetzung und Rechtsgrundlage: Ihre Mitglieder sind externe Fachleute und Interessenvertreterinnen und -vertreter statt Ratsmitglieder, und sie stützt sich auf das Organisationsrecht von Regierung und Verwaltung statt auf das Parlamentsrecht. Den Typ gibt es auf Bundes- wie auf Kantonsebene (z.B. die Wettbewerbskommission des Bundes; im Kanton Waadt die commissions extraparlementaires). Eine Kommission, deren Mitglieder Ratsmitglieder sind, fällt auch dann nicht unter diesen Wert, wenn sie bei der Exekutive angesiedelt ist; sie wird als Kommission oder Ad-hoc-Kommission mit dem Exekutivrat als übergeordneter Gruppe erfasst.  |
| | [act:enum/group_type/committee_extraparliamentary](act:enum/group_type/committee_extraparliamentary) |
| interest_group |  Interessengruppe zu einem Sachthema: sowohl die parlamentarische Gruppe, in der sich Ratsmitglieder fraktionsübergreifend zusammenschliessen, als auch die Interessengruppe aus der Zivilgesellschaft.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| oversight_body |  Unabhängiges Aufsichts- oder Prüforgan, das dem beaufsichtigten Organ nicht angehört und ihm nicht berichtet (z.B. Eidgenössische Finanzkontrolle EFK und kantonale Finanzkontrollen, Aufsichtsbehörde über die Bundesanwaltschaft AB-BA, Eidgenössische Finanzmarktaufsicht FINMA, Ombudsstellen).  |
| | [act:enum/group_type/oversight_body](act:enum/group_type/oversight_body) |
| council_secretariat |  Verwaltungseinheit, die einen Rat bedient, unabhängig von der örtlichen Bezeichnung (Parlamentsdienste, Ratssekretariat, Staats-, Kantons-, Standes-, Stadt- oder Gemeindekanzlei). Wird für den Legislativ- wie für den Exekutivrat verwendet: Die Staatskanzlei ist die Stabsstelle des Exekutivrates, die Parlamentsdienste sind jene des Legislativrates.  |
| | [act:enum/group_type/council_secretariat](act:enum/group_type/council_secretariat) |
| court |  Gericht / Judikative auf jeder Ebene (z.B. Bundesgericht, Kantonsgericht, Bezirksgericht).  |
| | [act:enum/group_type/court](act:enum/group_type/court) |
| association |  Verein.  |
| | [act:enum/group_type/association](act:enum/group_type/association) |
| petition_carrier |  Petitionsträger.  |
| | [act:enum/group_type/petition_carrier](act:enum/group_type/petition_carrier) |
| university |  Universität oder Bildungseinrichtung als ausgelagerter Träger öffentlicher Aufgaben.  |
| | [act:enum/group_type/university](act:enum/group_type/university) |
| other |  Anderer Gruppentyp, nicht durch Standardkategorien abgedeckt.  |
| | [act:enum/group_type/other](act:enum/group_type/other) |







</div>
\newpage

# Mitgliedschaften (Memberships)

Das Membership-Schema bildet die Beziehung zwischen Personen und Gruppen ab und ist das zentrale Bindeglied im Akteur-Schema.

- **Abgrenzung zu Interessenbindungen (`InterestLink`):** `Membership` erfasst die *formale Zugehörigkeit* einer Person zu einer Gruppe innerhalb des Akteur-Schemas (z. B. Partei-, Kommissions- oder Parlamentsmitgliedschaft). Interessenbindungen und Interessenkonflikte zu Organisationen *ausserhalb* des Schemas sind bewusst davon getrennt und werden über `InterestLink` abgebildet (siehe folgendes Kapitel).
- **Referenz mit Momentaufnahme statt Einbettung (`person_reference`/`group_reference`):** Eine Mitgliedschaft verweist auf Person und Gruppe und hält dabei deren wichtigste Identifikationsmerkmale zum Zeitpunkt der Verknüpfung fest. So bleibt der Eintrag historisch korrekt, auch wenn sich Person oder Gruppe später ändern.
- **Aktivität explizit oder abgeleitet (`is_active`):** Ob eine Mitgliedschaft aktiv ist, kann explizit über `is_active` gesetzt oder aus der zeitlichen Gültigkeit abgeleitet werden. Ist `is_active` nicht gesetzt, ergibt sich die Aktivität aus `valid_from`/`valid_through`.
- **Mitgliedschaft ≠ Stimmrecht (`authorized_to_vote`):** Das Stimmrecht wird getrennt von der Mitgliedschaft geführt – typischerweise `false` bei Ersatzmitgliedern (ausser im Einsatz), Beobachtenden, dem Sekretariat und Gästen.
- **Rolle als kontrolliertes Vokabular mit Freitext-Option (`role_type`):** Die Rolle in der Gruppe (z. B. Mitglied, Präsidium, Stellvertretung) wird über ein kontrolliertes Vokabular (`RoleEnum`) angegeben; für nicht abgedeckte Rollen dient der Wert `other` mit einer freien Bezeichnung.
- **Wahlkreis an der Mitgliedschaft statt an der Person (`electoral_district`):** Der Wahlkreis beschreibt nicht die Person, sondern das Mandat – dieselbe Person kann über die Zeit oder auf verschiedenen föderalen Ebenen aus unterschiedlichen Wahlkreisen gewählt sein. `ElectoralDistrict` führt deshalb keine eigene zeitliche Gültigkeit, sondern erbt die `valid_from`/`valid_through` der umschliessenden Mitgliedschaft. Für die Identifikation sind die LINDAS-Ressourcen der Schweizer Raumeinheiten vorgesehen (siehe `global_uri`).



## Klasse: Membership 


_Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die eine formale Zugehörigkeit darstellt (z.B. Parteimitglied, Kommissionsmitglied, Parlamentarier/in). Im Unterschied zu InterestLink, der externe Interessenbindungen und Interessenkonflikte zu Organisationen ausserhalb des Akteur-Schemas abbildet._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält.  |
| group_reference | 1 <br/> [GroupReference](#GroupReference) | Kurzreferenz auf eine Gruppe, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) | Link zum Wahlbezirk.  |
| role_type | 0..1 <br/> [RoleType](#RoleType) | Rolle der Person in der Mitgliedschaft oder Funktion.  |
| authorized_to_vote | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Person in der Gruppe stimmberechtigt ist. Typischerweise false für Ersatzmitglieder (wenn nicht im Einsatz), Beobachter/innen, Sekretär/innen und Gäste.  |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Mitgliedschaft derzeit aktiv ist. Kann `valid_from`/`valid_through` ergänzen oder ersetzen. Wenn nicht gesetzt, wird die Aktivität aus den zeitlichen Gültigkeitsfeldern abgeleitet.  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [memberships](#memberships) | range | [Membership](#Membership) |



















</div>



## Klasse: RoleType 


_Rolle einer Person in einer Mitgliedschaft oder Funktion (z.B. Mitglied, Präsident/in, Stellvertreter/in). Wenn eine Rolle im vorgeschlagenen RoleEnum-Vokabular nicht enthalten ist, kann der Wert 'other' verwendet werden; in diesem Fall soll im Slot `role_label` eine beschreibende Bezeichnung angegeben werden. Die Bezeichnung kann auch verwendet werden, wenn eine spezifische Rollenbezeichnung nötig ist, selbst wenn in `role_type_enum` bereits ein passender semantischer Wert vorhanden ist; bei `role_type_enum = other` soll sie angegeben werden._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](#RoleEnum) | Rolle der Person in der Mitgliedschaft oder Funktion.  |
| role_label | * <br/> [MultilingualValue](#MultilingualValue) | Spezifische Rollenbezeichnung. Dieses Feld kann verwendet werden, wenn eine konkrete Rollenbezeichnung benötigt wird, auch wenn in `role_type_enum` bereits ein passender semantischer Wert vorhanden ist; bei `role_type_enum = other` soll diese Bezeichnung angegeben werden. Die Bezeichnung wird mit der Sprache erfasst, in der sie publiziert wird; wird sie in mehreren Sprachen publiziert, wird pro Sprache ein Eintrag erfasst.  |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [role_type_enum](#role_type_enum)
- [role_label](#role_label)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [role_type](#role_type) | range | [RoleType](#RoleType) |




##### Regeln


- Wenn der Rollentyp 'other' ist, muss eine beschreibende Bezeichnung angegeben werden.

















</div>

## Enum: RoleEnum 




_Rollen, die eine Person im Rahmen einer Mitgliedschaft haben kann._




<div data-search-exclude markdown="1">

URI: [act:RoleEnum](https://ld.ech.ch/schema/0294/actors/RoleEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| member |  Gewöhnliches Mitglied (Standard).  |
| president |  Präsident oder Vorsitzender der Gruppe.  |
| deputy |  Stellvertretung oder Vize.  |
| other |  Andere Rolle; für eine beschreibende Bezeichnung role_label verwenden.  |







</div>



## Klasse: ElectoralDistrict 


_Wahlkreis oder Wahlregion, die einer Mitgliedschaft zugeordnet ist. Die zeitliche Gültigkeit wird von der umschliessenden Mitgliedschaft übernommen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Für IRI-Referenzen sollen die LINDAS-Ressourcen verwendet werden. Die IRI für die verschiedenen Verwaltungsebenen der Schweizer Raumeinheiten sind bei LINDAS zu finden: https://ld.admin.ch/country/CHE. Unter den Links im Abschnitt schema:containsPlace kann die gewünschte Ebene gefunden werden. Beispiele für die einzelnen Verwaltungsebenen: - Land - Schweiz: https://ld.admin.ch/country/CHE - Kanton - Aargau: https://ld.admin.ch/canton/19 - Bezirk - Brig: https://ld.admin.ch/district/2301 - Gemeinde - Versoix: https://ld.admin.ch/municipality/6644 <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [electoral_district](#electoral_district) | range | [ElectoralDistrict](#ElectoralDistrict) |



















</div>
\newpage

# Interessenbindungen (Interest Links)

Das InterestLink-Schema erfasst Interessenbindungen, Interessenkonflikte und Verflechtungen von Personen mit Organisationen. Es orientiert sich an den Transparenzanforderungen für Parlamentsmitglieder gemäss [Bundesversammlung – Interessenbindungen](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Abgrenzung zu Mitgliedschaften (`Membership`):** `InterestLink` bildet Bindungen zu Organisationen *ausserhalb* des Akteur-Schemas ab (Interessenkonflikte, Politikfinanzierung) – im Unterschied zur formalen Zugehörigkeit *innerhalb* des Schemas, die über `Membership` erfasst wird.
- **Obligatorische Klassifikation (`interest_type`):** Jede Bindung wird zwingend nach Art eingeordnet (berufliche Tätigkeit, politische Ämter, Verein), angelehnt an die Offenlegungskategorien der Bundesversammlung.
- **Organisation über UID referenzierbar (`organization_uid`):** Ist die Organisation im UID-Register erfasst, wird sie über ihre UID referenziert – das ermöglicht Auswertungen, z. B. mit NOGA-Codes. Erfasst wird das Austauschformat von eCH-0108, also `CHE` gefolgt von neun Ziffern ohne Trennzeichen (`CHE106063525`). Für Organisationen ohne UID stehen `organization_name`/`organization_address` bereit; die Rechtsform folgt einem kontrollierten Vokabular (`LegalFormEnum`).
- **Umfang und Entschädigung (`is_paid`, `committee`, `function_role`):** Neben Gremium und Funktion innerhalb der Organisation wird explizit festgehalten, ob die Position bezahlt ist – ein zentraler Transparenzaspekt.





## Klasse: InterestLink 


_Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation ausserhalb des Akteur-Schemas._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).  |
| organization_name | 0..1 <br/> [String](#String) | Name der Organisation oder des Unternehmens.  |
| organization_uid | 0..1 <br/> [String](#String) | UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.  |
| organization_address | 0..1 <br/> [String](#String) | Adresse der Organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Tätigkeit bezahlt ist.  |
| committee | 0..1 <br/> [String](#String) | Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung).  |
| function_role | 0..1 <br/> [String](#String) | Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in).  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [organization_uid](#organization_uid)
- [organization_name](#organization_name)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |
| [Person](#Person) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |














### Beispiele
#### Beispiel: Eigene Gesellschaft, operativ geführt

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Burkart Advisory GmbH, Baden
legal_form: '0107'
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Beispiel: Unbezahltes Präsidium einer politischen Allianz

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Allianz Sicherheit Schweiz, Baden
legal_form: '0109'
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Beispiel: Verwaltungsratsmandat in einer Holding

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Birchmeier Holding AG, Döttingen
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Beispiel: Verwaltungsratsmandat in einer Immobiliengesellschaft

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Bovida Real Estate AG, Baar
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Beispiel: Mitgliedschaft in einem Branchenverband

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: '0109'
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Beispiel: Stiftungsratsmandat mit UID der Organisation

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
organization_uid: CHE109810537
legal_form: '0110'
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```
#### Beispiel: Beiratsmandat ohne Organstellung

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Stiebel Eltron AG, Lupfig
legal_form: '0106'
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Beispiel: Ehrenamtliche Mitwirkung im Trägerverein eines Grossprojekts

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Verein Landesausstellung Svizra27, Aarau
legal_form: '0109'
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Beispiel: Präsidium eines Wirtschaftsverbands

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: '0109'
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Beispiel: Präsidium einer Bundespartei

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FDP.Die Liberalen
legal_form: '0109'
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Beispiel: Verwaltungsratsmandat in einem Technologieunternehmen

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: ELCA Group SA, Lausanne
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```






</div>

## Enum: InterestTypeEnum 




_Typen von Interessenbindungen (Interessenkonflikte, Politikfinanzierung)._




<div data-search-exclude markdown="1">

URI: [act:InterestTypeEnum](https://ld.ech.ch/schema/0294/actors/InterestTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| professional_activity |  Berufliche Tätigkeit ausserhalb des politischen Mandats (z.B. Anstellung, selbstständige Tätigkeit, Beratungsmandate, Verwaltungsratsmandate in Privatunternehmen).  |
| | [act:enum/interest_type/professional_activity](act:enum/interest_type/professional_activity) |
| political_office |  Politisches Amt oder Mandat auf anderen föderalen Ebenen oder in anderen Körperschaften (z.B. Mitgliedschaft in kantonalen/kommunalen Parlamenten, Regierungsrat, ausserparlamentarische Kommission).  |
| | [act:enum/interest_type/political_office](act:enum/interest_type/political_office) |
| association |  Mitgliedschaft in Vereinen, Verbänden oder Interessenorganisationen (z.B. Branchenverbände, Berufsverbände, Lobbyorganisationen, Stiftungen, gemeinnützige Vereine).  |
| | [act:enum/interest_type/association](act:enum/interest_type/association) |







</div>

## Enum: LegalFormEnum 




_Rechtsformen gemäss der Codeliste des Bundesamts für Statistik auf der I14Y-Plattform, konform zu eCH-0108 (Unternehmensstammdaten und Unternehmensregister). Siehe https://register.ld.admin.ch/i14y/concept/legalForm_




<div data-search-exclude markdown="1">

URI: [act:LegalFormEnum](https://ld.ech.ch/schema/0294/actors/LegalFormEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| 0101 |  Einzelunternehmen. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0101](https://register.ld.admin.ch/i14y/concept/legalForm/0101) |
| 0103 |  Kollektivgesellschaft (KlG). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0103](https://register.ld.admin.ch/i14y/concept/legalForm/0103) |
| 0104 |  Kommanditgesellschaft (KmG). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0104](https://register.ld.admin.ch/i14y/concept/legalForm/0104) |
| 0105 |  Kommanditaktiengesellschaft (KmAG). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0105](https://register.ld.admin.ch/i14y/concept/legalForm/0105) |
| 0106 |  Aktiengesellschaft (AG). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0106](https://register.ld.admin.ch/i14y/concept/legalForm/0106) |
| 0107 |  Gesellschaft mit beschränkter Haftung (GmbH). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0107](https://register.ld.admin.ch/i14y/concept/legalForm/0107) |
| 0108 |  Genossenschaft. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0108](https://register.ld.admin.ch/i14y/concept/legalForm/0108) |
| 0109 |  Verein. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0109](https://register.ld.admin.ch/i14y/concept/legalForm/0109) |
| 0110 |  Stiftung. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0110](https://register.ld.admin.ch/i14y/concept/legalForm/0110) |
| 0111 |  Zweigniederlassung eines ausländischen Unternehmens. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0111](https://register.ld.admin.ch/i14y/concept/legalForm/0111) |
| 0113 |  Besondere Rechtsform. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0113](https://register.ld.admin.ch/i14y/concept/legalForm/0113) |
| 0114 |  Kommanditgesellschaft für kollektive Kapitalanlagen (KmGK). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0114](https://register.ld.admin.ch/i14y/concept/legalForm/0114) |
| 0115 |  Investmentgesellschaft mit variablem Kapital (SICAV). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0115](https://register.ld.admin.ch/i14y/concept/legalForm/0115) |
| 0116 |  Investmentgesellschaft mit festem Kapital (SICAF). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0116](https://register.ld.admin.ch/i14y/concept/legalForm/0116) |
| 0117 |  Institut des öffentlichen Rechts. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0117](https://register.ld.admin.ch/i14y/concept/legalForm/0117) |
| 0118 |  Nichtkaufmännische Prokura. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0118](https://register.ld.admin.ch/i14y/concept/legalForm/0118) |
| 0119 |  Haupt von Gemeinderschaft. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0119](https://register.ld.admin.ch/i14y/concept/legalForm/0119) |
| 0151 |  Zweigniederlassung. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0151](https://register.ld.admin.ch/i14y/concept/legalForm/0151) |
| 0220 |  Verwaltungseinheit des Bundes. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0220](https://register.ld.admin.ch/i14y/concept/legalForm/0220) |
| 0221 |  Verwaltungseinheit des Kantons. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0221](https://register.ld.admin.ch/i14y/concept/legalForm/0221) |
| 0222 |  Verwaltungseinheit des Bezirks. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0222](https://register.ld.admin.ch/i14y/concept/legalForm/0222) |
| 0223 |  Verwaltungseinheit der Gemeinde. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0223](https://register.ld.admin.ch/i14y/concept/legalForm/0223) |
| 0224 |  Andere öffentlich-rechtliche Verwaltungseinheit. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0224](https://register.ld.admin.ch/i14y/concept/legalForm/0224) |
| 0230 |  Einrichtung des öffentlichen Rechts des Bundes. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0230](https://register.ld.admin.ch/i14y/concept/legalForm/0230) |
| 0231 |  Einrichtung des öffentlichen Rechts des Kantons. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0231](https://register.ld.admin.ch/i14y/concept/legalForm/0231) |
| 0232 |  Einrichtung des öffentlichen Rechts des Bezirks. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0232](https://register.ld.admin.ch/i14y/concept/legalForm/0232) |
| 0233 |  Einrichtung des öffentlichen Rechts der Gemeinde. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0233](https://register.ld.admin.ch/i14y/concept/legalForm/0233) |
| 0234 |  Andere Einrichtung des öffentlichen Rechts. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0234](https://register.ld.admin.ch/i14y/concept/legalForm/0234) |
| 0302 |  Einfache Gesellschaft. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0302](https://register.ld.admin.ch/i14y/concept/legalForm/0302) |
| 0312 |  Betriebsstätte oder Schweizer Vertretung eines ausländischen Unternehmens. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0312](https://register.ld.admin.ch/i14y/concept/legalForm/0312) |
| 0327 |  Ausländisches öffentliches Unternehmen. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0327](https://register.ld.admin.ch/i14y/concept/legalForm/0327) |
| 0328 |  Ausländische öffentliche Verwaltung. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0328](https://register.ld.admin.ch/i14y/concept/legalForm/0328) |
| 0329 |  Internationale Organisation. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0329](https://register.ld.admin.ch/i14y/concept/legalForm/0329) |
| 0355 |  Übrige Genossenschaft. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0355](https://register.ld.admin.ch/i14y/concept/legalForm/0355) |
| 0361 |  Trust. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0361](https://register.ld.admin.ch/i14y/concept/legalForm/0361) |
| 0362 |  Fonds. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0362](https://register.ld.admin.ch/i14y/concept/legalForm/0362) |
| 0441 |  Ausländisches Unternehmen. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0441](https://register.ld.admin.ch/i14y/concept/legalForm/0441) |
| 0571 |  Rechtsform unbestimmt oder unbekannt. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0571](https://register.ld.admin.ch/i14y/concept/legalForm/0571) |







</div>
\newpage

# Geteilte Elemente

## Reference Classes

`PersonReference` und `GroupReference` werden verwendet, um Personen bzw. Gruppen **lokal** innerhalb einer anderen Entität zu referenzieren. Neben dem eigentlichen Link zur vollständigen Entität werden dabei nur die relevanten Informationen zum **Zeitpunkt der Verknüpfung** gespeichert – es müssen also nicht alle Informationen einer Person oder Gruppe bei jeder Erwähnung wiederholt werden.

Ein Beispiel: Eine Motion verweist auf die Person, die sie eingereicht hat. Zusätzlich zum Link auf die vollständige Personen-Entität speichert die Motion lokal Informationen wie die politische Partei oder die Rolle der Person **zum Zeitpunkt der Einreichung**. Wechselt die Person später die Partei oder die Rolle, bleibt die Information in der Motion dennoch korrekt und unveränderlich.

Dies dient drei Zwecken:

- **Nützliche lokale Daten** ohne aufwändige Abfragen der vollständigen Entität
- **Keine Redundanz**, da nicht alle Informationen bei jeder Erwähnung wiederholt werden müssen
- **Implizite Versionierung**, da die lokale Referenz unverändert bleibt, auch wenn sich die verknüpfte Entität später ändert

Anders als eine Entität ist eine Referenz nicht aus sich heraus identifiziert – sie benennt bloss eine identifizierte Entität. Deshalb ist die `global_uri` hier nicht obligatorisch: Verlangt wird nur, dass mindestens eine der beiden Angaben `local_id` oder `global_uri` gesetzt ist. Ein System, das von der referenzierten Entität nur die lokale Id kennt, gibt diese an; sie wird innerhalb derselben Lieferung aufgelöst. Über die Lieferung hinaus verweist die `global_uri`.



## Klasse: PersonReference 


_Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Ermöglicht historische Korrektheit auch wenn sich die Person später ändert. Die referenzierte Person wird über `local_id` oder `global_uri` bezeichnet; mindestens eines von beiden ist erforderlich._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Obligatorischer Kurzname zur Identifikation der Person innerhalb der Organisation (z.B. mit Geburtsjahr zur Unterscheidung von Personen mit gleichem Namen).  |
| label_long | 0..1 <br/> [String](#String) | Optionaler langer Anzeigename mit akademischen Titeln und vollständigem amtlichem Namen (z.B. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> [String](#String) | Name des Gremiums zum Zeitpunkt der Verknüpfung.  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator der referenzierten Entität. Er wird innerhalb derselben Lieferung aufgelöst. <br/><br/>Vererbung: [HasReferenceIdentification](#HasReferenceIdentification) |
| global_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Die eindeutige, global gültige URI der referenzierten Entität. Im Unterschied zu einer local_id ist sie auch über die Lieferung hinaus auflösbar. <br/><br/>Vererbung: [HasReferenceIdentification](#HasReferenceIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasReferenceIdentification](#HasReferenceIdentification) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [local_id](#local_id)
- [global_uri](#global_uri)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |
| [InterestLink](#InterestLink) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |



















</div>



## Klasse: GroupReference 


_Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Die referenzierte Gruppe wird über `local_id` oder `global_uri` bezeichnet; mindestens eines von beiden ist erforderlich. Eine `local_id` wird innerhalb derselben Lieferung aufgelöst, eine `global_uri` auch darüber hinaus._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abkürzung (kann mehrsprachig sein).  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator der referenzierten Entität. Er wird innerhalb derselben Lieferung aufgelöst. <br/><br/>Vererbung: [HasReferenceIdentification](#HasReferenceIdentification) |
| global_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Die eindeutige, global gültige URI der referenzierten Entität. Im Unterschied zu einer local_id ist sie auch über die Lieferung hinaus auflösbar. <br/><br/>Vererbung: [HasReferenceIdentification](#HasReferenceIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasReferenceIdentification](#HasReferenceIdentification) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [local_id](#local_id)
- [global_uri](#global_uri)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [parent_groups](#parent_groups) | range | [GroupReference](#GroupReference) |
| [Membership](#Membership) | [group_reference](#group_reference) | range | [GroupReference](#GroupReference) |



















</div>

## Mehrfach benutzte Klassen

Eine Adresse wird in `street_address`, `postal_code`, `postal_locality` und `country` geschrieben und kann über `address_uri` ins Amtliche Gebäudeadressverzeichnis von swisstopo verweisen. Die letzte Zahl dieser URI ist die EGAID, der eidgenössische Gebäudeadressidentifikator; `https://geo.ld.admin.ch/location/address/101009806` bezeichnet damit „Rue de Genève 17, 1003 Lausanne" als amtlich geführte Gebäudeadresse.

`address_uri` ist optional. Die geschriebene Adresse allein ist zulässig, vorzuziehen ist aber der Verweis über die EGAID: Sie ist ein eindeutiger Identifikator und über die Zeit stabil, während Strassennamen geändert, Gemeinden fusioniert und Postleitzahlen neu zugeschnitten werden.

Um zur EGAID zu gelangen, kann man die [Such-API von geo.admin.ch](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Rue+de+Gen%C3%A8ve+17+1003+Lausanne&type=locations&origins=address) benutzen oder mit dem [Amtlichen Verzeichnis der Gebäudeadressen](https://www.swisstopo.admin.ch/de/amtliches-verzeichnis-der-gebaeudeadressen) abgleichen. Erfasst wird das Ergebnis in `address_uri`.



## Klasse: Address 


_Eine Adresse mit einem Typ (z.B. Privatadresse, Geschäftsadresse) und einem Wert._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](#AddressTypeEnum) | Typ der Adresse.  |
| address_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | URI der Adresse aus dem Amtlichen Gebäudeadressverzeichnis (swisstopo). Der letzte Abschnitt der URI ist die EGAID, der eidgenössische Gebäudeadressidentifikator dieses Verzeichnisses. Beispiel einer gültigen URI: https://geo.ld.admin.ch/location/address/101904050 — dasselbe Verzeichnis ist als Kartenlayer einsehbar unter https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis  |
| street_address | 0..1 <br/> [String](#String) | Strassenadresse.  |
| postal_code | 0..1 <br/> [Integer](#Integer) | Postleitzahl.  |
| postal_locality | 0..1 <br/> [String](#String) | Ort.  |
| country | 0..1 <br/> [String](#String) | ISO 3166-1 alpha-2 Ländercode.  |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [postal_locality](#postal_locality)
- [address_uri](#address_uri)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [addresses](#addresses) | range | [Address](#Address) |
| [Group](#Group) | [addresses](#addresses) | range | [Address](#Address) |














### Beispiele
#### Beispiel: swiss politicians Beat Jans 1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```
#### Beispiel: groups Konsumenteninformation und -schutz 1

```yaml
address_type: businessAddress
address_uri: https://geo.ld.admin.ch/location/address/101009806
street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
  585
postal_code: '1001'
postal_locality: Lausanne
country: CH

```






</div>

## Enum: AddressTypeEnum 




_Adresstypen._




<div data-search-exclude markdown="1">

URI: [act:AddressTypeEnum](https://ld.ech.ch/schema/0294/actors/AddressTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| privateAddress |  Privatadresse.  |
| businessAddress |  Geschäftsadresse.  |
| localAddress |  Lokaladresse.  |







</div>



## Klasse: Contact 


_Kontaktinformation einer Person mit Angabe eines Typs (z.B. E-Mail, LinkedIn) und eines Werts._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| contact_type | 1 <br/> [ContactTypeEnum](#ContactTypeEnum) | Typ der Kontaktinformation.  |
| value | 1 <br/> [String](#String) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.  |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [contacts](#contacts) | range | [Contact](#Contact) |
| [Group](#Group) | [contacts](#contacts) | range | [Contact](#Contact) |



















</div>
\newpage

# Anhang A – Referenzen & Bibliographie

Angegeben ist jeweils die Version, gegen die dieser Standard erarbeitet wurde.

## Standards der Fachgruppe „Politische Geschäfte"

| | |
|---|---|
|[eCH-0292]|eCH-0292: Metaprozesse zu politischen Geschäften, Version 1.0.0 – gemeinsame Datenelemente: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|[eCH-0293]|eCH-0293: Öffentlicher Ratsbetrieb, Version 1.0.0: [https://www.ech.ch/de/ech/ech-0293](https://www.ech.ch/de/ech/ech-0293)|
|[eCH-0295]|eCH-0295: Parlamentarische Geschäfte, Version 1.0.0: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|[eCH-0296]|eCH-0296: Erlasse und Gesetzestexte, Version 1.0.0: [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|[eCH-0297]|eCH-0297: Öffentliche Konsultationen, Version 1.0.0: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Weitere eCH-Standards

| | |
|---|---|
|[eCH-0011]|eCH-0011: Datenstandard Personendaten, Version 9.0.0 (Genehmigt, 27.07.2023). Grundlage der Namenstypen in `NameTypeEnum` (`personNameData`): [https://www.ech.ch/de/ech/ech-0011/9.0.0](https://www.ech.ch/de/ech/ech-0011/9.0.0)|
|[eCH-0108]|eCH-0108: Datenstandard: Unternehmensstammdaten und Unternehmensregister, Version 6.0.0 (Genehmigt, 04.04.2024). Definiert das Austauschformat der UID (`organization_uid`) und ist der Standard, zu dem die Rechtsform-Codeliste in `LegalFormEnum` konform ist: [https://www.ech.ch/de/ech/ech-0108/6.0.0](https://www.ech.ch/de/ech/ech-0108/6.0.0)|

## Codelisten und weitere Quellen

| | |
|---|---|
|[I14Y]|Interoperabilitätsplattform des Bundesamts für Statistik. Bezugsquelle der Codelisten für Rechtsform (`LegalFormEnum`) und Geschlecht (`GenderCodeEnum`): [https://www.i14y.admin.ch](https://www.i14y.admin.ch)|
|[LINDAS]|Linked Data Service der Schweizerischen Bundesverwaltung. Identifikatoren der Schweizer Raumeinheiten (Land, Kanton, Bezirk, Gemeinde) für `spatial` und `ElectoralDistrict`: [https://ld.admin.ch](https://ld.admin.ch)|
|[NOGA]|Allgemeine Systematik der Wirtschaftszweige des Bundesamts für Statistik. Ermöglicht Auswertungen über die UID referenzierter Organisationen.|
|[Wikidata]|Freie Wissensdatenbank. Entitäts-IRI (`http://www.wikidata.org/entity/Q…`) in `wikidata_uri`: [https://www.wikidata.org](https://www.wikidata.org)|
|[ISO 639-1]|ISO (International Organization for Standardization). Sprachcodes, verwendet im Slot `language` von `MultilingualValue`.|
|[schema.org]|Gemeinsames Vokabular für strukturierte Daten. Quelle mehrerer `slot_uri`-Zuordnungen: [https://schema.org](https://schema.org)|
|[LinkML]|Modellierungssprache, in der dieser Standard definiert ist: [https://linkml.io](https://linkml.io)|

