-- Ueberschriften ohne Kapitelnummer nach eCH-0003-Vorlage.
--
-- In der Vorlage sind nur die Kapitel von der Einleitung bis zu den
-- Urheberrechten nummeriert. Die Formatvorlagen dafuer liegen in
-- input/template.docx; sie heben die Nummerierung von Ueberschrift 1/2 auf:
--
--   # Zusammenfassung {.unnumbered .unlisted}  -> "Nebentitel" (nicht im Inhaltsverzeichnis)
--   # Anhang A – … {.unnumbered}               -> "Anhang Überschrift"
--   ## … {.unnumbered}                         -> "Anhang Überschrift 2"
--
-- Die Ueberschrift wird dabei zum Absatz mit custom-style; die Sprungmarke
-- bleibt ueber die Kennung des Div erhalten.

local styles = { 'Anhang Überschrift', 'Anhang Überschrift 2' }

function Header(h)
  if not h.classes:includes('unnumbered') then return nil end
  local style
  if h.classes:includes('unlisted') then
    style = 'Nebentitel'
  else
    style = styles[h.level]
  end
  if not style then return nil end
  return pandoc.Div({ pandoc.Para(h.content) },
    pandoc.Attr(h.identifier, {}, { ['custom-style'] = style }))
end
