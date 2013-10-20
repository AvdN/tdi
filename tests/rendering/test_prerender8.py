
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<x tdi="xnode">
    <y tdi="ynode">
        <z tdi="znode">
        </z>
    </y>
</x>
<a tdi=":xnode">
    <b tdi="bnode">
    </b>
</a>
""".lstrip())

class Model(object):

    def render_xnode(self, node):
        node.repeat(None, u"abc")

    def render_znode(self, node):
        node.content = node.ctx[1]

    def render_bnode(self, node):
        node.content = u', '.join(node.ctx[1])



def test_model(capsys, pure):
    template.render(prerender=Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<x>
    <y>
        <z>a</z>
    </y>
</x><a>
    <b>a, b</b>
</a><x>
    <y>
        <z>b</z>
    </y>
</x><a>
    <b>b, c</b>
</a><x>
    <y>
        <z>c</z>
    </y>
</x>

"""
