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
| [TLCConcept](TLCConcept.md) | Ein Begriff, auf den das Dokument verweist (akn:TLCConcept), etwa ein zeitlic... |  no  |
| [OriginalRef](OriginalRef.md) | Verweis auf die ursprüngliche Fassung des Erlasses (akn:original) |  no  |
| [NoteRef](NoteRef.md) | Verweis auf eine in den Metadaten gehaltene Anmerkung |  no  |
| [ActiveRef](ActiveRef.md) | Verweis auf einen Erlass, den dieses Dokument ändert |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [FRBRAuthor](FRBRAuthor.md), [TLCOrganization](TLCOrganization.md), [TLCRole](TLCRole.md), [TLCReference](TLCReference.md), [Ref](Ref.md), [TLCConcept](TLCConcept.md), [OriginalRef](OriginalRef.md), [NoteRef](NoteRef.md), [ActiveRef](ActiveRef.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
|  |
| #JI |
| #SK |





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
- value: ''
- value: '#JI'
- value: '#SK'
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRAuthor
- TLCOrganization
- TLCRole
- TLCReference
- Ref
- TLCConcept
- OriginalRef
- NoteRef
- ActiveRef
range: string

```
</details></div>