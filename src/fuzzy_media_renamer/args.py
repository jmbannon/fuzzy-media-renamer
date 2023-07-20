import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--tvdb_id", "-db", type=str, required=True)
parser.add_argument(
    "path",
    metavar="PATH",
    nargs="*",
    help="path to media file(s) and/or directories",
)
