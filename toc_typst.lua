-- For Typst output, replace the Word TOC field (raw openxml block) with a
-- Typst #outline() at the same spot (under the "Inhaltsverzeichnis" heading).
function RawBlock(el)
  if el.format == 'openxml' and el.text:find('TOC') then
    if FORMAT:match('typst') then
      return pandoc.RawBlock('typst', '#outline(title: none, indent: auto, depth: 2)')
    end
  end
  return el
end
