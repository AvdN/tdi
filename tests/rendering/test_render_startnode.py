
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="nested">
    <xnode tdi="a"></xnode>
</node>
""".lstrip())

class Model(object):

    def render_a(self, node):
        node.content = u'hey'


def test_model(capsys, pure):
    model = Model()
    template.render(model, startnode='nested.a')
    print
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<xnode>hey</xnode>
"""
