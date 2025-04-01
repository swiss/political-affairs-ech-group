function read_file(filename)
    print("Reading file: " .. filename)
    local f = io.open(filename, "r")
    if not f then
        io.stderr:write("Cannot open file: " .. filename .. "\n")
        return ""
    end
    local content = f:read("*all")
    f:close()
    return content
end

function process_includes(el)
    if el.t == "Para" then
        -- Convert paragraph elements into a single string
        local text = pandoc.utils.stringify(el)
        print("Processing paragraph: " .. text)

        -- Extract the filename using pattern matching
        local filename = text:match("^!include%s+(.+)$")
        print("Filename extracted: " .. (filename or "nil"))

        if filename then
            local included_content = read_file(filename)
            if included_content ~= "" then
                return pandoc.read(included_content).blocks
            else
                return { pandoc.Para({ pandoc.Str("[Missing file: " .. filename .. "]") }) }
            end
        end
    end
end

return {
    { Para = process_includes }
}
