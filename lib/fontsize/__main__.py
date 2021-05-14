#!/usr/bin/env python3

import argparse
import os
import sys

from rich.console import Console
from rich.table import Table

from . import __version__
from .size import FontSize


def main():  # pragma: no cover
    run(sys.argv[1:])


def run(argv):
    # rich package console objects
    console = Console()
    error_console = Console(stderr=True)
    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(
        description="Font file and OpenType table size reporting tool"
    )
    parser.add_argument(
        "--version", action="version", version="font-size v{}".format(__version__)
    )
    parser.add_argument("FONTPATHS", help="One or more font file paths", nargs="*")

    args = parser.parse_args(argv)

    for fontpath in args.FONTPATHS:
        # validations
        if not os.path.exists(fontpath):
            error_console.print(
                f"[bold red][ERROR][/] {fontpath} does not appear to be a valid "
                f"file path. Please enter a path to a font and try again."
            )
            sys.exit(1)

        # instantiate FontSize object
        # this calculates file size data with a fontTools TTFont obj
        try:
            fontsize = FontSize(fontpath)
        except Exception as e:
            error_console.print(
                f"[bold red][ERROR][/] Attempt to read {fontpath} raised the "
                f"following error: {e}"
            )
            sys.exit(1)

        print()
        console.print(f"[green]{fontpath}[/]\n")

        table = Table(
            title="Summary Statistics", show_header=True, header_style="bold magenta"
        )
        table.add_column("Statistic", style="dim", justify="right")
        table.add_column("Size (B)", justify="right")
        table.add_row(
            "Total",
            f"{fontsize.total_bytes/1.0:.2f}",
        )
        table.add_row(
            f"Avg per encoded glyph ({fontsize.encoded_glyphs})",
            f"{fontsize.per_enc_glyph_bytes:.2f}",
        )
        table.add_row(
            f"Avg per total glyph ({fontsize.total_glyphs})",
            f"{fontsize.per_total_glyph_bytes:.2f}",
        )
        console.print(table)

        tt_tables = fontsize.get_table_tags()

        table_ottables = Table(
            title="OpenType Table Sizes",
            show_header=True,
            header_style="bold magenta",
            show_lines=True,
        )
        table_ottables.add_column(
            "OpenType Table", style="dim", width=25, justify="right"
        )
        table_ottables.add_column("Size (B)", justify="right")
        table_ottables.add_column("% Total", justify="right")
        for tt_table in sorted(tt_tables):
            size = fontsize.tables[tt_table]
            percent_size = (size / fontsize.total_bytes) * 100
            table_ottables.add_row(f"{tt_table}", f"{size}", f"{percent_size:.3f}")
        print()
        console.print(table_ottables)
