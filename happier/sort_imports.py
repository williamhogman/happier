import isort


def sort_imports(f):
    isort.SortImports(
        f,
        multi_line=3,
        trailing_comma=True,
        use_parentheses=True,
        line_width=88,
        q=True,
    )
