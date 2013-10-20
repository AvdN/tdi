
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
<anode tdi="grumpf" tdi:overlay="-foo">
    <bnode tdi="gna"></bnode>
</anode>
""".lstrip()))

class Model(object):
    def render_nested(self, node):
        node['been'] = u'here'

    def render_gna(self, node):
        node.content = u"whoa!"


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<node>
    \n\
    <bnode>whoa!</bnode>

    <xnode></xnode>
</node>
"""
