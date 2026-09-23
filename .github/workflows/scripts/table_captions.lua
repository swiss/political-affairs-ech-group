-- Beschriftet die Tabellen der generierten Schema-Doku nach eCH-0003-Vorlage:
-- Absatz im Stil "Beschriftung" unter der Tabelle, "Tabelle N: Text", wobei N
-- ein Word-Feld SEQ ist. Das Tabellenverzeichnis im Anhang (TOC \c "<Label>")
-- findet die Tabellen ueber dieses Feld.
--
-- Beschriftet werden nur Tabellen direkt unter einer Ebene-3-Ueberschrift
-- (Attribute, Verwendungen, Zulaessige Werte). Deckblatt und Anhang-Tabellen
-- bleiben ohne Beschriftung, wie in der Vorlage.

local labels = { de = 'Tabelle', fr = 'Tableau', en = 'Table' }

local label = 'Tabelle'
local h2 = nil  -- Klasse bzw. Enum, zu der die Tabelle gehoert
local h3 = nil  -- Abschnitt: Attribute, Verwendungen, ...

-- "Klasse: Person" -> "Person"
local function element_name(header)
  local text = pandoc.utils.stringify(header.content)
  return (text:gsub('^[^:]*:%s*', ''):gsub('%s+$', ''))
end

local function caption_para(text)
  local field = string.format(
    '<w:fldSimple w:instr=" SEQ %s \\* ARABIC "><w:r><w:t>1</w:t></w:r></w:fldSimple>',
    label)
  local inlines = {
    pandoc.Str(label), pandoc.Space(),
    pandoc.RawInline('openxml', field),
    pandoc.Str(': ' .. text),
  }
  return pandoc.Div({ pandoc.Para(inlines) }, { ['custom-style'] = 'caption' })
end

return {
  {
    Meta = function(meta)
      local lang = meta.lang and pandoc.utils.stringify(meta.lang) or 'de'
      label = labels[lang:sub(1, 2)] or label
    end,
  },
  {
    traverse = 'topdown',
    Header = function(h)
      if h.level <= 2 then h3 = nil end
      if h.level == 2 then h2 = element_name(h) end
      if h.level == 3 then h3 = pandoc.utils.stringify(h.content) end
      if h.level > 3 then h3 = nil end
      return h, false
    end,
    Table = function(t)
      if not (h2 and h3) then return t, false end
      local text = h2 .. ' – ' .. h3
      h3 = nil  -- nur die erste Tabelle nach der Ueberschrift
      return { t, caption_para(text) }, false
    end,
  },
}
