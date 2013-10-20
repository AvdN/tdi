
from tdi._test_support import pure, dedent

from tdi.markup.soup import parser as _parser
from tdi.markup.soup import decoder as _decoder
from tdi.markup.soup import dtd as _dtd

def test_ie_cond_comments4(capsys, pure):
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
    parser.feed(dedent("""
    <node>
        <!--[if !IE 8]>
        <xnode tdi="foo"></xnode>
        <![endif]-->
    </node>
    """, normalize=True))
    parser.finalize()

    print builder.events == [
        ('handle_starttag', ('node', [], False, '<node>')),
        ('handle_text', ('\n    ',)),
        ('handle_comment', (
            '<!--[if !IE 8]>\n    <xnode tdi="foo"></xnode>\n    <![endif]-->',
        )),
        ('handle_text', ('\n',)),
        ('handle_endtag', ('node', '</node>'))
    ]

    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
True
"""
