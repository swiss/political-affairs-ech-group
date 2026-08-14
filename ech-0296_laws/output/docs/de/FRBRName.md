

## Klasse: FRBRName 


_Ein mehrsprachiger Namenseintrag des FRBR-Works (akn:FRBRname). Enthält den offiziellen Langtitel und eine optionale Abkürzung. Ein Eintrag pro Sprache._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| xml_lang | 0..1 <br/> [String](String.md) | XML-Sprachattribut (xml:lang), z.B. 'de', 'fr', 'it', 'rm', 'en'. |
| value | 0..1 <br/> [String](String.md) | Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet. |
| short_form | 0..1 <br/> [String](String.md) | Kurzform-Abkürzung des Gesetzesnamens (@shortForm), z.B. 'BV' (Deutsch), 'Cst.' (Französisch).  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [FRBRWork](FRBRWork.md) | [frbr_names](frbr_names.md) | range | [FRBRName](FRBRName.md) |














### Beispiele
#### Beispiel FRBRName: bgoe excerpt 1 4

```yaml
frbr_names:
- xml_lang: rm
  value: >-
    Lescha federala dals 17 da december 2004 davart il princip da la transparenza
    da l'administraziun (Lescha da transparenza, LTrans)
  short_form: LTrans

```
#### Beispiel FRBRName: sr101 excerpt 1 3

```yaml
frbr_names:
- xml_lang: it
  value: Costituzione federale della Confederazione Svizzera del 18 aprile 1999
  short_form: Cost.

```
#### Beispiel FRBRName: bgoe excerpt 1 3

```yaml
frbr_names:
- xml_lang: it
  value: >-
    Legge federale del 17 dicembre 2004 sul principio di trasparenza dell'amministrazione
    (Legge sulla trasparenza, LTras)
  short_form: LTras

```
#### Beispiel FRBRName: sr101 excerpt 1 2

```yaml
frbr_names:
- xml_lang: fr
  value: Constitution fédérale de la Confédération suisse du 18 avril 1999
  short_form: Cst.

```
#### Beispiel FRBRName: bgoe excerpt 1 2

```yaml
frbr_names:
- xml_lang: fr
  value: >-
    Loi fédérale du 17 décembre 2004 sur le principe de la transparence dans l'administration
    (Loi sur la transparence, LTrans)
  short_form: LTrans

```
#### Beispiel FRBRName: bgoe excerpt 1 5

```yaml
frbr_names:
- xml_lang: en
  value: >-
    Federal Act of 17 December 2004 on Freedom of Information in the Administration
    (Freedom of Information Act, FoIA)
  short_form: FoIA

```
#### Beispiel FRBRName: bgoe excerpt 1 1

```yaml
frbr_names:
- xml_lang: de
  value: >-
    Bundesgesetz vom 17. Dezember 2004 über das Öffentlichkeitsprinzip der Verwaltung
    (Öffentlichkeitsgesetz, BGÖ)
  short_form: BGÖ

```
#### Beispiel FRBRName: sr101 excerpt 1 4

```yaml
frbr_names:
- xml_lang: rm
  value: Constituziun federala da la Confederaziun svizra dals 18 d'avrigl 1999
  short_form: Cst.

```
#### Beispiel FRBRName: sr101 excerpt 1 1

```yaml
frbr_names:
- xml_lang: de
  value: Bundesverfassung der Schweizerischen Eidgenossenschaft vom 18. April 1999
  short_form: BV

```






</div>