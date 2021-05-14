#!/usr/bin/env python3

import argparse
import sys

from fontsize import __version__


def main():  # pragma: no cover
    run(sys.argv[1:])


def run(argv):
    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(
        description="Font file and OpenType table size reporting tool"
    )
    parser.add_argument(
        "--version", action="version", version="font-size v{}".format(__version__)
    )
    args = parser.parse_args(argv)
