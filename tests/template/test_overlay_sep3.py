
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <znode tdi="nested" tdi:overlay="foo">
        <ynode tdi="subnested"></ynode>
    </znode>
    <xnode tdi=":nested" tdi:overlay="bar"> separator </xnode>
</node>
""".lstrip()).overlay(html.from_string("""
<anode tdi:overlay="foo" tdi="zonk"> overlayed </anode>
<bnode tdi=":zonk"> zonked </bnode>
""".lstrip()))

class Model(object):
    def render_nested(self, node):
        for subnode, item in node.iterate([0, 1]):
            subnode.content = item


def test_overlay_sep3(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <anode>0</anode><bnode> zonked </bnode><anode>1</anode>
    \n\
</node>
"""
