\newpage

# Documents as a last-resort fallback

The schemas of this eCH expert group are designed to publish information as structured data whenever possible.

Documents should therefore not be used as the normal way to convey information. They may be added to the data model only as a last resort, when the relevant information cannot yet be represented in a structured form.

This fallback supports the gradual transition from legacy documents to a fully data-modelled approach.

# Modelling of the document structure (FRBR)

As in other data models, we propose adopting the Functional Requirements for Bibliographic Records (FRBR) model. This approach is also used by ELI, which this eCH expert group uses for legal texts.

The hierarchy of classes makes it possible to represent different versions of a document and to extend them later, for example with regard to language and format.

The model distinguishes between a Work, an Expression, and a Manifestation. The following definitions and examples are based on Wikipedia:

## Work

Abstract: A work is a "distinct intellectual or artistic creation." For example, Beethoven's Ninth Symphony is a work, regardless of who performs it.

The work is the main container for one document. It holds different expressions and manifestions for different versions of the same document. But it shall not be used to mix documents with different content. 

It holds the unique identifier for this work and a document category for a high-level overview. The document categories are defined by this standard.

Attached to the Work is one or multiple expressions as described below.

{{include:ech-0292_meta/output/docs/Work.md}}

### Dokumentenkategorien (document_category)

{{include:ech-0292_meta/output/docs/DocumentCategoryEnum.md}}


## Expression

Abstract: An expression is "the specific intellectual or artistic form that a work takes each time it is 'realized.'" An audiobook and a text edition of a book are different expressions of the same work. For music, this includes both writing down the sheet music and performing it. Each draft of the score is an expression. The professionally recorded 1996 London Philharmonic performance of Beethoven's Ninth is another expression.

Typically per language on distinct expression is created. An expression holds additionally to the attributes of the work, the title and description in the according language of the expression.

Attached to the Expression is one or multiple Manifestation as decribed below.

{{include:ech-0292_meta/output/docs/Expression.md}}

## Manifestation

Abstract: A manifestation is "the physical embodiment of an expression of a work. As an entity, manifestation represents all the physical objects that bear the same characteristics, in respect to both intellectual content and physical form." The recordings of the 1996 performance released on vinyl are one manifestation. The same performance released on CD is another manifestation.

With the manifestion the final URL to the actual document is added. There can be one more more manifestations, which are differing in the differnt formats (e.g. PDF, DOCX, HTML) of the document provided.

Both the Expression and the Manifestation carry creation and modification dates via the common mixin `HasCreationModificationDates`. All FRBR entities are identified via the common mixin `HasIdentification`.


{{include:ech-0292_meta/output/docs/Manifestation.md}}
{{include:ech-0292_meta/output/docs/HasIdentification.md}}
{{include:ech-0292_meta/output/docs/HasCreationModificationDates.md}}
