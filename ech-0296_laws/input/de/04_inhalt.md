\newpage

# Inhalt

Der Erlass selbst ist das Element `akn:act`. Es trägt den Erlasstyp im Attribut `@name`, dazu die Metadaten, den Vorspann, eine allfällige Präambel und den Hauptteil.

{{include:ech-0296_laws/output/docs/Act.md}}

{{include:ech-0296_laws/output/docs/ActTypeEnum.md}}

## Vorspann und Präambel

{{include:ech-0296_laws/output/docs/Preface.md}}

{{include:ech-0296_laws/output/docs/PrefaceP.md}}

{{include:ech-0296_laws/output/docs/Preamble.md}}

## Gesetzeshierarchie

Die Gliederung eines Erlasses ist rekursiv: Buch, Titel, Teil, Kapitel, Unterkapitel, Abschnitt und Unterabschnitt können ineinander verschachtelt werden, bis auf der untersten Ebene der Artikel steht. Welche Ebene in welcher vorkommen darf, ist nicht durch die Struktur selbst, sondern durch die Fedlex-Regeln bestimmt.

Eine Eigenheit ist `akn:level`: Seine erlaubten Kinder sind diejenigen des nächsten Vorfahren, der selbst kein `level` ist. Das lässt sich in einem XSD nicht ausdrücken und wird deshalb über Schematron geprüft (FLX-HR-001-lv).

{{include:ech-0296_laws/output/docs/ActBody.md}}

{{include:ech-0296_laws/output/docs/Book.md}}

{{include:ech-0296_laws/output/docs/Title.md}}

{{include:ech-0296_laws/output/docs/Part.md}}

{{include:ech-0296_laws/output/docs/Chapter.md}}

{{include:ech-0296_laws/output/docs/Subchapter.md}}

{{include:ech-0296_laws/output/docs/Section.md}}

{{include:ech-0296_laws/output/docs/Subsection.md}}

{{include:ech-0296_laws/output/docs/Level.md}}

## Artikel und Absätze

{{include:ech-0296_laws/output/docs/Article.md}}

{{include:ech-0296_laws/output/docs/Subdivision.md}}

{{include:ech-0296_laws/output/docs/Paragraph.md}}

{{include:ech-0296_laws/output/docs/Transitional.md}}

{{include:ech-0296_laws/output/docs/Proviso.md}}

## Blockinhalte

Auf der untersten Ebene stehen die Inhaltsblöcke: Absätze, Listen und Tabellen.

{{include:ech-0296_laws/output/docs/Content.md}}

{{include:ech-0296_laws/output/docs/BlockParagraph.md}}

{{include:ech-0296_laws/output/docs/BlockList.md}}

{{include:ech-0296_laws/output/docs/BlockListItem.md}}

{{include:ech-0296_laws/output/docs/Table.md}}

{{include:ech-0296_laws/output/docs/TableRow.md}}

{{include:ech-0296_laws/output/docs/TableCell.md}}
