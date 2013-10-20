
from tdi._test_support import pure

from tdi.model_adapters import RenderAdapter
from tdi import html

template = html.from_string("""
<anode tdi="level1">
    <node tdi="-nested" tdi:scope="foo.bar" tdi:overlay="ov">
        <xnode tdi="a" tdi:scope="baz"></xnode>
    </node>
    <ynode tdi="-:nested">lalala</ynode>
</anode>
""".lstrip()).overlay(html.from_string("""
<znode tdi:scope="zonk">
    <widget tdi:overlay="ov" tdi:scope="zapp">widget!</widget>
</znode>
""".lstrip()))


def test_overlay_scope2(capsys, pure):
    template.render(None, adapter=RenderAdapter.for_prerender)
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<anode tdi:scope="=+" tdi="+level1">
    <widget tdi:scope="=+foo.bar" tdi="+nested">widget!</widget>
    \n\
</anode>
"""
