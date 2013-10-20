
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node>
    <xnode tdi="foo"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_foo(self, node):
        try:
            node[u'b\xe9lah'] = u'bl\xf6d'
        except UnicodeError:
            node[u'blah'] = u'bl\xf6d'


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <xnode blah="bl&#246;d"></xnode>
</node>
"""
