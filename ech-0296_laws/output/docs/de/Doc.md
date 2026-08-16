

## Klasse: Doc 


_Ein beiliegendes Dokument (akn:doc). Das @name-Attribut nennt die Art; Fedlex verwendet 'annex'. Es führt einen eigenen Identifikationsblock, der in den Fedlex-Dateien die URIs des zugehörigen Erlasses wiederholt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| doc_name | 0..1 <br/> [DocNameEnum](DocNameEnum.md) | Art des beiliegenden Dokuments (akn:doc/@name). |
| meta | 0..1 <br/> [ActMeta](ActMeta.md) | Metadaten-Abschnitt des Erlasses (akn:meta). |
| preface_ref | 0..1 <br/> [Preface](Preface.md) | Vorspann des Erlasses (akn:preface). |
| main_body | 0..1 <br/> [MainBody](MainBody.md) | Hauptteil des beiliegenden Dokuments (akn:mainBody). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Component](Component.md) | [doc_ref](doc_ref.md) | range | [Doc](Doc.md) |



















</div>