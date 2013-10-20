
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <znode tdi="nested" tdi:overlay="foo">
        <ynode tdi="subnested"></ynode>
    </znode>
    <xnode tdi="a"></xnode>
</node>
""".lstrip()).overlay(html.from_string("""
<anode tdi="grumpf" tdi:overlay="foo">
    <bnode tdi:overlay="bar"></bnode>
</anode>
<anode tdi="zonk" tdi:overlay="bar">
    <bnode tdi="schnick"></bnode>
</anode>
""".lstrip())).overlay(html.from_string("""
<anode tdi="zonk" tdi:overlay="bar">
    <bnode tdi="schnick"></bnode>
</anode>
""".lstrip()))

class Model(object):
    def render_nested(self, node):
        node['been'] = u'here'

    def render_schnick(self, node):
        node.content = u"something"


def test_overlay_nested2(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
<node>
    <anode been="here">
    <anode>
    <bnode>something</bnode>
</anode>
</anode>
    <xnode></xnode>
</node>
"""
