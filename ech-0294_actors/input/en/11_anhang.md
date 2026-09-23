\newpage

# Annex A – References & Bibliography {.unnumbered}

Where a version is stated, it is the one this standard was developed against.

## Standards of the "Political Affairs" specialist group {.unnumbered}

The standards of the specialist group are developed jointly and reference one another. All of them currently carry the status "In Arbeit" (in progress; as of 10 August 2026); no version is therefore stated.

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0292|eCH-0292: Meta-processes for political affairs – shared data elements: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0293|eCH-0293: Public council operations: [https://www.ech.ch/de/ech/ech-0293](https://www.ech.ch/de/ech/ech-0293)|
|eCH-0295|eCH-0295: Parliamentary affairs: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0296|eCH-0296: Legal acts and legislative texts: [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|eCH-0297|eCH-0297: Public consultations: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Further eCH standards {.unnumbered}

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0011|eCH-0011: Datenstandard Personendaten, version 9.0.0 (approved, 27.07.2023). Basis of the name types in `NameTypeEnum` (`personNameData`): [https://www.ech.ch/de/ech/ech-0011/9.0.0](https://www.ech.ch/de/ech/ech-0011/9.0.0)|
|eCH-0108|eCH-0108: Datenstandard: Unternehmensstammdaten und Unternehmensregister, version 6.0.0 (approved, 04.04.2024). Defines the exchange format of the UID (`organization_uid`) and is the standard the legal form code list in `LegalFormEnum` conforms to: [https://www.ech.ch/de/ech/ech-0108/6.0.0](https://www.ech.ch/de/ech/ech-0108/6.0.0)|

## Code lists and further sources {.unnumbered}

| | |
|------------------|----------------------------------------------------------------------------------|
|I14Y|Interoperability platform of the Federal Statistical Office. Source of the code lists for legal form (`LegalFormEnum`) and sex (`GenderCodeEnum`): [https://www.i14y.admin.ch](https://www.i14y.admin.ch)|
|LINDAS|Linked Data Service of the Swiss federal administration. Identifiers of the Swiss spatial units (country, canton, district, municipality) for `spatial` and `ElectoralDistrict`: [https://ld.admin.ch](https://ld.admin.ch)|
|NOGA|General Classification of Economic Activities of the Federal Statistical Office. Enables analyses via the UID of referenced organisations.|
|Wikidata|Free knowledge base. Entity IRI (`http://www.wikidata.org/entity/Q…`) in `wikidata_uri`: [https://www.wikidata.org](https://www.wikidata.org)|
|ISO 639-1|ISO (International Organization for Standardization). Language codes, used in the `language` slot of `MultilingualValue`.|
|schema.org|Shared vocabulary for structured data. Source of several `slot_uri` assignments: [https://schema.org](https://schema.org)|
|LinkML|The modelling language in which this standard is defined: [https://linkml.io](https://linkml.io)|

\newpage

# Annex B – Cooperation & Verification {.unnumbered}

Specialist group "Political Affairs", subgroup "Political Actors":

| | |
|---|---|
|Julie Silberstein|Federal Statistical Office|
|Laurence Brandenberger|University of Zurich, IPZ|
|Daniela Koller|Canton of Thurgau|
|Thomas Roth||
|Stefan Oderbolz|EBP|
|Fabian Davolio|Parliamentary Services|
|Orhan Saeedi|Canton of Basel-Stadt|
|Christian Gutknecht|Glue AG|
|Michael Luggen|Federal Chancellery|

<!-- TODO specialist group: complete/correct organisations and the version history. -->

| Version | Date | Author | Remark |
|---|---|---|---|
| 1.0.0 | 2026-08-10 | Specialist group "Political Affairs" | Submitted as proposal |

# Annex C – Abbreviations and Glossary {.unnumbered}

| | |
|---|---|
|FADP|Swiss Federal Act on Data Protection, in force since 1 September 2023.|
|I14Y|Interoperability platform of the Federal Statistical Office; source of several code lists.|
|IRI|Internationalized Resource Identifier. Extension of the URI to the full Unicode character set.|
|JSON-LD|JSON for Linking Data. Serialisation of linked data in JSON.|
|LINDAS|Linked Data Service of the Swiss Federal Administration.|
|LinkML|Linked Data Modeling Language. The modelling language in which this standard is defined.|
|NOGA|General Classification of Economic Activities of the Federal Statistical Office.|
|RDF|Resource Description Framework. Data model for linked data; delivered here as Turtle (.ttl).|
|UID|Business Identification Number. Unique key of a Swiss enterprise according to the Federal Statistical Office.|
|URI|Uniform Resource Identifier. Unique identifier of a resource.|
|XSD|XML Schema Definition. W3C recommendation for defining structures of XML documents.|

# Annex D – Changes in comparison to the previous version {.unnumbered}

This is the first version.

\newpage

# Annex E – Table of Figures {.unnumbered}

None

# Annex F – Table of Tables {.unnumbered}

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \h \z \c "Table" </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Right-click &gt; "Update field" to generate the table of tables.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```
