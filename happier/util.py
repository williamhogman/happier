import os
import os.path

ROOTS = {
    "pyproject.toml",
    "requirements.txt",
    "Pipfile",
}


def find_root(cwd: str = None, max_jumps: int = 7):
    if cwd is None:
        return os.getcwd()
    if max_jumps == 0:
        return None

    files = {f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))}

    roots_found = files.intersection(ROOTS)

    if len(roots_found) > 0:
        return cwd
    else:
        return find_root(os.path.abspath(os.path.join(cwd, "..")))
