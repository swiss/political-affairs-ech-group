\newpage

# Inhalt

Der Erlass selbst ist das Element `akn:act`. Es trägt den Erlasstyp im Attribut `@name`, dazu die Metadaten, den Vorspann, eine allfällige Präambel und den Hauptteil.

{{include:ech-0296_laws/output/docs/Act.md}}

{{include:ech-0296_laws/output/docs/ActTypeEnum.md}}

## Vorspann und Vorspruch

Der Vorspann trägt, was den Erlass benennt: Nummer, Titel, Kurztitel, Abkürzung und Datum. Wie fein das ausgezeichnet wird, unterscheidet sich zwischen den Ebenen. Fedlex setzt Nummer und Titel in je einen eigenen Absatz und lässt den Rest als Fliesstext stehen; der Kanton Zürich zeichnet in *einem* Absatz die Ordnungsnummer, den Erlasstitel, den Kurztitel, die Abkürzung und das Datum je einzeln aus.

Deshalb sind diese Angaben nicht eigene Felder des Absatzes, sondern Inline-Elemente wie die Textauszeichnung: Nur so bleibt ihre Reihenfolge untereinander erhalten. Die Anforderung von Fedlex — Nummer und Titel müssen im Vorspann vorkommen (FLX-PF-001 und -002) — ist damit eine Regel über den Inhalt, nicht über die Struktur.

{{include:ech-0296_laws/output/docs/Preface.md}}

{{include:ech-0296_laws/output/docs/PrefaceP.md}}

{{include:ech-0296_laws/output/docs/DocNumber.md}}

{{include:ech-0296_laws/output/docs/DocTitle.md}}

{{include:ech-0296_laws/output/docs/DocketNumber.md}}

{{include:ech-0296_laws/output/docs/ShortTitle.md}}

{{include:ech-0296_laws/output/docs/Abbr.md}}

{{include:ech-0296_laws/output/docs/DocDate.md}}

### Vorspruch

Der Vorspruch nennt, wer den Erlass beschliesst und worauf er sich beruft: die Eingangsformel, die Erwägungen und die weiteren Absätze.

{{include:ech-0296_laws/output/docs/Preamble.md}}

{{include:ech-0296_laws/output/docs/Formula.md}}

{{include:ech-0296_laws/output/docs/Citations.md}}

{{include:ech-0296_laws/output/docs/Citation.md}}

## Schlussformel und Beilagen

Am Ende eines Erlasses stehen Ort, Datum und Unterschriften — im Kanton Zürich als `akn:conclusions`, das Fedlex nicht führt. Beilagen stehen in `akn:attachments`; jede Beilage ist wieder ein vollständiger Erlass, weshalb sie dieselbe Klasse verwendet.

{{include:ech-0296_laws/output/docs/Conclusions.md}}

{{include:ech-0296_laws/output/docs/Attachments.md}}

{{include:ech-0296_laws/output/docs/Attachment.md}}

{{include:ech-0296_laws/output/docs/ComponentRef.md}}

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

Auf der untersten Ebene stehen die Inhaltsblöcke: Absätze, Listen und Tabellen. Sie stehen nicht in getrennten Listen je Art, sondern in einer einzigen geordneten Folge — `content_blocks` —, weil ein Absatz im Erlass auf eine Aufzählung folgen kann und darauf wieder ein Absatz. Getrennte Listen würden diese Reihenfolge verlieren; in der Bundesverfassung betrifft das 23 Stellen. Welche Art ein Eintrag hat, sagt er selbst über `element_type` — dasselbe Verfahren, mit dem auch die Textauszeichnung ihre Reihenfolge hält.

{{include:ech-0296_laws/output/docs/BlockElement.md}}

{{include:ech-0296_laws/output/docs/Content.md}}

{{include:ech-0296_laws/output/docs/BlockParagraph.md}}

{{include:ech-0296_laws/output/docs/BlockList.md}}

{{include:ech-0296_laws/output/docs/BlockListItem.md}}

{{include:ech-0296_laws/output/docs/Table.md}}

{{include:ech-0296_laws/output/docs/TableRow.md}}

{{include:ech-0296_laws/output/docs/TableCell.md}}

## Anhänge

Ein Erlass kann Dokumente mitführen, die nicht Teil seines Artikeltextes sind — im Bundesrecht regelmässig einen Anhang. Solche Dokumente stehen in `akn:components` und sind je ein eigenes `akn:doc` mit eigenem Vorspann und eigenem Hauptteil. Beim Öffentlichkeitsgesetz enthält der Anhang die Änderung bisherigen Rechts, beim Datenschutzgesetz ebenso.

Zwei Eigenheiten sind dabei festzuhalten. Erstens wiederholt der Anhang in den Fedlex-Dateien die Identifikation des Erlasses unverändert — dieselben ELI-URIs, dieselben Daten und Namen. Er ist also nicht eigenständig identifiziert, sondern Teil desselben Werks. Zweitens nutzt sein Vorspann nicht die Absatzstruktur des Erlasses, sondern die generischen Behälter `akn:container` und `akn:block`. Deren `@name` ist in AKN frei wählbar; dieser Standard führt die Werte, die Fedlex tatsächlich verwendet, als Aufzählung: `headerOfAnnex` für den Behälter, `heading` und `num` für den Block.

Der Hauptteil eines Anhangs (`akn:mainBody`) kennt die Gesetzeshierarchie nicht. Er nimmt Absätze und Ebenen unmittelbar auf — und darin wieder dieselben Inhalts- und Auszeichnungselemente wie der Erlass selbst, bis hin zur Fussnote mit Verweis auf die Amtliche Sammlung.

{{include:ech-0296_laws/output/docs/Components.md}}

{{include:ech-0296_laws/output/docs/Component.md}}

{{include:ech-0296_laws/output/docs/Doc.md}}

{{include:ech-0296_laws/output/docs/DocNameEnum.md}}

{{include:ech-0296_laws/output/docs/MainBody.md}}

{{include:ech-0296_laws/output/docs/Container.md}}

{{include:ech-0296_laws/output/docs/ContainerNameEnum.md}}

{{include:ech-0296_laws/output/docs/Block.md}}

{{include:ech-0296_laws/output/docs/BlockNameEnum.md}}
