# Organe im Politischen Prozess

Ein Organ in dieser Definition ist einzig eine ansammlung von Personen. (Ohne weitere semantik.) Sie wird typisiert um die Art des Organs zu bestimmen.

## Allgemeinen Felder eines Organes

group
- id (local)
- globalid / tb named
- type  enum -> Partei, Liste, Arbeitsgruppe 
- type_label: "" (Wenn spezifischer lokaler Namen vorhanden.)
- valid_from:
- valid_to:
- name: (Mehrsprachig)
- abrev: (Mehrsprachig)
- description:
- landing_page:
- parent_group: (0:n)   Um die Parteienhierarchie (CH-Kanton-Gemeinde) abzubilden, aber auch um Parteien an ein Parlament zu binden.
- municipality_nr: gemeindenummer / agvch nummer
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
-> Gemeinden, Kantone und Bund
Zu diskutieren mit Hans-Peter

* Partei
* Liste (kann Teil einer Partei sein, oder nicht)
* Fraktion 
* Parlamentskomission
* Delegation
* Ad-Hoc Komission
* Arbeitsgruppen
* Interessengruppen

* Departemente
* Ausserparlementarische Komissionen

## Parteien
- url_statutes: (optional)
- party_color: (optional)

## Memberships

- 

## 
