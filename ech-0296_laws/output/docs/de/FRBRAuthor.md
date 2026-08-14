

## Klasse: FRBRAuthor 


_Ein Autoren- oder Rechteinhaber-Eintrag einer FRBR-Entität (akn:FRBRauthor). @href referenziert die Organisation; @as referenziert die Rolle (beide als Dokument-interne Anker)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| href | 0..1 <br/> [String](String.md) | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| as_role | 0..1 <br/> [AnchorRef](AnchorRef.md) | Rolle des Autors (akn:FRBRauthor/@as), als Anker-Referenz, z.B. '#publisher', '#rightsHolder'.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](FRBRWork.md) | [frbr_authors](frbr_authors.md) | range | [FRBRAuthor](FRBRAuthor.md) |
| [FRBRExpression](FRBRExpression.md) | [frbr_authors](frbr_authors.md) | range | [FRBRAuthor](FRBRAuthor.md) |
| [FRBRManifestation](FRBRManifestation.md) | [frbr_authors](frbr_authors.md) | range | [FRBRAuthor](FRBRAuthor.md) |














### Beispiele
#### Beispiel FRBRAuthor: sr101 excerpt 1 2

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#rightsHolder'

```
#### Beispiel FRBRAuthor: sr101 excerpt 1 1

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#publisher'

```
#### Beispiel FRBRAuthor: bgoe excerpt 1 1

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#publisher'

```
#### Beispiel FRBRAuthor: bgoe excerpt 1 2

```yaml
frbr_authors:
- href: '#ch.bk'
  as_role: '#rightsHolder'

```






</div>