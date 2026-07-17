---
title: "eCH-0294 Politische Akteure: Personen, Gruppen und Organe"
lang: de
toc: false
---

| **Name**              | **Politische Akteure: Personen, Gruppen und Organe**                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| **eCH-Nummer**        | eCH-0294                                                                                                                   |
| **Kategorie**         | Entwurf                                                                                                                    |
| **Reifegrad**         | Fachgruppen interner Review                                                                                                |
| **Version**           | 0.5                                                                                                                        |
| **Status**            |                                                                                                 |
| **Beschluss am**      |                                                                                                                            |
| **Ausgabedatum**      |                                                                                                                            |
| **Ersetzt Version**   | 0.0                                                                                                                        |
| **Voraussetzungen**   | eCH-0292 (Gemeinsame Datenelemente)                                                                                        |
| **Beilagen**          | -                                                                                                                          |
| **Sprachen**          | Deutsch (Original) - English (Datamodel)                                                                                    |
| **Autoren**           | Fachgruppe politische Geschäfte: Julie Silberstein, Laurence Brandenberger, Daniela Koller, Thomas Roth, Stefan Oderbolz, Fabian Davolio, Orhan Saeedi, Christian Gutknecht, Michael Luggen |
| **Herausgeber / Vertrieb** | Verein eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)                             |

\newpage

# Abstrakt

Der Entwurf eCH-0294 „Politische Akteure: Personen, Gruppen und Organe“ definiert ein einheitliches Datenmodell zur strukturierten Publikation politischer Akteure in der Schweiz. Er umfasst natürliche Personen, politische Gruppen und Organe, Mitgliedschaften zwischen Personen und Gruppen sowie Interessenbindungen. Ziel ist es, föderal übergreifend vergleichbare, maschinenlesbare und nachnutzbare Informationen bereitzustellen, um Transparenz, Nachvollziehbarkeit und Analysefähigkeit politischer Prozesse zu verbessern.

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

## Der Standard eCH-0294 – Politische Akteure

Dieser Standard definiert vier Hauptklassen:

- **Person** – Natürliche Personen im politischen Kontext
- **Group** – Gremien, Parteien, Fraktionen, Räte, Kommissionen, Organisationen etc.
- **Membership** – Verbindung zwischen Personen und Gruppen
- **InterestLink** – Interessenbindungen von Personen

`Membership` ist das zentrale Bindeglied zwischen `Person` und `Group` und hält fest, in welchem Parlament, in welcher Kommission etc. eine Person aktiv ist oder war. `InterestLink` ermöglicht die Beschreibung von Interessenbindungen.
\newpage

# Person

Das Personenschema beschreibt natürliche Personen im politischen Kontext.

- **Stabile Person, zeitlich gültige Merkmale:** Die `Person` selbst trägt keine zeitliche Gültigkeit, ihre Merkmale hingegen schon – Name, Staatsangehörigkeit, Geschlecht, Beruf, Ausbildung und Wahlkreis tragen je eigene `valid_from`/`valid_through`. So bleibt die Identität der Person stabil, während sich einzelne Angaben über die Zeit ändern und die Historie erhalten bleibt (z. B. Namensänderung bei Heirat oder Wechsel des Wahlkreises).
- **Obligatorischer Anzeigename (`label`) neben strukturierten Namen (`names`):** Jede Person hat einen zwingenden Kurznamen, damit auch bei unvollständigen Angaben immer ein Anzeigename vorhanden ist. Empfohlen wird die Kombination aus amtlichem Namen (`PersonOfficialName`) und Rufname (`PersonCallFirstName`), bei Namensgleichheit ergänzt um das Geburtsjahr. `label_long` nimmt zusätzlich akademische Titel auf; die feingliedrige, typisierte Namensstruktur (`names`) ist optional deren Nutzung ist aber angezeigt. In einigen Fällen ist die Benutzung von spezifischen Typen, wie der amtliche Name (`PersonOfficialName`) eine gesetzliche Vorrausetzung.
- **Namenstypen nach amtlicher Systematik:** Die Namenstypen (`NameTypeEnum`) folgen der Registerharmonisierung des BFS bzw. eCH-0011 (u. a. amtlicher Name, angestammter Name, Allianzname, Rufname sowie Varianten für ausländische Ausweise). Damit sind die Namen mit den amtlichen Personenregistern kompatibel, und deren Semantik klar.
- **`birth_year` als datensparsame Alternative zu `birth_date`:** Ist das genaue Geburtsdatum nicht verfügbar oder nicht zur Veröffentlichung bestimmt, kann nur das Geburtsjahr angegeben werden. Liegt ein `birth_date` vor, hat es Vorrang.
- **Mehrfachwerte statt Einzelwerte:** Namen, Staatsangehörigkeiten und Geschlechtsangaben sind als Listen mit zeitlicher Gültigkeit modelliert – etwa für Doppelbürgerschaften, Namensänderungen oder eine sich ändernde Geschlechtsangabe.
- **Harmonisierung über föderale Ebenen (Langzeitziel):** Die Verknüpfung derselben Person über die föderalen Ebenen hinweg ist ein wichtiges Langzeitziel. Der Aufbau einer zentralen Personendatenbank liegt ausserhalb des Auftrags der eCH-Fachgruppe. Da für diesen Zweck bereits eine offene, etablierte Infrastruktur besteht, wird **Wikidata als übergreifender Identifikator empfohlen** (`wikidata_uri`); zusammen mit global eindeutigen Identifikatoren (URIs) lässt sich die Zuordnung so schrittweise über die Systeme hinweg harmonisieren.




## Klasse: Person 


_Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._

__



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
| electoral_district | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) | Link zum Wahlbezirk.  |
| interest_links | * <br/> [InterestLink](#InterestLink) | Sammlung von Interessenbindungen.  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |














### Beispiele
#### Beispiel: Person-swiss_politicians_Beat_Jans

```yaml
local_id: 4032
global_uri: https://data-example.parlament.ch/person/4032
wikidata_uri: https://www.wikidata.org/wiki/Q813067
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
electoral_district:
  district: Basel-Stadt
  valid_from: 2010-01-01

```






</div>



## Klasse: Name 


_Ein Name mit einem Typ (z.B. Rufname, amtlicher Name) und einem Wert und einer zeitlichen Gültigkeit._

__



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




_Kategorien von Namenstypen gemäss eCH-0011 (personNameData) und https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master, URI gemäss I14Y Identifier aber als Klasse und nicht als Attribut. Beschreibungen und Übersetzungen gemäss I14Y._

__



<div data-search-exclude markdown="1">

URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| PersonOfficialName |  Gemäss amtlichen Katalog der Merkmale (Nr. 211) Registerharmonisierung: Name gemäss amtlichen Unterlagen. Der amtliche Name entspricht dem Namen im schweizerischen Zivilstandsregister. Bei ausländischen Personen ohne Zivilstandsereignis in der Schweiz entspricht dieser Name dem Namen im ausländischen Pass oder auf der Identitätskarte (siehe 214 sowie Weisung des SEM über die Bestimmung und Schreibweise der Namen von ausländischen Staatsangehörigen vom 1. Januar 2012. Im Ausnahmefall siehe auch "Name nach Deklaration" (z. B. Asyl), wenn keine amtlichen Dokumente vorliegen). Der amtliche Name kann aus einem oder mehreren Teilen bestehen.  |
| | [https://register.ld.admin.ch/i14y/concept/personOfficialName](https://register.ld.admin.ch/i14y/concept/personOfficialName) |
| PersonOriginalName |  Gemäss amtlichen Katalog der Merkmale (Nr. 212) Registerharmonisierung: Angestammter Name gemäss amtlichen Unterlagen, den eine Person unmittelbar vor ihrer ersten Eheschliessung oder Begründung einer eingetragenen Partnerschaft geführt hat oder, gestützt auf einen Namensänderungsentscheid, als neuen Ledignamen erworben hat (Art. 24 Abs. 2 ZStV, SR 211.112.2).  |
| | [https://register.ld.admin.ch/i14y/concept/personOriginalName](https://register.ld.admin.ch/i14y/concept/personOriginalName) |
| PersonAllianceName |  Gemäss amtlichen Katalog der Merkmale (Nr. 213) Registerharmonisierung: Der Allianzname zeigt die Verbindung von zwei Personen auf, die verheiratet sind oder in einer eingetragenen Partnerschaft leben. Ein bereits verwendeter Allianzname kann nach Auflösung der Ehe oder der Partnerschaft weiterverwendet werden, wenn der amtliche Name bei der Auflösung nicht geändert wurde. Dabei wird dem amtlichen Namen mittels Bindestrich der Ledigname des Partners/der Partnerin oder der eigene Ledigname angehängt. Der Allianzname kann auf Antrag im Pass oder auf der Identitätskarte eingetragen werden.  |
| | [https://register.ld.admin.ch/i14y/concept/personAllianceName](https://register.ld.admin.ch/i14y/concept/personAllianceName) |
| PersonNameOnForeignPassport |  Gemäss amtlichen Katalog der Merkmale (Nr. 214) Registerharmonisierung: Für Personen mit ausländischer Nationalität. Dieser Name entspricht dem Eintrag im Reisepass gemäss der maschinenlesbaren Zone (MRZ) des Reisepasses. Enthält die MRZ abgekürzte Namen oder Vornamen, sind diese möglichst in voller Länge gemäss visuell lesbarer Zone des Ausweispapieres zu erfassen.  |
| | [https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport) |
| PersonAliasName |  Gemäss amtlichen Katalog der Merkmale (Nr. 215) Registerharmonisierung: Name (z. B. Künstler- oder Ordensname), der aufgrund eines bewilligten Gesuchs geführt werden darf. Der Aliasname kann aus einem oder mehreren Teilen (z. B. auch aus Aliasvorname und Aliasname) bestehen.  |
| | [https://register.ld.admin.ch/i14y/concept/personAliasName](https://register.ld.admin.ch/i14y/concept/personAliasName) |
| PersonOtherName |  Gemäss amtlichen Katalog der Merkmale (Nr. 216) Registerharmonisierung: Weitere amtliche Namen gemäss schweizerischen Zivilstandsdokumenten (Art. 24 Abs. 3 ZStV) oder ausländischen Dokumenten, welche weder Familiennamen noch Vornamen sind.  |
| | [https://register.ld.admin.ch/i14y/concept/personOtherName](https://register.ld.admin.ch/i14y/concept/personOtherName) |
| PersonDeclaredForeignerName |  Gemäss amtlichen Katalog der Merkmale (Nr. 217) Registerharmonisierung: Für Personen mit ausländischer Nationalität, die keine offiziellen Dokumente besitzen (hauptsächlich im Asylbereich).  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName) |
| PersonFirstName |  Gemäss amtlichen Katalog der Merkmale (Nr. 221) Registerharmonisierung: Vornamen gemäss Geburtsurkunde oder Zivilstandsregister/Infostar in der aufgeführten Reihenfolge bzw. gemäss ausländischen Ausweispapieren.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstName](https://register.ld.admin.ch/i14y/concept/personFirstName) |
| PersonCallFirstName |  Gemäss amtlichen Katalog der Merkmale (Nr. 222) Registerharmonisierung: Eine Person hat das Recht, aus der Liste ihrer amtlichen Vornamen einen Rufnamen auszuwählen. Der Rufname kann aus einem oder mehreren Vornamen (aus den "amtlichen Vornamen") bestehen.  |
| | [https://register.ld.admin.ch/i14y/concept/personCallFirstName](https://register.ld.admin.ch/i14y/concept/personCallFirstName) |
| PersonFirstNameOnForeignPassport |  Gemäss amtlichen Katalog der Merkmale (Nr. 223) Registerharmonisierung: Für Personen mit ausländischer Nationalität. Zu benutzen in Verbindung mit dem Namen im ausländischen Pass."  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport) |
| PersonDeclaredForeignerFirstName |  Gemäss amtlichen Katalog der Merkmale (Nr. 224) Registerharmonisierung: Für Personen mit ausländischer Nationalität, die keine amtlichen Dokumente besitzen (hauptsächlich im Asylbereich). Zu benutzen in Verbindung mit dem Namen gemäss Deklaration.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName) |







</div>



## Klasse: LanguageProficiency 


_Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die bevorzugte Sprache oder die Muttersprache handelt._

__



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

__



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

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| gender_code | 1 <br/> [GenderCodeEnum](#GenderCodeEnum) | Geschlechtscode. Empfohlene Werte: male, female, diverse .  |
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




_Geschlechtscodes für Personen. Wenn das Geschlecht nicht bekannt ist, soll kein Geschlechtseintrag hinzugefügt werden. Der Code `diverse` soll zusammen mit einer Bezeichnung verwendet werden, um weitere Angaben zum selbst deklarierten Geschlecht bereitzustellen._

__



<div data-search-exclude markdown="1">

URI: [act:GenderCodeEnum](https://ld.ech.ch/schema/0294/actors/GenderCodeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| male |  Männlich. |
| |  |
| female |  Weiblich. |
| |  |
| diverse |  Divers / nicht-binär. |
| |  |







</div>



## Klasse: Occupation 


_Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Codes, ob die Position bezahlt ist, und der zeitlichen Gültigkeit._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Position bezahlt ist.  |
| occupation_code | 0..1 <br/> [String](#String) | ISCO-19 Code der Tätigkeit.  |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| organization_uid | 0..1 <br/> [String](#String) | UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen UID-Register (uid.admin.ch).  |
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
#### Beispiel: Occupation-swiss_politicians_Beat_Jans_Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>



## Klasse: Training 


_Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B. Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19 Codes und der zeitlichen Gültigkeit._

__



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

__



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
| |  |







</div>



## Klasse: ElectoralDistrict 


_Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitlicher Gültigkeit._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| district | 1 <br/> [String](#String) | Wahlkreis oder Wahlregion.  |
| valid_from | 0..1 <br/> [Date](#Date) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](#HasTemporalValidity) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [electoral_district](#electoral_district) | range | [ElectoralDistrict](#ElectoralDistrict) |














### Beispiele
#### Beispiel: ElectoralDistrict-swiss_politicians_Beat_Jans_1

```yaml
district: Basel-Stadt
valid_from: 2010-01-01

```






</div>

\newpage

# Gruppen und Organe (Groups)

Das Group-Schema bildet politische Gruppen, Organisationen und Körperschaften ab.

- **Ein generisches Modell statt vieler Spezialklassen:** Parlamente, Parteien, Fraktionen, Kommissionen, Departemente, Gerichte und zivilgesellschaftliche Organisationen werden alle als *eine* Klasse `Group` abgebildet und über `group_type` unterschieden. Das hält das Modell einfach und ohne Schemaänderung erweiterbar – Legislative, Exekutive, Judikative und Zivilgesellschaft sind damit gleichermassen abbildbar.
- **Gruppen und Sub-Gruppen über `parent_groups`:** Untergeordnete Gruppen verweisen auf ihre übergeordnete Gruppe – z. B. eine Kommission des Ständerats, eine Subkommission innerhalb einer Kommission, eine Kantonalpartei unter ihrer Mutterpartei oder eine Behörde innerhalb einer Direktion. Die Hierarchie entsteht so aus diesen Verweisen statt aus einer festen Ebenenstruktur. Sie bleibt meist innerhalb desselben `group_type`; typenübergreifende und mehrfache Verweise sind aber möglich (z. B. eine Fraktion, die zugleich auf ihr Parlament und ihre Partei verweist).
- **Zeitliche Gültigkeit auch für Gruppen:** Über `valid_from`/`valid_through` lassen sich z. B. nur während einer Legislatur bestehende Kommissionen oder Umbenennungen und Fusionen von Parteien abbilden.



## Klasse: Group 


_Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](#GroupType) | Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Benennung und Beschreibung der Gruppierung wird über `label` gemacht.  |
| label | 1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abkürzung (kann mehrsprachig sein).  |
| description | * <br/> [MultilingualValue](#MultilingualValue) | Kurze Beschreibung der Gruppierung.  |
| landing_page | 0..1 <br/> [Uri](#Uri) | Website mit weiteren Informationen.  |
| parent_groups | * <br/> [Uriorcurie](#Uriorcurie) | Übergeordnete Gruppe. Zum Beispiel die Mutterpartei zu Kantonalparteien, oder zur Beschreibung der Hierarchie in der Exekutive. Auch zur Verknüpfung von Subkommissionen mit Kommissionen oder Fraktionen mit Parlament und Partei. (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament und Fraktion → Partei.)  |
| spatial | 0..1 <br/> [String](#String) | Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land). Formate: Gemeinde: ld.admin.ch/municipality/1234, Kanton: ld.admin.ch/canton/23, Bund: ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](#Contact) | Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.  |
| addresses | * <br/> [Address](#Address) | Adressen mit Typ (privat, geschäftlich, lokal).  |
| statutes_url | 0..1 <br/> [String](#String) | URL zu Parteistatuten (PDF oder Webseite; optional für Parteien).  |
| party_color | 0..1 <br/> [String](#String) | Parteifarbe als Hexadezimalwert (optional für Parteien, z.B. "#FF0000").  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
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



















</div>



## Klasse: GroupType 


_Art der Gruppe (z.B. Partei, Kommission, Parlament, Departement)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| group_type_enum | 0..1 <br/> [GroupTypeEnum](#GroupTypeEnum) | Link zum kontrollierten Vokabular für Gruppentypen.  |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [group_type](#group_type) | range | [GroupType](#GroupType) |



















</div>

## Enum: GroupTypeEnum 




_Typen politischer Gruppen und Organisationen._

__



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
| parliament |  Parlament auf Bundes-, Kantons- oder Gemeindeebene (z.B. Bundesversammlung, Nationalrat, Ständerat, Grosser Rat, Kantonsrat, Gemeindeparlament).  |
| | [act:enum/group_type/parliament](act:enum/group_type/parliament) |
| delegation |  Delegation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| commission |  Kommission (ständig oder ad-hoc), einschliesslich Aufsichtskommissionen (z.B. GPK), Sachkommissionen, Parlamentarische Untersuchungskommissionen (PUK) und Rechnungsprüfungskommissionen.  |
| | [act:enum/group_type/commission](act:enum/group_type/commission) |
| faction |  Parlamentsfraktion.  |
| | [act:enum/group_type/faction](act:enum/group_type/faction) |
| parliamentary_bureau |  Parlamentsbüro.  |
| | [act:enum/group_type/parliamentary_bureau](act:enum/group_type/parliamentary_bureau) |
| presidency |  Präsidium des Parlaments.  |
| | [act:enum/group_type/presidency](act:enum/group_type/presidency) |
| government |  Regierung / Exekutive als Gesamtorgan (z.B. Bundesrat, Regierungsrat, Stadtrat / Gemeinderat).  |
| | [act:enum/group_type/government](act:enum/group_type/government) |
| department |  Departement.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Amt.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| extraparliamentary_commission |  Ausserparlamentarische Kommission mit Regierungsauftrag (z.B. Bankrat der Schweizerischen Nationalbank, FINMA).  |
| | [act:enum/group_type/extraparliamentary_commission](act:enum/group_type/extraparliamentary_commission) |
| interest_group |  Interessengruppe aus der Zivilgesellschaft.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| control_body |  Kontroll- oder Aufsichtsorgan (z.B. Eidgenössische Finanzkontrolle EFK, Aufsichtsbehörde AB-BA).  |
| | [act:enum/group_type/control_body](act:enum/group_type/control_body) |
| parliamentary_services |  Parlamentsdienste.  |
| | [act:enum/group_type/parliamentary_services](act:enum/group_type/parliamentary_services) |
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
- **Referenzen mit Snapshot statt Einbettung (`person_reference`/`group_reference`):** Eine Mitgliedschaft verweist über leichtgewichtige Referenzen auf Person und Gruppe und hält dabei deren wichtigste Identifikationsmerkmale zum Zeitpunkt der Verknüpfung fest. So bleibt der Eintrag historisch korrekt, auch wenn sich Person oder Gruppe später ändern.
- **Aktivität explizit oder abgeleitet (`is_active`):** Ob eine Mitgliedschaft aktiv ist, kann explizit über `is_active` gesetzt oder aus der zeitlichen Gültigkeit abgeleitet werden. Ist `is_active` nicht gesetzt, ergibt sich die Aktivität aus `valid_from`/`valid_through`.
- **Mitgliedschaft ≠ Stimmrecht (`authorized_to_vote`):** Das Stimmrecht wird getrennt von der Mitgliedschaft geführt – typischerweise `false` bei Ersatzmitgliedern (ausser im Einsatz), Beobachtenden, dem Sekretariat und Gästen.
- **Rolle als kontrolliertes Vokabular mit Freitext-Option (`role_type`):** Die Rolle in der Gruppe (z. B. Mitglied, Präsidium, Stellvertretung) wird über ein kontrolliertes Vokabular (`RoleEnum`) angegeben; für nicht abgedeckte Rollen dient der Wert `other` mit einer freien Bezeichnung.



## Klasse: Membership 


_Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die eine formale Zugehörigkeit darstellt (z.B. Parteimitglied, Kommissionsmitglied, Parlamentarier/in). Im Unterschied zu InterestLink, der externe Interessenbindungen und Interessenkonflikte zu Organisationen ausserhalb des Akteur-Schemas abbildet._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.  |
| group_reference | 1 <br/> [GroupReference](#GroupReference) | Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.  |
| role_type | 0..1 <br/> [RoleType](#RoleType) | Rolle der Person in der Mitgliedschaft oder Funktion.  |
| authorized_to_vote | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Person in der Gruppe stimmberechtigt ist. Typischerweise false für Ersatzmitglieder (wenn nicht im Einsatz), Beobachter/innen, Sekretär/innen und Gäste.  |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Mitgliedschaft derzeit aktiv ist. Kann `valid_from`/`valid_through` ergänzen oder ersetzen. Wenn nicht gesetzt, wird die Aktivität aus den zeitlichen Gültigkeitsfeldern abgeleitet.  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
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

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](#RoleEnum) | Rolle der Person in der Mitgliedschaft oder Funktion.  |
| label | 0..1 <br/> [String](#String) | Spezifische Rollenbezeichnung. Dieses Feld kann verwendet werden, wenn eine konkrete Rollenbezeichnung benötigt wird, auch wenn in `role_type_enum` bereits ein passender semantischer Wert vorhanden ist; bei `role_type_enum = other` soll diese Bezeichnung angegeben werden.  |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [role_type_enum](#role_type_enum)
- [label](#label)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [role_type](#role_type) | range | [RoleType](#RoleType) |




##### Regeln


- Wenn der Rollentyp 'other' ist, muss eine beschreibende Bezeichnung angegeben werden.

















</div>

## Enum: RoleEnum 




_Rollen, die eine Person im Rahmen einer Mitgliedschaft haben kann._

__



<div data-search-exclude markdown="1">

URI: [act:RoleEnum](https://ld.ech.ch/schema/0294/actors/RoleEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| member |  Gewöhnliches Mitglied (Standard).  |
| |  |
| president |  Präsident oder Vorsitzender der Gruppe.  |
| |  |
| stellvertreter |  Stellvertreter / Vize.  |
| |  |
| other |  Andere Rolle; für eine beschreibende Bezeichnung role_label verwenden.  |
| |  |







</div>
\newpage

# Interessenbindungen (Interest Links)

Das InterestLink-Schema erfasst Interessenbindungen, Interessenkonflikte und Verflechtungen von Personen mit Organisationen. Es orientiert sich an den Transparenzanforderungen für Parlamentsmitglieder gemäss [Bundesversammlung – Interessenbindungen](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Abgrenzung zu Mitgliedschaften (`Membership`):** `InterestLink` bildet Bindungen zu Organisationen *ausserhalb* des Akteur-Schemas ab (Interessenkonflikte, Politikfinanzierung) – im Unterschied zur formalen Zugehörigkeit *innerhalb* des Schemas, die über `Membership` erfasst wird.
- **Obligatorische Klassifikation (`interest_type`):** Jede Bindung wird zwingend nach Art eingeordnet (berufliche Tätigkeit, politische Ämter, Verein), angelehnt an die Offenlegungskategorien der Bundesversammlung.
- **Organisation über UID referenzierbar (`organization_uid`):** Ist die Organisation im UID-Register erfasst, wird sie über ihre UID (eCH-0097, `CHE-XXX.XXX.XXX`) referenziert – das ermöglicht Auswertungen, z. B. mit NOGA-Codes. Für Organisationen ohne UID stehen `organization_name`/`organization_address` bereit; die Rechtsform folgt einem kontrollierten Vokabular (`LegalFormEnum`).
- **Umfang und Entschädigung (`is_paid`, `committee`, `function_role`):** Neben Gremium und Funktion innerhalb der Organisation wird explizit festgehalten, ob die Position bezahlt ist – ein zentraler Transparenzaspekt.





## Klasse: InterestLink 


_Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation ausserhalb des Akteur-Schemas._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).  |
| organization_name | 0..1 <br/> [String](#String) | Name der Organisation oder des Unternehmens.  |
| organization_uid | 0..1 <br/> [String](#String) | UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen UID-Register (uid.admin.ch).  |
| organization_address | 0..1 <br/> [String](#String) | Adresse der Organisation.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Rechtsform der Organisation. Siehe kontrolliertes Vokabular: https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Gibt an, ob die Position bezahlt ist.  |
| committee | 0..1 <br/> [String](#String) | Gremium innerhalb der Organisation (z.B. Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung).  |
| function_role | 0..1 <br/> [String](#String) | Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in).  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
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
#### Beispiel: InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Allianz Sicherheit Schweiz, Baden
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Beispiel: InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Burkart Advisory GmbH, Baden
legal_form: '0107'
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Stiebel Eltron AG, Lupfig
legal_form: '0106'
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Birchmeier Holding AG, Döttingen
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Verein Landesausstellung Svizra27, Aarau
legal_form: 0109
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Beispiel: InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: 0109
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: 0109
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Bovida Real Estate AG, Baar
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: ELCA Group SA, Lausanne
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FDP.Die Liberalen
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Beispiel: InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: '0110'
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```






</div>

## Enum: InterestTypeEnum 




_Typen von Interessenbindungen (Interessenkonflikte, Politikfinanzierung)._

__



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




_Rechtsformen basierend auf der Codeliste des eidgenössischen UID-Registers (eCH-0098). Siehe https://register.ld.admin.ch/i14y/concept/legalForm_

__



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



## Klasse: PersonReference 


_Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Ermöglicht historische Korrektheit auch wenn sich die Person später ändert._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Obligatorischer Kurzname zur Identifikation der Person innerhalb der Organisation (z.B. mit Geburtsjahr zur Unterscheidung von Personen mit gleichem Namen).  |
| label_long | 0..1 <br/> [String](#String) | Optionaler langer Anzeigename mit akademischen Titeln und vollständigem amtlichem Namen (z.B. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> [String](#String) | Name des Gremiums zum Zeitpunkt der Verknüpfung.  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |
| [InterestLink](#InterestLink) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |



















</div>



## Klasse: GroupReference 


_Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abkürzung (kann mehrsprachig sein).  |
| local_id | 0..1 <br/> [String](#String) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [group_reference](#group_reference) | range | [GroupReference](#GroupReference) |



















</div>

## Mehrfach benutzte Klassen



## Klasse: Address 


_Eine Adresse mit einem Typ (z.B. Privatadresse, Geschäftsadresse) und einem Wert._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](#AddressTypeEnum) | Typ der Adresse.  |
| address_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | URI der Adresse aus dem eidgenössischen Gebäudeadressverzeichnis. Der Layer ist zugänglich unter https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis. Beispiel einer gültigen URI: https://geo.ld.admin.ch/location/address/101904050  |
| street_address | 0..1 <br/> [String](#String) | Strassenadresse.  |
| postal_code | 0..1 <br/> [Integer](#Integer) | Postleitzahl.  |
| postal_locality | 0..1 <br/> [String](#String) | Ort.  |

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
#### Beispiel: Address-swiss_politicians_Beat_Jans_1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```






</div>

## Enum: AddressTypeEnum 




_Adresstypen._

__



<div data-search-exclude markdown="1">

URI: [act:AddressTypeEnum](https://ld.ech.ch/schema/0294/actors/AddressTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| privateAddress |  Privatadresse.  |
| |  |
| businessAddress |  Geschäftsadresse.  |
| |  |
| localAddress |  Lokaladresse.  |
| |  |







</div>



## Klasse: Contact 


_Kontaktinformation einer Person mit Angabe eines Typs (z.B. E-Mail, LinkedIn) und eines Werts._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| contact_type | 1 <br/> [ContactTypeEnum](#ContactTypeEnum) | Typ der Kontaktinformation.  |
| value | 1 <br/> [String](#String) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [contacts](#contacts) | range | [Contact](#Contact) |
| [Group](#Group) | [contacts](#contacts) | range | [Contact](#Contact) |



















</div>
