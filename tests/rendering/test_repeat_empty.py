
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
        node.nested.repeat(self.repeat_nested, [])
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
    \n\
    <xnode></xnode>
</node>
"""
