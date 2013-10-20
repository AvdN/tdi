
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item"><xnode tdi="xitem"><ynode tdi="yitem">
</ynode></xnode></node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        node.repeat(self.repeat_item, [1, 2, 3, 4])

    def repeat_item(self, node, item):
        node.replace(None, node.xitem, 'foo')

    def render_yitem(self, node):
        node.content = repr(node.ctx)


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<xnode><ynode>(0, 1, ())</ynode></xnode><xnode><ynode>(1, 2, ())</ynode></xnode><xnode><ynode>(2, 3, ())</ynode></xnode><xnode><ynode>(3, 4, ())</ynode></xnode>
"""
