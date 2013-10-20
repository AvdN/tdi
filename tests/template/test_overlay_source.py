
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <znode tdi:overlay="foo">
        <ynode tdi="subnested"></ynode>
    </znode>
    <xnode tdi="a"></xnode>
</node>
""".lstrip()).overlay(html.from_string("""
<anode tdi="grumpf" tdi:overlay="&lt;foo">
    <bnode tdi="gna"></bnode>
</anode>
""".lstrip())).overlay(html.from_string("""
<anode tdi="grumpf2" tdi:overlay="<foo">
    <bnode tdi="gna2"></bnode>
</anode>
""".lstrip())).overlay(html.from_string("""
<anode tdi="grumpf3" tdi:overlay="foo">
    <bnode tdi="gna3"></bnode>
</anode>
""".lstrip()))

class Model(object):
    def render_grumpf(self, node):
        node['been'] = u'here'

    def render_grumpf2(self, node):
        node['been2'] = u'here2'

    def render_grumpf3(self, node):
        node['been3'] = u'here3'

    def render_gna(self, node):
        node.content = u"whoa!"

    def render_gna2(self, node):
        node.content = u"whoa!2"

    def render_gna3(self, node):
        node.content = u"whoa!3"

    def render_nested(self, node):
        node.content = u"wiped"


def test_overlay_source(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <anode been="here">
    <bnode>whoa!</bnode>
</anode>
    <xnode></xnode>
</node>
"""
