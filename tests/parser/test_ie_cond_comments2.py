
from tdi._test_support import pure, dedent

from tdi.markup.soup import parser as _parser
from tdi.markup.soup import decoder as _decoder

def test_ie_cond_comments2(capsys, pure):
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


    builder = Builder()
    parser = _parser.SoupParser.html(builder)
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
        ('handle_text', ('<!--[if !IE 8]>',)),
        ('handle_text', ('\n    ',)),
        ('handle_starttag', ('xnode', [('tdi', '"foo"')], False,
            '<xnode tdi="foo">')),
        ('handle_endtag', ('xnode', '</xnode>')),
        ('handle_text', ('\n    ',)),
        ('handle_text', ('<![endif]-->',)),
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
