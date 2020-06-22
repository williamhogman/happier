import subprocess as sp


def black(root: str) -> None:
    sp.run(["python", "-m", "black", "-q", root])
