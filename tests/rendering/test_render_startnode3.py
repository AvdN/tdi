
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<anode tdi="level1">
    <bnode tdi:scope="bar">
        <node tdi="nested">
            <cnode tdi:scope="baz" tdi="subnested">sup.</cnode>
        </node>
    </bnode>
</anode>
""".lstrip())


def test_model(capsys, pure):
    template.render(startnode='subnested')
    print
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<cnode>sup.</cnode>
"""
