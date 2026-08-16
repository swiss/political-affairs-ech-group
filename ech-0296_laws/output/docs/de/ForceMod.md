

## Klasse: ForceMod 


_Eine Änderung der Rechtskraft: ein Erlass oder ein Teil davon tritt in Kraft, ausser Kraft, wird aufgeschoben, verlängert, neu erlassen oder für verfassungswidrig erklärt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| mod_type | 0..1 <br/> [String](String.md)&nbsp;or&nbsp;<br />[ModTypeEnum](ModTypeEnum.md) | Art der Änderung (@type); die zulässigen Werte sind die von Akoma Ntoso. |
| period | 0..1 <br/> [String](String.md) | Die Zeitgruppe, in der die Änderung gilt (@period). |
| mod_sources | * <br/> [ModSource](ModSource.md) | Die Stellen, welche die Änderung bewirken (akn:source). |
| mod_destinations | * <br/> [ModDestination](ModDestination.md) | Die Stellen, die geändert werden (akn:destination). |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement. <br/><br/>Vererbung: [Modification](Modification.md) |






















</div>