---
search:
  boost: 5.0
---

# Slot: subheading 


_Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006)._




<div data-search-exclude markdown="1">



URI: [laws:subheading](https://ld.ech.ch/schema/0296/laws/subheading)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Book](Book.md) | Buch-Ebene eines Erlasses (akn:book) |  no  |
| [Title](Title.md) | Titel-Ebene eines Erlasses (akn:title) |  no  |
| [Part](Part.md) | Teil-Ebene eines Erlasses (akn:part) |  no  |
| [Chapter](Chapter.md) | Kapitel-Ebene eines Erlasses (akn:chapter) |  no  |
| [Subchapter](Subchapter.md) | Unterkapitel-Ebene (akn:subchapter) |  no  |
| [Section](Section.md) | Abschnitt-Ebene (akn:section) |  no  |
| [Subsection](Subsection.md) | Unterabschnitt-Ebene (akn:subsection) |  no  |
| [Level](Level.md) | Transparente Strukturebene (akn:level) |  no  |
| [Article](Article.md) | Ein Artikel, die primäre legislative Einheit (akn:article) |  no  |
| [Subdivision](Subdivision.md) | Ein Unterabschnitt in einem Artikel, der zusammengehörige Absätze gruppiert (... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MixedText](MixedText.md) |
| Domäne von | [Book](Book.md), [Title](Title.md), [Part](Part.md), [Chapter](Chapter.md), [Subchapter](Subchapter.md), [Section](Section.md), [Subsection](Subsection.md), [Level](Level.md), [Article](Article.md), [Subdivision](Subdivision.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: subheading
annotations:
  description_de:
    tag: description_de
    value: 'Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role=''reference''
      kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading
      pro Element (FLX-HD-006).

      '
  xml_element:
    tag: xml_element
    value: akn:subheading
  schematron_rules:
    tag: schematron_rules
    value: 'FLX-HD-006: max one subheading; FLX-XF-005: fedlex:role=''reference''
      only allowed on subheading

      '
description: 'Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role=''reference''
  kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro
  Element (FLX-HD-006).

  '
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:subheading
rank: 1000
domain_of:
- Book
- Title
- Part
- Chapter
- Subchapter
- Section
- Subsection
- Level
- Article
- Subdivision
range: MixedText

```
</details></div>