

## Klasse: ActMeta 


_Metadaten-Abschnitt des Erlasses (akn:meta). Enthält die FRBR-Identifikation (Work-, Expression-, Manifestations-Ebene) sowie benannte Referenz-Definitionen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| identification_ref | 0..1 <br/> [Identification](Identification.md) | FRBR-Identifikationsblock (akn:identification). |
| references_ref | 0..1 <br/> [References](References.md) | Referenzen-Abschnitt der Metadaten (akn:references). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](Act.md) | [meta](meta.md) | range | [ActMeta](ActMeta.md) |
| [Doc](Doc.md) | [meta](meta.md) | range | [ActMeta](ActMeta.md) |














### Beispiele
#### Beispiel ActMeta: bgoe 1 1

```yaml
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

```
#### Beispiel ActMeta: sr101 1 1

```yaml
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

```






</div>