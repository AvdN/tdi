
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <node tdi="nested">
        <node tdi="subnested"></node>
    </node><tdi tdi=":-nested">
    </tdi>
    <xnode tdi="a"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        node.nested.repeat(self.repeat_nested, [1, 2, 3, 4])
        return True

    def repeat_nested(self, node, item):
        node['j'] = item

    def render_subnested(self, node):
        node.content = u'should be here %s' % node.ctx[1]

    def render_a(self, node):
        node.content = u"should not be here"


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <node j="1">
        <node>should be here 1</node>
    </node>
    <node j="2">
        <node>should be here 2</node>
    </node>
    <node j="3">
        <node>should be here 3</node>
    </node>
    <node j="4">
        <node>should be here 4</node>
    </node>
    <xnode></xnode>
</node>
"""
