

## Klasse: Identification 


_FRBR-Identifikationsblock (akn:identification) mit Work-, Expression- und Manifestations-Beschreibungen. Das @source-Attribut referenziert die verantwortliche Organisation als Dokument-internen Anker (z.B. '#ch.bk')._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](AnchorRef.md) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| frbr_work | 0..1 <br/> [FRBRWork](FRBRWork.md) | FRBR-Work-Ebenen-Beschreibung (akn:FRBRWork). |
| frbr_expression | 0..1 <br/> [FRBRExpression](FRBRExpression.md) | FRBR-Expression-Ebenen-Beschreibung (akn:FRBRExpression). |
| frbr_manifestation | 0..1 <br/> [FRBRManifestation](FRBRManifestation.md) | FRBR-Manifestations-Ebenen-Beschreibung (akn:FRBRManifestation). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActMeta](ActMeta.md) | [identification_ref](identification_ref.md) | range | [Identification](Identification.md) |



















</div>