# Organe im Politischen Prozess

Ein Organ in dieser Definition ist einzig eine ansammlung von Personen. (Ohne weitere semantik.) Sie wird typisiert um die Art des Organs zu bestimmen.

## Allgemeinen Felder eines Organes

group
- id (local)
- uri politics.ld.admin.ch/party/1
- type  enum -> Partei, Liste, Arbeitsgruppe 
- type_label: "" (Wenn spezifischer lokaler Namen vorhanden.)
- valid_from:
- valid_to:
- name: (Mehrsprachig)
- abrev: (Mehrsprachig)
- description:
- landing_page:
- parent_group: (0:n)   Um die Parteienhierarchie (CH-Kanton-Gemeinde) abzubilden, aber auch um Parteien an ein Parlament zu binden.
- spatial: gemeindenummer / agvch nummer ld.admin.ch/muncipality/234 ld.admin.ch/canton/2
- contact:
   - type: email, contact_website, linked-in, twitter; # Guideline: E-mail is quasi mandatory and should be always provided.
   - contact: "michael.luggen@...";
- address: 
   - addressType: enum ? -> privateAddress, businessAddress, localAddress,
   - addressURI: , (super präferenziert)
   - streetAddress: ,
   - postalCode: ,
   - postalLocality: , 

## Verschiedene Typen von Organen

* Gruppen, beinhalten Mitglieder ausweisen wollen (Listen)
* Gruppen, Identifizieren (Departemente, Gerichte)

-> Gemeinden, Kantone und Bund
Zu diskutieren mit Hans-Peter

-> Anwendungszweck der Struktur
* Organisation innerhalb eines Parlamentssystems
* Publikation an die öffentichkeit
* Systeme mit Politischen Personen
* Analysen mit Personen welche in Gruppen leben
* Parteiliste global - UNIBE

-> Ausdrücken der Ebene:
* localExtend: Gemeinde Root
* level: canton, municipality (abstract)


Hierarchien innerhalb eines Types: Departement, Amt / Fraktion / Parteien

# Sicht Parlamentsmitglied
* Legislative
  * Parlamente Föderale Ebene
    * Bund (beide Kammern) / Kanton / Gemeinde
  * Delegation
  * Komission
    * Attribute:
       * ständig / (Ad-Hoc) nicht ständige
       * Aufsichtkomissionen / Sachkomissionen
    * Geschäftsprüfungskommission (ständige Aufsichtskommission)
    * PUK (nichständige Aufsichtkommision)
    * Rechnungsprüfungskommission 
  * Fraktion
  * Parlamentsbüro
  * Präsidium des Parlaments
* Exekutive = Regierung / Verwaltung
  * Department
  * Amt
  * Ausserparlementarische Komissionen (z.B. Bankrat)
  * Arbeitsgruppe (Ad-Hoc APK)
* Zivilgesellschaft
   * Partei
   * Liste (kann Teil einer Partei sein, oder nicht) 
   * Interessengruppen
* Andere
  * Kontrollorgane
    * Finanzkontrolle
    * AB-BA
  * Parlamentsdienste
*	(Parteilose und/oder fraktionslose Parlamentsmitglieder)


# Sicht Parlamentsgeschäft
* Legislative
* Exekutive
  * Ausgelagerte Träger öffentlicher Aufgaben
    * Universitäten
* Judikative
  * Gerichte
* Zivilgesellschaft
  * Petitionsträger
  * Verein



## Parteien
Jede Föderaleebene, wird als eigene Gruppierung geführt.
- url_statutes: (optional)
- party_color: (optional)
