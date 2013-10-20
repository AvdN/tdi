
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item"><xnode tdi="xitem"></xnode></node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        xnode = node.copy()
        def foo(node, item):
            node.content = item
        node.xitem.replace(None, xnode).repeat(foo, (1, 2))


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node><node>1</node><node>2</node></node>
"""
