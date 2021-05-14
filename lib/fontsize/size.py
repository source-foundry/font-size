#!/usr/bin/env python3

import os

from fontTools.ttLib import TTFont


class FontSize(object):
    def __init__(self, filepath):
        self.ttfont = TTFont(filepath)
        self.filepath = filepath
        self.total_glyphs = 0
        self.encoded_glyphs = 0
        self.total_bytes = 0
        self.per_enc_glyph_bytes = 0.0
        self.per_total_glyph_bytes = 0.0
        self.tables = {}
        self._calculate_sizes()

    def _calculate_sizes(self):
        self.total_bytes = os.path.getsize(self.filepath)
        self._calc_per_encoded_glyph_size()
        self._calc_per_total_glyph_size()
        self._calc_table_sizes()

    def _calc_per_encoded_glyph_size(self):
        self.encoded_glyphs = len(self.ttfont.getBestCmap())
        self.per_enc_glyph_bytes = self.total_bytes / self.encoded_glyphs

    def _calc_per_total_glyph_size(self):
        self.total_glyphs = len(self.ttfont.getGlyphSet())
        self.per_total_glyph_bytes = self.total_bytes / self.total_glyphs

    def _calc_table_sizes(self):
        tables = self.get_table_tags()
        for table in tables:
            self.tables[table] = self.ttfont.reader.tables[table].length

    def get_table_tags(self):
        return [tag for tag in self.ttfont.keys() if tag != "GlyphOrder"]
