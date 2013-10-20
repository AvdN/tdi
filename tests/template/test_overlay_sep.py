
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
<anode tdi:overlay="bar"> overlayed </anode>
""".lstrip()))

class Model(object):
    def render_nested(self, node):
        for subnode, item in node.iterate([0, 1]):
            subnode.content = item


def test_overlay_sep(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <znode>0</znode><anode> overlayed </anode><znode>1</znode>
    \n\
</node>
"""
