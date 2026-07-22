// eCH PDF template for the per-language PDF export via `pandoc --pdf-engine=typst`.
// The DOCX pipeline is unaffected; this is only used for PDF output.
// Logo path is resolved against the Typst root (pass --pdf-engine-opt=--root=<repo>).

#let ech-grey = rgb("#7f7f7f")
#let ech-logo = "/ech-0292_meta/input/ech-logo.png"
#let footer-info = "$footer-info$"

$if(title)$#set document(title: "$title$")$endif$

#set page(
  paper: "a4",
  margin: (left: 2.5cm, right: 2cm, top: 2.6cm, bottom: 2cm),
  header: context {
    grid(
      columns: (1fr, auto),
      align(bottom)[#box(baseline: 35%, image(ech-logo, height: 1.2cm)) #text(11pt, fill: black)[E-Government Standards]],
      align(bottom + right)[#text(9pt, fill: ech-grey)[Page #counter(page).display() of #counter(page).final().first()]],
    )
    v(3pt)
    line(length: 100%, stroke: 0.6pt + ech-grey)
  },
  footer: context {
    line(length: 100%, stroke: 0.6pt + ech-grey)
    v(3pt)
    set text(8pt, fill: ech-grey)
    grid(columns: (1fr, auto),
      [eCH registered association],
      align(right)[www.ech.ch / info\@ech.ch],
    )
    v(2pt)
    text(size: 8pt, fill: ech-grey)[#footer-info]
  },
)

#set text(font: ("Arial", "Liberation Sans", "Arimo"), size: 10pt$if(lang)$, lang: "$lang$"$endif$)
// Left-aligned (ragged right) body to match the Word rendering.
#set par(justify: false, leading: 0.6em, spacing: 0.9em)
#set heading(numbering: "1.1")
#show heading: set block(above: 1.2em, below: 0.6em)

// Tables: no outer grid, bold header row, zebra body rows, left/top aligned (like Word).
#set table(
  stroke: none,
  inset: 6pt,
  align: left + top,
  fill: (_, y) => if y == 0 { none } else if calc.odd(y) { luma(242) } else { none },
)
// pandoc emits `align: (auto, auto)` inside an `align(center)` figure, so cells
// inherit centering. Force left/top on every cell to match the Word rendering.
#show table.cell: set align(left + top)
#show table.cell.where(y: 0): set text(weight: "bold")

// Let long tables (pandoc wraps them in a figure) break across pages.
#show figure: set block(breakable: true)

$if(title)$
#v(0.6cm)
#text(19pt, weight: "bold")[$title$]
#v(0.8cm)
$endif$

$body$
