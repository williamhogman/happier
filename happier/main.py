import happier.sources as sources
import happier.util as util
from happier.black_fmt import black
from happier.perform_autoflake import perform_autoflake
from happier.sort_imports import sort_imports


def main():
    root = util.find_root()
    fileset = list(sources.iter_source_code([root]))
    for f in fileset:
        sort_imports(f)
        perform_autoflake(f)
    black(root)
