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
  * Staatskalender (?)
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
   



* Use Case
  * Alle mögliche Anzeige und offizielen Namen (für Websites)
    * Beispiele:
      * UR: [Alois (1981) Arnold](https://www.ur.ch/behoerdenmitglieder/6447)
      * UR: [Alois (1965) Arnold](https://www.ur.ch/behoerdenmitglieder/6370)
      * TI: [Fausto "Gerri" Beretta-Piccoli](https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269)
  * Übernahme von den Wahlsystemen ( Politische Rechte ).
  * Überlegungen zu Datenschutz / Öffentlichkeitsrecht -> ein Kapitel mit Analyse des IST Zustands / Rechtsgrundlage oder Toolkit ?
  * [Ersetzung der privaten Wohnadresse als Identifikator der Urheber von Volksinitiativen](https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20243425)
  * [Verhinderung der Pflicht zur Veröffentlichung der Wohnadressen von Parlamentsmitgliedern](https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20233913)
  * Gleiche Namen im Parlament: https://www.parlament.ch/centers/documents/de/gleichnamige-ratsmitglieder.pdf

  
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
