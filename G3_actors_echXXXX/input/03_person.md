# Person

## Meeting 22.05.2025

* Möglichst übernahme von eCH44 bezüglich Identifikation.

* Amtlicher Name genügend? -> oft ist der Rufname, wie damit umgehen?
* Undefined Name Type als Option?
* Aliase ? -> mit Geburtsdatum
* offizieler Name (eindeutig in der Zeit, für apel)

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
  * Externe Identifikatoren
    * Wikidata? ( Italienisches Parlament )
    * https://metagrid.ch/
    * GND / VIAF
    * SmartVote
    * SelectCandidateSurvey
   
   * Wikidata (Attrib Swiss Parlament ID (ratsid bei wikidata hinzufügen))
   * Wikidata wird der Identifer vom Ratssystem? Problem mit Wikidata als extern organisiert.
   * Wikidata als prefered secondary Identifier.


* Use Case
  * Alle mögliche Anzeige und offizielen Namen (für Websites)
  * 

  
```
Person1: {
ID: ???

label: "Michael Luggen",
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
```


  # Use Case

  -> UseCase 1: 
