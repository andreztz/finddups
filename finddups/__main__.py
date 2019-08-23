import argparse
from pathlib import Path
from finddups import _hash, find_duplicate
import errno
import os


def is_path(path):
    path = Path(path)
    if not path.is_dir() and not path.exists():
        raise argparse.ArgumentTypeError(
            "{} - Directory not found.".format(path.resolve())
        )
    return path.resolve


def main():
    parser = argparse.ArgumentParser(
        description="Find and delete duplicate files."
    )
    parser.add_argument(
        "--dir", type=is_path, required=True, help="Target directory."
    )
    parser.add_argument(
        "--file-type", default="*", help="Find specific file type."
    )
    parser.add_argument(
        "--hash-type", default="sha256", help="Cryptographic hash function."
    )

    args = parser.parse_args()

    path = args.dir()
    ftype = args.file_type
    htype = args.hash_type
    # try:
    files = find_duplicate(path, ftype, htype=htype)

    for key, values in files.items():
        print(key)
        print(len(values))
        for item in values:
            print(item)
    # TODO: Format Output
    # TODO: send to trash
    # >>> from send2trash import send2trash
    # >>> send2trash('some_file')
    # except Exception as exc:
    #     print(exc)


if __name__ == "__main__":
    main()
