import hashlib
from pathlib import Path


def chunk_reader(f, chunk_size=1024):
    # max chunk_size 65536 ????
    while True:
        data = f.read(chunk_size)
        if not data:
            break
        yield data


def _hash(f, hash_func):
    _hash = hash_func()
    with open(f, "rb") as f:
        for data in chunk_reader(f):
            _hash.update(data)
    return _hash.hexdigest()


def find_duplicate(folder, ftype="*", **kwargs):
    """
    # https://docs.python.org/3.7/library/hashlib.html#hash-algorithms
    folder -> path to target
    ftype -> find only by ftype (ex.: .pdf)
    htype -> function hash.
    return {hash: ["path/file1.ext", "other_path/file1.ext"...] ...}
    """

    hash_func = kwargs.get("htype", "sha256")

    if not hasattr(hashlib, hash_func):
        msg = (
            "{} is not hash function.\n"
            "see: https://docs.python.org/3.7/library/hashlib.html#hash-algorithms"
        )

        raise ValueError(msg.format(hash_func))

    hash_func = getattr(hashlib, hash_func)

    dups = {}

    files = Path(folder).rglob("*.{}".format(ftype))

    for file in files:
        if file.is_file():
            dups.setdefault(_hash(file, hash_func), []).append(file)

    # RuntimeError: dictionary changed size during iteration ????
    for key, value in dups.copy().items():
        if len(value) <= 1:
            del dups[key]

    return dups
