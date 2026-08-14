

## Klasse: TLCOrganization 


_Eine benannte Organisation als Referenz im Dokument (akn:TLCOrganization). Beispiel: die Bundeskanzlei (ch.bk)._




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
| [References](References.md) | [tlc_organizations](tlc_organizations.md) | range | [TLCOrganization](TLCOrganization.md) |














### Beispiele
#### Beispiel TLCOrganization: Declaration of the publishing body

```yaml
tlc_organizations:
- eId: ch.bk
  href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
  show_as: Bundeskanzlei

```






</div>