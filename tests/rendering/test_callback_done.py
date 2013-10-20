
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <node tdi="nested">
        <node tdi="subnested"></node>
    </node>
    <xnode tdi="a"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        node.nested.replace(self.replace_nested, node.a)
        return True

    def replace_nested(self, node):
        node['been'] = u'here'
        node.content = u'yes'

    def render_a(self, node):
        node.content = u"should not be here"


def test_model(capsys, pure):
    model = Model()
    template.render(model)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <xnode been="here">yes</xnode>
    <xnode></xnode>
</node>
"""
