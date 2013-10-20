
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
<anode tdi="grumpf" tdi:overlay="&gt;foo">
    <bnode tdi="gna"></bnode>
</anode>
""".lstrip())).overlay(html.from_string("""
<anode tdi="grumpf2" tdi:overlay="<foo">
    <cnode tdi="gna2"></cnode>
</anode>
""".lstrip())).overlay(html.from_string("""
<anode tdi="grumpf3" tdi:overlay="<foo">
    <dnode tdi="gna3"></dnode>
</anode>
""".lstrip()))

class Model(object):
    def render_nested(self, node):
        node['been2'] = u'here2'

    def render_gna2(self, node):
        node.content = u"whoa!2"


def test_overlay_target(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <anode been2="here2">
    <cnode>whoa!2</cnode>
</anode>
    <xnode></xnode>
</node>
"""
