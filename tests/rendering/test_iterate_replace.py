
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
        for subnode, item in node.iterate([1, 2, 3, 4]):
            xitem = subnode.xitem
            xitem.replace(None, xitem.yitem)
            xitem.a.content = item

def test_model(capsys, pure):
    model = Model()
    template.render(model)
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
