
from tdi._test_support import pure

from tdi.model_adapters import RenderAdapter
from tdi import html

template = html.from_string("""
<anode tdi="level1">
    <node tdi="-nested" tdi:scope="foo.bar">
        <xnode tdi="a" tdi:scope="baz"></xnode>
    </node>
    <ynode tdi="-:nested">lalala</ynode>
</anode>
""".lstrip())


def test_model(capsys, pure):
    template.render(None, adapter=RenderAdapter.for_prerender)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<anode tdi:scope="=+" tdi="+level1">
    <node tdi:scope="=-foo.bar" tdi="-nested">
        <xnode tdi:scope="=+foo.bar.baz" tdi="+a"></xnode>
    </node><ynode tdi:scope="=-foo.bar" tdi="-:nested">lalala</ynode>
    \n\
</anode>
"""
