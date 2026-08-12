# Ontological Structural Form (LinkML)

Official LinkML tutorial excerpt on mapping existing ontologies/knowledge graphs to LinkML — kept as
reference for mapping the ELI ontology (and jolux/Fedlex data) into our own LinkML schema in
`pipeline/schema`.

## Overview

The ontological or knowledge graph schema style in LinkML focuses on hierarchical classification of
entities within a domain, and the use of inheritance to propagate down attributes.

NOTE this form is somewhat orthogonal to the others, and as such we may later choose to separate this into
its own document.

This form can often be easily intermingled with the other forms in this document.

## Example Ontology

### Base Class

```yaml
classes:
  CreativeWork:
    description: "A base class representing any form of creative work"
    attributes:
      title:
        description: "Title of the creative work"
        range: string
      creator:
        description: "Creator of the work (individual or organization)"
        range: string
      creation_date:
        description: "Date when the work was created or published"
        range: date
      description:
        description: "A brief description of the work"
        range: string
      language:
        description: "Language of the work"
        range: Language
      license:
        description: "License under which the work is distributed"
        range: LicenseType
```

### SubClasses

```yaml
  Book:
    is_a: CreativeWork
    description: "Written works, primarily textual in nature"
    attributes:
      isbn:
        description: "International Standard Book Number"
        range: string
      publisher:
        description: "Publisher of the book"
        range: string
      number_of_pages:
        description: "Total number of pages"
        range: integer
      genre:
        description: "Genre of the book"
        range: BookGenre
      format:
        description: "Format of the book (e.g., Hardcover, Paperback, Ebook)"
        range: BookFormat

  Album:
    is_a: CreativeWork
    description: "Musical works released in a collection (album)"
    attributes:
      release_date:
        description: "Release date of the album"
        range: date
      record_label:
        description: "Record label that released the album"
        range: string
      genre:
        description: "Musical genre of the album"
        range: MusicGenre
      tracklist:
        description: "List of tracks in the album"
        range: string

  Art:
    is_a: CreativeWork
    description: "Works of visual art, including paintings, sculptures, and digital art"
    attributes:
      medium:
        description: "Medium used in the artwork (e.g., oil, watercolor, digital)"
        range: ArtMedium
      dimensions:
        description: "Dimensions of the artwork"
        range: string
      style:
        description: "Artistic style of the artwork (e.g., abstract, realism)"
        range: ArtStyle
      gallery:
        description: "Gallery where the artwork is displayed or housed"
        range: string

  Film:
    is_a: CreativeWork
    description: "Motion picture works, including movies and short films"
    attributes:
      director:
        description: "Director of the film"
        range: string
      release_date:
        description: "Release date of the film"
        range: date
      cast:
        description: "Cast members of the film"
        range: string
      genre:
        description: "Genre of the film"
        range: FilmGenre
      running_time:
        description: "Total running time of the film"
        range: string

  Software:
    is_a: CreativeWork
    description: "Computer software and applications"
    attributes:
      developer:
        description: "Developer of the software"
        range: string
      release_date:
        description: "Release date of the software"
        range: date
      version:
        description: "Version of the software"
        range: string
      platform:
        description: "Platform for which the software is developed"
        range: SoftwarePlatform
```
