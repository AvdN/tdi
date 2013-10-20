
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<x tdi="xnode">
    <y tdi="ynode">
        <z tdi="znode">
        </z>
    </y>
</x>
""".lstrip())

class Model(object):

    def render_xnode(self, node):
        node.repeat(None, "abc")

    def render_znode(self, node):
        node.content = node.ctx[1]



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
</x><x>
    <y>
        <z>b</z>
    </y>
</x><x>
    <y>
        <z>c</z>
    </y>
</x>
"""
