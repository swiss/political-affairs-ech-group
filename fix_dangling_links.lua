-- Replace internal links whose #anchor has no matching header with plain text.
-- (LinkML type refs like [String](#String) point to non-existent sections;
--  Word tolerates dangling links, Typst errors on missing labels.)
function Pandoc(doc)
  local ids = {}
  doc:walk({ Header = function(h)
    if h.identifier and h.identifier ~= '' then ids[h.identifier] = true end
  end })
  return doc:walk({ Link = function(l)
    if l.target:sub(1,1) == '#' and not ids[l.target:sub(2)] then
      return l.content
    end
    return l
  end })
end
