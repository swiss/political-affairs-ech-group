\newpage

# Textauszeichnung

Innerhalb eines Absatzes, einer Überschrift, einer Nummer oder einer Tabellenzelle steht Text nicht für sich: Er ist mit Verweisen, Hervorhebungen, Fussnoten und Platzhaltern durchsetzt, und zwar in der Reihenfolge, in der er gelesen wird. Dieser gemischte Inhalt wird nicht als undurchsichtige Zeichenkette abgelegt, sondern als geordnete Liste eigener Klassen. Ein Textstück und ein Auszeichnungselement sind dabei gleichrangige Geschwister — dafür steht `TextRun`, der einen reinen Zeichenlauf trägt.

Diese Modellierung ist aufwendiger als ein einzelnes Textfeld, aber sie ist die Voraussetzung dafür, dass ein Verweis auf einen anderen Erlass maschinell auffindbar bleibt und eine Fussnote ihren eigenen Inhalt behält, statt im Fliesstext aufzugehen.

{{include:ech-0296_laws/output/docs/MixedText.md}}

{{include:ech-0296_laws/output/docs/InlineElement.md}}

{{include:ech-0296_laws/output/docs/TextRun.md}}

{{include:ech-0296_laws/output/docs/Ref.md}}

{{include:ech-0296_laws/output/docs/AuthorialNote.md}}

{{include:ech-0296_laws/output/docs/Inline.md}}

{{include:ech-0296_laws/output/docs/Placeholder.md}}

{{include:ech-0296_laws/output/docs/Span.md}}

{{include:ech-0296_laws/output/docs/B.md}}

{{include:ech-0296_laws/output/docs/I.md}}

{{include:ech-0296_laws/output/docs/Sup.md}}

{{include:ech-0296_laws/output/docs/Br.md}}

{{include:ech-0296_laws/output/docs/XmlContent.md}}

## Auszeichnungen der kantonalen Praxis

Der Kanton Zürich zeichnet im Text mehr aus als der Bund: den definierten Begriff, den Verweis auf eine Anmerkung, die handelnde Person und ihre Rolle, das Datum im Fliesstext, die Unterschriftszeile und den Zeilenumbruch innerhalb eines Absatzes. Person und Rolle verweisen dabei auf ihre Deklaration im Referenzblock, statt den Namen bloss hinzuschreiben.

{{include:ech-0296_laws/output/docs/Def.md}}

{{include:ech-0296_laws/output/docs/NoteRef.md}}

{{include:ech-0296_laws/output/docs/Person.md}}

{{include:ech-0296_laws/output/docs/Role.md}}

{{include:ech-0296_laws/output/docs/DateInline.md}}

{{include:ech-0296_laws/output/docs/Signature.md}}

{{include:ech-0296_laws/output/docs/Eol.md}}
