

## Klasse: FormatType 


_Halter für akn:FRBRformat: ein @value (typischerweise 'xml') plus das optionale Erweiterungsattribut fedlex:generator (FLX-XF-002)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| value | 0..1 <br/> [String](String.md) | Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet. |
| fedlex_generator | 0..1 <br/> [String](String.md) | Fedlex-Erweiterungsattribut fedlex:generator bei akn:FRBRformat[@value='xml']. Identifiziert das Werkzeug, das die XML-Datei erzeugt hat. Nur bei FRBRformat erlaubt (FLX-XF-002).  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRManifestation](FRBRManifestation.md) | [frbr_format](frbr_format.md) | range | [FormatType](FormatType.md) |



















</div>