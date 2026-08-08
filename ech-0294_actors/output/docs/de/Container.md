

## Klasse: Container 


_Container für politische Akteure, Gruppen und Beziehungen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| persons | * <br/> [Person](Person.md) | Sammlung von Personen.  |
| groups | * <br/> [Group](Group.md) | Sammlung von Gruppen.  |
| memberships | * <br/> [Membership](Membership.md) | Sammlung von Mitgliedschaften.  |
| interest_links | * <br/> [InterestLink](InterestLink.md) | Sammlung von Interessenbindungen.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |

















### Beispiele
#### Beispiel: interest links

```yaml
# Interessenbindungen Beispieldaten
# Quelle: https://api.openparldata.ch/v1/interests/ und parlament.ch
# Bodies: CHE (Bundesversammlung), ZH (Kanton Zürich), BS (Kanton Basel-Stadt),
#         261 (Stadt Zürich), 351 (Stadt Bern)

global_uri: act:interest_links_example
interest_links:
  
  # --- Thierry Burkart (FDP, Ständerat AG) ---
  
  # Berufliche Tätigkeit: eigene Beratungsfirma
  - global_uri: act:il_burkart_001
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: professional_activity
    organization_name: Burkart Advisory GmbH, Baden
    legal_form: "0107"  # GmbH
    committee: Geschäftsleitung
    function_role: Geschäftsführer
    is_paid: true

  # Verwaltungsrat AG
  - global_uri: act:il_burkart_002
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: professional_activity
    organization_name: Birchmeier Holding AG, Döttingen
    legal_form: "0106"  # AG
    committee: Verwaltungsrat
    function_role: Mitglied
    is_paid: true

  # Verwaltungsrat AG
  - global_uri: act:il_burkart_003
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: professional_activity
    organization_name: Bovida Real Estate AG, Baar
    legal_form: "0106"  # AG
    committee: Verwaltungsrat
    function_role: Mitglied
    is_paid: true

  # Verwaltungsrat IT-Unternehmen
  - global_uri: act:il_burkart_004
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: professional_activity
    organization_name: ELCA Group SA, Lausanne
    legal_form: "0106"  # AG
    committee: Verwaltungsrat
    function_role: Mitglied
    is_paid: true

  # Verbandspräsidium (bezahlt)
  - global_uri: act:il_burkart_005
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: association
    organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
    legal_form: "0109"  # Verein
    committee: Zentralvorstand
    function_role: Präsident
    is_paid: true

  # Parteiamt
  - global_uri: act:il_burkart_006
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: association
    organization_name: FDP.Die Liberalen
    legal_form: "0109"  # Verein
    committee: Vorstand
    function_role: Präsident
    is_paid: true

  # Stiftung (ehrenamtlich)
  - global_uri: act:il_burkart_007
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: association
    organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
    organization_uid: CHE-109.810.537
    legal_form: "0110"  # Stiftung
    committee: Stiftungsrat
    function_role: Vizepräsident
    is_paid: false

  # Beirat Unternehmen
  - global_uri: act:il_burkart_008
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: professional_activity
    organization_name: Stiebel Eltron AG, Lupfig
    legal_form: "0106"  # AG
    committee: Beirat
    function_role: Beirat
    is_paid: true

  # Branchenverband (bezahlt)
  - global_uri: act:il_burkart_009
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: association
    organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
    legal_form: "0109"  # Verein
    committee: Vorstand
    function_role: Mitglied
    is_paid: true

  # Ehrenamtliche Vereinsmitgliedschaften
  - global_uri: act:il_burkart_010
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: association
    organization_name: Allianz Sicherheit Schweiz, Baden
    legal_form: "0109"  # Verein
    committee: Vorstand
    function_role: Präsident
    is_paid: false

  - global_uri: act:il_burkart_011
    person_reference:
      global_uri: http://www.wikidata.org/entity/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: association
    organization_name: Verein Landesausstellung Svizra27, Aarau
    legal_form: "0109"  # Verein
    committee: Vorstand
    function_role: Mitglied
    is_paid: false
```
#### Beispiel: swiss politicians

```yaml
global_uri: act:swiss_politicians_example
persons:
  - local_id: 4032
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
      - training_type: "3223"  # Master Universität, ETH (inklusive Lizentiat / Diplom)
        value: dipl. nat. ETH
    contacts:
      - contact_type: email
        value: beat.jans@admin.ch
      - contact_type: contact_website
        value: http://www.beat-jans.ch

  # Use case Namensverwendung — Gleichnamigkeit: Im Kanton Uri gibt es zwei
  # verschiedene Personen mit identischem Namen "Alois Arnold". Das obligatorische
  # `label` unterscheidet sie über das Geburtsjahr.
  - local_id: 6447
    global_uri: https://www.ur.ch/behoerdenmitglieder/6447
    label: Alois Arnold (1981)
    birth_year: 1981
    names:
      - name_type: PersonFirstName
        value: Alois
      - name_type: PersonOfficialName
        value: Arnold

  - local_id: 6370
    global_uri: https://www.ur.ch/behoerdenmitglieder/6370
    label: Alois Arnold (1965)
    birth_year: 1965
    names:
      - name_type: PersonFirstName
        value: Alois
      - name_type: PersonOfficialName
        value: Arnold

  # Use case Namensverwendung — Rufname: Der amtliche Vorname ("Fausto",
  # PersonFirstName) weicht vom Rufnamen ("Gerri", PersonCallFirstName) ab;
  # das `label` nutzt den Rufnamen.
  - local_id: 1269
    global_uri: "https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269"
    label: Gerri Beretta-Piccoli
    names:
      - name_type: PersonFirstName
        value: Fausto
      - name_type: PersonCallFirstName
        value: Gerri
      - name_type: PersonOfficialName
        value: Beretta-Piccoli

  # Use case Namensverwendung — Namensvariante (echter Fall, Stadtparlament
  # Winterthur): "Cristina Bozzi-Brunel" wird auch als "Cristina Brunel" geführt.
  # Der amtliche Doppelname und der Ledigname werden über typisierte `names`
  # abgebildet (Annahme: Brunel = Ledigname/PersonOriginalName — bei Bedarf anpassen).
  - local_id: 280958
    global_uri: https://parlament.winterthur.ch/behoerdenmitglieder/280958
    label: Cristina Bozzi-Brunel
    names:
      - name_type: PersonFirstName
        value: Cristina
      - name_type: PersonOfficialName
        value: Bozzi-Brunel
      - name_type: PersonOriginalName
        value: Brunel

  - local_id: 72c7232be92944e3876f3b6723824ff9
    global_uri: https://stadtrat.bern.ch/de/mitglieder/detail.php?gid=72c7232be92944e3876f3b6723824ff9
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
      - training_type: "3223"  # Master Universität, ETH (inklusive Lizentiat / Diplom)
        value: MLaw
# memberships:
#   - global_uri: https://data-example.parlament.ch/membership/4032-bundesrat
#     valid_from: 2023-12-13
#     person_reference:
#       local_id: 4032
#       global_uri: https://www.admin.ch/de/beat-jans
#       label: Beat Jans
#     group_reference:
#       global_uri: ch:FC
#       label: Bundesrat
#     electoral_district:
#       global_uri: ch:canton/12
```
#### Beispiel: groups

```yaml
# Beispiele für Gruppen und Organe unterschiedlicher Typen. Alle Einträge sind
# echte Fälle. `global_uri` ist der Identifikator und muss die einzelne Gruppe
# eindeutig bezeichnen; verwendet wird durchwegs die gruppenspezifische Adresse
# der publizierenden Stelle. Eine Übersichtsseite über alle Fraktionen oder
# Kommissionen taugt dafür nicht, weil sie mehrere Gruppen bezeichnet.
# `local_id` ist die Kennung von openparldata.ch.
#
# `group_type` zeigt das Zusammenspiel von kontrolliertem Vokabular
# (`group_type_enum`) und der herkunftsspezifischen Bezeichnung (`label`):
# Der Enum-Wert macht Gruppen über Kantone und Ebenen hinweg vergleichbar,
# das Label bewahrt die Benennung der publizierenden Stelle.
global_uri: act:groups_example
groups:
  # Interessengruppe (parlamentarische Gruppe) der Bundesversammlung. Der Name
  # ist dreisprachig geführt, die Beschreibung nur auf Französisch — beides
  # bildet `MultilingualValue` mit je einem Eintrag pro vorhandener Sprache ab.
  # `global_uri` ist hier fiktiv: Die Bundesversammlung publiziert ihre
  # parlamentarischen Gruppen nur gesammelt in einem PDF und vergibt je Gruppe
  # keine eigene Adresse. So saehe ein eindeutiger Identifikator in ihrem
  # Namensraum aus; das Sammel-PDF steht als `landing_page`.
  - local_id: 6627
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
          L'intergroupe parlementaire « Information et défense des consommateurs » réunit toutes
          les sensibilités politiques. Cet intergroupe a pour mission d'informer et de
          sensibiliser les élu·e·s aux questions relatives à la défense des consommateur·rice·s
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
        street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale 585
        postal_code: "1001"
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

  # Zivilgesellschaftliche Organisation — sie führt das Sekretariat der
  # vorangehenden parlamentarischen Gruppe. Anders als parlamentarische Organe
  # ist sie eine im Handelsregister eingetragene juristische Person und trägt
  # deshalb eine `organization_uid`. Diese ist der stabilere Identifikator als
  # die Webadresse, die sich bei jedem Relaunch ändern kann.
  - global_uri: https://www.frc.ch/
    organization_uid: CHE-106.063.525
    legal_form: "0109"  # Verein
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

  # Gemeindeparlament — `spatial` verweist auf die BFS-Gemeindenummer
  - local_id: 700
    global_uri: https://www.stadt.sg.ch/home/verwaltung-politik/demokratie-politik/stadtparlament.html
    label:
      - value: Stadtparlament St. Gallen
        language: de
    group_type:
      group_type_enum: council_legislative
      label:
        - value: Parlament (Legislativrat)
          language: de
    spatial: https://ld.admin.ch/municipality/3203

  # Ausserparlamentarische Kommission des Bundes: Ihre Mitglieder sind externe
  # Fachleute, nicht Ratsmitglieder, und sie stützt sich auf das
  # Organisationsrecht von Regierung und Verwaltung. Sie gehört zu den wenigen
  # Kommissionen mit eigener Entscheidbefugnis; der Regelfall ist die blosse
  # Beratung der Verwaltung.
  - global_uri: https://www.weko.admin.ch/
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

  # Kantonsparlament — dient den beiden folgenden Einträgen als übergeordnete
  # Gruppe (`parent_groups`).
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

  # Exekutivrat desselben Kantons, mit der Staatskanzlei als nachgeordneter
  # Stabsstelle. Das Paar zeigt, dass `council_secretariat` nicht auf das
  # Parlament beschränkt ist: Die Staatskanzlei bedient die Exekutive, die
  # Parlamentsdienste die Legislative — derselbe Typ, verschiedene Räte.
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
        label: Regierungsrat Basel-Stadt

  # Die beiden Kantonalparteien, deren Namen die weiter unten stehende Fraktion
  # trägt. Ihr Verweis geht auf die jeweilige Bundespartei — jede föderale Ebene
  # ist eine eigene Gruppe, und hier liegt eine echte Über-/Unterordnung vor.
  # Die Bundesparteien sind nicht mitgeliefert: Weil sie ausserhalb der
  # Lieferung liegen, werden sie über `global_uri` benannt und nicht über eine
  # `local_id`, die nur innerhalb der Lieferung auflösbar wäre.
  - global_uri: https://bs.die-mitte.ch/
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

  - global_uri: https://www.evp-bs.ch/
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

  # Fraktion im Grossen Rat Basel-Stadt. Sie zeigt den typenübergreifenden
  # Verweis über `parent_groups`: Eine Fraktion (`parliamentary_group`) gehört
  # zum Parlament (`council_legislative`), also zu einem anderen `group_type`.
  # Dass die Fraktion von zwei Parteien getragen wird, ist demgegenüber keine
  # Über-/Unterordnung und darum kein `parent_groups`-Verweis. Der Name der
  # Fraktion benennt beide Parteien; der Verweis auf sie bleibt bewusst offen.
  - local_id: 1266
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

  # Kantonsparlament — übergeordnete Gruppe der folgenden Kommission
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

  # Ständige Kommission mit gebräuchlicher Abkürzung. Erst der Verweis auf den
  # Kantonsrat macht sichtbar, welchem Rat sie zugehört — der Typ allein sagt
  # das nicht.
  - local_id: 3
    global_uri: https://ar.ch/kantonsrat/kommissionen/staendige-kommissionen-des-kantonsrates/geschaeftspruefungskommission/
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
        label: Kantonsrat Appenzell Ausserrhoden

  # Ratsbüro
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
        label: Grosser Rat Basel-Stadt

  # Delegation in ein interkantonales Gremium
  - local_id: 5000
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
          La Commission interparlementaire de contrôle détention pénale est composée de 18
          députés issus des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel, Vaud et
          Valais.
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






</div>