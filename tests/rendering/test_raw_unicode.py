
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node>
    <xnode tdi="foo"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_foo(self, node):
        node.raw.content = u'Andr\xe9 <>'
        node.raw[u'foo'] = u"'Mal\xf3<>'"


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <xnode foo='Mal&#243;<>'>Andr&#233; <></xnode>
</node>
"""
