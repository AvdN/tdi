
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
        for subnode, item in node.nested.iterate([]):
            subnode['j'] = item
            subnode.content = u'should be here %s' % item
        return True

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
    \n\
    <xnode></xnode>
</node>
"""
