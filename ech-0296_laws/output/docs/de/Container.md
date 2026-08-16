

## Klasse: Container 


_Ein generischer Behälter (akn:container), dessen @name den Zweck nennt._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| container_name | 0..1 <br/> [ContainerNameEnum](ContainerNameEnum.md) | Zweck des Behälters (akn:container/@name). |
| blocks | * <br/> [Block](Block.md) | Blöcke innerhalb des Behälters (akn:block). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preface](Preface.md) | [containers](containers.md) | range | [Container](Container.md) |














### Beispiele
#### Beispiel Container: bgoe

```yaml
act_ref:
  act_name: publicLaw
  meta:
    identification_ref:
      source: '#ch.bk'
      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
        frbr_dates:
        - date_value: '2006-07-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '2004-12-17'
          frbr_date_name: jolux:dateDocument
        - … 1 weitere
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_country:
          value: CH
        frbr_number:
          value: '152.3'
        frbr_names:
        - xml_lang: it
          value: >-
            Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
            (Legge sulla trasparenza, LTras)
          short_form: LTras
        - xml_lang: fr
          value: >-
            Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans
            l'administration (Loi sur la transparence, LTrans)
          short_form: LTrans
        - … 3 weitere
        frbr_authoritative:
          value: 'true'
      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
        frbr_dates:
        - date_value: '2006-07-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '2004-12-17'
          frbr_date_name: jolux:dateDocument
        - … 1 weitere
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_language:
          language_value: de
      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
        frbr_dates:
        - date_value: '2006-07-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '2004-12-17'
          frbr_date_name: jolux:dateDocument
        - … 1 weitere
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_format:
          value: xml
          fedlex_generator: 2024-q4-rel-1.6.5
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
  preface_ref:
    preface_paragraphs:
    - inline_content:
      - element_type: DocNumber
        inline_content:
        - …
    - inline_content:
      - element_type: DocTitle
        inline_content:
        - …
        - …
        - … 1 weitere
    - … 2 weitere
  preamble_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - element_type: TextRun
        text: Die Bundesversammlung der Schweizerischen Eidgenossenschaft,
    - element_type: BlockParagraph
      inline_content:
      - element_type: TextRun
        text: gestützt auf Artikel 173 Absatz 2 der Bundesverfassung
      - element_type: AuthorialNote
        content_blocks:
        - …
      - … 5 weitere
    - … 1 weitere
  body:
    sections:
    - eId: sec_1
      num:
        inline_content:
        - …
      heading:
        inline_content:
        - …
      articles:
      - eId: art_1
        num: …
        heading: …
        paragraphs:
        - …
      - eId: art_2
        num: …
        heading: …
        paragraphs:
        - …
        - …
        - … 1 weitere
      - … 3 weitere
    - eId: sec_2
      num:
        inline_content:
        - …
      heading:
        inline_content:
        - …
      articles:
      - eId: art_6
        num: …
        heading: …
        paragraphs:
        - …
        - …
        - … 1 weitere
      - eId: art_7
        num: …
        heading: …
        paragraphs:
        - …
        - …
      - … 2 weitere
    - … 3 weitere
  components_ref:
    component_list:
    - doc_ref:
        doc_name: annex
        meta:
          identification_ref: …
        preface_ref:
          containers:
          - …
        main_body:
          content_blocks:
          - …
          levels:
          - …

```
#### Beispiel Container: sr101

```yaml
act_ref:
  act_name: publicLaw
  meta:
    identification_ref:
      source: '#ch.bk'
      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
        frbr_dates:
        - date_value: '2000-01-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '1999-04-18'
          frbr_date_name: jolux:dateDocument
        - … 1 weitere
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_country:
          value: CH
        frbr_number:
          value: '101'
        frbr_names:
        - xml_lang: de
          value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April
            1999
          short_form: BV
        - xml_lang: fr
          value: Constitution fédérale de la Confédération suisse du 18 avril 1999
          short_form: Cst.
        - … 3 weitere
        frbr_authoritative:
          value: 'true'
      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
        frbr_dates:
        - date_value: '2000-01-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '1999-04-18'
          frbr_date_name: jolux:dateDocument
        - … 1 weitere
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_language:
          language_value: de
      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/xml/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/xml
        frbr_dates:
        - date_value: '2000-01-01'
          frbr_date_name: jolux:dateEntryInForce
        - date_value: '1999-04-18'
          frbr_date_name: jolux:dateDocument
        - … 1 weitere
        frbr_authors:
        - href: '#ch.bk'
          as_role: '#publisher'
        - href: '#ch.bk'
          as_role: '#rightsHolder'
        frbr_format:
          value: xml
          fedlex_generator: 2026-q1-rel-1.8.5
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
  preface_ref:
    preface_paragraphs:
    - inline_content:
      - element_type: DocNumber
        inline_content:
        - …
    - inline_content:
      - element_type: DocTitle
        inline_content:
        - …
        - …
        - … 1 weitere
    - … 1 weitere
  preamble_ref:
    content_blocks:
    - element_type: BlockParagraph
      fedlex_role: heading
      inline_content:
      - element_type: B
        inline_content:
        - …
    - element_type: BlockParagraph
      inline_content:
      - element_type: TextRun
        text: Im Namen Gottes des Allmächtigen!
    - … 7 weitere
  body:
    titles:
    - eId: tit_1
      num:
        inline_content:
        - …
      heading:
        inline_content:
        - …
      articles:
      - eId: art_1
        num: …
        heading: …
        paragraphs:
        - …
      - eId: art_2
        num: …
        heading: …
        paragraphs:
        - …
        - …
        - … 2 weitere
      - … 5 weitere
    - eId: tit_2
      num:
        inline_content:
        - …
      heading:
        inline_content:
        - …
      chapters:
      - eId: tit_2/chap_1
        num: …
        heading: …
        articles:
        - …
        - …
        - … 30 weitere
      - eId: tit_2/chap_2
        num: …
        heading: …
        articles:
        - …
        - …
        - … 2 weitere
      - … 1 weitere
    - … 4 weitere
    provisos:
    - eId: disp_u1
      heading:
        inline_content:
        - …
      paragraphs:
      - eId: disp_u1/para
        content_ref: …
    - eId: disp_u2
      heading:
        inline_content:
        - …
      paragraphs:
      - eId: disp_u2/para
        content_ref: …
      levels:
      - eId: disp_u2/lvl_A
        num: …
        content_ref: …
      - eId: disp_u2/lvl_B
        num: …
        content_ref: …
      - … 24 weitere

```
#### Beispiel Container: zh idg

```yaml
act_ref:
  act_name: Grunderlass
  meta:
    identification_ref:
      source: ''
      frbr_work:
        frbr_this:
          value_uri: /akn/CH-ZH/act/2007-02-12/62-121/!main
        frbr_uri:
          value_uri: /akn/CH-ZH/act/2007-02-12/62-121
        frbr_dates:
        - date_value: '2007-02-12'
          frbr_date_name: ''
        frbr_authors:
        - href: '#kantonsrat'
          as_role: '#authority'
        frbr_country:
          value: CH-ZH
        frbr_subtype:
          value: Gesetz
        frbr_number:
          value: 62-121
      frbr_expression:
        frbr_this:
          value_uri: /akn/CH-ZH/act/2007-02-12/62-121/ger@/!main
        frbr_uri:
          value_uri: /akn/CH-ZH/act/2007-02-12/62-121/ger@
        frbr_dates:
        - date_value: '2007-02-12'
          frbr_date_name: ''
        frbr_authors:
        - href: '#SK'
          as_role: '#editor'
        - href: '#JI'
          as_role: '#coEditor'
        frbr_language:
          language_value: ger
      frbr_manifestation:
        frbr_this:
          value_uri: /akn/CH-ZH/act/2007-02-12/62-121/ger@.akn/!main
        frbr_uri:
          value_uri: /akn/CH-ZH/act/2007-02-12/62-121/ger@.akn
        frbr_dates:
        - date_value: '2007-02-12'
          frbr_date_name: ''
        frbr_authors:
        - href: '#SK-Publ'
          as_role: '#publisher'
        frbr_format:
          value: '#akn'
    references_ref:
      source: '#source'
      original_ref:
        eId: ro
        href: /akn/CH-ZH/act/EXPRESSION
        show_as: Gesetz über .. vom ...
      active_refs:
      - eId: ra_1
        href: /akn/CH-ZH/act/WORK
        show_as: Gesetz über .. vom ...
      - eId: ra_2
        href: /akn/CH-ZH/act/2022-35/cons/(aktuelle konsolidierte Fassung)
        show_as: Gesetz über .. vom ...
      tlc_organizations:
      - eId: kantonsrat
        href: https://data.zh.ch/vocabulary/legal-institution/2
        show_as: Kantonsrat
      - eId: SK
        href: https://data.zh.ch/vocabulary/organizational-entity/SK
        show_as: Staatskanzlei
      - … 2 weitere
      tlc_roles:
      - eId: authority
        href: https://data.zh.ch/vocabulary/role/author
        show_as: Beschliessendes Organ
      - eId: editor
        href: https://data.zh.ch/vocabulary/role/leadEditor
        show_as: Federführende Einheit
      - … 2 weitere
      tlc_references:
      - name_attr: language
        href: http://publications.europa.eu/resource/authority/language/DEU
        show_as: ger
      - name_attr: xml
        href: https://data.zh.ch/vocabulary/user-format/xml
        show_as: XML
      tlc_concepts:
      - eId: inForce
        href: ''
        show_as: ''
    notes_ref:
      source: ''
      note_list:
      - eId: note_1
        content_blocks:
        - …
      - eId: note_2
        content_blocks:
        - …
      - … 4 weitere
  preface_ref:
    preface_paragraphs:
    - inline_content:
      - element_type: DocketNumber
        eId: docketNum_1
        title_attr: Orndungsnummer
        inline_content:
        - …
      - element_type: DocTitle
        eId: actTitle
        title_attr: Erlasstitel
        inline_content:
        - …
      - … 3 weitere
  preamble_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - element_type: TextRun
        text: nach Einsichtnahme in die Anträge
    - element_type: BlockParagraph
      inline_content:
      - element_type: TextRun
        text: und
    - … 1 weitere
    formulas:
    - eId: formula_1
      name_attr2: openFormula
      content_blocks:
      - element_type: BlockParagraph
        inline_content:
        - …
    - eId: formula_2
      name_attr2: Verb
      content_blocks:
      - element_type: BlockParagraph
        inline_content:
        - …
    citations_ref:
    - citation_list:
      - eId: cit_1
        refers_to: ''
        content_blocks:
        - …
    - citation_list:
      - eId: cit_2
        refers_to: ''
        content_blocks:
        - …
  body:
    titles:
    - eId: title_1
      num:
        inline_content:
        - …
      heading:
        eId: title_1__heading_1
        inline_content:
        - …
      articles:
      - eId: title_1__art_1
        num: …
        heading: …
        paragraphs:
        - …
        - …
      - eId: title_1__art_2
        num: …
        heading: …
        paragraphs:
        - …
        - …
      - … 1 weitere
    - eId: title_2
      num:
        inline_content:
        - …
      heading:
        eId: title_2__heading_1
        inline_content:
        - …
      chapters:
      - eId: title_2__chp_A
        num: …
        heading: …
        articles:
        - …
        - …
        - … 2 weitere
      - eId: title_2__chp_B
        num: …
        heading: …
        articles:
        - …
        - …
        - … 4 weitere
    - … 7 weitere
  conclusions_ref:
    eId: conclusions
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - element_type: TextRun
        text: Im Namen des Regierungsrates
      - element_type: Eol
      - … 2 weitere
    - element_type: BlockList
      eId: conclusions__blocklist_1
      list_introduction:
        inline_content:
        - …
      items:
      - eId: conclusions__blocklist_1__item_1
        content_blocks:
        - …
        num: …
      - eId: conclusions__blocklist_1__item_2
        content_blocks:
        - …
        num: …
    - … 1 weitere
  attachments_ref:
    attachment_list:
    - act_ref:
        act_name: ''
        meta:
          identification_ref: …
        body:
          component_refs:
          - …

```






</div>