
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<anode tdi="level1">
</anode><bnode tdi="*:level1">
</bnode>
""".lstrip())

class Model(object):
    def render_level1(self, node):
        def repeat(node, item):
            node.content = item
        node.repeat(repeat, [1, 2, 3])

    def separate_level1(self, node):
        node['foo'] = 'bar'


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
