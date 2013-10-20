
from tdi._test_support import pure

from tdi.model_adapters import RenderAdapter
from tdi import html

template = html.from_string("""
<anode tdi="level1">
    <node tdi="-nested">
        <xnode tdi="a"></xnode>
    </node>
    <ynode tdi="-:nested">lalala</ynode>
</anode>
""".lstrip())

class Model(object):
    def render_nested(self, node):
        node.repeat(self.repeat_nested, (1, 2))

    def repeat_nested(self, node, item):
        pass


def test_model(capsys, pure):
    model = Model()
    res = template.render(model, adapter=RenderAdapter.for_prerender)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<anode tdi:scope="=+" tdi="+level1">
    \n\
        <xnode tdi:scope="=+" tdi="+a"></xnode>
    lalala
        <xnode tdi:scope="=+" tdi="+a"></xnode>
    \n\
    \n\
</anode>
"""
