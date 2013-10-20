
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node>
    <xnode tdi="zonk" tdi:scope="foo"></xnode>
</node>
""".lstrip())


class FooModel(object):
    def render_zonk(self, node):
        node.content = u"Yay."


class Model(object):
    def __init__(self):
        self.scope_foo = FooModel()


def test_model(capsys, pure):
    model = Model()
    template.render(model)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <xnode>Yay.</xnode>
</node>
"""
