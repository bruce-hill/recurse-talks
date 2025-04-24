-- Add target="_blank" and rel="noreferrer" to external links
function Link(el)
    if el.target:match("^[a-z]*://") then
        el.attr.attributes.target = "_blank"
        el.attr.attributes.rel = "noreferrer"
    end
    return el
end
