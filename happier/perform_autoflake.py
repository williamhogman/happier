import argparse
import sys

import autoflake


def perform_autoflake(f):
    args = argparse.Namespace()
    args.remove_all_unused_imports = True
    args.ignore_init_module_imports = True
    args.remove_duplicate_keys = True
    args.imports = ""
    args.expand_star_imports = True
    args.remove_unused_variables = True
    args.check = False
    args.in_place = True
    autoflake.fix_file(f, args, sys.stdout)
