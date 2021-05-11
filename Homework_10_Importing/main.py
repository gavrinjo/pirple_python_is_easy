import os
import shutil as sh
import argparse
from pathlib import Path

"""
Simple copy files script.
It uses "shutil copy2" to copy files including meta data.
Also uses "argparse" for command line arguments, since it is by design to compile script and use it as cmd tool.
And "pathlib" to make the path absolute, resolving all symlinks on the way. 
"""


parser = argparse.ArgumentParser(prog="Copy", description="Just a small showcase using 'argparse', 'pathlib' and 'shutil' modules for copying files")

# NOTE - Add the arguments
parser.add_argument("s", metavar="[Source]", type=str, help="absolute path and filename or subdirectory and filename. "
                                                            "Make the path absolute, resolving all symlinks on the way")
parser.add_argument("t", metavar="[Destination]", type=str, help="location to copy to")

# NOTE - Execute parse_args()
args = parser.parse_args()


def path_resolve(src):

    operand = [".", "*.*", "*"]

    try:
        if Path(src).resolve().exists():
            return Path(src).resolve()
        else:
            print("Bad command, invalid path or filename")
    except OSError:
        if src.split("\\")[-1] in operand:
            if Path("/".join(src.split("\\")[:-1])).resolve().exists():
                return Path("/".join(src.split("\\")[:-1])).resolve()
            else:
                print("Bad command, invalid path or filename")


def copy(src, dst):
    if path_resolve(src).is_file():
        sh.copy2(src, Path(dst).resolve())
    else:
        for obj in Path(path_resolve(src)).glob("*.*"):
            sh.copy2(Path(obj), Path(dst).resolve())


if __name__ == '__main__':
    copy(args.s, args.t)
