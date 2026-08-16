

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
#### Beispiel Container: sr101 excerpt

```yaml
# Auszug aus SR 101, Bundesverfassung der Schweizerischen Eidgenossenschaft,
# Fassung vom 3. März 2024. Werte übernommen aus der Fedlex-Datei
# misc/spec/input/examples/federal/SR-101-03032024-DE.xml -- gekürzt auf den
# vollständigen Metadatenblock, den Vorspann und den ersten Artikel, damit die
# Beispiele im Dokument lesbar bleiben.
act_ref:
  act_name: constitution

  meta:
    identification_ref:
      # Der Anker zeigt auf die Organisation, die in references deklariert ist.
      source: "#ch.bk"

      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303
        # Drei Datumsangaben desselben Werks, unterschieden über @name aus dem
        # Fedlex/JoLux-Vokabular: Inkrafttreten, Erlassdatum, Nachführungsstand.
        frbr_dates:
          - date_value: "2000-01-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "1999-04-18"
            frbr_date_name: jolux:dateDocument
          - date_value: "2024-03-03"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
          - href: "#ch.bk"
            as_role: "#rightsHolder"
        frbr_country:
          value: CH
        frbr_number:
          value: "101"
        # Die SR-Nummer wird nicht übersetzt, der Titel schon: je Sprache ein
        # Eintrag mit Kurzform.
        frbr_names:
          - xml_lang: de
            value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April 1999
            short_form: BV
          - xml_lang: fr
            value: Constitution fédérale de la Confédération suisse du 18 avril 1999
            short_form: Cst.
          - xml_lang: it
            value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
            short_form: Cost.
          - xml_lang: rm
            value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
            short_form: Cst.
        frbr_authoritative:
          value: "true"

      # Die Expression ist die sprachliche Fassung: dieselbe URI mit Sprachanteil.
      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
        frbr_dates:
          - date_value: "2000-01-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "1999-04-18"
            frbr_date_name: jolux:dateDocument
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        frbr_language:
          language_value: de

      # Die Manifestation ist die konkrete Datei -- hier das XML.
      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/1999/404/20240303/de
        frbr_dates:
          - date_value: "2024-03-03"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        frbr_format:
          value: xml

    # Stellen und Rollen stehen einmal hier; die Elemente oben verweisen mit
    # dokumentinternen Ankern darauf.
    references_ref:
      source: "#ch.bk"
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

  preface_ref:
    preface_paragraphs:
      - doc_number: "101"
      - doc_title:
          inline_content:
            - element_type: TextRun
              text: Bundesverfassung
            - element_type: Br
            - element_type: TextRun
              text: der Schweizerischen Eidgenossenschaft

  body:
    titles:
      - eId: tit_1
        num:
          inline_content:
            - element_type: TextRun
              text: "1. Titel: "
        heading:
          inline_content:
            - element_type: TextRun
              text: Allgemeine Bestimmungen
        articles:
          - eId: art_1
            # Die Artikelnummer ist im Original fett ausgezeichnet: ein B-Element
            # mit einem Textlauf darin, nicht eine Zeichenkette "Art. 1".
            num:
              inline_content:
                - element_type: B
                  inline_content:
                    - element_type: TextRun
                      text: Art. 1
            heading:
              inline_content:
                - element_type: TextRun
                  text: Schweizerische Eidgenossenschaft
            paragraphs:
              - eId: art_1/para
                content_ref:
                  block_paragraphs:
                    - inline_content:
                        - element_type: TextRun
                          text: >-
                            Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz,
                            Obwalden und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt
                            und Basel-Landschaft, Schaffhausen, Appenzell Ausserrhoden und
                            Appenzell Innerrhoden, St. Gallen, Graubünden, Aargau, Thurgau,
                            Tessin, Waadt, Wallis, Neuenburg, Genf und Jura bilden die
                            Schweizerische Eidgenossenschaft.

```
#### Beispiel Container: bgoe excerpt

```yaml
# Auszug aus SR 152.3, Bundesgesetz über das Öffentlichkeitsprinzip der
# Verwaltung (Öffentlichkeitsgesetz, BGÖ), Fassung vom 1. November 2023.
# Werte übernommen aus der Fedlex-Auslieferung
# https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
#
# Zweites Beispiel neben der Bundesverfassung: ein gewöhnliches Bundesgesetz
# (act_name: publicLaw statt constitution), mit Aufzählung im Absatz und den
# Referenzeinträgen für Sprache und Format, welche die Verfassungsdatei nicht
# führt.
act_ref:
  act_name: publicLaw

  meta:
    identification_ref:
      source: "#ch.bk"

      frbr_work:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101
        frbr_dates:
          - date_value: "2006-07-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "2004-12-17"
            frbr_date_name: jolux:dateDocument
          - date_value: "2023-11-01"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
          - href: "#ch.bk"
            as_role: "#rightsHolder"
        frbr_country:
          value: CH
        # Anders als die Verfassung trägt das Gesetz eine gegliederte SR-Nummer.
        frbr_number:
          value: "152.3"
        frbr_names:
          - xml_lang: de
            value: Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung (Öffentlichkeitsgesetz, BGÖ)
            short_form: BGÖ
          - xml_lang: fr
            value: Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans l'administration (Loi sur la transparence, LTrans)
            short_form: LTrans
          - xml_lang: it
            value: Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione (Legge sulla trasparenza, LTras)
            short_form: LTras
          - xml_lang: rm
            value: Lescha federala dals 17 da december 2004 davart il princip da la transparenza da l'administraziun (Lescha da transparenza, LTrans)
            short_form: LTrans
          - xml_lang: en
            value: Federal Act of 17 December 2004 on Freedom of Information in the Administration (Freedom of Information Act, FoIA)
            short_form: FoIA
        frbr_authoritative:
          value: "true"

      frbr_expression:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de
        frbr_dates:
          - date_value: "2006-07-01"
            frbr_date_name: jolux:dateEntryInForce
          - date_value: "2023-11-01"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        frbr_language:
          language_value: de

      frbr_manifestation:
        frbr_this:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml/main-text
        frbr_uri:
          value_uri: https://fedlex.data.admin.ch/eli/cc/2006/355/20231101/de/xml
        frbr_dates:
          - date_value: "2023-11-01"
            frbr_date_name: jolux:dateApplicability
        frbr_authors:
          - href: "#ch.bk"
            as_role: "#publisher"
        # Fedlex vermerkt am Format zusätzlich, welche Werkzeugversion die Datei
        # erzeugt hat -- ein Attribut aus dem Fedlex-Namensraum.
        frbr_format:
          value: xml
          fedlex_generator: 2024-q4-rel-1.6.5

    references_ref:
      source: "#ch.bk"
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
      # Sprache und Format zeigen auf kontrollierte Vokabulare: das der EU für
      # die Sprache, das von Fedlex für das Dateiformat.
      tlc_references:
        - name_attr: language
          href: http://publications.europa.eu/resource/authority/language/DEU
          show_as: de
        - name_attr: format
          href: https://fedlex.data.admin.ch/vocabulary/user-format/xml
          show_as: xml

  preface_ref:
    preface_paragraphs:
      - doc_number: "152.3 "
      - doc_title:
          inline_content:
            - element_type: TextRun
              text: Bundesgesetz
            - element_type: Br
            - element_type: TextRun
              text: über das Öffentlichkeitsprinzip der Verwaltung

  body:
    articles:
      - eId: art_1
        num:
          inline_content:
            - element_type: B
              inline_content:
                - element_type: TextRun
                  text: Art. 1
        heading:
          inline_content:
            - element_type: TextRun
              text: Zweck und Gegenstand
        paragraphs:
          # Ein einziger Absatz bleibt unnummeriert; die eId endet auf "para".
          - eId: art_1/para
            content_ref:
              block_paragraphs:
                - inline_content:
                    - element_type: TextRun
                      text: >-
                        Dieses Gesetz soll die Transparenz über den Auftrag, die Organisation und
                        die Tätigkeit der Verwaltung fördern. Zu diesem Zweck trägt es zur
                        Information der Öffentlichkeit bei, indem es den Zugang zu amtlichen
                        Dokumenten gewährleistet.

      - eId: art_2
        num:
          inline_content:
            - element_type: B
              inline_content:
                - element_type: TextRun
                  text: Art. 2
        heading:
          inline_content:
            - element_type: TextRun
              text: Persönlicher Geltungsbereich
        paragraphs:
          # Mehrere Absätze werden nummeriert, und der Absatz führt statt eines
          # Fliesstextes eine Aufzählung mit Einleitungssatz.
          - eId: art_2/para_1
            num:
              inline_content:
                - element_type: TextRun
                  text: "1"
            content_ref:
              block_lists:
                - eId: art_2/para_1/lst
                  list_introduction:
                    eId: art_2/para_1/listintro
                    inline_content:
                      - element_type: TextRun
                        text: " Dieses Gesetz gilt für:"
                  items:
                    - eId: art_2/para_1/lbl_a
                      num:
                        inline_content:
                          - element_type: TextRun
                            text: "a. "
                      block_paragraphs:
                        - inline_content:
                            - element_type: TextRun
                              text: die Bundesverwaltung;
                    - eId: art_2/para_1/lbl_b
                      num:
                        inline_content:
                          - element_type: TextRun
                            text: "b. "
                      block_paragraphs:
                        - inline_content:
                            - element_type: TextRun
                              text: >-
                                Organisationen und Personen des öffentlichen oder privaten Rechts,
                                die nicht der Bundesverwaltung angehören, soweit sie Erlasse oder
                                erstinstanzliche Verfügungen im Sinne von Artikel 5 des
                                Bundesgesetzes vom 20. Dezember 1968 über das
                                Verwaltungsverfahren erlassen;

  # Der Anhang des Erlasses: ein eigenes Dokument mit eigenem Vorspann und
  # Hauptteil. Sein Identifikationsblock, der in der Fedlex-Datei die URIs des
  # Erlasses unveraendert wiederholt, ist hier weggelassen.
  components_ref:
    component_list:
    - doc_ref:
        doc_name: annex
        preface_ref:
          containers:
          - container_name: headerOfAnnex
            blocks:
            - block_name: heading
              inline_content:
              - element_type: TextRun
                text: Anhang
        main_body:
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: (Art. 22)
          levels:
          - eId: annex_u1/lvl_u1
            heading:
              inline_content:
              - element_type: TextRun
                text: Änderung bisherigen Rechts
            content_ref:
              block_paragraphs:
              - inline_content:
                - element_type: TextRun
                  text: 'Die nachstehenden Gesetze werden wie folgt geändert:'
              - inline_content:
                - element_type: TextRun
                  text: …
                - element_type: AuthorialNote
                  block_paragraphs:
                  - inline_content:
                    - element_type: TextRun
                      text: Die Änderungen können unter
                    - element_type: Ref
                      href: https://fedlex.data.admin.ch/eli/oc/2006/355
                      inline_content:
                      - element_type: TextRun
                        text: AS
                      - element_type: B
                        inline_content:
                        - element_type: TextRun
                          text: '2006'
                      - element_type: TextRun
                        text: '2319'
                    - element_type: TextRun
                      text: konsultiert werden.

```






</div>