
from tdi._test_support import pure

from tdi.model_adapters import RenderAdapter
from tdi import html

template = html.from_string("""
<anode tdi="level1" tdi:prerender="remove-node">
    <node tdi="-nested">
        <xnode tdi="a">
            <znode tdi="b">foo</znode>
        </xnode>
    </node>
    <ynode tdi="-:nested">lalala</ynode>
</anode>
""".lstrip())

class Model(object):
    def render_a(self, node):
        node.b.content = u'hey'
        node.b.hiddenelement = True
        node.b['tdi:prerender'] = u'remove-node'

def test_model(capsys, pure):
    model = Model()
    res = template.render(model, adapter=RenderAdapter.for_prerender)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<anode tdi:scope="=+">
    <node tdi:scope="=-" tdi="-nested">
        <xnode>
            hey
        </xnode>
    </node><ynode tdi:scope="=-" tdi="-:nested">lalala</ynode>
    \n\
</anode>
"""
