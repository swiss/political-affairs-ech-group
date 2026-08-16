

## Klasse: Article 


_Ein Artikel, die primäre legislative Einheit (akn:article). Constraints (FLX-ART-*): - akn:num ist obligatorisch (FLX-ART-001) - nur Überschriften-Elemente (num, heading, subheading) sowie akn:paragraph und akn:subdivision sind als Kinder erlaubt (FLX-ART-002) - benötigt eindeutiges @eId (FLX-ART-003)_




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Element-Identifikator. Vom Fedlex-Schematron an jedem Artikel verlangt (FLX-EID-001); kantonale Sammlungen führen ihn nicht durchgehend.  |
| num | 1 <br/> [MixedText](MixedText.md) | Die Artikelnummer (z.B. 'Art. 1'). In jedem Artikel obligatorisch (FLX-ART-001). |
| heading | 0..1 <br/> [MixedText](MixedText.md) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](MixedText.md) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| paragraphs | * <br/> [Paragraph](Paragraph.md) | Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts. |
| subdivisions | * <br/> [Subdivision](Subdivision.md) | Unterabschnitt-Kindelemente (akn:subdivision) innerhalb eines Artikels. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](ActBody.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Book](Book.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Title](Title.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Part](Part.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Chapter](Chapter.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Subchapter](Subchapter.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Section](Section.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Subsection](Subsection.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Level](Level.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Transitional](Transitional.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Proviso](Proviso.md) | [articles](articles.md) | range | [Article](Article.md) |














### Beispiele
#### Beispiel Article: zh idg 9 2

```yaml
articles:
- eId: title_9__art_42
  num:
    inline_content:
    - element_type: TextRun
      text: § 42.
  heading:
    eId: title_9__art_42__heading
    inline_content:
    - element_type: TextRun
      text: Anpassung von Bezeichnungen
  paragraphs:
  - eId: title_9__art_42__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_9__art_42__para_1__content
      content_blocks:
      - …
      - …
  - eId: title_9__art_42__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_9__art_42__para_2__content
      content_blocks:
      - …
      - …

```
#### Beispiel Article: sr101 1 3

```yaml
articles:
- eId: art_3
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Kantone
  paragraphs:
  - eId: art_3/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: Article with a bold article number

```yaml
articles:
- eId: art_1
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Schweizerische Eidgenossenschaft
  paragraphs:
  - eId: art_1/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 3 6

```yaml
articles:
- eId: title_3__art_19
  num:
    inline_content:
    - element_type: TextRun
      text: § 19.
  subheading:
    eId: title_3__art_19__subheading
    inline_content:
    - element_type: TextRun
      text: d. Grenzüberschreitend
  paragraphs:
  - eId: title_3__art_19__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_19__para_1__content
      content_blocks:
      - …
      - …

```
#### Beispiel Article: zh idg 7 4

```yaml
articles:
- eId: title_7__art_33
  num:
    inline_content:
    - element_type: TextRun
      text: § 33.
  heading:
    eId: title_7__art_33__heading
    inline_content:
    - element_type: TextRun
      text: Beauftragte in Gemeinden und Organisationen
  paragraphs:
  - eId: title_7__art_33__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_33__para_1__content
      content_blocks:
      - …
  - eId: title_7__art_33__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_33__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 3 5

```yaml
articles:
- eId: title_3__art_18
  num:
    inline_content:
    - element_type: TextRun
      text: § 18.
  subheading:
    eId: title_3__art_18__subheading
    inline_content:
    - element_type: TextRun
      text: c. Für nicht personenbezogene Zwecke
  paragraphs:
  - eId: title_3__art_18__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_18__para_1__content
      content_blocks:
      - …
  - eId: ttitle_3__art_18__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_18__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 3 3

```yaml
articles:
- eId: title_3__art_16
  num:
    inline_content:
    - element_type: TextRun
      text: § 16.
  heading:
    eId: title_3__art_16__heading
    inline_content:
    - element_type: TextRun
      text: Bekanntgabe von Personendaten
  subheading:
    eId: title_3__art_16__subheading
    inline_content:
    - element_type: TextRun
      text: a. Allgemein
  paragraphs:
  - eId: title_3__art_16__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_16__para_1__content
      content_blocks:
      - …
      - …
  - eId: title_3__art_16__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_16__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 1 2

```yaml
articles:
- eId: title_1__art_2
  num:
    inline_content:
    - element_type: TextRun
      text: § 2.
  heading:
    inline_content:
    - element_type: TextRun
      text: Geltungsbereich
  paragraphs:
  - eId: title_1__art_2__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_1__art_2__para_1__content
      content_blocks:
      - …
  - eId: title_1__art_2__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: level_I__art_2__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 7 7

```yaml
articles:
- eId: title_7__art_36
  num:
    inline_content:
    - element_type: TextRun
      text: § 36.
  heading:
    eId: title_7__art_36__heading
    inline_content:
    - element_type: TextRun
      text: Empfehlungen und Einwirkungsbefugnisse
  paragraphs:
  - eId: title_7__art_36__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_36__para_1__content
      content_blocks:
      - …
  - eId: title_7__art_36__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_36__para_2__content
      content_blocks:
      - …
  - … 1 weitere

```
#### Beispiel Article: zh idg 7 10

```yaml
articles:
- eId: title_7__art_39
  num:
    inline_content:
    - element_type: TextRun
      text: § 39.
  heading:
    eId: title_7__art_39__heading
    inline_content:
    - element_type: TextRun
      text: Berichterstattung
  paragraphs:
  - eId: title_7__art_39__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_39__para_1__content
      content_blocks:
      - …

```
#### Beispiel Article: Article with numbered paragraphs

```yaml
articles:
- eId: art_2
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Zweck
  paragraphs:
  - eId: art_2/para_1
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - eId: art_2/para_2
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - … 2 weitere

```
#### Beispiel Article: zh idg 6 6

```yaml
articles:
- eId: title_6__art_29
  num:
    inline_content:
    - element_type: TextRun
      text: § 29.
  heading:
    eId: title_6__art_29__heading
    inline_content:
    - element_type: TextRun
      text: Gebühren und Entgelte
  paragraphs:
  - eId: title_6__art_29__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_29__para_1__content
      content_blocks:
      - …
  - eId: title_6__art_29__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_29__para_2__content
      content_blocks:
      - …
      - …
  - … 2 weitere

```
#### Beispiel Article: zh idg 3 2

```yaml
articles:
- eId: title_3__art_15
  num:
    inline_content:
    - element_type: TextRun
      text: § 15.
  heading:
    eId: title_3_art_15__heading
    inline_content:
    - element_type: TextRun
      text: Medien
  paragraphs:
  - eId: title_3__art_15__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_15__para_1__content
      content_blocks:
      - …
  - eId: title_3__art_15__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_15__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 6 3

```yaml
articles:
- eId: title_6__art_26
  num:
    inline_content:
    - element_type: TextRun
      text: § 26.
  heading:
    eId: title_6__art_26__heading
    inline_content:
    - element_type: TextRun
      text: Anhörung betroffener Dritter
  paragraphs:
  - eId: ttitle_6__art_26__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_26__para_1__content
      content_blocks:
      - …
  - eId: title_6__art_26__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_26__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 6 4

```yaml
articles:
- eId: title_6__art_27
  num:
    inline_content:
    - element_type: TextRun
      text: § 27.
  heading:
    eId: ttitle_6__art_27__heading
    inline_content:
    - element_type: TextRun
      text: Verfügung
  paragraphs:
  - eId: title_2__chp_F__art_27__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_27__para_1__content
      content_blocks:
      - …
  - eId: title_6__art_27__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_27__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 7 1

```yaml
articles:
- eId: title_7__art_30
  num:
    inline_content:
    - element_type: TextRun
      text: § 30.
  heading:
    eId: title_7__art_30__heading
    inline_content:
    - element_type: TextRun
      text: Stellung
  paragraphs:
  - eId: title_7__art_30__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: ttitle_7__art_30__para_1__content
      content_blocks:
      - …
  - eId: title_7__art_30__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_30__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 6 2

```yaml
articles:
- eId: ttitle_6__art_25
  num:
    inline_content:
    - element_type: TextRun
      text: § 25.
  heading:
    eId: title_6_art_25__heading
    inline_content:
    - element_type: TextRun
      text: Prüfung des Gesuchs
  paragraphs:
  - eId: ttitle_6__art_25__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_25__para_1__content
      content_blocks:
      - …
  - eId: title_6__art_25__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_25__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 7 9

```yaml
articles:
- eId: title_7__art_38
  num:
    inline_content:
    - element_type: TextRun
      text: § 37.
  heading:
    eId: title_7__art_38__heading
    inline_content:
    - element_type: TextRun
      text: Zusammenarbeit
  paragraphs:
  - eId: title_7__art_38__para_1
    num: {}
    content_ref:
      eId: title_7__art_38__para_1__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 3 4

```yaml
articles:
- eId: title_3__art_17
  num:
    inline_content:
    - element_type: TextRun
      text: § 17.
  subheading:
    eId: ttitle_3__art_17__subheading
    inline_content:
    - element_type: TextRun
      text: b. Besondere Personendaten
  paragraphs:
  - eId: title_3__art_17__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: ttitle_3__art_17__para_1__content
      content_blocks:
      - …
      - …
  - eId: ttitle_3__art_17__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_17__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 8 1

```yaml
articles:
- eId: title_8__art_40
  num:
    inline_content:
    - element_type: TextRun
      text: § 40.
  heading:
    eId: title_8__art_40__heading
    inline_content:
    - element_type: TextRun
      text: Vertragswidriges Bearbeiten von Personendaten
  paragraphs:
  - eId: title_8__art_40__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_8__art_40__para_1__content
      content_blocks:
      - …
  - eId: title_8__art_40__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_8__art_40__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: sr101 1 4

```yaml
articles:
- eId: art_4
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Landessprachen
  paragraphs:
  - eId: art_4/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 9 3

```yaml
articles:
- eId: title_9__art_43
  num:
    inline_content:
    - element_type: TextRun
      text: § 43.
  heading:
    eId: title_9__art_43__heading
    inline_content:
    - element_type: TextRun
      text: Aufhebung bisherigen Rechts
  paragraphs:
  - eId: title_9__art_43__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_9__art_43__para_1__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 6 1

```yaml
articles:
- eId: title_6__art_24
  num:
    inline_content:
    - element_type: TextRun
      text: § 24.
  heading:
    eId: title_6__art_24__heading
    inline_content:
    - element_type: TextRun
      text: Gesuch
  paragraphs:
  - eId: title_6__art_24__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_24__para_1__content
      content_blocks:
      - …
  - eId: title_6__art_24__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_24__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 1 3

```yaml
articles:
- eId: title_1__art_3
  num:
    inline_content:
    - element_type: TextRun
      text: § 3.
  heading:
    inline_content:
    - element_type: TextRun
      text: Begriffe
  paragraphs:
  - eId: title_1__art_3__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_1__art_3__para_1__content
      content_blocks:
      - …
      - …
      - … 5 weitere

```
#### Beispiel Article: sr101 1 6

```yaml
articles:
- eId: art_5_a
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
    - element_type: I
      inline_content:
      - …
    - … 1 weitere
  heading:
    inline_content:
    - element_type: TextRun
      text: Subsidiarität
  paragraphs:
  - eId: art_5_a/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: sr101 1 7

```yaml
articles:
- eId: art_6
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Individuelle und gesellschaftliche Verantwortung
  paragraphs:
  - eId: art_6/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 7 8

```yaml
articles:
- eId: title_7__art_37
  num:
    inline_content:
    - element_type: TextRun
      text: § 37.
  heading:
    eId: title_7__art_37__heading
    inline_content:
    - element_type: TextRun
      text: Zusammenarbeit
  paragraphs:
  - eId: title_7__art_37__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_37__para_1__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 6 5

```yaml
articles:
- eId: title_6__art_28
  num:
    inline_content:
    - element_type: TextRun
      text: § 28.
  heading:
    eId: title_6__art_28__heading
    inline_content:
    - element_type: TextRun
      text: Fristen
  paragraphs:
  - eId: title_6__art_28__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_28__para_1__content
      content_blocks:
      - …
  - eId: title_6__art_28__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_6__art_28__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 3 1

```yaml
articles:
- eId: title_3__art_14
  num:
    inline_content:
    - element_type: TextRun
      text: § 14.
  heading:
    eId: title_3__art_14__heading
    inline_content:
    - element_type: TextRun
      text: Informationstätigkeit von Amtes wegen
  paragraphs:
  - eId: title_3__art_14__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_14__para_1__content
      content_blocks:
      - …
  - eId: title_3__art_14__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_3__art_14__para_2__content
      content_blocks:
      - …
  - … 2 weitere

```
#### Beispiel Article: zh idg 7 5

```yaml
articles:
- eId: title_7__art_34
  num:
    inline_content:
    - element_type: TextRun
      text: § 34.
  heading:
    eId: title_7__art_34__heading
    inline_content:
    - element_type: TextRun
      text: Aufgaben
  paragraphs:
  - eId: title_2__chp_G__art_34__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_34__para_1__content
      content_blocks:
      - …
      - …

```
#### Beispiel Article: zh idg 4 3

```yaml
articles:
- eId: title_4__art_22
  num:
    inline_content:
    - element_type: TextRun
      text: § 22.
  heading:
    eId: ttitle_4__art_22__heading
    inline_content:
    - element_type: TextRun
      text: Sperren von Personendaten
  paragraphs:
  - eId: ttitle_4__art_22__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_4__art_22__para_1__content
      content_blocks:
      - …
  - eId: title_4__art_22__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_4__art_22__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 4 1

```yaml
articles:
- eId: title_4__art_20
  num:
    inline_content:
    - element_type: TextRun
      text: § 20.
  heading:
    eId: title_4__art_20__heading
    inline_content:
    - element_type: TextRun
      text: Zugang zu Informationen
  paragraphs:
  - eId: title_4__art_20__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_4__art_20__para_1__content
      content_blocks:
      - …
  - eId: title_4__art_20__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_4__art_20__para_2__content
      content_blocks:
      - …
  - … 1 weitere

```
#### Beispiel Article: zh idg 1 1

```yaml
articles:
- eId: title_1__art_1
  num:
    inline_content:
    - element_type: TextRun
      text: § 1.
  heading:
    inline_content:
    - element_type: TextRun
      text: Gegenstand und Zweck
  paragraphs:
  - eId: title_1__art_1__para_1
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - eId: ltitle_1__art_1__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_1__art_1__content
      content_blocks:
      - …
      - …

```
#### Beispiel Article: zh idg 7 3

```yaml
articles:
- eId: title_7__art_32
  num:
    inline_content:
    - element_type: TextRun
      text: § 32.
  heading:
    eId: title_7__art_32__heading
    inline_content:
    - element_type: TextRun
      text: Voranschlag und Haushaltführung
  paragraphs:
  - eId: title_7__art_32__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_32__para_1__content
      content_blocks:
      - …
  - eId: title_7__art_32__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_32__para_2__content
      content_blocks:
      - …
  - … 1 weitere

```
#### Beispiel Article: zh idg 4 2

```yaml
articles:
- eId: title_4__art_21
  num:
    inline_content:
    - element_type: TextRun
      text: § 21.
  heading:
    eId: title_4__art_21__heading
    inline_content:
    - element_type: TextRun
      text: Schutz eigener Personendaten
  paragraphs:
  - eId: title_4__art_21__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_4__art_21__para_1__content
      content_blocks:
      - …
      - …

```
#### Beispiel Article: zh idg 7 6

```yaml
articles:
- eId: ttitle_7__art_35
  num:
    inline_content:
    - element_type: TextRun
      text: § 35.
  heading:
    eId: title_7__art_35__heading
    inline_content:
    - element_type: TextRun
      text: Kontrollbefugnisse
  paragraphs:
  - eId: title_7__art_35__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_35__para_1__content
      content_blocks:
      - …
  - eId: title_7__art_35__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_35__para_2__content
      content_blocks:
      - …

```
#### Beispiel Article: zh idg 9 4

```yaml
articles:
- eId: title_9__art_44
  num:
    inline_content:
    - element_type: TextRun
      text: § 44.
  heading:
    eId: title_9__art_44__heading
    inline_content:
    - element_type: TextRun
      text: Anpassung anderer Erlasse
  paragraphs:
  - eId: title_9__art_44__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_9__art_44__para___content
      content_blocks:
      - …
      - …

```
#### Beispiel Article: zh idg 9 1

```yaml
articles:
- eId: title_9__art_41
  num:
    inline_content:
    - element_type: TextRun
      text: § 41.
  heading:
    eId: title_9__art_41__heading
    inline_content:
    - element_type: TextRun
      text: Übergangsrecht
  paragraphs:
  - eId: title_9__art_41__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_9__art_41__para_1__content
      content_blocks:
      - …
      - …

```
#### Beispiel Article: zh idg 5 1

```yaml
articles:
- eId: title_5__art_23
  num:
    inline_content:
    - element_type: TextRun
      text: § 23
  heading:
    eId: title_5__art_23__heading
    inline_content:
    - element_type: TextRun
      text: Interessenabwägung
  paragraphs:
  - eId: title_5__art_23__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: ttitle_5__art_23__para_1__content
      content_blocks:
      - …
  - eId: title_5__art_23__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_5__art_23__para_2__content
      content_blocks:
      - …
      - …
  - … 1 weitere

```
#### Beispiel Article: sr101 1 5

```yaml
articles:
- eId: art_5
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Grundsätze rechtsstaatlichen Handelns
  paragraphs:
  - eId: art_5/para_1
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - eId: art_5/para_2
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - … 2 weitere

```
#### Beispiel Article: zh idg 7 2

```yaml
articles:
- eId: title_7__art_31
  num:
    inline_content:
    - element_type: TextRun
      text: § 31.
  heading:
    eId: title_7_art_31__heading
    inline_content:
    - element_type: TextRun
      text: Personal
  paragraphs:
  - eId: title_7__art_31__para_1
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_31__para_1__content
      content_blocks:
      - …
  - eId: title_7__art_31__para_2
    num:
      inline_content:
      - …
    content_ref:
      eId: title_7__art_31__para_2__content
      content_blocks:
      - …
  - … 1 weitere

```






</div>