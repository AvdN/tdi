#!/usr/bin/env python
import warnings as _warnings
_warnings.resetwarnings()
_warnings.filterwarnings('error')

from tdi import LexerEOFError
from tdi.markup.soup import parser as _parser
from tdi.markup.soup import decoder as _decoder
from tdi.markup.soup import dtd as _dtd


class Builder(object):
    def __init__(self):
        self.events = []
        self.decoder = _decoder.HTMLDecoder('ascii')
    def __getattr__(self, name):
        if name.startswith('handle_'):
            def method(*args):
                self.events.append((name, args))
            return method
        raise AttributeError(name)


class Lexer(_parser.SoupLexer):
    def without(cls, listener):
        return cls(listener, conditional_ie_comments=False)
    without = classmethod(without)


builder = Builder()
parser = _parser.SoupParser(builder, _dtd.HTMLDTD(),
    lexer=Lexer.without
)
parser.feed("""
<node>
    <![if !IE 8]>
    <xnode tdi="foo"></xnode>
    <![endif]>
</node>
""".strip().replace('\r\n', '\n').replace('\r', '\n'))
try:
    parser.finalize()
except LexerEOFError, e:
    print str(e) == "Unfinished parser state MSECTION"
