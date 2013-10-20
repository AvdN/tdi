
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node>
    <xnode></xnode>
</node>
""".lstrip())


def test_model(capsys, pure):
    print template
    print template.tree
    template.render()
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
/
\\

/
  '<node>\\n    <xn...ode>\\n</node>\\n'
\\

<node>
    <xnode></xnode>
</node>
"""
