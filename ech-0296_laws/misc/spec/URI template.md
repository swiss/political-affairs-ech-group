# URI Template

URI = "base_uri" +


## Base URI

base_uri = "namespace" + "collection" + "year" "naturalidentifier"

required

### namespace
"https://fedlex.admin.ch/eli/"          // 
"https://fedlex.data.admin.ch/eli"      // Linked Data

### year 


## collection
“fga” for the Federal gazette
“oc” for the Official compilation
“cc” for the Classified compilation
“cons” for the publication of consultation procedures
“treaty” for the publication of international treaties
“fgae” for documents published as “reference” in texts published in the fga
“oce” for documents published as “reference” in texts published in the oc
“cce” for documents published as "reference” in texts published in the cc
“oe” for reports about ordonnances
“mog” for documents published in the Militäramtsblatt (MA) / Feuille officielle militaire (FOM) / Foglio ufficiale militare (FUM)
“ogc” for documents published in the Swiss Official Gazette of Commerce (SOGC)
“oldcc” for documents published in the Revised Compilation of Federal Acts and Ordinances 1848-1947 (BS)
“ob” for documents published in the Official Bulletin of the Federal Assembly
“cmog” for documents published in the Sammelband des Militäramtsblattes (SMA) / Recueil de la Feuille officielle militaire (RFM) / Raccolta del Foglio ufficiale militare (RFM)



## Document Structure
URI = "base_uri" + `/{subdivision type}_{id of the subdivision}/{subdivision type}_{id of the subdivision}`
