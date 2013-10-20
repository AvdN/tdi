
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<anode tdi="level1">
</anode><bnode tdi="*:level1">
</bnode>
""".lstrip())

class Model(object):
    def render_level1(self, node):
        for node, item in node.iterate([1, 2, 3]):
            node.content = item

    def separate_level1(self, node):
        node['foo'] = 'bar'


model = Model()
template.render(model)

def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<anode>1</anode><bnode>
</bnode><anode>2</anode><bnode>
</bnode><anode>3</anode>
"""
