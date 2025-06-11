# Person

## Meeting 22.05.2025 / 28.06.2025 / 11.06.2025

* Möglichst übernahme von eCH44 bezüglich Identifikation.

* Amtlicher Name genügend? -> oft ist der Rufname, wie damit umgehen?
* Undefined Name Type als Option?
* Aliase ? -> mit Geburtsdatum
* offizieler Name (eindeutig in der Zeit, für apel)
* Geburtsdatum
* Addresse

* Sprachen
* Staatsbürgerschaften
* Geschlecht (genders) mfd 
* persönliche Website (optional)
* Anzahl Kinder -> offspring
* Zivilstand -> ech44?
* Beschäftigung (experience / occupation)
  * Beruf / Arbeitsgeber (Interessenbindungen?)
  * Armeerang / Zivildienst / Zivilschutz 

### Namenstypen basierend nach eCH11

Typen ausgeschrieben: https://www.bfs.admin.ch/bfs/de/home/register/personenregister/registerharmonisierung/nomenklaturen.assetdetail.24565576.html 
Cross-Check: * Poltische Rechte

* Klare Guideline herausgeben, das der Amtliche Name bevorzugt ist.
* Wenn nicht abgesichert ist, dass es sich um ein einen Amtlichen Namen handelt, kannt auf label zurückgegriffen werden.
* Label braucht gute Erklärung damit es nicht missbraucht wird.


* Id Identifikation
  * AHV? - nice but difficult -> Möglichkeit
  * Ratsinformationssystem -> Möglichkeit (an CH44 orientiert)
    * Legislaturbasierend? verschiedene Ratssystemids vom selben Rat?
    * Rückwirkend IDs vergeben? -> Wikidata - "Datenraum Politik" / ähnlich Metagrid
  * Staatskalender (?)
  * Election:
    * Listennummer / Kandidatennummer
  * Externe Identifikatoren
    * Wikidata? ( Italienisches Parlament )
      * Wikidata; z.B. Swiss Parlament ID: https://www.wikidata.org/wiki/Property:P1307
        * [WikiProject Govdirectory/Switzerland](https://www.wikidata.org/wiki/Wikidata:WikiProject_Govdirectory/Switzerland)
      * Wikidata wird der Identifer vom Ratssystem? Problem mit Wikidata als extern organisiert.
      * Wikidata als prefered secondary Identifier.
 
    * https://metagrid.ch/
    * GND / VIAF
    * SmartVote
    * SelectCandidateSurvey
  

  
```
Person1: {
ID: ???

label: "Michael Luggen", (mandatory)
birthyear: "", (preference but optional)
birthdate: "", (optional)
names: 
[
  { nameType: familyNameOnForeignPassport , 
    value: "",
    validFrom: "",
    validUntil: "",
  },
  { nameType: callName,
    value: "luggi",
  },
]
}
address: [
    addressType: enum ? -> privateAddress, businessAddress, localAddress,
    addressURI: , (super präferenziert)
    streetAddress: ,
    postalCode: ,
    postalLocality: , 
]
```

```
Person1: {
ID: ???

label: "Alois (1920) Arnold", (mandatory)
birthyear: "1920", (preference but optional)
birthdate: "", (optional)
deathdate: "", (optional)
names: 
[
  { nameType: officialLastName , 
    value: "Arnold",
    validFrom: "05-07-1920", (optional)
    validUntil: "01-01-2020",
  },
  { nameType: officialLastName , 
    value: "Meier",
    validFrom: "01-01-2020", (optional)
  },
  { nameType: officialGivenName , 
    value: "Alois",
    validFrom: "1920",
    validUntil: "",
  },
  { nameType: callName,
    value: "luggi",
  },
]
}
```


  # Use Case

* Use Case
  * Alle mögliche Anzeige und offizielen Namen (für Websites) (besonders bei gleichnamigen)
    * Gleiche Namen im Parlament: https://www.parlament.ch/centers/documents/de/gleichnamige-ratsmitglieder.pdf
    * Beispiele:
      * UR: [Alois (1981) Arnold](https://www.ur.ch/behoerdenmitglieder/6447)
      * UR: [Alois (1965) Arnold](https://www.ur.ch/behoerdenmitglieder/6370)
      * TI: [Fausto "Gerri" Beretta-Piccoli](https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269)
  * Übernahme von den Wahlsystemen ( Politische Rechte ).
     * officialName (mandatory) / rufnamen werden bei der BK gesammelt

