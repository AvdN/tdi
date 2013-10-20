
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node>
    <xnode blah="blub" x=y tdi="foo"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_foo(self, node):
        del node[u'blah']

template.render(Model())

def test_model(capsys, pure):
    model = Model()
    template.render(model)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <xnode x=y></xnode>
</node>
"""
