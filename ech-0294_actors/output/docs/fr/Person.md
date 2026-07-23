

## Classe: Person 


_Une personne avec des identifiants, des noms, des adresses, des nationalités et des professions._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](String.md) | Nom d'affichage court et obligatoire permettant d'identifier la personne au sein de l'organisation (p. ex. avec l'ajout de l'année de naissance afin de distinguer des personnes portant le même nom). Recommandé : PersonOfficialName combiné avec PersonCallFirstName.  |
| label_long | 0..1 <br/> [String](String.md) | Nom d'affichage long et facultatif comprenant les titres académiques et le nom officiel complet (p. ex. « Dr. Maria Muster-Beispiel »).  |
| birth_year | 0..1 <br/> [Integer](Integer.md) | Année de naissance. À utiliser uniquement lorsqu'aucune `birthDate` complète n'est disponible.  |
| birth_date | 0..1 <br/> [Date](Date.md) | Date de naissance exacte si disponible et publique. Ce champ prime sur le champ `birthYear`.  |
| death_date | 0..1 <br/> [Date](Date.md) | Date de décès exacte.  |
| picture | 0..1 <br/> [Uri](Uri.md) | Lien vers une image (de préférence : PNG, puis JPG, puis GIF).  |
| names | * <br/> [Name](Name.md) | Noms de la personne avec type et valeur.  |
| addresses | * <br/> [Address](Address.md) | Adresses avec type (privée, professionnelle, locale).  |
| language_proficiencies | * <br/> [LanguageProficiency](LanguageProficiency.md) | Compétences linguistiques de la personne.  |
| citizenships | * <br/> [Citizenship](Citizenship.md) | Nationalités de la personne.  |
| genders | * <br/> [Gender](Gender.md) | Sexe de la personne.  |
| occupations | * <br/> [Occupation](Occupation.md) | Métiers ou professions de la personne.  |
| trainings | * <br/> [Training](Training.md) | Formations ou éducations de la personne. Directive : n'indiquer en principe que la qualification la plus élevée obtenue.  |
| contacts | * <br/> [Contact](Contact.md) | Informations de contact (e-mail, site web, réseaux sociaux). Directive : l'e-mail est quasi obligatoire et devrait toujours être fourni lorsqu'il est disponible.  |
| interest_links | * <br/> [InterestLink](InterestLink.md) | Collection de liens d'intérêts.  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [persons](persons.md) | range | [Person](Person.md) |














### Exemples
#### Exemple : Person-swiss_politicians_Beat_Jans

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

```
#### Exemple : Person-swiss_politicians_Gerri_Beretta-Piccoli

```yaml
local_id: 1269
global_uri: https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
label: Gerri Beretta-Piccoli
names:
- name_type: PersonFirstName
  value: Fausto
- name_type: PersonCallFirstName
  value: Gerri
- name_type: PersonOfficialName
  value: Beretta-Piccoli

```
#### Exemple : Person-swiss_politicians_Cristina_Bozzi-Brunel

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
#### Exemple : Person-swiss_politicians_Alois_Arnold_1965

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
#### Exemple : Person-swiss_politicians_Alois_Arnold_1981

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






</div>