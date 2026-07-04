"""Markdown extension: normalize [toc] -> [TOC] before toc extension runs.

Python-Markdown 3.10.2's toc extension does case-SENSITIVE matching for the
[ TOC ] marker. Some editors/ tools auto-lowercase [ TOC ] to [toc], which
breaks the generated table of contents. This preprocessor fixes it early in the
pipeline so the toc tree-processor always finds [ TOC ] regardless of what the
source file actually contains.
"""

import re
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class FixTocMarkerPreprocessor(Preprocessor):
    """Normalise [toc] → [TOC] in the raw markdown source lines."""

    _RE = re.compile(r'\[toc\]')

    def run(self, lines):
        return [self._RE.sub('[TOC]', line) for line in lines]


class FixTocMarkerExtension(Extension):
    """Register the preprocessor at priority 0 (runs before everything else)."""

    def extendMarkdown(self, md):
        md.preprocessors.register(
            FixTocMarkerPreprocessor(md), 'fix_toc_marker', 0
        )


def makeExtension(**kwargs):
    return FixTocMarkerExtension(**kwargs)
