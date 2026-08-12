

## Klasse: FRBRName 


_Ein mehrsprachiger Namenseintrag des FRBR-Works (akn:FRBRname). Enthält den offiziellen Langtitel und eine optionale Abkürzung. Ein Eintrag pro Sprache._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| xml_lang | 0..1 <br/> [String](String.md) | XML-Sprachattribut (xml:lang), z.B. 'de', 'fr', 'it', 'rm', 'en'. |
| value | 0..1 <br/> [String](String.md) | Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet. |
| short_form | 0..1 <br/> [String](String.md) | Kurzform-Abkürzung des Gesetzesnamens (@shortForm), z.B. 'BV' (Deutsch), 'Cst.' (Französisch).  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](FRBRWork.md) | [frbr_names](frbr_names.md) | range | [FRBRName](FRBRName.md) |



















</div>