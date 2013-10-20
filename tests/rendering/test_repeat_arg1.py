
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <node tdi="nested">
        <node tdi="subnested"></node>
    </node><tdi tdi=":-nested">
    </tdi>
</node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        def sep(node):
            node.hiddenelement = False
        node.nested.repeat(
            callback=self.repeat_nested, itemlist=[1, 2, 3, 4], separate=sep
        )
        return True

    def repeat_nested(self, node, item):
        node['j'] = item


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <node j="1">
        <node></node>
    </node><tdi>
    </tdi><node j="2">
        <node></node>
    </node><tdi>
    </tdi><node j="3">
        <node></node>
    </node><tdi>
    </tdi><node j="4">
        <node></node>
    </node>
</node>
"""
