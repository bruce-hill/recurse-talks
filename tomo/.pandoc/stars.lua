
local yes, no = "★", "☆"
return {
    {
        Str = function(elem)
            local rating, outof = elem.text:match("{{(%d+)/(%d+)}}")
            if rating then
                rating, outof = tonumber(rating), tonumber(outof)
                local s = yes:rep(rating)..no:rep(outof-rating)
                elem = pandoc.Span(pandoc.Str(s))
                elem.attributes.style = "font-size: 1.25em"
            end
            return elem
        end,
    }
}
