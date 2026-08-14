---
search:
  boost: 5.0
---

# Slot: href 


_URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs._



<div data-search-exclude markdown="1">



URI: [laws:href](https://ld.ech.ch/schema/0296/laws/href)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRAuthor](FRBRAuthor.md) | Ein Autoren- oder Rechteinhaber-Eintrag einer FRBR-Entität (akn:FRBRauthor) |  no  |
| [TLCOrganization](TLCOrganization.md) | Eine benannte Organisation als Referenz im Dokument (akn:TLCOrganization) |  no  |
| [TLCRole](TLCRole.md) | Eine benannte Rolle als Referenz im Dokument (akn:TLCRole) |  no  |
| [TLCReference](TLCReference.md) | Eine generische benannte Referenz im Dokument (akn:TLCReference) |  no  |
| [Ref](Ref.md) | Eine Inline-Referenz (akn:ref) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [FRBRAuthor](FRBRAuthor.md), [TLCOrganization](TLCOrganization.md), [TLCRole](TLCRole.md), [TLCReference](TLCReference.md), [Ref](Ref.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| #ch.bk |
| http://data.legilux.public.lu/resource/ontology/jolux#publisher |
| http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder |





## LinkML-Quelle

<details>
```yaml
name: href
annotations:
  description_de:
    tag: description_de
    value: URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen
      URIs.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
description: URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen
  URIs.
examples:
- value: '#ch.bk'
- value: http://data.legilux.public.lu/resource/ontology/jolux#publisher
- value: http://data.legilux.public.lu/resource/ontology/jolux#rightsHolder
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRAuthor
- TLCOrganization
- TLCRole
- TLCReference
- Ref
range: string

```
</details></div>