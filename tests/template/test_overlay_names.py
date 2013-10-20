
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <znode tdi:overlay="foo">
        <ynode tdi:overlay="bar"></ynode>
        <ynode tdi:overlay="<zonk"></ynode>
        <ynode tdi:overlay=">plenk"></ynode>
    </znode>
    <xnode tdi:overlay=">baz"></xnode>
</node>
""".lstrip())


def test_model(capsys, pure):
    print list(sorted(template.source_overlay_names))
    print list(sorted(template.target_overlay_names))
    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
['bar', 'foo', 'zonk']
['bar', 'baz', 'foo', 'plenk']
"""
