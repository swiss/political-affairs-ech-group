

## Klasse: References 


_Benannte Referenz-Definitionen für das gesamte Dokument (akn:references). Definiert Organisationen, Rollen und andere Entitäten, die über Anker (@href='#eId') referenziert werden._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](AnchorRef.md) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| tlc_organizations | * <br/> [TLCOrganization](TLCOrganization.md) | Benannte Organisations-Referenzen im Dokument (akn:TLCOrganization). |
| tlc_roles | * <br/> [TLCRole](TLCRole.md) | Benannte Rollen-Referenzen im Dokument (akn:TLCRole). |
| tlc_references | * <br/> [TLCReference](TLCReference.md) | Generische benannte Referenzen im Dokument (akn:TLCReference). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActMeta](ActMeta.md) | [references_ref](references_ref.md) | range | [References](References.md) |














### Beispiele
#### Beispiel References: bgoe 1 1

```yaml
references_ref:
  source: '#ch.bk'
  tlc_organizations:
  - eId: ch.bk
    href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
    show_as: Bundeskanzlei
  tlc_roles:
  - eId: publisher
    href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
    show_as: Editeur
  - eId: rightsHolder
    href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
    show_as: Détenteur des droits
  tlc_references:
  - name_attr: language
    href: http://publications.europa.eu/resource/authority/language/DEU
    show_as: de
  - name_attr: format
    href: https://fedlex.data.admin.ch/vocabulary/user-format/xml
    show_as: xml

```
#### Beispiel References: sr101 1 1

```yaml
references_ref:
  source: '#ch.bk'
  tlc_organizations:
  - eId: ch.bk
    href: https://fedlex.data.admin.ch/vocabulary/legal-institution/2
    show_as: Bundeskanzlei
  tlc_roles:
  - eId: publisher
    href: http://data.legilux.public.lu/resource/ontology/jolux#publisher
    show_as: Editeur
  - eId: rightsHolder
    href: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
    show_as: Détenteur des droits
  tlc_references:
  - name_attr: language
    href: http://publications.europa.eu/resource/authority/language/DEU
    show_as: de
  - name_attr: format
    href: https://fedlex.data.admin.ch/vocabulary/user-format/xml
    show_as: xml

```






</div>