from pathlib import Path
import shutil as sh
import argparse

parser = argparse.ArgumentParser(prog="Test", description="Just a small showcase using argument parser and path")

# NOTE - Add the arguments
parser.add_argument("-f", help="File name")
parser.add_argument("s", metavar="[Source location]", type=str, help="Source file location")
parser.add_argument("t", metavar="[Target location]", type=str, help="Destination")

# NOTE - Execute parse_args()
args = parser.parse_args()

filename = args.f
source = Path(args.s).resolve()
target = Path(args.t).resolve()


def copy(src, tar, file):

    if file is None:
        file = "*.*"

    s = Path.joinpath(src, file)
    t = Path.joinpath(tar, file)
    sh.copy2(str(s), str(t))


if __name__ == '__main__':
    copy(source, target, filename)
    print(filename)
    print(source)
    print(target)

