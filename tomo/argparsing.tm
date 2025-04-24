# Show a file tree

func show(path:Path, depth:Int, prefix="")
    say("$prefix$(path.base_name())")
    if path.is_directory() and depth > 0
        for child in path.children()
            show(child, depth-1, prefix++"  ")

func main(paths:[Path], verbose=no, max_depth=99)
    for p in paths
        if verbose
            say("Showing path: $p")
        show(p, max_depth)
