
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item"><xnode tdi="xitem"><ynode tdi="yitem">
<a tdi="-a" />
</ynode></xnode></node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        node.xitem.yitem
        node.repeat(None, [1, 2, 3, 4])

    def render_xitem(self, node):
        ctx = node.ctx
        node.replace(None, node.yitem).ctx = ctx

    def render_a(self, node):
        node.content = node.ctx[1]


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node><ynode>
1
</ynode></node><node><ynode>
2
</ynode></node><node><ynode>
3
</ynode></node><node><ynode>
4
</ynode></node>
"""
