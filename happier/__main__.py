""""""
import sys



from happier.sort_imports import sort_imports
from happier.black_fmt import black
import happier.sources as sources
import happier.util as util



def main():
    root = util.find_root()
    fileset = list(sources.iter_source_code([root]))
    for f in fileset:
        sort_imports(f)
        perform_autoflake(f)
    black(root)


main()
