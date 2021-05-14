from pathlib import Path

from fontTools.ttLib import TTFont

import pytest

from fontsize.size import FontSize


def get_ttf_fontpath():
    return Path("tests/fonts/Inter-Regular.ttf")


def get_otf_fontpath():
    return Path("tests/fonts/Inter-Regular.otf")


def get_woff_fontpath():
    return Path("tests/fonts/Inter-Regular.woff")


def get_woff2_fontpath():
    return Path("tests/fonts/Inter-Regular.woff2")


def test_fontsize_obj_instantiation_with_ttf():
    fs = FontSize(get_ttf_fontpath())
    assert type(fs.ttfont) is TTFont
    assert fs.filepath == get_ttf_fontpath()
    assert fs.total_glyphs == 2548
    assert fs.encoded_glyphs == 2500
    assert fs.total_bytes == 680112
    assert fs.per_enc_glyph_bytes == 680112 / 2500
    assert fs.per_total_glyph_bytes == 680112 / 2548
    assert len(fs.tables) == 17
    expected_tables = [
        "GDEF",
        "GPOS",
        "GSUB",
        "OS/2",
        "cmap",
        "cvt ",
        "fpgm",
        "gasp",
        "glyf",
        "head",
        "hhea",
        "hmtx",
        "loca",
        "maxp",
        "name",
        "post",
        "prep",
    ]
    for table in expected_tables:
        assert table in fs.tables

    # confirmed with data output from DTL OTM
    assert fs.tables["GDEF"] == 1030
    assert fs.tables["GPOS"] == 69754
    assert fs.tables["GSUB"] == 22092
    assert fs.tables["OS/2"] == 96
    assert fs.tables["cmap"] == 25916
    assert fs.tables["cvt "] == 316
    assert fs.tables["fpgm"] == 3605
    assert fs.tables["gasp"] == 8
    assert fs.tables["glyf"] == 508792
    assert fs.tables["head"] == 54
    assert fs.tables["hhea"] == 36
    assert fs.tables["hmtx"] == 10190
    assert fs.tables["loca"] == 10196
    assert fs.tables["maxp"] == 32
    assert fs.tables["name"] == 1682
    assert fs.tables["post"] == 25775
    assert fs.tables["prep"] == 239


def test_fontsize_obj_instantiation_with_otf():
    fs = FontSize(get_otf_fontpath())
    assert type(fs.ttfont) is TTFont
    assert fs.filepath == get_otf_fontpath()
    assert fs.total_glyphs == 2548
    assert fs.encoded_glyphs == 2500
    assert fs.total_bytes == 254772
    assert fs.per_enc_glyph_bytes == 254772 / 2500
    assert fs.per_total_glyph_bytes == 254772 / 2548
    assert len(fs.tables) == 12
    expected_tables = [
        "CFF ",
        "GDEF",
        "GPOS",
        "GSUB",
        "OS/2",
        "cmap",
        "head",
        "hhea",
        "hmtx",
        "maxp",
        "name",
        "post",
    ]
    for table in expected_tables:
        assert table in fs.tables

    # confirmed with data from DTL OTM
    assert fs.tables["CFF "] == 123697
    assert fs.tables["GDEF"] == 1030
    assert fs.tables["GPOS"] == 69754
    assert fs.tables["GSUB"] == 22092
    assert fs.tables["OS/2"] == 96
    assert fs.tables["cmap"] == 25916
    assert fs.tables["head"] == 54
    assert fs.tables["hhea"] == 36
    assert fs.tables["hmtx"] == 10190
    assert fs.tables["maxp"] == 6
    assert fs.tables["name"] == 1650
    assert fs.tables["post"] == 32


# TODO: add woff tests
# TODO: add woff2 tests
