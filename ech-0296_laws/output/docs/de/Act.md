

## Klasse: Act 


_Das Erlasselement (akn:act). Hauptinhaltselement eines AkomaNtoso-Dokuments. Das @name-Attribut gibt den Erlasstyp an (z.B. 'publicLaw')._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| act_name | 0..1 <br/> [ActTypeEnum](ActTypeEnum.md) | Erlasstyp (@name-Attribut von akn:act), z.B. 'publicLaw'. |
| meta | 0..1 <br/> [ActMeta](ActMeta.md) | Metadaten-Abschnitt des Erlasses (akn:meta). |
| preface_ref | 0..1 <br/> [Preface](Preface.md) | Vorspann des Erlasses (akn:preface). |
| preamble_ref | 0..1 <br/> [Preamble](Preamble.md) | Präambel des Erlasses (akn:preamble). |
| body | 0..1 <br/> [ActBody](ActBody.md) | Hauptteil des Erlasses (akn:body). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FedlexDocument](FedlexDocument.md) | [act_ref](act_ref.md) | range | [Act](Act.md) |



















</div>