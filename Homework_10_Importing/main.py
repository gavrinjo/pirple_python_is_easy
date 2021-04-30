import os
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
source = args.s
target = args.t


def copy(src, tar, file):
    if file is None:
        file = "*.*"  # ! This is not good, needs to be made in for loop

    s = os.path.join(src, file)
    t = tar
    sh.copy2(s, t)


if __name__ == '__main__':
    copy(source, target, filename)
    print(filename)
    print(source)
    print(target)
