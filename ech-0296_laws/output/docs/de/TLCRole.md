

## Klasse: TLCRole 


_Eine benannte Rolle als Referenz im Dokument (akn:TLCRole). Beispiele: publisher, rightsHolder._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| href | 0..1 <br/> [String](String.md) | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| show_as | 0..1 <br/> [String](String.md) | Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [References](References.md) | [tlc_roles](tlc_roles.md) | range | [TLCRole](TLCRole.md) |














### Beispiele
#### Beispiel TLCRole: sr101 excerpt 1 2

```yaml
tlc_roles:
- eId: rightsHolder
  href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
  show_as: Détenteur des droits

```
#### Beispiel TLCRole: bgoe excerpt 1 2

```yaml
tlc_roles:
- eId: rightsHolder
  href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
  show_as: Détenteur des droits

```
#### Beispiel TLCRole: Role publisher as an anchor

```yaml
tlc_roles:
- eId: publisher
  href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
  show_as: Editeur

```






</div>