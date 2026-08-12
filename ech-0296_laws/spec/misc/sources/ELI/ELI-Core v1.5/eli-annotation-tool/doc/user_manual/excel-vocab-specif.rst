.. -*- coding: utf-8 -*-

.. _excel-vocab-specif:

Describing a SKOS vocabulary in an Excel file
=============================================

The vocabularies used by the ELI annotation tool must be provided in
the SKOS standard. A vocabulary corresponds to a
``skos:ConceptScheme`` entity and contains several ``skos:Concept``
describing each of the terms inside the vocabulary.

It is possible to describe a vocabulary with an Excel worksheet. An
Excel workbook can contain several worksheets each describing a
different vocabulary. The worksheets have to conform to a specific
format.


General structure of the worksheet
----------------------------------

The upper part of the worksheet is named the header and contains
the metadata describing the *Concept Scheme*, ie the vocabulary
itself. The lower part is named the body and contains the
*Concepts*, ie the terms inside the vocabulary.

The header ends and the body begins at the line where ``Concept URI``
is found in the first column.

Please note that the cells must contain textual data. Other data
types, including for example hyperlinks, may provoke an error and be
ignored.


Properties describing the entities
----------------------------------

The *Concept Scheme* and the *Concept* entities are described
thanks to various properties. These properties can be:

* DCTERMS properties whose name must be prefixed with ``dct:``
* SKOS properties whose name must be prefixed with ``skos:``
* any customized properties whose prefix has been declared in the header

For example::

    dct:title
    skos:prefLabel
    euvoc:status

In the above example, the ``euvoc`` prefix must be declared and
associated with ``http://publications.europa.eu/ontology/euvoc#``
namespace.

When the value of the property can be in various languages, it is
possible to declare the name of the property and the language of the
values. The language is specified with its two-letters code. In such a
case, it is possible to declare multiple times the same property with
different languages each time. For example::

    skos:altLabel@en
    skos:altLabel@fr

Some properties can have multiple values. If such a case, it is
possible to declare the name of the property and the character that
will be used to separate the multiple values. For example::

    skos:altLabel@en[separator=","]
    skos:narrower[separator=";"]


Header
------

The header describes the *Concept Scheme*, ie the vocabulary
itself. The properties are defined in a set of consecutive rows. The
first column always contains the name of the property and the second
column the value of this property. Hence the header is a table with
two columns and as many rows as needed.

The first row of the header defines the URI of the *Concept Scheme*.
The name in the first column must be ``ConceptScheme URI`` and the
second column must give the URI of the ``skos:ConceptScheme``.

The following rows contains the properties describing the *Concept
Scheme*. These properties are either valid SKOS and DCTERMS properties
or custom properties prefixed by a custom prefix.

The custom prefixes used in the header or the body must be declared in
the header, each in a row whose first column is the prefix prefixed
with ``prefix:`` and whose second column is the URI associated to the
prefix.

Invalid properties or properties whose prefix is not declared will be
ignored when processing the file.

Here is an example of header:

.. csv-table::

   ConceptScheme URI,"http://data.sparna.fr/vocabularies/days"
   dct:title@en,Weekdays
   dct:description@en,The days of the week
   dct:description@fr,Les jours de la semaine
   euvoc:status, "http://publications.europa.eu/resource/authority/concept-status/CURRENT"
   prefix:euvoc,"http://publications.europa.eu/ontology/euvoc#"


Body
----

The body describes the *Concepts* inside the *Concept Scheme*, ie the
terms in the vocabulary. Each row defines a different *Concept*, the
columns being the various properties describing this *Concept*. Hence
the body is a table with as many columns as there are properties and
as many rows as there are *Concepts*.

The first row of the body contains the names of the properties used to
describe the *Concepts*. As explained above, the first column of this
row must be ``Concept URI``. The following columns are either valid
SKOS and DCTERMS properties or custom properties prefixed by a custom
prefix. Please keep in mind that the custom prefixes must have been
declared in the header.

Invalid properties or properties whose prefix is not declared will be
ignored when processing the file.

Here is an example of body. Because the table might be too large for
this document, it has been separated in two parts: the first three
columns and the last two columns.

.. csv-table:: First three columns of the body

   Concept URI, skos:prefLabel@en, skos:prefLabel@fr
   http://data.sparna.fr/vocabularies/days#monday, Monday, Lundi
   http://data.sparna.fr/vocabularies/days#tuesday, Tuesday, Mardi
   http://data.sparna.fr/vocabularies/days#wednesday, Wednesday, Mercredi
   http://data.sparna.fr/vocabularies/days#thursday, Thursday, Jeudi
   http://data.sparna.fr/vocabularies/days#friday, Friday, Vendredi
   http://data.sparna.fr/vocabularies/days#saturday, Saturday, Samedi
   http://data.sparna.fr/vocabularies/days#sunday, Sunday, Dimanche
   http://data.sparna.fr/vocabularies/days#week-end, Week-end, Fin de semaine

.. csv-table:: Last two columns of the body

   skos:narrower[separator=';'], skos:notation
   , MON
   , TUE
   , WED
   , THU
   , FRI
   , SAT
   , SUN
   http://data.sparna.fr/vocabularies/days#saturday ; http://data.sparna.fr/vocabularies/days#sunday, WKND
